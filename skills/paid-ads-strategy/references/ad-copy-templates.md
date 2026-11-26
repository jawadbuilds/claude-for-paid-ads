# Ad copy templates reference

Formulas for writing ad copy, with made-up small-business examples. Every example below is labelled "Example:" and invents no number, review or customer. Where a real figure belongs, the example shows a placeholder such as [real number]. Put in only a figure you can prove.

Run `human-copy-check` then `ad-claims-check` on any copy built from these formulas.

## Contents
- Primary text formulas
- Headline formulas
- CTA variations
- Platform copy limits
- Copy testing priority

## Primary text formulas

### Problem, agitate, solve (PAS)

```
[Problem statement, in the customer's words]
[What it costs them if it carries on]
[Your service as the fix]
[CTA]
```

Example: a mobile dog groomer (made up for illustration).
> Your dog hates the car, so grooming day is a battle.
> Every trip to a salon means a stressed dog and a lost afternoon.
> We come to your door with a fully equipped van and groom your dog on your drive.
> Book a visit in [area].

---

### Before, after, bridge (BAB)

```
[Current painful state]
[Desired future state]
[Your service as the bridge]
```

Example: a local bookkeeper (made up for illustration).
> Before: receipts in a shoebox and a tax deadline coming.
> After: your books up to date, so you know what you owe.
> We sort your records each month for a fixed fee of [price].

---

### Customer words lead

Use this only with a real quote you have written permission to use. Never write a testimonial yourself.

```
"[Exact quote from a real customer]" ([first name], [town])
[What you do]
[CTA]
```

Example: the structure only. The quote and name are placeholders, not a real customer.
> "[Real quote from a real customer]" ([first name], [town])
> We fit and repair boilers across [area].
> Get a quote.

---

### Feature, benefit bridge

```
[Feature]
[So that...]
[Which means...]
```

Example: a cleaning company (made up for illustration).
> Same cleaner every visit
> So they learn how you like your home kept
> Which means you do not have to explain it again each week

---

### Direct response

```
[Plain statement of the offer]
[Proof you can show: a real number, a real review, a real guarantee]
[CTA]
```

Example: a tutoring centre (made up for illustration).
> GCSE maths tutoring in [town], in small groups.
> [Real number] students taught since [year].
> Book a free trial lesson.

The trial lesson is only worth saying if it really is free and still on offer.

---

## Headline formulas

Write headlines in sentence case: capital on the first word and on names only.

### For search ads

| Formula | Example (made up for illustration) |
|---------|---------|
| [Keyword] + [benefit] | "Emergency plumber in [town]" |
| [Action] + [outcome] | "Get a boiler quote today" |
| [Keyword] + [differentiator] | "Dentist open on Saturdays" |
| [Price or offer] + [keyword] | "Boiler service from [price]" |
| [Keyword] + [trust fact you can prove] | "Gas Safe registered engineers" |

The last row is only for a fact that is true and checkable, such as a registration the business holds.

### For social ads

| Type | Example (made up for illustration) |
|------|---------|
| Outcome | "A tidy garden without giving up your weekends" |
| Specific detail | "What a boiler service includes, step by step" |
| Plain contrast | "Fixed price, agreed before we start" |
| Number of items | "[Number] things to check before hiring a roofer" |
| Local | "Serving [area] since [year]" |

---

## CTA variations

CTA means call to action: the button or line telling people what to do next.

### Soft CTAs (for people still deciding)

- Learn more
- See how it works
- See examples
- Get the guide

### Direct CTAs (for people ready to act)

- Book now
- Get a quote
- Call now
- Sign up
- Shop now

### Urgency CTAs

- Offer ends [real date]
- Limited time: [real offer]

Use these only when true, and check each one with `ad-claims-check`. Never write "Only X spots left" or "Last chance" unless the count or the deadline is real and you can show it.

### Action-oriented CTAs

- Get your free report
- See your options
- Book your first visit

---

## Platform copy limits

### Google responsive search ads

- Headlines: 30 characters each, at least 3 and up to 15.
- Descriptions: 90 characters each, at least 2 and up to 4.
- Two display path fields, 15 characters each.
- Up to 3 enabled responsive search ads per ad group.
- Ad strength (Google's rating of how varied your assets are) is not used to calculate Ad Rank or Quality Score.
- Include the search keyword naturally, and make the headlines differ from each other.

### Meta ads (Facebook and Instagram)

Figures from Meta's Ads Guide, checked 26 November 2026. Meta can change them, so check the Ads Guide before relying on them.
- Facebook Feed (image and video): primary text 50 to 150 characters recommended, headline 27 characters, 4:5 ratio, 1440x1800 recommended.
- Instagram Feed: primary text 125 characters, headline 40 characters, 4:5 ratio.
- Reels and Stories: 9:16 ratio, 1440x2560 recommended. Keep about 14% at the top, 35% at the bottom and 6% at each side free of text and logos.
- Put the hook in the first line, because longer text is cut off.
- Meta no longer applies a 20% text rule to images. Keep text on the image short enough to read at a glance.
- Emojis are optional. Test whether they suit the brand.

### LinkedIn ads

Outside this kit's main scope (Google and Meta). Check the platform's own spec page before using it. LinkedIn's current page lists introductory text at a maximum of 3,000 characters with about 150 shown before it is cut off, and a headline recommended at 70 characters with a maximum of 200.

---

## Copy testing priority

When testing ad copy, work through these in order of likely impact:

1. The hook or angle
2. The headline
3. The main benefit
4. The CTA
5. Supporting proof

Test one element at a time so the result is clear. Judge a test with the data gate in [the one stop rule](../SKILL.md#the-one-stop-rule), and use `ab-test-setup-and-analysis` for the setup.

---

*Framework lineage: adapted from Corey Haines' marketingskills pack (MIT), corrected and tightened for this kit.*
