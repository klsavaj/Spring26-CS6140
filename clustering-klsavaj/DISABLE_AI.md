# Disabling AI Coding Assistants for This Assignment

For this assignment, you should complete the work **without AI coding assistants**. This helps you build foundational skills and understand the concepts deeply. Please disable AI features in your coding environment before starting. I am including instructions for how to do this in VS Code and Google Colab - you may need to adjust these instructions if using other editors.

## VS Code

### Quick Method (Recommended)
1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. Type "Hide AI Features"
3. Select **"Chat: Hide AI Features"**
4. Restart VS Code if prompted

### Alternative: Disable via Settings
1. Open Settings: `Ctrl+,` (Windows/Linux) or `Cmd+,` (Mac)
2. Search for `chat.disableAIFeatures`
3. Check the box to enable this setting
4. Search for `github.copilot.enable`
5. Uncheck it or set it to `false`

### Verification
- You should no longer see gray inline code suggestions as you type
- The Copilot icon in the bottom-right should show as disabled

---

## Google Colab

### Steps to Disable
1. Open your Colab notebook
2. Click **Tools** → **Settings** in the top menu (or the gear icon in the upper right corner)
3. Look for the **"AI Assistance"** tab
4. Uncheck **Show AI-powered inline completions**
5. Check **Hide generative AI features**
6. Click **Close**

### Verification
- Type some code in a cell
- You should no longer see gray italic code suggestions appearing automatically
- The "Help me code" sparkle icon should be absent or inactive

---

## Quick Tips

- **Press ESC** to dismiss any AI suggestion if it appears
- These settings are usually account-level, so you'll need to re-enable AI features after completing this assignment if you want to use them later
- If you accidentally accept an AI suggestion, use `Ctrl+Z` / `Cmd+Z` to undo
