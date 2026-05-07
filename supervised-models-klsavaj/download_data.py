"""
Download and merge Maine 2024 election results with Census ACS demographic data.

Produces maine_election_data.csv with demographic features and election outcomes
for Maine municipalities, suitable for supervised learning tasks.

Usage:
    python download_data.py
"""

import json
import re
from pathlib import Path

import pandas as pd
import requests

# --- Configuration ---

ELECTION_URL = (
    "https://www.maine.gov/sos/sites/maine.gov.sos/files/inline-files/"
    "President%20and%20Vice%20President%20FINAL-Corrected%2020241205.xlsx"
)

CENSUS_URL = (
    "https://api.census.gov/data/2024/acs/acs5"
    "?get=NAME,B01003_001E,B19013_001E,B19301_001E,B01002_001E,B25077_001E,"
    "B25003_001E,B25003_002E,B23025_001E,B23025_002E,B23025_005E,"
    "B02001_001E,B02001_002E,B17001_001E,B17001_002E,"
    "B15003_001E,B15003_022E,B15003_023E,B15003_024E,B15003_025E"
    "&for=county%20subdivision:*&in=state:23&in=county:*"
)

CENSUS_VARIABLE_MAP = {
    "B01003_001E": "total_population",
    "B19013_001E": "median_household_income",
    "B19301_001E": "per_capita_income",
    "B01002_001E": "median_age",
    "B25077_001E": "median_home_value",
    "B25003_001E": "total_housing_units",
    "B25003_002E": "owner_occupied_units",
    "B23025_001E": "pop_16_plus",
    "B23025_002E": "in_labor_force",
    "B23025_005E": "unemployed",
    "B02001_001E": "race_total",
    "B02001_002E": "white_alone",
    "B17001_001E": "poverty_universe",
    "B17001_002E": "below_poverty",
    "B15003_001E": "edu_total",
    "B15003_022E": "bachelors",
    "B15003_023E": "masters",
    "B15003_024E": "professional",
    "B15003_025E": "doctorate",
}

OUTPUT_FILE = "maine_election_data.csv"

# Final columns for the output CSV
OUTPUT_COLUMNS = [
    "town",
    "total_population",
    "median_household_income",
    "per_capita_income",
    "median_age",
    "median_home_value",
    "pct_owner_occupied",
    "pct_in_labor_force",
    "pct_unemployed",
    "pct_white",
    "pct_poverty",
    "pct_bachelors_plus",
    "margin",
    "winner",
]


def download_election_data() -> pd.DataFrame:
    """Download and clean Maine 2024 presidential election results."""
    print("Downloading election data from maine.gov...")
    df = pd.read_excel(ELECTION_URL, header=0)

    # The first two data rows are sub-headers (VP names, party labels) -- skip them
    df = df.iloc[2:].reset_index(drop=True)

    # Standardize column names to what we expect
    # The Excel columns are: CTY, MUNICIPALITY, then candidate columns
    cols = df.columns.tolist()
    vote_cols = cols[2:]  # everything after CTY and MUNICIPALITY

    # Drop rows where both CTY and MUNICIPALITY are NaN (blank separator rows)
    df = df.dropna(subset=["CTY", "MUNICIPALITY"], how="all")

    # Drop county total rows (MUNICIPALITY contains "Total")
    df = df[~df["MUNICIPALITY"].astype(str).str.contains("Total", case=False, na=False)]

    # Drop STATE UOCAVA and Statewide Total rows
    df = df[~df["MUNICIPALITY"].astype(str).str.contains("STATE UOCAVA", case=False, na=False)]
    df = df[~df["MUNICIPALITY"].astype(str).str.contains("Statewide", case=False, na=False)]

    # Convert vote columns to numeric (they may be object dtype from header rows)
    for col in vote_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Clean municipality names: extract first name before "/"
    df["MUNICIPALITY"] = df["MUNICIPALITY"].astype(str).str.split("/").str[0].str.strip()

    # Identify Harris and Trump columns
    harris_col = [c for c in cols if "Harris" in str(c) or "harris" in str(c)]
    trump_col = [c for c in cols if "Trump" in str(c) or "trump" in str(c)]

    if not harris_col or not trump_col:
        raise ValueError(f"Could not find Harris/Trump columns. Available: {cols}")

    harris_col = harris_col[0]
    trump_col = trump_col[0]

    # Compute targets
    two_party_total = df[harris_col] + df[trump_col]
    df["harris_pct"] = df[harris_col] / two_party_total * 100
    df["trump_pct"] = df[trump_col] / two_party_total * 100
    df["margin"] = df["trump_pct"] - df["harris_pct"]  # positive = Trump won
    df["winner"] = (df["margin"] > 0).astype(int)  # 1=Trump, 0=Harris

    # Create a clean town name column for joining (lowercase for matching)
    df["town_clean"] = df["MUNICIPALITY"].str.lower().str.strip()

    print(f"  Election data: {len(df)} municipalities after cleaning")
    return df


def download_census_data() -> pd.DataFrame:
    """Download Census ACS 2024 5-year data for Maine county subdivisions."""
    print("Downloading Census ACS data...")
    resp = requests.get(CENSUS_URL, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    # First row is headers, rest is data
    headers = data[0]
    rows = data[1:]
    df = pd.DataFrame(rows, columns=headers)

    # Rename census variable codes to readable names
    df = df.rename(columns=CENSUS_VARIABLE_MAP)

    # Convert numeric columns
    numeric_cols = list(CENSUS_VARIABLE_MAP.values())
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Clean the NAME field to extract town name
    # Census names look like "Auburn city, Androscoggin County, Maine"
    # Extract base name before first comma, then strip type suffixes
    def clean_census_name(name: str) -> str:
        base = name.split(",")[0].strip()
        for suffix in [" city", " town", " plantation", " UT", " Township"]:
            if base.endswith(suffix):
                base = base[: -len(suffix)]
        return base.strip()

    df["town_clean"] = df["NAME"].apply(clean_census_name).str.lower().str.strip()

    print(f"  Census data: {len(df)} county subdivisions")
    return df


def compute_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """Compute percentage features from raw census counts."""
    df = df.copy()
    df["pct_owner_occupied"] = df["owner_occupied_units"] / df["total_housing_units"] * 100
    df["pct_in_labor_force"] = df["in_labor_force"] / df["pop_16_plus"] * 100
    df["pct_unemployed"] = df["unemployed"] / df["in_labor_force"] * 100
    df["pct_white"] = df["white_alone"] / df["race_total"] * 100
    df["pct_poverty"] = df["below_poverty"] / df["poverty_universe"] * 100
    df["pct_bachelors_plus"] = (
        (df["bachelors"] + df["masters"] + df["professional"] + df["doctorate"])
        / df["edu_total"]
        * 100
    )
    return df


def main():
    script_dir = Path(__file__).parent
    output_path = script_dir / OUTPUT_FILE

    # Step 1: Download election data
    election_df = download_election_data()

    # Step 2: Download census data
    census_df = download_census_data()

    # Step 3: Drop rows with sentinel values (-666666666) in any numeric column
    numeric_cols = list(CENSUS_VARIABLE_MAP.values())
    sentinel_mask = (census_df[numeric_cols] == -666666666).any(axis=1)
    n_sentinel = sentinel_mask.sum()
    census_df = census_df[~sentinel_mask]
    print(f"  Dropped {n_sentinel} census rows with sentinel values")

    # Step 4: Compute derived features
    census_df = compute_derived_features(census_df)

    # Step 5: Join on cleaned town name (case-insensitive -- both already lowered)
    merged = election_df.merge(census_df, on="town_clean", how="inner")

    n_election = len(election_df)
    n_matched = len(merged)
    n_unmatched = n_election - n_matched
    print(f"\n  Matched: {n_matched} towns")
    print(f"  Unmatched (dropped): {n_unmatched} towns")

    # Step 6: Drop rows with NaN or infinite derived features
    derived_cols = [
        "pct_owner_occupied",
        "pct_in_labor_force",
        "pct_unemployed",
        "pct_white",
        "pct_poverty",
        "pct_bachelors_plus",
        "margin",
        "winner",
    ]
    before = len(merged)
    merged = merged.replace([float("inf"), float("-inf")], float("nan"))
    merged = merged.dropna(subset=derived_cols)
    n_dropped_nan = before - len(merged)
    if n_dropped_nan > 0:
        print(f"  Dropped {n_dropped_nan} rows with NaN/infinite features")

    # Step 7: Prepare final output
    merged["town"] = merged["MUNICIPALITY"]
    final = merged[OUTPUT_COLUMNS].copy()
    final = final.sort_values("town").reset_index(drop=True)

    # Save
    final.to_csv(output_path, index=False)
    print(f"\nSaved {output_path} with shape {final.shape}")

    # Summary statistics
    print("\n--- Summary Statistics ---")
    print(final.describe().round(2).to_string())
    print("\n--- First 10 rows ---")
    print(final.head(10).to_string())
    print(f"\nWinner distribution: Trump={final['winner'].sum()}, Harris={len(final) - final['winner'].sum()}")


if __name__ == "__main__":
    main()
