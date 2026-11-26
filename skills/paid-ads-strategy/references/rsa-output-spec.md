# Responsive search ad output spec

When someone asks for Google responsive search ads (ads where Google mixes up to 3 of your headlines and 2 of your descriptions for each search), the output must fit Google's limits and this layout. `ad-creative` writes the words; this file sets the shape.

## Google's limits (checked on Google Ads Help, November 2026)

- **Headlines:** at least 3 and up to 15, each up to **30 characters** including spaces.
- **Descriptions:** at least 2 and up to 4, each up to **90 characters**.
- **Paths:** up to 2 display path fields, each up to **15 characters**.
- **Final URL:** present, starting https.
- **Ads per ad group:** up to 3 enabled responsive search ads.
- **Sitelink assets:** link text up to 25 characters, two description lines up to 35 characters each. **Callout assets:** up to 25 characters. **Structured snippet assets:** 3 to 10 values, each up to 25 characters.

The kit's own preference, not Google's rule: write 8 to 15 headlines that are each different and useful, and 4 descriptions. Never pad with filler to reach 15. Every headline must make sense on its own and next to any other.

## Count characters with a tool

Language models miscount characters. Count each line with a script when one can run, for example `py -3 -c "print(len('Free 30-minute maths lesson'))"`, and print the count next to each line. If no script can run, say the counts are approximate and leave a margin of two characters.

## Pinning

State any pinned position. The default is no pins. Pin only what must appear in a fixed place (a legally required line, or the brand name when the owner insists), because pinning narrows Google's choices.

## What comes with the ads

1. **Ad group structure:** each ad group, its theme, its keywords with match types, and which ads belong to it.
2. **Negative keywords:** for a new campaign, only the business's own brand name in non-brand campaigns, then "none yet: review the search terms report after 7 days (`search-term-mining`)". For a running campaign, only terms taken from its search terms report, each checked against searches that convert. Never a starter list.
3. **Sitelinks** (4 or more, each pointing to a real page) and **callouts** (4 or more), only with facts the owner has confirmed.

## Output order

Emit in this order, so the short parts are not lost if the answer runs long:

1. Ad group structure
2. Negative keywords
3. Sitelinks
4. Callouts
5. The ads

## Template

```
Ad group structure:
- AG1 [theme]: keywords (match types), ads RSA1, RSA2
- AG2 [theme]: ...

Negative keywords:
  Campaign level: [brand name, in non-brand campaigns only]
  From search terms: none yet, review after 7 days

Sitelinks (4 or more):
  - [link text, max 25] | [line 1, max 35] | [line 2, max 35] | [URL]

Callouts (4 or more, max 25 each):
  - [callout]

RSA1, [ad group]
  Final URL: https://...
  Path 1: ...   Path 2: ...
  Headlines (max 30 each):
    1. [headline] (NN)
    ...
  Descriptions (max 90 each):
    1. [description] (NN)
    ...
  Pinning: none (or list the pins)
  Claims to confirm: [any fact the owner must confirm before use]
```

## Check before sending

- Every headline 30 characters or fewer, every description 90 or fewer, counted by a script or marked approximate.
- At least 3 headlines and 2 descriptions per ad; no filler.
- No invented facts: no customer counts, ratings, guarantees, prices, discounts or "limited places" unless the owner confirmed them.
- No exclamation marks used for attention, and no repeated punctuation ("!!"), which Google's editorial rules reject.
- Then run `human-copy-check` and `ad-claims-check`, in that order.

If a check fails, fix it before sending. Do not send part of an ad.
