# Meta decision system

A routine for deciding which Meta ads to stop, keep, graduate or scale, built on two of the owner's numbers so each decision is arithmetic. It applies [the one stop rule](../SKILL.md#the-one-stop-rule) to Meta and adds Meta-specific checks. Every action here is a proposal for the owner, never a change made on your own.

Terms used: an **ad set** holds the budget, audience and placements; **CBO** (campaign budget, which Meta now calls Advantage campaign budget) lets Meta split one budget across ad sets; a **result** is the one thing that counts for the business (a booked trial, a sale, a qualified lead).

## The two anchor numbers

- **Target cost per result:** what the owner would be happy to pay.
- **Maximum cost per result:** the most they can pay and not lose money. `cost-ceiling-planner` works it out.

For lead generation, count the leads the owner would actually call worth having (a qualified lead), from their own records, where they track it. If only a share of leads are any good, the real cost per good lead is the cost per lead divided by that share. Example: £20 per lead and 40% of leads are good means £20 / 0.4 = £50 per good lead.

Review both numbers monthly with the owner.

## How many ads the budget can feed

More live ads than the budget can feed means every ad starves and nothing gets a fair read.

```
ads (or ad sets) the budget can judge in 14 days = (daily budget x 14) / (3 x maximum cost per result)
```

Example: £30 a day and a £45 maximum. 30 x 14 = £420. 3 x 45 = £135. 420 / 135 = 3.1, so about 3 ads in testing at once. To launch a new test at that limit, something has to stop first.

## Two campaigns once there is a winner

A small account starts with one campaign. Once at least one ad is a proven winner (below), a common structure is two campaigns over the same audience:

- **Main campaign**, most of the budget, holding only proven ads.
- **Testing campaign**, a smaller protected budget, holding new ideas.

Why: inside one campaign budget, Meta tends to give proven ads the spend, so new ads never get enough to be judged. The split protects the test budget. It is a practitioner habit, not a Meta rule, and it only makes sense when the testing budget alone can pass the spend gate for at least one ad in about two weeks.

Test a new idea as a simple image first where you can, and make the video version once the idea works, unless the idea only works as video (a demonstration, a testimonial).

## Testing the page as well as the ad

When the landing page is the biggest unknown, run the same ads into separate ad sets that differ only in the destination (for example the main page versus a shorter page, or a page versus a Meta instant form). Holding the ads the same makes the difference between ad sets the page. Judge each ad set with the spend gate. This is a practitioner-reported pattern, so test it rather than assume it.

## Stage 1: is Meta delivering it? (day 7)

Meta's spend split is a signal in itself. At day 7, for each test ad:

- Fair share = (campaign daily budget / number of active ads) x 7 x 0.5. An ad that spent less than this has been largely passed over by Meta. Propose replacing it with a new idea. This is a delivery judgement, not a results judgement, so it does not need the spend gate.
- An ad with no spend at all after 7 days: propose replacing it.

When reworking an ad Meta passed over, change the opening (the hook, the image or the format). Too few people saw it for the wording further down to matter.

## Stage 2: is it bringing results? (weekly, last 14 days)

Run in order and stop at the first that applies:

1. **Count check.** The owner's count must be within about 20% of Meta's for the same dates. If not, stop here and fix tracking (`tracking-preflight`).
2. **Spend gate.** Spent less than 3 times the maximum since its last significant change, or fewer than 7 days: **wait**. If the true cost per result were exactly the maximum, zero results after spending 3 times it would happen about 5% of the time; at 2 times, about 14%.
3. **Zero results past the gate:** propose stopping it, and drop the idea rather than reworking it.
4. **Quality** (only where the owner tracks lead quality): leads but none worth having means the angle attracts the wrong people. Propose a replacement with the same format and a different angle, and wording that tells the wrong people it is not for them.
5. **Cost:** at or under the target is a candidate winner. Between target and maximum, keep it and watch. Above the maximum, propose stopping it or fixing its weakest part.

Leave out the last few days that are still inside the normal delay between a click and a result.

## Graduating a winner

Move an ad from testing to the main campaign only when all of these hold: at least 5 results on the owner's count, cost per result at or under the target, running at least 14 days, and at least one result in the last 7 days. Launch it as a new ad in the main campaign. Do not edit the original.

## Signs an ad is wearing out

Meta publishes no frequency or fatigue thresholds. It does show its own labels in Ads Manager, such as "Creative limited" or "Creative fatigue", based on how an ad's cost per result compares with your past ads. Use those, and compare each ad with its own first week using the daily export: click-through rate falling, cost per thousand impressions rising, cost per result rising, frequency (average times each person saw it) climbing. Thirty-day totals hide this. `creative-fatigue-detection` has the full method.

Editing a live ad's creative restarts its learning; pausing does not. Launch the refreshed version as a new ad alongside the old one.

## Swap rules

Do not stop an ad that still brings results until its replacement is live. Keep one or two new ads ready. What to change depends on why it stopped working: passed over by Meta, change the hook or image; results but wrong people, change the angle; results too dear, change the offer or the audience; worn out, make a fresh version of the same proven idea.

## How many new ads to make

```
tests the budget can judge each month = (monthly budget x share given to testing) / (3 x maximum cost per result)
```

Example: £900 a month, a fifth for testing, £45 maximum: (900 x 0.2) / 135 = 1.3, so about one new idea a month can be judged properly. Plan production to match, and expect most new ideas not to beat the current winner.

When refreshing a winner, change the parts in this order of likely effect: the hook (who stops to look), the visual, the format, then the text and button.

## Scaling

Propose more budget only when: cost per real result has been at or under the target for two weeks in a row, there is at least one replacement ad ready, and the ads are not showing Meta's fatigue labels.

- Raise by about a fifth at a time, at most once a week. Meta says a budget change may count as a significant edit, which restarts learning, depending on its size, and gives no percentage. The fifth is a rule of thumb.
- If cost per result rises above the maximum after a step, propose going back to the previous budget and holding for two weeks.

## Lead forms (Meta instant forms)

Forms that fill themselves from the person's profile bring many leads who barely remember sending them. Ways to raise quality, each a test:

- Use the **Higher intent** form type, which adds a review step before sending.
- Ask one to three short questions that sort serious enquirers from the rest.
- Make the thank-you message say exactly what happens next and when.

Form or landing page: test both if the budget allows two ad sets. Judge them on the owner's count of good leads, not on Meta's lead count.

## Advantage+ campaigns

Advantage+ is Meta's name for its more automated campaign set-ups. They need enough results to learn: Meta's learning phase ends after about 50 results in the week after the last significant edit. Budget for that is roughly the target cost per result x 50 / 7 per day. Example: £25 target x 50 / 7 = about £179 a day. Below that, the campaign stays in learning, which is normal on a small budget but means its results swing more.

## Partnership ads

A partnership ad runs from a creator's or partner's account with their permission, so it reaches people who already follow and trust them. It is a way to reach new people once the main campaign has stopped finding them. Judge it with the same spend gate. Promote content that already does well with the creator's own audience, pick a creator whose followers are the business's customers, and agree in writing how long and where the ad may run. Formats are covered in [meta-creative-formats.md](../../ad-creative/references/meta-creative-formats.md).

## Weekly routine

- Once a week: pull the last 14 days by day, run Stage 2 on every test ad, look for wearing-out signs on every main ad.
- Mid-week: launch new tests into free slots; run Stage 1 on ads that reached day 7.
- Monthly: review the target and maximum with the owner, and the list of ads.

---

*Adapted from practitioner operating systems, notably Ivan Falco's ads-skills, via Corey Haines' marketingskills (MIT). Learning phase and lead form facts checked against Meta Business Help in November 2026; every other number is a rule of thumb.*
