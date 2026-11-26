# Platform specs

Character limits, counts and image sizes for Google and Meta ads, checked on the platforms' own help pages on 26 November 2026. Platforms change these, so check the ad preview before launch, and when a number here and the platform's form disagree, the form wins. Spaces count as characters everywhere.

## Google Ads

### Responsive search ads

Source: Google Ads Help, "About responsive search ads".

| Element | Limit | How many |
|---|---|---|
| Headline | 30 characters | 3 minimum, 15 maximum |
| Description | 90 characters | 2 minimum, 4 maximum |
| Display path 1 and 2 | 15 characters each | Optional |
| Final URL | | Required |

- Google shows up to 3 headlines and 2 descriptions at a time, in any order unless pinned. Each headline must make sense on its own and next to any other.
- Up to 3 enabled responsive search ads per ad group.
- Pin only what must sit in a fixed place. Pinning narrows Google's choices.
- Ad strength is Google's rating of how varied and relevant the headlines are. Google says it is not used to calculate Ad Rank or Quality Score, so treat it as advice, not a score to chase.
- Google's editorial rules reject repeated punctuation ("!!") and symbols used only for attention. Avoid exclamation marks in headlines.

A useful headline mix for 8 to 15 headlines (the kit's suggestion): a few with the keyword, a few with the main benefit, one or two with a confirmed fact (price, area, a real figure), one or two that say what to do next, one with the brand name. Descriptions: one benefit with a fact, one feature with what it means for the customer, one that answers the main worry, one with the next step.

### Assets shown with search ads

Google calls these assets (they used to be called extensions).

| Asset | Limit |
|---|---|
| Sitelink: link text | 25 characters |
| Sitelink: description line 1 and 2 | 35 characters each |
| Callout | 25 characters |
| Structured snippet: each value | 25 characters, 3 to 10 values |

### Performance Max asset group

Performance Max is Google's campaign type that runs on Search, YouTube, Display, Discover, Gmail and Maps from one set of assets. Source: Google Ads Help, Performance Max asset specifications.

| Asset | Limit | How many |
|---|---|---|
| Headline | 30 characters | 3 to 15 |
| Long headline | 90 characters | 1 to 5 |
| Description | 90 characters | 2 to 5, and Google's set-up page asks for one short description of 60 characters or fewer |
| Business name | 25 characters | 1, required |
| Call to action | Chosen from Google's list | Required |

| Image | Ratio | Recommended size | Minimum |
|---|---|---|---|
| Landscape | 1.91:1 | 1200 x 628 | 600 x 314 |
| Square | 1:1 | 1200 x 1200 | 300 x 300 |
| Portrait | 4:5 | 960 x 1200 | 480 x 600 |
| Logo, square | 1:1 | 1200 x 1200 | 128 x 128 |
| Logo, landscape | 4:1 | 1200 x 300 | 512 x 128 |

Up to 20 images and 5 logos per asset group; image files up to 5120 KB. Google's pages disagree on the number of videos allowed, so check the form. If no video is supplied, Google may make one from the images.

## Meta (Facebook and Instagram)

Source: the Meta Ads Guide (facebook.com/business/ads-guide), which gives recommendations by placement. Text longer than the recommendation is allowed but gets cut off behind "See more".

| Placement | Primary text | Headline | Ratio and size |
|---|---|---|---|
| Facebook Feed (image or video) | 50 to 150 characters recommended | 27 characters | 4:5, 1440 x 1800 recommended |
| Instagram Feed | 125 characters | 40 characters | 4:5, 1440 x 1800 recommended |
| Instagram Reels | 44 characters | | 9:16, 1440 x 2560 recommended |
| Instagram Stories | 125 characters | | 9:16, 1440 x 2560 recommended |

- Put the hook in the first line, because that is what shows before the cut.
- For Reels and Stories, keep about 14% at the top, 35% at the bottom and 6% at each side free of text and logos, so the app's own buttons do not cover them.
- Meta does not publish a fixed recommendation for the description line in every placement, and it may not show. Do not rely on it for anything important.
- One set of copy usually runs across several placements, so write the primary text so the first 40 or so characters make sense alone, and keep the headline near 27 characters.
- Meta no longer rejects images for having a lot of text, but text-heavy images are hard to read on a phone. Keep text on the image short.

### Lead ads (Meta instant forms)

Form types: More volume, Higher intent (adds a review step before sending), Rich creative. Field and text limits appear in the form builder; use what it shows.

## Other platforms

Outside this kit's main scope (Google and Meta). Check the platform's own spec page before using any of these. Checked November 2026:

- LinkedIn single image ad: introductory text up to 3,000 characters, about 150 shown before it is cut; headline about 70 recommended, 200 maximum; images 1200 x 628 (1.91:1) or 1200 x 1200 (1:1). Carousel: 2 to 10 cards, card headline 45 characters. Text ads: headline 25, description 75. `linkedin-ads-audit` covers LinkedIn accounts.
- TikTok in-feed ad text: up to 100 characters (Latin script), 4 to 60 recommended; display name up to 20 characters; video 9:16, 1:1 or 16:9.
- X website card headline: up to 70 characters, about 50 shows fully.

## Counting characters

- Count with a script when one can run (`py -3 -c "print(len('your line'))"`). Language models miscount.
- Emoji can count as two characters. The kit's copy rules avoid them anyway.
- Dynamic keyword insertion (`{KeyWord:default}`) can put a long search into a headline. Make the default fit, and check what the longest keyword would look like.

## Writing for several platforms at once

Start with the tightest limit and work outwards:

1. Google headlines (30 characters): the core message.
2. Facebook headline (27) and Instagram headline (40): the same message, adjusted.
3. Meta primary text: the hook in the first line, then the detail.

The core message then works everywhere.
