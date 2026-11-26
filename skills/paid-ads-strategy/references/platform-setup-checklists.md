# Platform setup checklists

Setup checklists for Google Ads and Meta Ads, with a short reason beside each item that is not obvious. Menus move, so ask what the person sees on their own screen before pointing at a button. Nothing here changes an account: each item is something to check or to propose to the owner.

## Contents
- Google Ads setup
- Meta Ads setup
- Outside this kit's main scope
- Universal pre-launch checklist

## Google Ads setup

### Account foundation

- [ ] Google Ads account created and verified
- [ ] Billing information added (ads cannot run without it)
- [ ] Time zone and currency set correctly (neither can be changed later)
- [ ] Account access granted to team members, with the lowest role that lets them do their job

### Conversion tracking

A conversion is the action you want, such as a purchase or an enquiry. See `tracking-preflight` for the full check.

- [ ] Google tag installed on all pages (so actions can be measured)
- [ ] Conversion actions created (purchase, lead, signup)
- [ ] Conversion values assigned, if the value differs between actions
- [ ] Enhanced conversions considered (they pass hashed customer details to improve matching)
- [ ] Test conversions fire correctly
- [ ] If conversions are also imported from GA4 next to the native Google tag, use one source for each action. Never count the same booking twice (see `tracking-preflight`).

### Analytics integration

- [ ] Google Analytics 4 linked
- [ ] Auto-tagging enabled (it lets Google Analytics tie each visit to the ad that caused it)
- [ ] GA4 audiences available in Google Ads
- [ ] Cross-domain tracking set up, if there are multiple domains

### Audience setup

- [ ] Remarketing tag verified (it lets you reach past visitors)
- [ ] Website visitor audiences created:
  - All visitors, over a window you choose
  - Visitors to key pages (pricing, contact, booking)
  - Converters, so they can be excluded from campaigns meant for new customers
- [ ] Customer Match list uploaded, if the owner has one and consents to using it

### Campaign readiness

- [ ] Negative keywords added only from your own search terms report, and checked so they do not block a converting search. Do not start from a ready-made list.
- [ ] Location targeting set. The two options are "Presence or interest" (the default) and "Presence", so check which one fits the business.
- [ ] Language targeting set
- [ ] Ad schedule configured only if the business cannot take enquiries at certain hours
- [ ] Device settings reviewed once the account has its own data by device

### Assets (what Google used to call ad extensions)

- [ ] Sitelink assets (extra links under the ad to relevant pages)
- [ ] Callout assets (short benefit phrases)
- [ ] Structured snippet assets (a list of types, services or features)
- [ ] Call assets, if phone enquiries are valuable
- [ ] Lead form assets, if using them
- [ ] Price assets, if applicable
- [ ] Image assets, where available

### Brand protection

- [ ] A brand campaign running, so the business shows for its own name
- [ ] Competitor campaigns considered, only with the owner's agreement
- [ ] Brand terms kept out of non-brand campaigns if the search terms report shows them landing there

---

## Meta Ads setup

### Business portfolio foundation

Meta calls the old Business Manager a business portfolio (managed in Meta Business Suite and Business Settings).

- [ ] Business portfolio created
- [ ] Business verified, if running certain ad types
- [ ] Ad account created within the business portfolio
- [ ] Payment method added
- [ ] Team access configured with proper roles

### Pixel and tracking

- [ ] Meta pixel installed on all pages (the code that reports visits and actions to Meta)
- [ ] Standard events configured:
  - PageView (automatic)
  - ViewContent (product or service pages)
  - Lead (form submissions)
  - Purchase (sales)
  - AddToCart and InitiateCheckout (if ecommerce)
- [ ] Conversions API set up for server-side tracking (it sends events from your server, so fewer are lost to browser blocking)
- [ ] Check Event Match Quality in Events Manager and fix what it flags
- [ ] Test events in Events Manager

### Domain

- [ ] Domain verified in Business Settings. It controls who can edit link previews, and Meta still recommends it.
- [ ] Event prioritisation: Meta announced in 2023 that the limit of 8 events and the prioritisation step would no longer be needed. Confirm in Events Manager, which has changed since (see `tracking-preflight`).

### Audience setup

- [ ] Custom audiences created:
  - Website visitors, over windows you choose
  - Key page visitors
  - Video viewers
  - Page and Instagram engagers
  - Customer list uploaded
- [ ] Lookalike audience from a source of at least 100 people from one country (1% is the closest match)
- [ ] Saved audiences for common targeting

### Catalogue (ecommerce)

- [ ] Product catalogue connected
- [ ] Product feed updating correctly
- [ ] Catalogue sales campaigns enabled
- [ ] Dynamic product ads configured

### Creative assets

From Meta's Ads Guide, checked 26 November 2026. Meta can change these, so check the Ads Guide.
- [ ] Facebook Feed images and videos: 4:5 ratio, 1440x1800 recommended
- [ ] Instagram Feed: 4:5 ratio
- [ ] Reels and Stories: 9:16 ratio, 1440x2560 recommended, with about 14% at the top, 35% at the bottom and 6% at each side free of text and logos (so the app's buttons do not cover them)
- [ ] Ad copy variations ready (limits are in [ad-copy-templates.md](ad-copy-templates.md))
- [ ] UTM parameters in all destination URLs (so analytics shows which ad each visit came from)

### Compliance

- [ ] Special Ad Categories declared, if housing, credit, employment, or social issues, elections or politics
- [ ] Landing page complies with Meta's policies
- [ ] No prohibited content in ads

---

## Outside this kit's main scope (Google and Meta)

LinkedIn, X and TikTok each have their own setup steps, spec pages and help centres. Check the platform's own spec page before using it. For a LinkedIn review, see `linkedin-ads-audit`.

---

## Universal pre-launch checklist

Before launching any campaign:

- [ ] Create the campaign paused (see `launch-paused`) so nothing spends until the owner says yes
- [ ] Conversion tracking tested with a real conversion
- [ ] Landing page loads quickly and works on a phone
- [ ] UTM parameters working
- [ ] Budget set correctly (daily or lifetime)
- [ ] Start and end dates correct
- [ ] Targeting matches the intended audience
- [ ] Ad creative approved by the owner
- [ ] Team told about the launch
- [ ] Reporting view ready

---

*Framework lineage: adapted from Corey Haines' marketingskills pack (MIT), corrected and tightened for this kit.*
