# Meta creative variety playbook

Meta described Andromeda, its ad retrieval system (the part that picks which ads are worth considering for each person), in late 2024 and rolled it out through 2025. Practitioners report that variety of creative matters more since then, and that the older habits of narrow interest stacking and a single scaled winner work less well. Treat what follows as practitioner method to test on your own account, not as platform fact. Meta's current help pages are the authority on how delivery works.

## Variety of creative is the main lever

- Practitioners describe fresh creative as the thing that keeps delivery healthy. Ads of the same type shown to the same people tire out, and Meta labels this on the ad ("Creative fatigue", "Creative limited") by comparing cost per result with your earlier ads. Meta publishes no frequency or fatigue numbers.
- Simple still images are quick and cheap to make, so they let a small team test more ideas than video does. Some advertisers report that plain, native-looking stills beat expensive video. Test it on your own account before believing it.
- Set aside a regular hour each week to make a few new ads for the offer that already works. Volume of genuinely different ideas matters more than polish.

## Creative does the targeting (broad audience, specific creative)

- The older approach stacked interests and narrowed the audience, hoping to find the right buyer. The approach practitioners now describe is to target broadly (for example, just the country) and let the creative say who it is for.
- Some advertisers find longer ad copy helps, because it tells the right person more about the offer. Test it rather than assuming.
- How to test: take your best ad that runs with narrow targeting, duplicate it into a new ad set with no extra targeting, and run both side by side for at least 7 full days under [the one stop rule](../SKILL.md#the-one-stop-rule).
- Broad often wins when the account already gets enough results for Meta to learn from. Meta's own learning bar is about 50 results a week per ad set. On a small account that is below that bar, test broad against your current ad set and keep the one that costs less per result. Do not switch everything.

## Identity words in the copy

- Take your winning ad and duplicate it with a word that names a group, placed in the headline or the first line of the copy.
- Example (made up for illustration): "Weekly maths lessons for your child" becomes "Weekly GCSE maths lessons for Year 10". The new words tell the right parent "this is for me", and they help Meta see who the ad suits.
- Check each version against your usual claims rules (`ad-claims-check`) before it goes live, and keep the offer itself true.

## Same-voice variants of a proven ad

- Take your winning ad and ask Claude to make versions for a named group. A prompt that works:
  > Read this ad and be its author. Imagine I show the next ad to 100 people who know this writer: not 1 in 100 should be able to tell it was written by someone else. Now write it for [group].
- The output should read almost the same, with small shifts in what matters to that group. Work in order: body copy, then headlines, then the image.
- Put the variants in one ad set and let Meta spread the spend.
- Limit: variants this close count as one concept. Use them to adapt a proven winner for a group. New reach comes from genuinely new concepts, so keep testing those separately.

## Second chance for passed-over ads

- When you launch many ads in one ad set, Meta often gives most of the spend to a few and leaves the rest nearly unspent.
- An ad that got almost no spend has not been tested, so it has not lost. If you have a good reason to believe in it, move it into its own ad set and see what happens.
- This is something to test, not a promise: some of those ads may do well when they are not competing with the favourites, and many will not. Judge them by the same rule as any ad.

## Native-looking ads

- Polished, obvious-advert styling often gets scrolled past. Look at what content does well natively in your niche on Instagram, Facebook, TikTok or YouTube, and make ads that look and sound like it.
- To see what is working in your niche, use a personal account you already have, or the Meta Ad Library (see `meta-ad-library-research`). Do not create extra accounts for research: fake accounts can break platform rules.
- If you have an organic video that already did well, running that same video as an ad is a strong, cheap test.

## Planning ads across variants

Near-identical ads count as one concept, even when different people make them. A hundred creators making the same talking-head video amount to one idea, and copies of a winner can take reach from the winner. Credit for this lesson sits in the bottom line.

- **Plan on three axes.** Every ad argues one **concept** (a single truth about the product), through one **angle** (for example "saves time" or "works with what you already use"), to one **awareness level** (new to the category, or already comparing options). Put these in a small table. It shows which concept, said which way, to which audience, is winning. Without it you pay for lessons you cannot read back.
- **Judge ads on the result that matters.** For a small business that is a booked trial lesson or a sale, not a page view or a click. If that result is too rare to optimise on, optimise on an earlier step but still judge the ads on the real result. See [meta-decision-system.md](meta-decision-system.md) for the weekly results bar.
- **Test the funnel inside Instagram's in-app browser before spending.** Open a real ad preview on a phone and tap through. Check that the page loads, the promise matches the ad, and every event reaches your analytics (`tracking-preflight`). Safari on a desktop does not count, because most people see your page inside the app.
- **Read the funnel stage by stage.**
  - People watch but few click: the ad earned attention but not the click.
  - People click but few convert: the landing page breaks the ad's promise (`landing-page-audit`).
  - Conversions arrive but from the wrong customers: look at the offer, the targeting and the campaign structure. On a small account a cost cap can stop delivery, as a cost per result goal set too low does, so change it with care.
- **Give each ad a fair run.** Follow [the one stop rule](../SKILL.md#the-one-stop-rule): at least 7 full days and the spend gate before judging. A Friday launch meets a different audience than a Monday one. A winner can also weaken when its budget is raised a lot at once, so raise budgets in steps you can afford and watch each step.
- **Keep a lessons file.** A short note you update after each test: what you tried, what happened, what you will try next. Draft the next round of ad ideas from it.

## Ad sequencing (build the path, not one winner)

Meta has said its ranking models read a person's activity as an ordered timeline. The practical idea: the second ad someone sees is judged against the first. Stop testing every ad in isolation and ask what ad 2 says to someone who has already seen ad 1.

Explicit sequencing in auction campaigns has been rolling out account by account. The setup is narrow, so check Meta's current help pages before planning around it. As reported by practitioners:

- Objective: Awareness (Maximize reach) or Engagement (ThruPlay), not Sales or Leads.
- Frequency control set to Target frequency, not the default cap.
- Lifetime budget at the ad set level, for at least 7 days, with Advantage campaign budget (campaign budget optimisation, where Meta splits one budget across ad sets) off.
- At least two ads in the ad set.

Size the sequence to the flight. A 3-week flight showing one ad every 7 days fits three ads. Two or three ads is the usual range, because longer paths lose people.

A typical path is hook, then problem, then proof (a real review or case study), then offer. Each ad assumes the last was seen, so ad 3 does not explain the product again.

Trade-off: target frequency usually costs more per impression than standard delivery, so judge a sequence on later results, ideally against a group that does not see it, rather than on the cost of impressions. For conversion objectives, where sequencing is not available, approximate the path with retargeting: people who watched or engaged with the hook ad see the proof ad, then the offer.

---

*Framework lineage: adapted from Corey Haines' marketingskills pack (MIT). The method on creator-ad volume and the three-axis plan draws on a Wispr Flow marketing lead's account of scaling ads; sequencing framing from Cody Schneider and Jon Loomer's testing. These are practitioner reports, not platform statements.*
