# Connect Meta Ads (Facebook and Instagram)

Meta runs its own connector for AI assistants. It is the official route, and Meta does not list a fee for it. At the time of writing (November 2026) it is in open beta, so screens may differ from this page.

**Connector address:** `https://mcp.facebook.com/ads`

## Before you sign in: what you are giving access to

The connector can read performance reports and account history. It can also create and edit campaigns, ad sets and ads, upload images and videos, manage custom audiences and catalogs, check pixel data quality and run A/B tests. That is real access to an account that spends money.

What it creates does not spend straight away. Meta's pages describe new campaigns, ad sets and ads as created paused, and in builds done with this kit in October and November 2026 they appeared in the Ads Manager draft. Either way, nothing spends until it is published or switched on, so check the status on screen before you do that.

If you only want Claude to read your numbers, use [exported reports](use-exports.md). With an export Claude cannot change anything.

## What you need

- A Facebook login that has access to the ad account
- Claude. Claude Code needs a paid Claude plan

## Steps in the Claude app

1. Open **Customize**, then **Connectors**.
2. Choose **+ Add**, then **Add custom connector**.
3. Paste `https://mcp.facebook.com/ads` and save.
4. Sign in with Facebook in the window that opens. Type your password yourself. Claude never sees it.
5. Pick the ad accounts you want Claude to reach.

A free Claude account can add only one custom connector. A connector added in the Claude app is also available in Claude Code when you sign in with the same account, so this is the simplest route for both.

## Adding it straight to Claude Code

Meta documents a Claude Code command that needs the ID of a Meta app you own. Most people do not have one, and Meta says you do not need one: add the connector in the Claude app as above. If you do have an app, follow [Meta's own steps](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-get-started).

## Check it worked

Ask: `what is the name of my Meta ad account and how much did it spend in the last 7 days?`

If Claude answers with your real account name and a number, you are connected.

## Limit what Claude can do, if your account has the control

Meta is rolling out a control that lets you allow or block actions for each ad account, such as creating campaigns. Meta says it has limited availability and needs full control of the business, so you may not see it.

1. Go to **Settings** in Meta Business Suite.
2. Below **Integrations**, look for **Ads MCP server**.
3. Select the ad account you want to manage.
4. Allow or block specific actions.

If it is not there, your safe routes are exported reports, and reading every proposed change before you approve it.

## Good to know

- Meta's Business Help page says accounts are restricted for breaking advertising rules, and that using the connector does not by itself put an account at risk. Follow Meta's advertising rules as you would in Ads Manager.
- Budgets inside the connector are counted in the smallest unit of your currency. For pounds, dollars and euros, 2000 means 20.00. For a currency with no smaller unit, such as yen, 2000 means 2000. Always check the amount on screen before you publish.
- If something will not publish, ask Claude to read the `meta-connector-field-notes` skill. It lists the common causes.

Sources: [Meta's ads connector documentation](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview), [Meta Business Help](https://www.facebook.com/business/help/1456422242197840) and [Claude Help on custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).
