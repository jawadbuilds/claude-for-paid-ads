# Playbook for lead generation with long sales cycles (B2B)

Rules for businesses that sell to other businesses (B2B), where a sale can take weeks or months after the first enquiry, the platforms' conversion counts mislead, and the quality of a lead matters more than its cost. A small consumer business selling a one-off product or a local service will find most of this heavier than it needs; the parts on lead quality and break-even still apply. Use it with the [Meta decision system](meta-decision-system.md) and the [Google Search playbook](google-search-playbook.md). Stop, keep and scale decisions follow [the one stop rule](../SKILL.md#the-one-stop-rule).

## Five stages, past the funnel

The usual funnel stops at the first conversion. A B2B sale does not: lost deals, open deals and existing customers can all be reached with ads. Plan across five stages:

| Stage | Aim | Typical offer | What to measure |
|---|---|---|---|
| Create | Become known and trusted | Useful content, a point of view | Cost per person who consumed it, cost per sales opportunity overall |
| Capture | Turn buyers who are looking into leads | Demos, trials, quotes | Sales pipeline value per pound spent, cost per opportunity |
| Accelerate or activate | Close open deals faster, or turn free users into paying ones | Case studies, webinars, events | Time to close, paid sign-ups |
| Revive | Restart lost deals | A new offer or a guided trial | Opportunities restarted, cost per opportunity |
| Expand | Grow existing customers | Referral schemes, new features | Extra revenue from customers |

The lower stages (expand, revive, accelerate) are small, cheap and quick to pay back. Create is the biggest and slowest. Building from the bottom up usually shows a return sooner.

## Leading and lagging signals

When deals close in six months you cannot steer on closed sales. Split every stage's numbers:

- **Leading** (move within a month, steer on these): click-through rate, cost per lead, cost per qualified lead.
- **Lagging** (move over months, the truth, reviewed monthly or quarterly): sales pipeline per pound spent, revenue the ads helped win, time to close.

The leading number must track the lagging one. If cost per lead falls while the pipeline does not grow, the leading number has stopped meaning anything. Fix what you count before touching the ads.

## Break-even cost per lead and per click

Work targets out from the business's own numbers, not from benchmarks:

```
break-even cost per lead (on revenue) = average deal value x share of leads that become customers
break-even cost per click             = cost per lead you can pay x landing page conversion rate
```

Example: deals worth £3,000 on average and 1 lead in 10 becomes a customer gives £3,000 x 0.10 = £300 per lead. At a 5% landing page conversion rate, £300 x 0.05 = £15 per click.

This break-even is on revenue, not profit. A business paying £300 per lead here loses money once its own costs are counted. Set the maximum cost per lead below it by the margin the business needs, as `cost-ceiling-planner` does. That maximum is the number the one stop rule uses.

## Stopping and keeping

There is no separate kill rule in this file. Use [the one stop rule](../SKILL.md#the-one-stop-rule) with the maximum cost per **qualified** lead where the owner tracks quality: check the count, wait until the ad has spent 3 times that maximum and run 7 days, allow for the delay before leads are judged, then propose. Never stop an ad that still brings good leads before a replacement is ready.

## Optimising for quality, not form fills

The platforms' bidding aims at whatever you tell them is a conversion. Tell them "form filled" and they find cheap form fillers: cost per lead falls while sales dry up. In order:

1. **Send later outcomes back to the platform.** When a lead becomes a qualified lead, an opportunity or a customer, upload that event: Google's offline conversion import (matched on the click ID, `gclid`) and Meta's Conversions API with lead stages. Both are free features but need set-up; check the current help pages.
2. **Value different results differently.** A demo request is worth more than a guide download.
3. **Until that works, read lead quality by hand every week**: who the leads are, not only what they cost.

Compare platform conversion counts with the owner's records monthly. When they disagree, the owner's records win.

## Scoring lead quality

The platform cannot see lead quality, so the person who talks to leads scores each one from 0 to 3 on three things:

- **Urgency:** 0 just browsing, 3 needs it now with a date.
- **Budget:** 0 no budget or authority, 3 budget agreed.
- **Fit:** 0 not the kind of customer the business serves, 3 exactly that kind.

Log each score against the ad that brought the lead. After about 20 scored leads per ad, compare ads by average score as well as cost. The ad with the cheapest leads is often the one bringing the weakest ones. A spreadsheet is enough.

## Ways to grow, by what limits you

| | Little effort | More effort |
|---|---|---|
| **Budget available** | Wider audiences, more segments | New countries or regions (needs translated pages and ads) |
| **Budget limited** | New ads, angles and formats | A different objective or bidding approach that buys results more cheaply |

## Can you measure it?

Before adding budget, check that you can see: results by channel, a working conversion count (checked with `tracking-preflight`), website analytics, and leads followed through to sales in the owner's records. If any of these is missing, fix it before spending more, because every judgement will be a guess.

## Trying a new channel

Before committing to a new channel, run a small test with a fixed budget (for example enough for a week or two) to learn what clicks and impressions really cost for your audience. Published benchmarks and platform estimates are often wrong for a specific audience. Judge results, not only costs, with the spend gate.

---

*Adapted from practitioner playbooks, notably Ivan Falco's ads-skills, via Corey Haines' marketingskills (MIT). Every number here is either the owner's own or a worked example.*
