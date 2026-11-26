# Google Ads audit checklist (ecommerce)

An itemised audit of a live ecommerce Google Ads and Merchant Center account: 31 items across 10 categories (29 scored, 2 marked as ideas and not scored). It is built to find wasted spend, find new customers to reach, and spot extra revenue before scaling up.

This checklist is for ecommerce accounts. Lead-gen and local service accounts should mark the Merchant Center and Shopping items "not applicable" and work through the rest.

**Load [audit-guardrails.md](audit-guardrails.md) first. It governs how every item below is scored.** Each check resolves to exactly one of four results: pass, fail, unknown or not applicable. An unknown (the evidence was not available) lowers coverage and never lowers health. Not applicable (for example, Shopping checks on a lead-gen account) affects neither. Do not grade what you could not see, do not invent negative keywords, and draft every change before touching a live account.

Work from top to bottom. For each item, record the result, the evidence you saw (or the missing source), and, on a fail, a draft fix rather than an applied one.

---

## Tracking

1. **Conversion tracking configuration.** Confirm a single source of truth for purchases. Two systems counting the same order (a GA4 import plus the native tag, or a duplicate Google tag) inflates conversions and makes the bidder chase volume that is not real. Fail if orders are double counted or the purchase value is missing. Pass on a verified test conversion with the right value and currency. Deep dive: `tracking-preflight`.

## Targeting

2. **Customer list for audience targeting.** Check that a hashed customer email list (emails scrambled before upload) is uploaded and actually used: as a signal for Performance Max and Demand Gen (lookalike segments in Demand Gen need a seed list of more than 100 matched people), and as an exclusion where it belongs (existing buyers on campaigns not meant for upsell). Uploaded but unused is a fail. Deep dive: Customer Match in [audience-targeting.md](audience-targeting.md).
3. **Negative keyword lists** *(Search, Shopping)*. Review shared and campaign-level negatives for queries that are irrelevant, out of market or unprofitable and are using up budget. No search terms report means unknown, not fail. Never name candidate negatives from imagination: request the report and run the overblocking review (see audit-guardrails).

## Campaign structure

4. **Branded and non-branded split.** Keep brand traffic in its own campaign. Brand terms buried inside generic or catch-all campaigns inflate blended ROAS (return on ad spend: revenue divided by spend) and hide weak non-brand results. Fail if brand and non-brand share a campaign with no way to read them apart.

## Merchant Center

5. **Shipping settings.** Confirm the configured shipping speeds and costs match what the business really does. Understated speed loses auctions, and overstated speed risks disapproval. Free-shipping thresholds should show.
6. **Promotions.** Check that live sales, discounts and standing offers are set up as Merchant Center promotions, so they can show as promotion links on Shopping ads. Missing promotions mean lost clicks.
7. **Product feed titles.** Titles are cut off when shown, so the words that matter most should come first. Check that the main search keyword, then the key feature, sit near the start of the title (roughly the first 70 characters; check Merchant Center's own guidance). A brand-first title wastes that space unless the brand is what people search.
8. **Product images.** Judge whether images stand out in the Shopping results (clean, on a white background where required, but different from competitors). Weak images limit clicks whatever the bid.
9. **Store quality overview.** Read the Merchant Center diagnostics: disapprovals, missing or invalid attributes (GTIN, availability, price mismatches) and feed warnings. Disapproved products earn no impressions and nobody is told.
10. **Product ratings.** Check that product ratings sync from the review source and show as stars. A feed that is set up but shows no stars is worth chasing.
11. **Impressions on eligible products.** Check the whole catalogue is getting served, rather than a handful of hero products taking all the impressions. Eligible products with zero impressions are untested stock.

## Shopping

12. **Campaign segmentation.** Check each Shopping or Performance Max segment has enough conversions to let the bidder learn. A common rule of thumb is about 30 to 50 or more a month. It is a habit, not a Google rule, so compare with the account's own results. Too many segments starve every one, so consolidate before adding structure.
13. **Budget allocation across products.** Trace whether spend goes to the products that earn their cost. If losers use the budget while winners are capped, that is a reallocation fail. Draft the shift, and do not restructure a learning campaign as a reflex.

## Bidding and budget

14. **Bidding strategy for brand** *(Search)*. On brand, clicks are cheap and close to certain. A basic target ROAS or Maximise conversion value strategy can let Google overpay for volume you would win anyway. Consider tighter control, or a modest target, on brand.
15. **Campaign bidding targets.** Sanity-check every target ROAS or target CPA against the campaign type (brand or non-brand, hero products or long tail). One blanket target across mismatched economics is a fail. Per audit-guardrails, one budget-to-CPA ratio does not fit every objective.
16. **Non-branded terms in brand campaigns.** Read the brand campaign's search terms for generic queries that leaked in. Move them to non-brand so brand ROAS is not propped up by spend meant for finding new customers.
17. **Bidding strategy for non-brand** *(Search, Performance Max, Shopping, Demand Gen)*. Match the strategy to the volume and the goal. Value-based bidding needs conversion data, and thin campaigns may need manual bids or target CPA first. A strategy that does not fit low volume never leaves learning. Google publishes no minimum number of conversions for Target CPA. It suggests judging over 30 days with at least 30 conversions, so treat any "you need N conversions" figure as a rule of thumb.

## Search

18. **New search terms for expansion.** Mine the search terms report for converting queries you do not yet target directly. Add them as keywords, and feed the wording back into product titles and content. The same report gates item 3, so pull it once and use it for both.
19. **Ad copy performance.** Check click-through rate (the share of people who see the ad and click it) against the account's own earlier period, and whether weak ads are being refreshed. Ad strength is not used to calculate Ad Rank or Quality Score, so do not chase it for its own sake. Weak copy raises cost per click through Quality Score before it ever costs a sale.
20. **Brand keyword match types.** Brand keywords usually run exact or phrase match. Broad match on brand invites Google to spend brand budget on loosely related, lower-intent queries.
21. **Brand ad copy quality.** Verify brand ads use consistent formatting, lead with the main selling points and follow the promotional calendar. Brand is the highest-intent surface, so generic brand copy underperforms with an audience that is already close to buying.
22. **Quality Score.** Low Quality Score means a higher cost per click and a lower position for the same bid. Read it as a diagnostic (expected click-through rate, ad relevance and landing page experience), not something to push up for its own sake.

## Performance Max

PMax means Performance Max, Google's all-channel campaign type.

23. **PMax signals.** Check that asset groups carry audience signals, such as search themes and the customer list, rather than empty signal fields. Signals are advisory, not binding, but empty ones give up a real lever.
24. **PMax budget on Shopping.** Shopping is usually where the money is made inside PMax. Confirm a meaningful share of PMax spend lands there (from the account report or product-level data) rather than drifting to low-intent display and video.

## Landing page

25. **Head-to-head competitor pages** *(not scored, an idea)*. "Us versus them" pages capture people comparing options. Their absence is an opportunity, and a missing page is no defect. Any comparison must be accurate and fair, and carry only claims the business can back up (see `ad-claims-check`).
26. **Advertorials.** Check whether cold Google traffic meets a story-led, editorial-style landing page as well as a plain product page. Keep this only where the page is clearly labelled as an ad, per the platforms' rules.
27. **Landing page optimisation.** Confirm the ad's promise (offer, price, hero product) appears clearly at the top of the landing page. A mismatch between ad and page wastes the click whatever the bid, and fixing it is often the biggest post-click gain. Deep dive: `landing-page-audit`.

## Demand Gen

28. **Performance by format.** Split Demand Gen results by channel (YouTube, Discover, Gmail, Display), as the report shows it. Menus move, so ask what the person sees. A blended Demand Gen number hides both the winner and the drain.
29. **Quiz funnel for cold traffic** *(not scored, an idea)*. A quiz can warm up and sort cold traffic through a personalised path. A missing quiz is not a defect, so list it as an idea only.
30. **Demand Gen demographics.** Analyse performance by age, gender, parental status and household income, if shown, to catch mis-serving and inform exclusions or bid adjustments.
31. **Top-of-funnel campaign** *(Search)*. Confirm something is reaching cold audiences who do not yet know the product, with a conversion goal and not a bare awareness objective. An account that is all bottom of funnel tops out at existing demand.

---

## Deep dives for items 1 and 3

These two checks find the most money on most accounts. When either fails, run the deeper version.

### Conversion signal audit (item 1)

Item 1 asks whether conversions are counted correctly. This asks whether the bidder is learning from the right actions. Smart Bidding (bidding where Google sets the bid for each auction) optimises toward whatever is in the "Conversions" column, so a cheap action included there trains the account to buy more of it. Setup steps live in `tracking-preflight`; this is the audit.

Pull every active conversion action with its category, count setting (one or every), value (static or dynamic), primary or secondary status, and recent volume. Then check:

1. **Low-intent actions feeding bidding.** Newsletter signups, page views, scroll depth, add-to-cart on a lead-gen account, or any form fill that sales would not call a lead. If one is primary, the bidder is optimising toward it.
2. **Double counting.** The same event tracked twice (a GA4 import plus the native tag, or two tags on one thank-you page), or a lead action set to count "every" when a person can submit more than once.
3. **Value mismatches.** A static value on an action whose real value varies (purchases of different sizes, leads that close at different values), or values that ignore margin or close rate.
4. **Primary or secondary.** Only actions that track revenue or qualified leads should be primary. Keep the rest secondary (observation only) so you can still report on them.
5. **Lead quality, for lead gen.** Match a sample of recent conversions to what happened next in the owner's own records. If one action's leads rarely become customers, it should not be teaching the bidder.

End with the single change most likely to improve lead or revenue quality, and what to check before making it. Changing which actions are primary resets learning on every campaign that uses them, so draft it for approval and time it outside a busy period.

### Wasted spend and negatives (item 3)

With a search terms report (and a placement report for Display, PMax or Demand Gen) for the last 30 to 60 days:

1. **Flag only what passes the gate.** First apply [the one stop rule](../SKILL.md#the-one-stop-rule): the owner's own count must be within about 20% of the platform's, and the term or placement must have spent at least 3 times the owner's maximum cost per result with no results, or carry a meaning the business does not sell. Use the break-even conversion rate maths in [reading-google-ads-data.md](reading-google-ads-data.md) before calling low-spend terms wasted. Below the gate, the answer is "too little data to judge yet".
2. **Group them by reason:** irrelevant intent, wrong location, junk placements, competitor terms you do not want, job seekers, and so on.
3. **Split the list in two:**
   - Clear from the account's own data: the meaning is something the business does not sell.
   - Check before excluding: brand-adjacent terms, early research queries, and anything that might help a later sale. These need a human call.
4. **Total the spend each list would have saved last period.** That number is what gets the list reviewed.

The negatives stay a draft for approval. Run the overblocking review in [audit-guardrails.md](audit-guardrails.md) on every candidate. Check match type behaviour in [google-search-playbook.md](google-search-playbook.md): negatives do not match close variants, and a negative broad match keyword blocks a search only when all its words are in the search, in any order.

---

## Rolling it up

- Score only verified items. Present health (pass and fail ratio on verified checks) and evidence coverage (share of applicable checks you could verify) as two separate numbers, and never blend them.
- Follow the coverage bands in audit-guardrails: graded at 80% or more, provisional at 60% to 79%, and below 60% report findings and unknowns instead of a health score.
- List every unknown with the exact evidence needed to resolve it (usually the search terms report, Merchant Center access, conversion action settings, or account-level PMax and Demand Gen reports).
- Deliver fails as draft fixes: current state, proposed change, expected effect and how to undo it. Apply only with the owner's clear yes.

---

*Adapted into this skill's framing from ECHELONN's public Google Ads Audit Checklist (Jackson Blackledge, ECHELONN.IO). Item structure credited; descriptions and scoring are rewritten in this kit's voice and paired with the four-state audit model in [audit-guardrails.md](audit-guardrails.md). The deep dives for items 1 and 3 re-express the conversion signal audit and wasted-spend finder from Marek Dąbrowski's "The Paid Ads Operator's Guide to Claude" (Adlume, 2026-07-16).*
