# The operating check: a weekly review that ends in a decision

A regular account check is useful only if it ends in a call someone can act on. A list of numbers with no decision gets read and changes nothing, while the problem it hinted at keeps costing money.

Run it weekly on every account, and daily for a few days after a launch or a big change. Once the data is in hand it takes about 15 minutes. [audit-guardrails.md](audit-guardrails.md) decides what counts as evidence, and [the one stop rule](../SKILL.md#the-one-stop-rule) decides every stop, keep or scale call.

## Inputs

Pull the same inputs each time, for this period against the previous comparable one, and also for the **last 6 to 8 periods** (weeks on a weekly check). That range shows the account's normal ups and downs, and the HOLD call depends on it. The kit's guide `docs/use-exports.md` says how to export each one.

- Spend and budget by campaign, and how fast the month's budget is being used (`pacing-monitor`)
- Impressions, clicks, cost per click, click-through rate, cost per thousand impressions, and on Google the impression share lost to budget and to rank
- Results, cost per result and (for shops) sales value, each with its attribution window named
- The owner's own count of results for the same dates, and lead quality if they track it
- Frequency and click-through rate by day for the ads with the most spend
- Landing page conversion rate by device, from website analytics if set up
- Change history for the period (who changed what, and when)

If an input is not available, mark it **MISSING** and carry on. Do not estimate it.

## The check, in order

Work from top to bottom. A cause higher up explains symptoms lower down, so stop at the first real cause instead of chasing its effects.

| # | Question | What to look at | Typical cause when it moved |
|---|---|---|---|
| 1 | Did spend move? | Spend against budget, limited by budget, delivery problems | A budget change, a campaign limited, a payment problem |
| 2 | Did traffic change? | Clicks, cost per click, click-through rate, cost per thousand impressions, new search terms or placements | More competition, match types drifting, a placement taking spend |
| 3 | Did results change? | Conversion rate, cost per result, lead quality | An offer change, the season, worse leads, recent days not yet complete |
| 4 | Did ads wear out? | Frequency, click-through rate against the ad's own first week, spend sitting on a few old ads | The same people seeing the same ads, no new ads |
| 5 | Did the page break? | Page speed, form errors, the phone versus computer gap | A site update, a broken form, a script blocking the page |
| 6 | Did tracking break? | Platform counts against the owner's count and analytics | A tag removed, a tag firing twice, a consent banner change |

Check the change history against every movement. A number that moved the day after a budget change, a bidding change or a new ad probably moved because of it.

The most recent days undercount results wherever people take time to book or buy. Treat them as incomplete, and never call a trend from them alone.

**One period against one period is not a trend.** A week that looks bad against last week often means last week was unusually good. Before any call other than HOLD on a performance number, check where this period sits against the last 6 to 8: inside that range is normal variation; outside it, or three or more periods moving the same way, is a movement worth acting on. Three things do not need this baseline, because they are facts or set by the owner's limits: spend and tracking problems, a broken page, and the one stop rule, which compares results with the owner's maximum cost per result rather than with the ad's own history (an ad that has always been too expensive is normal for itself and still too expensive).

## The decision

Every check ends in **exactly one** call for the account, and optionally one for each campaign that moved:

| Call | Meaning | When |
|---|---|---|
| **HOLD** | Change nothing; check again at the next check | Movement inside the normal range, too little data (below the spend gate), still learning, or recent days incomplete |
| **FIX** | A named problem with a known fix | A broken form, a winning campaign capped by budget, a disapproved ad, a tag that stopped firing |
| **TEST** | A hypothesis worth spending money to answer | A new ad for a worn-out one, a page variant, a bidding change with enough results behind it |
| **INVESTIGATE** | The data cannot be trusted yet, so no performance call is possible | The owner's count and the platform's differ by more than about 20%, counts jumped with no business reason, an input is MISSING |

Rules for the call:

- **INVESTIGATE beats everything.** While tracking is in doubt, no performance call is valid.
- **FIX names the problem and the fix.** "Performance is down" is not a FIX.
- **TEST names the hypothesis, the number to watch and when it stops** (for a stop or keep test, the spend gate).
- **HOLD still needs a reason**, and what would change it.
- **No call moves money on its own.** Budget, bid, status and tracking changes go to the owner as a proposal (current state, change, expected effect, how to undo) and wait for a clear yes.

Every call ends with three short lists: **facts** (in the data), **hypotheses** (inferred), and **missing data** (what would change the decision).

## The one-minute summary

Close the week with a summary the owner can read in a minute (`weekly-account-summary` writes a fuller one):

1. **Results against target.** One line per account or campaign, marked green (at or under target), amber (between target and maximum) or red (above maximum), on the owner's count.
2. **What moved and why.** The top two or three movements, each with a likely cause and how sure you are (high, medium, low).
3. **Decisions for next week.** Each labelled HOLD, FIX, TEST or INVESTIGATE, with one line on why.

Leave out numbers nobody will act on. Name any missing data that limits a conclusion, and say that any change that moves money is waiting for the owner's yes.

## Making it a habit

Run the check by hand for a few weeks before automating any of it. Doing it by hand shows which inputs are hard to get and which calls keep coming up.

---

*The ordered check, the four calls and the summary are re-expressed from Marek Dąbrowski's "The Paid Ads Operator's Guide to Claude" (Adlume, 16 July 2026), adapted to this kit's guardrails.*
