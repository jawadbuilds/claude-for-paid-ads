# Audience targeting reference

Targeting ideas for Google and Meta. Menus and option names move, so ask what the person sees on their own screen before pointing at a button.

## Contents
- Google Ads audiences
- Meta audiences
- Audience size
- Exclusions
- Outside this kit's main scope

## Google Ads audiences

### Search campaigns

**Keywords** are the main targeting on Search:
- Exact match, written [keyword]: the most precise, with lower volume.
- Phrase match, written "keyword": moderate precision and volume.
- Broad match, written keyword: the highest volume. It works best with Smart Bidding (bidding where Google sets the bid for each auction from your goal).

**Audience layering:**
- Add audiences in "observation" mode first. Observation lets you see how each audience performs without narrowing who sees the ads.
- Look at performance by audience in the account's own data.
- Switch an audience to "targeting" mode only if the data shows it clearly does better and the owner agrees to narrow the reach.
- Affinity and in-market segments (Google's pre-built groups of people by interests and buying research) can be added in observation on Search. They are more often used for targeting on Display, YouTube and Demand Gen.

**RLSA (remarketing lists for search ads: past site visitors, matched to what they search for):**
- Consider a higher bid, or different ads, for past visitors searching your terms.
- Exclude people who already converted from campaigns meant to find new customers.

### Display, YouTube and Demand Gen

**Custom segments** (the current name for custom intent audiences):
- You choose the search terms, URLs or apps that describe your ideal customer, and Google finds people who match.
- A good place to start is the terms that already convert for you, taken from the search terms report.

**In-market segments:**
- People Google sees actively researching a type of product or service.
- Pre-built by Google, so you pick from its list.

**Affinity segments:**
- Based on long-term interests and habits.
- Broad, so better suited to awareness than to getting enquiries.

**Customer Match:**
- Upload a list of customer emails or phone numbers so the platform can match them to accounts.
- Use it to show different ads to existing customers, or to leave them out.

**Lookalike segments (Demand Gen):**
- Google's old "similar audiences" were removed in 2023. Demand Gen now offers lookalike segments built from a seed list, and the seed list needs more than 100 matched people.
- A seed list of your best customers works better than a list of everyone who ever enquired.

---

## Meta audiences

### Core audiences (location, age, interests)

On Meta, start broad unless the account's own data shows a narrower audience works better. Meta's delivery system finds the people most likely to get a result, and every extra interest you stack narrows the audience and can make delivery slower and dearer.

- Add interests one at a time and compare against a broad version of the same ad set.
- Exclude existing customers where the platform allows it.

**Demographics:**
- Age and gender, only if the product really is specific to them.
- Location, down to a postcode or a radius around a shop.
- Language.

**Detailed targeting options:**
- Meta has removed many detailed targeting options over the years. Check which detailed targeting options Meta still offers in the account before planning around one.

### Custom audiences

**Website visitors** (needs the Meta pixel or Conversions API working; see `tracking-preflight`):
- All visitors, for up to 180 days.
- Visitors to specific pages.
- Visitors by how often they came or how long they stayed, if the account offers it.

**Customer list:**
- Upload emails or phone numbers.
- Refresh the list now and then so it stays accurate.

**Engagement audiences:**
- People who watched a set share of a video.
- People who engaged with the Page or the Instagram profile.
- People who opened a lead form.

**App activity:**
- People who installed the app or took an action inside it.

### Lookalike audiences

**Source audience quality matters:**
- A source of paying customers usually teaches Meta more than a list of leads, and leads more than all site visitors.
- Meta needs at least 100 people from one country in the source.
- A bigger source is better. "1,000 or more" is a common habit among advertisers, not a Meta rule.

**Size:**
- Meta's range in Ads Manager is 1% to 10% of the people in the chosen country. 1% is the closest match to the source and the smallest reach.
- The bands people use (1% to 3% for balance, 3% to 5% for scale, 5% to 10% for awareness) are conventions, not Meta guidance. Test one against another with your own results.

**Layering:**
- Try a lookalike on its own first. Adding interests on top narrows it further.
- Exclude the source audience so you do not pay to reach your own customers.

---

## Audience size

There is no magic number. A rule in plain words:
- Too small, and delivery is slow and costly because the platform has few people to find.
- Too broad, and spend goes to people who will never buy.
- A local business can have a small audience, and that is fine. A plumber serving one town should expect a small audience.

If delivery is slow or the cost per result is high, compare the same ad set at a wider and a narrower setting against the account's own earlier period.

---

## Exclusions

Keep these out of campaigns meant to find new customers, where the platform allows it:
- Existing customers, from a customer list (unless the campaign is an upsell).
- Recent converters, using a short window you choose, such as the last 7 to 14 days (a rule of thumb).
- Website visitors to pages that show the wrong intent, such as a careers or support page, where this is relevant and the platform allows it.
- Employees, by uploading a list of their emails, where the platform allows it.

---

## Outside this kit's main scope (Google and Meta)

Check the platform's own spec page before using any of this.
- LinkedIn: targeting is by job title, function, seniority, company size and industry. Use LinkedIn's own help pages, or `linkedin-ads-audit` for a review.
- TikTok and X: use each platform's own Ads Manager help pages. This kit does not cover them.

---

*Framework lineage: adapted from Corey Haines' marketingskills pack (MIT), corrected and tightened for this kit.*
