---
name: tracking-preflight
description: The check to run before any ad money is spent, and whenever results look wrong. Confirms the pixel or tag is on the site, the right action is counted once, and links are labelled. Use for "is my tracking working", "conversions look wrong", "before I launch", or zero conversions with real clicks.
metadata:
  origin: "Original to this kit."
---

# Tracking preflight

If conversions are not counted correctly, every other decision is made on wrong numbers. Run this before the first launch and again whenever results look odd.

## What you need

- The website address and the page a person reaches after converting (the thank-you page, or the event that fires)
- Read access to the ad account through a connector, or screenshots of its conversion settings
- The one action that counts as success for this business

## The six checks

Work through them in order. For each one, record **pass**, **fail** or **not checked**, and say how you checked. Never guess a pass. Every tool named here is free.

1. **The code is on the site.** Open the landing page, view its source (right-click, then "View page source") and search for `fbq(`, `gtag(`, `googletagmanager.com` and `GTM-`. A tag loaded through Google Tag Manager does not show up in the source as `fbq(` or `gtag(`. You will only see the `GTM-` container. In that case use the browser tools: Meta Pixel Helper (a Chrome extension from Meta) lists every pixel that loads, and Google Tag Assistant (tagassistant.google.com) lists every Google tag. Note each ID you find. Two different IDs of the same kind, or one ID loading twice, is a fail until it is explained.
2. **The success action exists.** There is an event or conversion action for the real success moment. A page view alone does not count. In Google Ads, open Goals, then Conversions, then Summary, and list each action with whether it is marked primary. In Meta, open Events Manager and list the events it receives. Name the one that means success.
3. **It fires once.** Walk through the conversion yourself, or ask the person to, with Meta Pixel Helper or Tag Assistant open. In Meta, the Test events tab in Events Manager shows each event as it arrives. One real action must produce one event. Two means double counting, and none means it is broken.
4. **One primary conversion.** The campaign optimises for one action. In the Google conversions summary, count the actions marked primary that the campaign uses. Several primary actions, or a soft one such as a page view, mislead the platform and inflate the count.
5. **Links are labelled.** Ad links carry UTM labels (source, medium, campaign) so analytics can tell ad visitors from everyone else. Use `utm-tracking-generator` if they are missing. For Google Ads, also check that auto-tagging is switched on in the account settings.
6. **The numbers agree.** Compare the last 7 to 30 days of conversions in the ad platform with the business's own record (orders, form entries, CRM). A gap of more than about 20% needs an explanation before spend goes up.

If nobody can run a live test, because the owner cannot use the tools or you only have a saved copy of the page, read the code you have. Report what it shows as "seen in the code", and mark the firing checks "not checked". Only a live test shows that an event fires once.

Menus move. If a path here does not match what the person sees, ask what is on their screen.

## Common causes when a check fails

- The tag was added in two places, so everything fires twice.
- A site redesign or domain move removed the tag from some pages.
- The thank-you page can be reached without converting, so visits to it are counted as conversions.
- The consent banner blocks the tag for most visitors.
- The conversion counts a button click, not a completed form.

## Output

```
Tracking preflight: [site], [date]
1. Code on site:        pass / fail / not checked, with what was found
2. Success action:      ...
3. Fires once:          ...
4. One primary:         ...
5. Links labelled:      ...
6. Numbers agree:       ...

Safe to spend: yes / no / not yet
Fix first: [the single most important fix, in plain steps]
```

## Rules

- Do not change tags, pixels or conversion settings yourself. Give the steps and let the person apply them, or ask for a clear yes for each change.
- Never ask for passwords or tokens.
- If a check cannot be done, say so and mark it "not checked".
