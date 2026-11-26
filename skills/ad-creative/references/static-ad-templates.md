# Static ad template library

Structural templates for static (image) ad creative. Each one is a layout with slots for your own copy. The structure is a starting point; the inputs (your real reviews, your real offer, your real photos) make it yours.

Use these when you need several static ad concepts for Meta, Instagram or display. Cycle through the whole set rather than settling on two or three favourites. Different templates give you different angles, and the winner is often not the one you would have picked by hand.

## How to read the tiers

Each template carries a tier (S, A, B, C, E, F) and a funnel role. The tiers are one practitioner's ranking of what scaled in large Meta accounts. They are not a platform fact and they do not predict what will work in your account. A small account should judge each template on its own results, using the one stop rule in `paid-ads-strategy`.

With that said, the tiers are a useful way to think about what each format is for:

- S and A tiers: formats said to reach cold audiences (people who have never heard of you). Try these first when you need fresh reach.
- B and C tiers: the supporting cast. They tend to work better on people who already know the problem or already know you. A B-tier template can still be your best converter for warm traffic, so do not drop one just because it does not reach cold audiences.
- E and F tiers: formats said to have faded, or to carry rights or compliance risk. They are flagged so you do not spend a batch on them by accident.

Read the tiers as a guess about reach, not about quality. For the full map across all Meta formats, including video, see `references/meta-creative-formats.md`. This library covers the static slice only.

## How to use this library

1. Ground first. Read your inputs (your best past ads, customer reviews, comments under your ads, your brand voice) before writing anything. See Path A and Path C in the skill.
2. Cycle through templates. For a batch, spread concepts across the set. For cold reach, lean towards the S and A tiers; for warm audiences and retargeting, lean on the B tier. Skip the E and F formats unless you have a specific reason.
3. Fill slots from source material. Every variation takes its copy from a real review, a past winning ad or a real comment, and says which one.
4. Write the visual brief. Each concept includes enough direction that a designer, a friend with a phone camera, or a free design tool can produce it without guessing.

## Generation rules

- Every variation includes: template name, headline, body copy, visual brief and source grounding.
- Source grounding means the review, winning ad or comment the concept is based on. Do not write a variation without it.
- Never invent a claim, a statistic, a testimonial, a customer count, a rating or a press mention. Where an example below needs a figure, it shows a bracketed placeholder such as "[real figure from your data]". Fill it from your own records or leave the line out.
- Use customer language wherever you can. Do not paraphrase a review into marketing-speak.
- Match your brand voice on tone.
- Any ad that carries a claim, a quote, a result or a comparison goes through `ad-claims-check` before it is published.

---

## The templates

Each template is tagged with a tier and a role. See "How to read the tiers" above.

### 1. Headline statement

One bold line of text, one hero shot of the product or the work, a plain background. The headline does the work.

- **Tier**: B. Role: mid-funnel supporting cast. This is an old print-era format and it only works with strong messaging. It pairs well with a callout treatment (templates 9 and 17).
- **Structure**: One dominant text line (over half the visual weight), the product image, a small logo.
- **Copy slot**: One claim specific enough to stop the scroll.
- **Shop example**: "The last pair of boots you'll need to buy for years." Use only if you can back it.
- **Service example**: "Your boiler serviced in one visit, at a price agreed first."
- **Source it from**: Your strongest past hook, or the benefit that comes up most often in reviews.

### 2. Us vs. them

A side-by-side comparison. The competitor or the "old way" sits on the left, greyed out. You sit on the right, in full colour. Four to six rows.

- **Tier**: B. Role: mid-funnel supporting cast. It converts people who are already weighing you against an alternative. It is rarely the format that opens cold reach.
- **Structure**: Two columns, a tick or cross per row, your side visually alive.
- **Copy slot**: Comparison rows. Each row is a real difference you can prove, not filler.
- **Shop example**: "Typical shop: ships in [their real time]. Us: ships in [your real time]."
- **Service example**: "Typical quote: price after the visit. Ours: price before we turn up."
- **Compliance**: Comparisons must be true and provable. Read the Competitor callout notes (template 14) and run the ad through `ad-claims-check`.
- **Source it from**: Reviews that mention switching, or comments comparing you with an alternative.

### 3. Stat callout

One dominant number takes up most of the frame, with a line of context below.

- **Tier**: C. Role: situational supporting cast. Number-led statics tend to work for awareness and traffic goals and under-deliver on direct sales. Use it only when the number really is what sets you apart.
- **Structure**: A giant figure, one line of context, a product or logo anchor.
- **Copy slot**: A real number you can show where it came from.
- **Shop example**: "[real figure from your data] orders shipped this year."
- **Service example**: "[real figure from your records] jobs finished on the day we quoted."
- **Real and checkable**: The number must come from your own records, a survey you ran or a published source you can link to, and you must be able to show the working. Never round it up or invent it. `ad-claims-check` reviews the ad before it runs. A figure about health, money or results may be restricted, so check the platform's policy.
- **Source it from**: Your own order, booking or customer records.

### 4. Review card

A star-rated review styled like a screenshot of a real review. Reviewer name, rating, date.

- **Tier**: E. Role: faded format. Testimonial statics often disappoint unless the review is a genuine standout: specific, surprising and word for word. Skip generic praise and keep this for the one review that makes you stop.
- **Structure**: Looks like the review site where your buyers actually read reviews (Google, Trustpilot, Facebook or whichever applies to you).
- **Copy slot**: A real review, word for word. The realism is the point.
- **Shop example**: A review card quoting a real customer's line about reordering. Use their exact words, not these.
- **Service example**: A review card quoting a real customer on how the visit went.
- **Real and checkable**: The review must exist, be quoted exactly and be traceable to a named place where anyone can find it. Get the reviewer's permission where the site or the law requires it. Do not edit the wording or invent a rating. `ad-claims-check` reviews the ad before it runs, and some sites limit how their reviews can be reused, so check the site's terms.
- **Source it from**: `inputs/reviews/`, word for word.

### 5. Testimonial stack

Three customer quotes stacked vertically, each with a photo, a name and one line.

- **Tier**: E. Role: faded format, same class as the review card. Only worth a slot if all three quotes are specific and each answers a different worry.
- **Structure**: Three short rows. Each quote should be scannable in about two seconds.
- **Copy slot**: Three real quotes covering different objections or benefits.
- **Shop example**: Three real customers, one on quality, one on delivery, one on service.
- **Service example**: Three real clients, one on price clarity, one on timing, one on the result.
- **Real and checkable**: Every quote, name and photo must belong to a real customer who agreed to appear. Never write a testimonial yourself or merge two into one. `ad-claims-check` reviews the ad before it runs.
- **Source it from**: Reviews. Pick for coverage of different worries, not for enthusiasm.

### 6. Before and after

A split image showing two states, with minimal labels. Product results, workflow or visual proof.

- **Tier**: B. Role: mid-funnel supporting cast. It shows the payoff to people who already know the problem. It rarely opens cold reach on its own.
- **Structure**: Two panels, a divider, a short label on each state.
- **Copy slot**: Label each state in the customer's words ("Sunday-night spreadsheet dread" and "Reports send themselves").
- **Shop example**: A real customer's room or garden before and after using your product.
- **Service example**: A real job photographed before and after the work.
- **Real and checkable**: Both photos must be of a real job or customer, taken by you, unretouched, with permission to use them. Before and after images are restricted on Meta and Google in areas such as health, weight, body image, beauty and finance, so check the platform's policy before using this template there. `ad-claims-check` reviews the ad before it runs.
- **Source it from**: "I used to X, now I Y" language in reviews, and your own job photos.

### 7. Problem and answer

The pain point on top (text or image), the product as the answer below.

- **Tier**: B. Role: mid-funnel supporting cast. It is close to objection handling, which tends to work quickly. It is strongest when the pain uses the customer's exact words.
- **Structure**: Two zones, tension above and relief below.
- **Copy slot**: The pain in the customer's own words, then the product's one-line answer.
- **Shop example**: "Tired of searching three shops for the right size?" Then a photo of your size guide.
- **Service example**: "Waiting in all day for a tradesperson who never turns up?" Then your booked time slot.
- **Source it from**: The most common pain phrasing in `inputs/reviews/`, word for word.

### 8. Founder message

A handwritten-style or plain-text note from the founder or owner. Conversational and personal.

- **Tier**: S. Role: cold-reach format. Founder content is said to be the most reliable first top performer at any production level, because the story of why you started connects with people who have the same problem. Try this first.
- **Structure**: A note-style layout, the owner's name or photo, no glossy product shot.
- **Copy slot**: "I started this because..." One honest paragraph with no marketing polish.
- **Shop example**: "I started this shop because I could never find [the thing you could not find]."
- **Service example**: "I started this business after [the real thing that happened to you]."
- **Source it from**: Your actual story. This template collapses if it is made up.

### 9. Feature spotlight (ingredient spotlight)

The product in the centre, with four to six callout boxes around the edges naming key parts.

- **Tier**: B. Role: mid-funnel supporting cast. This is a callout treatment, one of the more reliable static layouts, and it pairs with the headline statement. When the callouts teach rather than sell, it moves towards the educational infographic (template 19).
- **Structure**: A centre image, radiating callouts, each callout 3 to 6 words.
- **Copy slot**: The parts buyers actually ask about, not your full feature list.
- **Shop example**: A product photo with callouts on the material, the fit and the care instructions.
- **Service example**: A photo of your van or kit with callouts on what is included in a visit.
- **Source it from**: The features or ingredients that come up most in reviews and comments.

### 10. Press mention

"As seen in" with publication logos and a pull quote.

- **Tier**: F. Role: avoid by default. Logo walls carry a rights and permissions risk, and a logo can imply an endorsement you do not have.
- **Structure**: A logo row, one strong quote, a product anchor.
- **Copy slot**: A real quote from real coverage.
- **Shop example**: A quote from a real local-news piece about your shop, with the paper's name in plain text.
- **Service example**: A quote from a real article or podcast that featured you.
- **Rule**: Never use a publication's logo or name unless the coverage is real and you have the right to show it. Check the outlet's logo-usage terms. Quote the words exactly, with the date and a link you can produce on request.
- **Real and checkable**: The coverage must exist and be findable by anyone. `ad-claims-check` reviews the ad before it runs.
- **Source it from**: Actual press, podcasts, newsletters or analyst mentions.

### 11. Lifestyle hero

The product in use in a real setting. Minimal copy, aspirational but not salesy.

- **Tier**: B. Role: mid-funnel supporting cast. An organic, phone-camera look reads as native and supports other formats well, but it does not reliably open cold reach by itself. For clothing, see the mood board (template 18).
- **Structure**: One photograph does the work, plus at most a short line and a logo.
- **Copy slot**: Five to eight words with a touch of identity ("Mornings, handled.").
- **Shop example**: Your product on a kitchen counter in a real routine.
- **Service example**: Your tutor and a student at a real kitchen table, with the family's permission.
- **Source it from**: The visual patterns of your best past ads, and identity language in reviews.

### 12. Numbered list

"Five reasons [audience] are switching to [your business]." Icons beside each point.

- **Tier**: E. Role: faded format. Listicle statics worked a year or two ago and have flattened since. The educational infographic (template 19) is the healthier version of the same idea. Do not lead a batch with this.
- **Structure**: Numbered rows, an icon and a short line each, a product anchor at the bottom.
- **Copy slot**: Each reason is a different angle: pain, outcome, proof, difference, price.
- **Shop example**: "Three reasons local customers order from us again." Fill each with a real reason from reviews.
- **Service example**: "Three things clients tell us they liked about booking us."
- **Source it from**: The most common switching reasons across your reviews.

### 13. FAQ card

A common objection as the question, answered directly.

- **Tier**: B. Role: mid-funnel supporting cast. This is objection handling in static form, and it tends to work quickly. The objection phrased the way customers phrase it is the whole hook.
- **Structure**: The question prominent, a short answer, a product anchor.
- **Copy slot**: The objection in the customer's wording. Recognition is the hook.
- **Shop example**: "Will it fit if I'm between sizes?" Followed by your real returns and exchange policy.
- **Service example**: "Do I need to be home during the visit?" Followed by your real answer.
- **Real and checkable**: The answer must be true today. Do not include a figure such as a test size or a success rate unless [real figure from your data] backs it. Health, money and results answers can be restricted, so check the platform's policy.
- **Source it from**: `inputs/comments/`, the objections people post publicly under your ads.

### 14. Competitor callout

Name a specific competitor (or the usual category default) and explain the difference. Bold but factual.

- **Tier**: B. Role: mid-funnel supporting cast. A sharper version of us vs. them. It works on comparison shoppers who already have you in their shortlist, and it is not a cold-reach opener.
- **Structure**: Their name against yours, one clear axis of difference.
- **Copy slot**: A difference you can defend with facts. Comparisons invite scrutiny.
- **Shop example**: "[Competitor] charges [their real delivery fee]. We charge [your real delivery fee]."
- **Service example**: "[Competitor] charges a call-out fee. We don't." Use only if it is true and current.
- **Real and checkable**: Every comparison must be true, current, fair and provable, with a dated source you can show. Some platforms and some countries restrict naming competitors, so check the platform's policy and your local advertising rules. `ad-claims-check` reviews the ad before it runs.
- **Source it from**: Competitor mentions in reviews and comments. Customers often name the alternative for you.

### 15. Origin story

A founder photo with the story of why you started. Longer copy than other formats.

- **Tier**: S. Role: cold-reach format, from the same family as the founder message. The specific moment that started it connects with people who share the problem. It also works for warm and retargeting audiences.
- **Structure**: A portrait or team photo, two or three short paragraphs, the product in a secondary position.
- **Copy slot**: The specific moment or frustration that started the business. Specifics are the credibility.
- **Shop example**: "We started with one market stall in [real year] and [what really happened next]."
- **Service example**: "We were the customers first. The [service] we needed didn't exist near us, so we set it up."
- **Source it from**: The real story. It tends to work better on warm audiences than cold ones.

### 16. Grid static (multi-product or bundle)

A tidy grid of your range, a bundle or a collection in one clean frame. Optional "shop the set" line.

- **Tier**: A. Role: cold-reach format. It is easy to make and shows range, so a cold viewer can pick out the item that fits them. A sensible first static to try when you sell more than one product.
- **Structure**: Four to nine product tiles on a neutral ground, consistent lighting and crop, a small logo and an optional bundle price.
- **Copy slot**: Minimal. A collection name or a "build your bundle" line.
- **Shop example**: A 3 by 3 grid of your best sellers with "[real bundle price]" if you sell a bundle.
- **Service example**: A grid of your service packages with the real starting price for each.
- **Source it from**: The products or bundles your reviews and comments cluster around. Lead with the combinations customers ask for.

### 17. Callout

The product hero with three to five short labels pointing at specific parts. The "what makes this different" annotated directly on the image.

- **Tier**: B. Role: mid-funnel supporting cast. A durable static layout that pairs with the headline statement and underlies the feature spotlight. Cheap to iterate and quick to read.
- **Structure**: A centre product, leader lines to three to five labels, each label 2 to 5 words.
- **Copy slot**: The attributes buyers actually ask about, not spec-sheet filler.
- **Shop example**: A pair of shoes with callouts on the sole, the material and the weight.
- **Service example**: A photo of a finished job with callouts on the materials used and the guarantee you really give.
- **Source it from**: The features that recur in reviews and ad comments.

### 18. Mood board (clothing and home)

A curated collage of product, texture, setting and palette, assembled like a pinboard. Identity rather than information.

- **Tier**: B. Role: mid-funnel supporting cast, for clothing and home brands where the look is the product. It sells the world the buyer is opting into.
- **Structure**: Three to six tiles mixing product shots, fabric or texture, and a scene, in one cohesive palette.
- **Copy slot**: At most a short identity line ("Quiet luxury, everyday.").
- **Shop example**: A small capsule of this season's pieces laid out with a location shot.
- **Service example**: Rarely applicable. Use the lifestyle hero (template 11) instead.
- **Source it from**: The visual language of your best past ads, and the style words customers use in reviews.

### 19. Educational infographic

A single frame that teaches something true: how something works, a comparison, a simple process. Styled to read as content rather than an ad.

- **Tier**: B. Role: mid-funnel supporting cast, and under-used. It earns attention that hard-sell formats do not. It is the healthier version of the faded numbered list.
- **Structure**: A diagram, cycle or labelled cross-section, with minimal branding until the anchor.
- **Copy slot**: One genuine, checkable teaching point.
- **Shop example**: "How to measure your foot at home" as a three-step diagram.
- **Service example**: "What happens in your first tutoring session" as a three-step flow.
- **Real and checkable**: Every claim in the graphic must be true and provable. Run it through `ad-claims-check`.
- **Source it from**: The "but how does it work?" questions in comments, and documented facts about your product.

### 20. Challenging a belief

Leads with a contrarian statement naming a belief your customer holds, then corrects it. A confrontational hook, resolved below.

- **Tier**: B. Role: mid-funnel supporting cast. It works when you really know the customer's limiting beliefs and have a specific, earned correction. As a static it needs a crisp visual contrast.
- **Structure**: A bold belief statement at the top, the correction below, the product as the proof.
- **Copy slot**: The belief in the customer's words, then the fact that corrects it. State the fact plainly instead of staging a "You don't need X, you need Y" reveal.
- **Shop example**: "Many people think a cheaper pan lasts as long as a dear one. Here is what [real test or real return rate] showed."
- **Service example**: "Many parents think tutoring only helps when a child is already failing. Here is what we see with [real description of your students]."
- **Real and checkable**: The correcting fact must be real and sourced. `ad-claims-check` reviews the ad before it runs.
- **Source it from**: Objections and misconceptions in comments and reviews.

### 21. Tweet or Reddit screenshot

A single post styled as a native screenshot. Real social proof as the creative, strongest as the first frame.

- **Tier**: B. Role: mid-funnel supporting cast, and especially useful as a hook or first frame.
- **Structure**: A faithful post card with an avatar, a handle, a timestamp and engagement counts.
- **Copy slot**: A real post, word for word. An unprompted mention, or your own best organic line.
- **Shop example**: A real customer's public post about your shop, with their permission.
- **Service example**: A real client's public post about the booking, with their permission.
- **Real and checkable**: Use real posts only, and ask permission from the author where needed. A faked screenshot breaks platform rules and customer trust. `ad-claims-check` reviews the ad before it runs.
- **Source it from**: Real social mentions, your own organic posts, or `inputs/comments/`.

### 22. Handwriting or sticky note

Deliberately low-polish: a handwritten note, a sticky note or plain text on a photo. The unpolished look reads as native.

- **Tier**: B. Role: supporting cast, and a good fit for sale periods because it looks quick and time-sensitive. Rotate it in for real sales and launches rather than running it all the time.
- **Structure**: One scrappy element (a note, a marker scrawl, a screenshot) over the product or a plain ground.
- **Copy slot**: A blunt, human line with the offer or the reason, in plain words.
- **Shop example**: A sticky note reading "[real discount] off until [real end date]."
- **Service example**: A note reading "Booking now for [real month]."
- **Real and checkable**: Urgency is fine only when it is true. State a real end date that you will honour, and never reset it to keep an ad running.
- **Source it from**: The offer itself, and the plain way a customer would remind a friend.

### More templates from live ad libraries

Templates 23 to 32 come from a review of long-running statics in public ad libraries (November 2026). Their tiers are provisional: a starting guess from the format family each belongs to. Your own account's results override them. An ad that stays up for a long time shows that someone kept paying for it, which is not proof that it paid off.

### 23. Apology letter ("We're so sorry")

A mock apology that turns out to be good news: "We want to apologise to everyone who bought..." then the reason (it sold out, a price drop, a new flavour), then the offer.

- **Tier**: B (provisional). Role: supporting cast and sales-period option, from the founder's-letter family. The apology headline stops the scroll because brands rarely say sorry in ads, and the twist carries the offer.
- **Structure**: A big "We're sorry" headline, three to five short letter-style lines, the offer in bold, the product small or absent.
- **Copy slot**: A real reason to "apologise" (stock ran out, the old price was too high, customers missed a feature) and a real offer. The apology must be playful, never a fake recall or safety notice.
- **Shop example**: "We're so sorry. We ran out of [product] twice last month. It is back in stock now."
- **Service example**: "Sorry to everyone we couldn't fit in last month. We now have slots on [real days]."
- **Source it from**: The offer, plus a true story behind it (a sell-out, a price change, a feature customers missed).

### 24. Important update

An announcement card: "Important update" over plain text stating a real change (price, availability, a new area, a new plan).

- **Tier**: B (provisional). Role: supporting cast. It is strongest when the update is real news to people who already know your category, and it reads like a notice rather than an ad.
- **Structure**: A solid background, an "Important update" label, three or four short lines, one highlighted number or name, a logo at the bottom.
- **Copy slot**: One real change with its specifics (the new price, the date, who qualifies).
- **Shop example**: "Important update: we now deliver to [real area]. Delivery from [real price]."
- **Service example**: "Important update: we now cover [real town] too."
- **Compliance**: Never style it as a message from a platform, a regulator, or the reader's bank or employer.
- **Source it from**: Real product, pricing or availability changes from your own records.

### 25. Reassurance list ("Stop thinking something is wrong with you")

Tells the reader to stop blaming themselves, lists the specific experiences that are normal, then offers the product as a way to handle them.

- **Tier**: B (provisional). Role: supporting cast for problem-aware buyers who feel alone with the problem. Relief is the hook and the list shows you understand.
- **Structure**: A bold "Stop thinking..." headline, three or four bullets of specific experiences, one line naming the product.
- **Copy slot**: The experiences in the customer's exact words, each one specific enough to feel seen.
- **Shop example**: "Stop thinking you're bad at gifts. Not knowing what to buy a person who has everything is normal."
- **Service example**: "Stop thinking your child is the only one who dreads maths homework. It is common, and it is fixable."
- **Compliance**: In health, do not diagnose and do not tell people to ignore symptoms. Meta has rules against ads that imply a negative personal attribute or condition, so check the platform's policy.
- **Source it from**: Reviews and forum posts where customers describe what they thought was wrong with them.

### 26. Simple guarantee

The guarantee is the headline: "If you don't love it in 60 days, we'll refund you."

- **Tier**: B (provisional). Role: mid-funnel supporting cast for cautious, risk-averse buyers. The risk reversal does the persuading.
- **Structure**: The guarantee as the headline, one line on why it is safe to try, a product shot, a trust marker.
- **Copy slot**: The real guarantee terms in plain words: the timeframe, the condition and what the customer gets back.
- **Shop example**: "Not the right fit? Send it back within [your real number of days] for a refund."
- **Service example**: "If you are not happy with the work, we will come back and put it right at no charge." Use only if it is your real policy.
- **Real and checkable**: Only use a guarantee you already have in writing, and state its real conditions in the ad. If you have no written guarantee, do not make one up for the ad. A guarantee in an ad is a promise the business must keep, and `ad-claims-check` reviews the ad before it runs.
- **Source it from**: Your actual refund or guarantee policy.

### 27. With and without

Two side-by-side states of the same person or task: with the old way and with you. Unlike before and after, nothing has to change over time.

- **Tier**: B (provisional). Role: mid-funnel supporting cast, from the us vs. them family. It is easier to back up than a before and after because it compares two approaches, not one person's results.
- **Structure**: A split frame, a contrasting colour per side, "With [old way]" against "With [you]", two or three outcome lines under each.
- **Copy slot**: The same outcome measured both ways (steps taken, time spent, price paid).
- **Shop example**: "With a regular shop: [real number] steps to order. With us: [real number]."
- **Service example**: "With a typical booking: [real wait]. With us: [real wait]."
- **Compliance**: If you name a competitor, follow the Competitor callout rules (template 14).
- **Source it from**: Switching stories in reviews, and your own measured figures.

### 28. Venn diagram

Two or three circles for the things the buyer wants, with the product in the overlap.

- **Tier**: C (provisional). Role: situational supporting cast. It works when the product really is "the only one that does all of these" and falls flat when the circles are generic.
- **Structure**: A one-line problem headline, two or three labelled circles, the logo in the overlap, a plain background.
- **Copy slot**: Benefits that buyers normally have to trade off against each other.
- **Shop example**: "Good quality" and "Fair price" and "Delivered this week", with your shop in the middle. Use only if all three are true.
- **Service example**: "Qualified tutors" and "Evening slots" and "Fixed monthly price", with your business in the middle.
- **Source it from**: Reviews that say "the only one that...", and the trade-offs buyers mention in comparison posts.

### 29. Stages (progression comic)

A three or four panel sequence showing how the buyer's situation develops, ending with the product.

- **Tier**: B. Role: mid-funnel supporting cast (progression is B-tier in the format map). Each panel advances the story, so it holds attention longer than a single frame.
- **Structure**: A "The four stages of [problem]" headline, numbered panels with one line each, a final panel or banner with the product.
- **Copy slot**: Stages the buyer recognises from their own experience, in their words.
- **Shop example**: "The four stages of buying a sofa: browse, measure, order, realise it doesn't fit through the door."
- **Service example**: "The four stages of finding a plumber: search, wait, get a quote, still wait."
- **Compliance**: Do not promise medical outcomes in panel copy. Panels are claims too.
- **Source it from**: The order in which customers describe trying things in reviews ("first I tried X, then Y").

### 30. Character story ("This is Mike")

A simple character (a stick figure or plain illustration) with a three-line story: who they are, the problem, what they did. It ends with "Be like Mike."

- **Tier**: C (provisional). Role: situational supporting cast. It borrows a familiar meme structure and suits audiences who respond to humour, and problems that are awkward to show on a real person.
- **Structure**: A "This is [name]." headline, a short story in three lines, a simple drawing, a "Be like [name]." closer.
- **Copy slot**: A persona the buyer recognises, with a specific routine and problem.
- **Shop example**: "This is Sam. Sam runs three times a week. Sam's knees hurt. Sam changed shoes. Be like Sam."
- **Service example**: "This is Priya. Priya spent Fridays doing her own bookkeeping. Priya hired a bookkeeper. Be like Priya."
- **Real and checkable**: The character is made up and should be obviously illustrative. Do not present it as a real customer or add a result you cannot show.
- **Source it from**: Your ideal customer's most common profile and their most common fix.

### 31. Signs checklist

"Seven signs your running shoes are worn out" or "Homeowners: notice these?" A self-check list the reader ticks against themselves.

- **Tier**: C (provisional). Role: situational supporting cast, a cousin of the faded numbered list. It holds up better because the reader checks themselves against the list instead of reading reasons to buy.
- **Structure**: A "[N] signs..." headline, four to nine short items (tick boxes or bullets), a supporting image, the product or call to action last.
- **Copy slot**: Signs in the buyer's words that are true for the problem, not a list built to make everyone qualify.
- **Shop example**: "Five signs your running shoes are worn out."
- **Service example**: "Five signs your boiler needs a service."
- **Compliance**: In health, symptom lists must not imply a diagnosis or push people to self-treat. Meta restricts ads that assert personal health conditions, so check the platform's policy.
- **Source it from**: Reviews and support messages describing what people noticed before buying.

### 32. Exaggerated visual

A striking, exaggerated image (a screaming knee, a giant product, a surreal scene) with a short, direct headline and a line or two of proof.

- **Tier**: B (provisional). Role: supporting cast, with cold reach when the image is strange enough to stop the scroll. The image does the hook, and the copy should be plain so the ad does not feel like a trick.
- **Structure**: One exaggerated image covering most of the frame, a headline of 3 to 6 words, one or two proof lines, a small product.
- **Copy slot**: The pain or result the image exaggerates, stated literally.
- **Shop example**: An illustrated sofa sinking into the floor: "Still sitting on your old sofa?"
- **Service example**: An inbox drawn as a collapsing tower: "Behind on your admin?"
- **Compliance**: Bodies and body parts trigger Meta's personal-health rules. Do not shame, and do not use before and after body images for weight loss.
- **Source it from**: The strongest pain metaphor customers use in reviews.

## Visual styles (apply to any template)

A style changes how a template looks, not what it argues. Pair any template with one of these to get a new-looking ad without a new angle. Test the style and the template separately so you know which one moved results.

| Style | What it looks like | Pairs well with |
|---|---|---|
| Dark mode text | White text on black, a phone-note feel, no imagery | Founder message, Reassurance list |
| Retro computer screen | A blue terminal or old monitor, monospace type | Reassurance list, Headline statement |
| Billboard | The message on a roadside billboard in a photo | Headline statement, Us vs. them (a two-panel billboard) |
| Notice board or flyer | A taped-up poster or flyer on a wall | Signs checklist, Headline statement |
| Presentation slide | The message on a conference screen with a speaker and audience | Challenging a belief, Headline statement |
| Whiteboard | Handwritten marker on a whiteboard | Us vs. them, With and without |
| Handwritten sign | A real person holding a hand-lettered sign | Review card, Origin story |
| Mirror writing | Text written on a bathroom mirror | Problem and answer, Reassurance list |
| Magazine or news card | A "News" label and editorial headline layout | Educational infographic, Important update |
| Newspaper | A newspaper front page with the offer as the headline | Sticky note sales, Important update |
| Vintage print ad | A 1950s or 60s illustrated ad with period type | Exaggerated visual, Headline statement |
| Illustration | Hand-drawn or children's-book style art | Character story, Educational infographic |
| Meme | A known meme template with the two states labelled | With and without, Before and after |
| Retro app frame | The design shown inside an old paint program or retro phone screen | Sticky note, Founder message |

Rules for styles that borrow a real look:

- News and magazine styles must not copy a real outlet's name, masthead or logo, and must not make an ad look like independent reporting. A "News" label is fine only when the content is real news about you.
- A retro app frame is a visual style. A fake system dialog is something else: an ad that looks like an operating-system alert, a notification, a "sensitive content" screen or a working button shows features that do not exist, and Meta rejects it. Keep the frame obviously decorative, and keep the call to action in the ad's real button.
- Vintage and tabloid styles invite tabloid claims ("doctors stunned", "amazingly, it worked"). Keep claims to what you can back up. The style is the joke and the claim is not.

---

## Per-concept output format

Each generated concept follows this structure:

```markdown
## Concept [N]: [Template name]

**Headline**: [the headline copy]
**Body**: [supporting copy, if the template uses it]
**Visual brief**: [what a designer, a phone photo or a free design tool should show: layout, subject, text placement, colours]
**Grounded in**: [which review, past winning ad or comment this traces to, quoted or named]
**Checks needed**: [any claim, quote, comparison or result in the concept, and where its proof is kept]
```

The visual brief is a plain description. An image-generation tool is optional and is never required. Photos you take yourself of your real product, your real work or your real premises are usually the safest and most believable source.

Record each concept's tier alongside its template so the reviewer sees the role at a glance. For a larger batch, add an `INDEX.md` listing every concept with its template, tier and grounding source, so the reviewer can scan the batch quickly.

## Batch distribution

A beginner should start with 3 to 5 concepts, not 50. A small budget cannot judge more than that: each concept needs to spend about 3 times the owner's maximum cost per result before it can be judged (see the one stop rule in `paid-ads-strategy`). Example: if your maximum cost per result is £20, each concept needs about £60 of spend before you can read it, so five concepts need about £300.

For a larger batch (for example 50 concepts, for an account with a big budget and a regular creative routine), spread variations across the template set and let tier and funnel goal shape the weighting rather than splitting evenly:

- For cold reach, weight towards the S and A tiers (Founder message, Origin story, Grid static).
- For warm audiences and retargeting, lean on the B tier (Callout, FAQ card, Before and after, Competitor callout, Simple guarantee, With and without).
- For a real sale, add Apology letter, Important update and Sticky note, only when the offer and its end date are real.
- Treat the provisional tiers on templates 23 to 32 as guesses until your account has results.
- Skip the E and F formats (Press mention, Testimonial statics, Numbered list) unless you have a specific reason.

If your own results show certain templates consistently winning, shift towards about 60% proven templates and 40% full-set coverage, and never drop coverage to zero. Creative gets tired, so the template that works this month may not work next month.

---

Credit: adapted from Corey Haines' marketingskills pack (MIT licence). The tier ranking is based on one practitioner's public ranking of Meta creative formats, and templates 23 to 32 come from a review of public ad libraries.
