---
name: launch-paused
description: The safe way to build and switch on a campaign through a connector. Everything is created paused, checked, then switched on one piece at a time by the person. Use for "build this campaign", "set up the ads", "launch", "publish", or any request that would make ads start spending.
metadata:
  origin: "Original to this kit."
---

# Launch paused

An AI that can create ads can also spend money by mistake. This is the routine that prevents it. It applies to every build, on every platform.

## The rule

**Nothing is created live.** Campaigns, ad sets, ad groups and ads are created paused, or as drafts where the platform has drafts. The person switches them on, or tells you to in plain words for that specific item.

## Before building

Agree each of these with the person, one at a time. Show your recommendation and the reason, then let them choose. Do not assume a setting and move on.

1. Goal: the one action being optimised for
2. Budget: daily amount, currency, and the total they are willing to lose while testing
3. Who: country or area, age range, and any restriction
4. Where the ad sends people: the exact landing page address
5. Creative: the images, videos and text to use
6. Dates: start, and end if there is one

Run `tracking-preflight` first. If it says "not safe to spend", stop and fix that.

## Building

1. Write the whole plan as a short table: every campaign, ad set and ad, with its settings. Get a yes for the plan.
2. Create from the top down: campaign, then ad set or ad group, then ads.
3. After each object, read it back from the platform and compare it with the plan. Fix any difference before going on.
4. Read the platform's own error and warning fields after every step. Fix them now. An object with a hidden error will be rejected later, when it is harder to trace.

## Before switching on

Give the person this checklist with the real values filled in:

- [ ] Budget is daily, in the right currency, and the amount is correct (watch for platforms that count in pence or cents)
- [ ] Location and age match the plan
- [ ] Google: Search partners and the Display Network are off unless you chose them. A new Search campaign usually has both switched on
- [ ] Google: location is set to people in the place, not people interested in it, unless you chose otherwise
- [ ] Google: auto-applied recommendations are off, or you know exactly which are on
- [ ] Meta: Advantage+ audience and Advantage+ placements are choices you made, not defaults you missed
- [ ] The landing page opens and loads in under about three seconds
- [ ] The link carries its UTM labels
- [ ] The conversion being optimised for is the right one
- [ ] The preview of each ad looks right on a phone
- [ ] The copy has passed `human-copy-check` and every claim has passed `ad-claims-check`
- [ ] No object shows an error or a rejection

## Switching on

- Switch on one campaign at a time, never everything at once.
- Check it again an hour later and the next morning: is it delivering, is anything rejected, is spend in line with the daily budget?
- Do not judge results for the first few days. Say when you will look again and what would make you stop early.

## Rules

- Never switch on, raise a budget, or delete anything without a clear yes that names that item.
- A yes for one change is not a yes for the next one.
- If the platform publishes immediately with no paused option, tell the person before you call it and let them decide.
