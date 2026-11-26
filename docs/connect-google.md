# Connect Google Ads

Google publishes a free, open-source connector: [googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp). It runs on your own computer.

**Be honest with yourself about this one.** It needs some technical setup. If the steps below look unfamiliar, use [exported reports](use-exports.md) instead. Every skill in this kit works with exports, and you lose nothing by starting that way.

## What you need

- Python 3.11 or newer, and [pipx](https://pipx.pypa.io/stable/#install-pipx)
- A Google Cloud project with the **Google Ads API** switched on
- The `gcloud` command-line tool, to sign in
- A Google login that has access to the Google Ads account

## Steps

Google's own README is the source of truth and is kept up to date. Follow it here: [Quickstart and setup](https://github.com/googleads/google-ads-mcp#quickstart--setup). In outline:

1. **Create or choose a Google Cloud project** and switch on the Google Ads API for it.
2. **Create an OAuth client** in your Google Cloud project (type: desktop app) and download its JSON file. The sign-in command needs this file.
3. **Sign in** with the `gcloud auth application-default login` command from the README, giving it the scopes it lists and your client file. It saves a credentials file and prints where it put it. Note that path.
4. **Add the connector to Claude Code.** Take the `mcpServers` block from the README, fill in your credentials path and project ID, and save it as `.mcp.json` in your project folder, or add it with `claude mcp add-json`.
5. **If you use a manager account,** add your manager customer ID as the README describes.
6. Restart Claude Code.

Allow an hour or more the first time. The README does not ask for a Google Ads developer token, but the connector has a setting for one. If you get an error that mentions it, stop and use exports.

Never paste a password, key or token into a chat with Claude. The sign-in happens in Google's own window, and the settings file holds only a path to the credentials file.

## Check it worked

Ask: `list the Google Ads accounts you can see`

If Claude lists your account, you are connected.

## What the connector can do

It is built mainly for reading and reporting. A small set of changes (creating assets, uploading videos, managing labels) goes through a two-step "propose and confirm" process, so nothing changes without your approval.

For anything it cannot change, Claude tells you the exact steps to do yourself in Google Ads.

## If you get stuck

Ask Claude: `help me set up the Google Ads connector, I'm new to this`. It goes one step at a time. Or switch to [exports](use-exports.md) and come back to this later.
