# Reading Google Ads data without false conclusions

Load this before analysing, auditing or reporting on a Google Ads account, or before deciding whether to stop, keep or scale anything in one. [audit-guardrails.md](audit-guardrails.md) covers how to grade what you find. This file covers how the data misleads you before you get that far. The decision itself follows [the one stop rule](../SKILL.md#the-one-stop-rule).

Google Ads reports leave things out by design. Default views omit data without saying so, names suggest contents they do not have, and small accounts produce numbers that look like findings. Most wrong conclusions come from not knowing this, not from bad reasoning.

Where a line names an API field (in `code`), it matters only to someone using the Google Ads API or a connector. In the Google Ads screens, ask what the person sees; menus move.

## What the data hides

### Search terms are a sample, not the total

Google does not show searches made by too few people. On small accounts a large share of clicks, often half or more in practice, has no search term shown. The terms you can see lean towards common searches.

- Any claim about "what this campaign is buying" carries the ratio: *of the 13 clicks Google shows, out of 33 in total.*
- Look at the report **unfiltered first**. Filtering to terms with clicks drops terms that only had impressions.
- **Nothing recovers the hidden searches.** The search is never passed to the website, so analytics can show what each visitor did, never what they typed.

```
clicks shown    = sum of clicks in the search terms report
total clicks    = campaign clicks for the same dates
clicks hidden   = total clicks - clicks shown
```

### Names describe intentions, not contents

An ad group called "Competitor" can hold entirely different keywords. Read the keyword list and the search terms; treat every name as a label someone typed once.

### "Conversions" can be several things in one column

The Conversions column counts every conversion action marked primary (plus any secondary action a campaign goal pulls in). "All conv." adds the rest. One campaign's conversions might mix a page view, a form and a booking, or count the same booking twice through two actions.

- Split conversions by conversion action (the "Conversion action" segment) before calling anything a lead or a sale.
- Check each action's count setting ("one" or "every") and whether it is primary.
- Compare with the owner's own count. See "Check the count is real first" in [the skill](../SKILL.md#check-the-count-is-real-first).
- Google Ads now offers only data-driven and last click attribution. With few conversions, data-driven credit for any one campaign is soft; do not read much into it.

### One ad group can send traffic to several pages

Each ad has its own final URL, and old pages stay in rotation after a new one is launched. Before concluding anything about a landing page, check which pages the ads point to and how clicks split between them.

### Dates are click dates

Conversions are reported on the date of the click that led to them. A booking made today can appear a week earlier. When the owner says "we got a booking today" and the report says the 11th, both are right: "clicked on the 11th".

### Identical campaign names are often old experiments

Finished experiment campaigns can keep the original campaign's name. Check the campaign type and serving status before believing there are duplicates.

### Change history

The Change history page in Google Ads covers the past 2 years. Through the API, `change_event` gives field-level detail for only the last 30 days. Say which one you looked at, and when a change is older than what you can see, say that instead of guessing a cause.

### Other people change the account

The owner, a past freelancer, automated rules, scripts and Google's own auto-applied recommendations all leave changes. Change history shows who or what made each change. Report what it shows, not a guess at why.

## The window is not the whole story

A 30-day export of a campaign that has run for a year is a slice.

- **Find out how long something has run** before quoting any efficiency number. Quote recent and lifetime figures when they differ.
- **Do not average across changes.** If bids, keywords, budget, ads or targeting changed mid-period, the period is several set-ups averaged together.
- **Bid-only changes** spoil cost and volume comparisons but leave questions about intent and audience readable.
- **A bid strategy that is learning cannot be judged.** The Status column shows "Learning". Fixing a confirmed break (tracking down, a wrong address) still comes first.

## Small numbers

Most false findings in small accounts are sample-size mistakes that look like insight. Doubt runs both ways: one conversion on one click proves no more than zero conversions on five clicks disproves.

Zero conversions in N clicks only rules out conversion rates at or above these (95% confidence):

| Clicks | Rules out a conversion rate of | What you can say |
|---|---|---|
| 5 | 45% or more | Nothing. Zero is the expected result |
| 10 | 26% or more | Still nothing useful |
| 30 | 10% or more | You can start to doubt a strong conversion rate |
| 50 | 6% or more | Meaningful for high-intent searches |
| 100 | 3% or more | Underperforming if the break-even rate is above 3% |

Before calling spend wasted, work out the conversion rate it needs to be worth keeping:

```
break-even conversion rate = cost per click / maximum cost per result
```

The one stop rule's spend gate (3 times the maximum cost per result) is the same test in money: it equals 3 / break-even conversion rate clicks, which rules out the break-even rate with about 95% confidence when there are zero results. Example: £1.60 a click and a £48 maximum: 1.60 / 48 = 3.3%, so about 90 clicks, or £144.

If a term has not reached that, it is unmeasured, not failing. Say how long a readable sample will take at its current clicks. "Let it run" is honest only with a date. At five clicks a month, sometimes the honest answer is that you never will know, and the decision rests on relevance alone.

## Documents describe a day; accounts move

Audits and reports were true when written. Every number in them is out of date until pulled again. Carry the date with the claim: *as of the audit on the 2nd*.

## Stating findings

Know which of these each claim is:

- **Verified:** pulled this session, unfiltered, and checked against a total
- **Inferred:** reasoned from verified data, and could be wrong
- **Out of date:** from a document, an earlier session or the owner, with its date

**The test before a finding reaches the owner or a client: could they disprove it in a minute in their own account?** They have the same reports. State the limits first (clicks shown out of total, sample size, changes mid-period). It costs nothing and makes the rest believable.

If a claim is about a landing page, open the page. Booking widgets and chat boxes load with JavaScript and may not appear in a plain fetch, so their absence there is not evidence.

When the owner challenges a finding and is right, say so plainly and move on.

## Conclusions that sound right

| Sounds like | Usually |
|---|---|
| "This campaign has zero conversions" | True on the day the document was written |
| "The search terms are junk" | You are seeing only part of the clicks |
| "That ad group targets the wrong intent" | It is *named* that; the keywords say otherwise |
| "£X wasted on those terms" | Below the spend gate, so unmeasured |
| "It converted, so the term works" | One conversion on one click is noise |
| "Performance fell in August" | Bids changed three times that month |
| "Traffic lands on the new page" | Two ads serve; one points at the old page |
| "It brought a booking" | It brought a conversion; check which action |
| "There are duplicate campaigns" | Old experiments with the same name |
| "Cost per lead is £30, so it fits" | The count includes double counting; check the owner's number |

---

*Adapted from Corey Haines' marketingskills (MIT). Change history, attribution and conversion column facts checked against Google Ads Help in November 2026.*
