# No setup: use exported reports

You do not have to connect anything. Download a report from your ad account and give the file to Claude. The basic exports below are enough for an audit. Some skills need one more file, listed further down, and Claude tells you which.

This is the best way to start. It takes two minutes and Claude cannot change anything in your account.

## Google Ads

1. Open Google Ads and go to **Campaigns**.
2. Set the date range at the top right. The last 30 days is a good default.
3. Press the **Download** button above the table and choose **.csv**.

For a fuller audit, repeat for these tables:

| Table | Where | Why |
|---|---|---|
| Search terms | Campaigns, then Insights and reports, then Search terms | Finds wasted spend |
| Keywords | Campaigns, then Audiences, keywords and content, then Search keywords | Quality Score and bids |
| Ads | Campaigns, then Ads | Which ads work |

## Meta Ads Manager

1. Open Ads Manager.
2. Set the date range. The last 30 days is a good default.
3. Choose the **Ads** tab, so each ad is one row.
4. Open **Reports**, choose **Export table data**, and pick **.csv**.

For audience or placement questions, add a breakdown first (by age, gender, placement or country), then export again.

## Extra files some skills ask for

| What | Where | Used for |
|---|---|---|
| A split by day | Google: the Segment button above the table, then Time, then Day, before you download. Meta: Breakdown, then Time, then Day | Trends, tired ads, pacing |
| Meta placements | Breakdown, then Delivery, then Placement | Finding placements that spend and bring nothing |
| Google networks | Segment, then Network (with search partners) | Finding spend on search partners and the Display Network |
| Google conversion settings | Goals, then Conversions, then Summary, and download | Checking what is being counted |
| Your own count | The number of sales or leads from your shop, form tool or CRM for the same dates | Checking the ad platform's count is real |

## What an export cannot tell Claude

- What changed in the account and when. Say so if you changed budgets, ads or tracking in the period.
- Settings that are not columns, such as location options or who an ad set targets. Claude will ask.
- Anything about a date range you did not export.

## Give it to Claude

Drag the files into the chat, or tell Claude where they are saved. Then say what you want:

```text
Here are my Google Ads exports for the last 30 days. Audit the account.
```

Tell Claude your **currency** and **time zone**. It will ask if you forget.

## Tips

- Menus move. If a step does not match your screen, tell Claude what you see and it will adapt.
- Export the same date range for every table, or the numbers will not line up.
- Do not delete columns. More columns help, and Claude ignores what it does not need.
- A report contains business data. Share it only where you are happy for it to be read.
