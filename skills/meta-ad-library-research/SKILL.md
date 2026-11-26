---
name: meta-ad-library-research
description: Free competitor research in the public Meta Ad Library - what rivals are running on Facebook and Instagram, which ads have lasted, and what that says about what works. Use for "what ads are my competitors running", "find winning ads in my niche", "build a swipe file", or before writing new creative. Needs no API key and no paid tool.
metadata:
  origin: "Original to this kit."
---

# Meta Ad Library research

The Meta Ad Library is public and free. Anyone can see the ads a Facebook Page is running. Used well, it tells you what your competitors keep paying for, which is the best free signal of what works.

## What the Library shows, and what it does not

**Shows:** every active ad for a Page, its text, image or video, button, link, start date, and where it runs (Facebook, Instagram, Messenger, Audience Network).

**Does not show:** spend, results, or targeting. Reach and audience details appear only for ads shown in the EU and for political or issue ads.

**A bias to remember:** the Library keeps ads shown in the EU for a year after they stop, and ads about social issues, elections or politics for seven years. Other ads disappear once they are inactive. A rival who advertises only in the US or the Gulf will look smaller than they are.

## Route 1: by hand (works for everyone)

1. Open `facebook.com/ads/library`.
2. Choose the country, set the category to "All ads", and search for the competitor's Page name.
3. Open the Page's ads. Sort mentally by start date.
4. For each ad worth noting, record the fields in the table below.

Aim for 3 to 5 competitors and the 10 to 20 longest-running ads from each. That is enough to see the pattern.

## Route 2: with a browser tool (if one is available in this session)

Open the same public pages and read them. Go slowly:

- **One page at a time.** Several fast, parallel page loads get the connection blocked for a while. A blocked page looks like "No ads match your search". If you see that on a Page you know is advertising, stop and wait. Do not retry in a loop.
- **Scroll to load more.** The first screen held about 30 ads when this was last checked, in November 2026. The rest load as you scroll.
- **Template ads.** Some ads show placeholders such as `{{product.name}}`. The real text is in the individual cards of the ad. Read those.
- **Never click "Close" on an ad's detail view when you only need a screenshot.** Capture the dialog as it is.

## Route 3: a free local app (optional, for heavy research)

`athm793/meta-ads-scraper` is a free, open-source app (Apache-2.0) that runs on your own computer, needs no API key, and stores what it finds in a local file. It needs Node.js 20 or newer. See its README for setup. It is not part of this kit and nothing here depends on it.

## Google's side: the Ads Transparency Center

Google has a free public library too, at `adstransparency.google.com`. Search for the advertiser's name or website, then choose the country and the time range. It shows the ads they ran on Search, YouTube and the Display Network, with the format and the dates each was last shown. It shows no spend and no results. Record the same fields as below.

## What to record

| Field | Why it matters |
|---|---|
| Advertiser | who |
| Start date and days running | the main signal: ads kept for 30 days or more are usually working |
| Format | image, video, carousel |
| Shape | square, vertical (9:16), or landscape |
| First line (the hook) | what stops the scroll |
| Angle | question, number, how-to, offer, urgency, curiosity, social proof, plain statement |
| Offer and button | what they ask people to do |
| Landing page | where the click goes |
| Number of versions | many versions of one idea means they are scaling it |

## Reading the pattern

- **Long-running ads** are the ones to study. New ads may be tests that fail next week.
- **Repeated angles across several competitors** mean the market responds to that angle.
- **Gaps** are angles nobody is using. They are either a chance or a sign it has been tried and dropped. Say which you think it is, and why.
- **Format mix** tells you what the audience is used to seeing.

## Output

1. A table of the ads recorded, longest-running first
2. The three to five patterns that repeat, each with the ads that show it
3. Three creative ideas to test that follow a proven pattern without copying an ad
4. What you could not see (spend, results, targeting) so nobody mistakes this for performance data

## Rules

- Read only public pages. Do not log in to anyone's account to see more.
- Learn the pattern and write new ads. Never copy a competitor's text, images or video.
- Days running is a clue, not proof. Say "likely working", never "is profitable".
- Use it for research and respect Meta's terms.
