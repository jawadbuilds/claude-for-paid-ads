# Safety

An assistant that can reach your ad account can also spend your money. These are the rules every agent in this kit follows, and the settings you can use to enforce them.

## The rules every agent follows

1. Audits, reports and research never change your account.
2. Before any change, you see exactly what will change: the item, the setting, the old value, the new value and what it does to spend. Nothing happens until you say yes to that change.
3. New campaigns, ad sets, ad groups and ads are created paused or as drafts. You switch them on.
4. Changes are made one at a time. After each one, the agent reads it back from the platform and confirms it matches.
5. A yes covers one change. Approving one thing does not approve the next.
6. If a number is missing, the agent asks for it. It does not estimate.
7. Agents never ask for a password, card number, key or token. You sign in yourself, in the platform's own window.
8. Ad copy is checked twice before it is used: once for AI-sounding or unclear lines, and once for invented numbers, prices and promises.

## Settings that enforce it

You do not have to rely on the rules alone.

- Start with [exported reports](use-exports.md). With them, Claude cannot reach your account at all.
- Limit what Meta's connector may do. In Meta Business Suite, go to Settings, then Integrations, then Ads MCP server, and block actions such as creating campaigns, if your business has that control. Meta says it is not available to everyone yet. See [connect Meta](connect-meta.md).
- Google's connector is built mainly for reading, and its few changes need a second confirmation.
- Claude Code asks before it uses a tool. Keep those prompts on for ad tools.
- Use the limits the platforms give you. Meta has an account spending limit for accounts that pay automatically. Google has account budgets only for accounts on monthly invoicing, so on a normal card-paying Google account your limit is the daily budget of each campaign. A platform limit holds whatever any tool does.

The agents' read-only behaviour rests on their instructions. A plugin cannot reliably block a connector's write tools without knowing what the connector is called on your computer, which is why the settings above matter.

If you want a harder stop in Claude Code, block the one tool that makes Meta ads live. It was called `ads_activate_entity` when this was written, in November 2026. Type `/mcp` to see what your Meta connector is called, then add `mcp__<that name>__ads_activate_entity` to the deny list in your Claude Code permission settings. Claude can then prepare everything and cannot switch anything on.

## What this kit does not do

- It does not promise results. No tool can.
- It does not give legal, tax or financial advice.
- It does not replace your own judgement. Read every change before you approve it.

## If something goes wrong

1. Pause the campaign in the ad platform yourself. That always works.
2. Tell Claude what happened and ask it to read back the current state of the account.
3. If you think the kit behaved wrongly, [open an issue](https://github.com/jawadbuilds/claude-for-paid-ads/issues).
