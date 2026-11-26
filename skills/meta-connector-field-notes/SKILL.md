---
name: meta-connector-field-notes
description: Hard-won notes on building Meta campaigns through Meta's official ads connector - draft mode, the image rule that breaks ads, locations, under-18 limits, and how to find errors the connector hides. Read before creating or publishing anything through the Meta ads connector, or when a draft ad will not publish.
metadata:
  origin: "Original to this kit. Learned from real campaign builds, October to November 2026."
---

# Meta connector field notes

These notes come from building real campaigns through Meta's official ads connector (`https://mcp.facebook.com/ads`). The connector was in open beta at the time, so details will change. Every note was last seen in October or November 2026. Treat each note as "check this first", and trust what the connector returns over what is written here.

## How the connector behaves

- **Creating does not spend.** Meta's pages say new campaigns, ad sets and ads are created paused. In these builds they appeared in the Ads Manager draft. Either way nothing spends until it is published or switched on, so read the status on screen.
- **Publishing is live.** The activate or publish call makes things run. Never call it without a clear yes from the person for those exact objects. See `launch-paused`.
- **Errors come back with the object.** Each result carries a list of active errors. Read it every time and fix what it says before moving on.

## Build order that works

1. Campaign, with the budget set at ad set level and no campaign budget
2. Ad set: daily budget, placements, audience, optimisation goal
3. Upload media
4. Creatives
5. Ads
6. Preview each ad by its creative

After each step, read the object back and compare it with the plan.

## Things that go wrong, and the fix

**Budgets are in the smallest unit of the currency.** For pounds, dollars and euros, 2000 means 20.00, not 2,000. For a currency with no smaller unit, such as yen, 2000 means 2000. Check the budget on screen in Ads Manager before anything is published.

**Media needs a public address.** Uploading a file from the computer needs a widget. The reliable route is to give the connector a public link to the image or video.

**Image link and image hash together break the ad.** Passing an image link when creating a creative can store both the link and Meta's hash for it. The ad then fails with an error about a redundant spec. Fix: read the image hash from the account's image list, recreate the creative with the hash only, then create a new ad. Then try to delete the broken ad. If the connector refuses because the ad was never published, leave it and see the note on draft-only objects below.

**Addresses are not accepted as locations.** A location given as a street address is rejected ("could not geocode"). Give latitude and longitude instead. Look the coordinates up first.

**Audiences under 18 are tightly limited.** For an audience that includes under-18s, only age and locations of city size or larger are allowed. No radius pins, no interests, no location types. An ad set that breaks this is rejected at publish, not when it is created.

**There is no interest search.** The connector cannot look up detailed targeting options. Either leave targeting broad, or read the ID of a known option from an older ad set that already uses it. Let the person add interests in Ads Manager if they want them.

**Instant lead forms cannot be created.** For leads, use a website campaign that optimises for a lead event from the pixel, or have the person build the form in Ads Manager.

**The Instagram account may look missing.** The list of Instagram accounts can come back empty even when one is attached. Ads still run on Instagram. Pass the Instagram account ID on creatives when you have it.

**A landing-page-view goal needs an event.** Giving only the pixel as the promoted object is rejected at publish. Include the event type as well, or leave the promoted object out.

## Finding errors the connector hides

- **A draft that says "needs validation" with no errors** has not been checked yet. Save its name again, unchanged. That makes Meta re-check it and return the real errors.
- **A publish call can report success and still fail.** The call returns "publishing" even when Meta later rejects some objects. Rejected objects stay in the draft, shown as being edited, with an empty error list. Re-save them to see the real error.
- **Publish one campaign at a time**, and list only the objects you mean to publish. Old draft ads with errors can block a whole batch.
- **Draft-only objects cannot be deleted through the connector.** They stay as clutter until the person uses "Discard drafts" in Ads Manager.
- **An edit in Ads Manager can break a connector-made ad.** It can turn the ad's creative into an inline copy with no image. Fix: point the ad back at its original creative ID.

## Reading your own account

Your own ads, ad sets, targeting and breakdowns by age, gender, placement and country are all readable through the connector. Its Ad Library search is thin, so for competitor research use `meta-ad-library-research`.

## Rules

- Decide goals, budgets and audiences with the person, option by option. Do not assume and set.
- Say plainly when you are not sure how the connector behaves. Test with a draft, never with a live object.
- If something here turns out to be wrong, believe the connector.
