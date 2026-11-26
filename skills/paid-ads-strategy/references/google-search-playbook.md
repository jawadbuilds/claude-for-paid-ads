# Google Search playbook

Operating rules for Google Search campaigns: where to spend first, how to structure the account, when to loosen match types, how to handle negative keywords and bidding, and when Performance Max (PMax, Google's campaign type that runs across all its channels) earns a place. Every stop, keep or scale decision follows [the one stop rule](../SKILL.md#the-one-stop-rule). For writing responsive search ads, see [rsa-output-spec.md](rsa-output-spec.md). Menus move, so ask what the person sees.

## The intent ladder

Spend opens one rung at a time. Each rung opens only after the one below brings real results at or under the owner's target cost per result:

1. **Brand.** Searches for the business's own name. Cheapest clicks, most likely to convert. Worth running only once people actually search for the name; a new business with no brand searches has nothing to buy here.
2. **High-intent non-brand.** People ready to buy ("maths tutor online", "emergency plumber Leeds"). Most of the budget lives here.
3. **Competitor.** People comparing ("[competitor] alternative"). Usually dearer clicks and fewer results. Run it only with a page that answers the comparison honestly.
4. **Problem-aware.** People with the problem who are not shopping yet ("how to help my child with algebra"). Slower to pay back. Only after rungs 1 and 2 work.
5. **Awareness.** Display, YouTube, Demand Gen. Last, and only with spare budget.

Skipping rungs is how small accounts spend their budget with nothing to show for it.

## Brand bidding and the pause test

Bidding on your own name protects it when competitors bid on it. If nobody else bids on it and your website already fills the results page, test pausing the brand campaign and watch the total results from brand searches (paid plus unpaid), not only the paid ones. If the total holds, the brand ads were taking credit for visits you would have had anyway. If it drops, turn them back on. Give brand its own small budget so it cannot take money from the campaigns you need data from.

## Search catches demand, it does not create it

If almost nobody searches for what is sold, say so, and suggest Meta or another channel instead of forcing keywords nobody types. Google's Keyword Planner (free inside Google Ads) shows rough search volumes. Its figures are forecasts, so label them as forecasts.

## Account structure

Give each of these its own budget:

- **Brand**, never sharing a budget with anything else
- **Non-brand high-intent**: one campaign, with ad groups by theme
- **Competitor**, if run, because its costs are different
- **Remarketing**, separate from Search

Why separate budgets: in a shared budget the cheapest campaign (usually brand) takes the money from the ones you need to learn about.

- **Themed ad groups.** A handful of closely related keywords that share one intent and one promise. If two keywords need different pages or different promises, split them. Two or three responsive search ads per ad group (Google allows up to three enabled).
- **Do not split too thin.** A campaign that cannot reach the [one stop rule](../SKILL.md#the-one-stop-rule) spend gate within a few weeks cannot be judged. Merge it into another. The number of ad groups a budget can judge in 14 days is (daily budget x 14) / (3 x maximum cost per result).
- **Settings to check on every new Search campaign.** Search partners and the Display Network off at first, as a rule of thumb, so the first results are easy to read; test them later as their own change. Location option "Presence" (people in or regularly in the area) rather than the default "Presence or interest", for a business that serves a set area.
- **Do not compete with yourself.** The same keyword at the same match type in two ad groups or campaigns splits the data. Give each search one home (`keyword-cannibalization-check`).

## Keywords and match types

Take keywords from how customers describe the problem (their messages, reviews, your own search terms report), not how the business describes the product. A keyword with few searches and clear intent beats one with many searches and mixed intent.

Match types, in this order:

1. Start on **phrase and exact match** for high-intent terms. Exact match still matches close variants (plurals, misspellings, same meaning).
2. Read the search terms report weekly (below).
3. Add **broad match** only when the count is real, the campaign uses a smart bidding strategy, and it already gets regular results. A rule of thumb is about 30 real results a month in the campaign. Google recommends broad match with smart bidding, so this is the kit's caution for small accounts, not Google's rule.

**AI Max for Search** follows the same caution. It matches searches beyond your keyword list, can rewrite ad text to fit the search, and can send clicks to other pages on your site (final URL expansion). If you test it: exclude pages that should not get ad traffic (jobs, blog, login), check the search terms and landing pages it chose each week, and compare against a campaign without it.

## Negative keywords

A negative keyword stops your ad showing for searches that contain it.

- **Build time:** add only the business's own name as a negative in non-brand campaigns, so brand searches go to the brand campaign. No starter list. A word that looks like junk for one business is the best customer for another: "free" is the best search term for a business that offers a free trial lesson, "course" is the product for a training business.
- **After data:** add negatives from the search terms report only, as `search-term-mining` describes. A search term qualifies when its meaning is something the business plainly does not sell (it skips the spend gate, with the evidence shown), or when it has passed the [one stop rule](../SKILL.md#the-one-stop-rule) gate with zero results.
- **Check every candidate** against searches that convert, so it blocks nothing that brings results.

How negative match types behave (confirmed on Google's help pages): negatives do not match close variants. A negative broad match keyword blocks a search only when all its words are in the search, in any order, so the negative broad "free trial" does not block "free" alone. A negative phrase blocks the words in that order. A negative exact blocks only that exact search. Most accidental over-blocking and under-blocking comes from this.

Negate the clearly wrong, not the merely uncertain. An uncertain term needs more data.

## The weekly search terms review

Once a week for each campaign, three passes:

1. **Waste.** Terms with a meaning the business does not sell, and terms past the spend gate with zero results. Propose them as negatives.
2. **Winners.** Search terms that bring results and are not keywords yet. Propose adding them as phrase or exact keywords in the right ad group.
3. **Drift.** Phrase or broad matches pulling in a nearby but wrong meaning. Propose a tighter match type or a negative.

All three are proposals for the owner, shown with the term, its clicks, cost and results, and the dates.

## Bidding

Rules of thumb, not Google's rules (Google publishes no minimum number of conversions for Target CPA):

| Real results a month in the campaign | Bidding |
|---|---|
| Count not yet real | Manual cost per click, starting no higher than the break-even cost per click |
| Count real, few results | Maximise conversions without a target |
| About 30 or more, steady | Maximise conversions with a target cost per result (Google now also calls this Target CPA), set at the owner's target and no lower than what results have really cost lately |
| Real sale values reported back | Maximise conversion value, with a target return when values are steady |

Avoid Maximise clicks once the count is real and the goal is results: it buys clicks, not results. Enhanced CPC no longer exists for Search (Google ended it in March 2025). Change targets in small steps and wait at least a week or two between them, because each change makes the strategy relearn. Budget facts from Google: a campaign can spend up to 2 times its average daily budget on one day, and no more than 30.4 times the daily budget in a month, so a single high day is normal.

## Quality Score and landing pages

Quality Score (1 to 10, per keyword) is Google's diagnostic of expected click-through rate, ad relevance and landing page experience. Google describes it as a diagnostic, not a target. A low score usually means paying more for the same position, so fix the weak part before raising the bid (`quality-score-breakdown`). What helps the page: the headline repeats the promise of the ad and the search, one job and one button per page, a page that loads quickly on a phone, and proof near the top. Form length is a filter: short forms bring more leads of lower quality, longer forms fewer and better ones. Ask only for what the business needs at that step (`landing-page-audit`).

## Performance Max

Order of value for most small accounts: brand Search, then high-intent non-brand Search, then remarketing, then Performance Max, then broad awareness. Performance Max earns budget only after the clearer Search wins are working. Do not run it as the first campaign, on a count that is not real, or on a budget that cannot pass the spend gate.

When it does run: add the brand name as a brand exclusion (or it can take credit for brand searches that Search would win more cheaply), give it audience signals from the owner's own customer list, check its search terms insights for overlap with Search keywords, and compare the quality of its leads with Search leads in the owner's own records. Supply your own video if possible, or Google may build one from your images.

## The weekly scorecard

Seven numbers, each against the account's own earlier weeks, not a benchmark: spend, results by the owner's count, cost per real result, the share of leads that become customers (from the owner's records), Search impression share, impression share lost to budget, impression share lost to rank. Lost to budget means the budget ran out before the day ended; lost to rank means the bid or Quality Score was too low to show. They are different problems with different fixes.

---

*Adapted from practitioner playbooks, notably Ivan Falco's ads-skills, via Corey Haines' marketingskills (MIT). Platform facts checked against Google Ads Help in November 2026; every number not credited to Google is a rule of thumb.*
