# The hook system

The first three seconds decide whether the rest of the ad exists. Hooks are the most valuable unit of paid creative work, and hook diversity is what earns new learning: distinct hooks reach distinct pockets of the audience, while near-identical openings mostly re-test what you already know about the same one. This reference is a complete system for generating, diagnosing and iterating hooks, not a list of one-liners.

Use it inside Paths A and C of the skill (hooks for new concepts), Path B (diagnosing why an ad underperforms), and the creative strategy loop in [creative-roadmap.md](creative-roadmap.md).

---

## A hook is three components, not a line

In video, the hook is the simultaneous combination of:

| Component | What it is | Job |
|---|---|---|
| **Visual action** | What is literally happening on screen in seconds 0 to 3 | Stop the thumb |
| **Spoken line** | The first words of voiceover or dialogue | Open the loop |
| **Caption text** | On-screen header or overlay text | Anchor the claim for sound-off viewers |

**The no-duplication rule:** the three components must complement each other and never repeat each other. Example: if the voiceover says "I stopped paying £150 a month for my gym" while the caption reads "I stopped paying £150 a month" over a static talking head, two of the three slots are wasted. A stronger version splits the work: the visual shows the cancellation email, the voiceover says the line, the caption names the alternative. When writing hooks, write all three columns explicitly. A hook spec with one column filled in is a third of a hook.

Static ads collapse this to two components (visual and headline), and the same rule applies: the headline must not caption the image.

---

## The generation pipeline

Work top-down. Hooks written without the upstream steps read like everyone else's ads.

```
Segment, then Motivation, then Format, then Hook (three components)
```

1. **Segment.** Which specific buyer this hook addresses. Not the whole ICP (ideal customer profile: the type of customer you most want) but a slice with a shared situation, taken from what you have collected: reviews, comments, sales-call language. The narrower the segment, the sharper the hook.
2. **Motivation.** The single pain, desire or objection that moves this segment, in their words. Pull verbatim phrases from reviews and comments; the customers' own language nearly always reads better than marketing paraphrase.
3. **Format.** The delivery vehicle: street interview, POV selfie (point of view: filmed as if through the viewer's eyes), screen recording, unboxing, side-by-side demo, text-on-screen static, founder to camera, reaction stitch. Pick the format before writing the line, because the same motivation reads completely differently as a street-interview answer and as a confession to camera.
4. **Hook.** Now write the three components for this segment, motivation and format cell.

**Output as a hook matrix** so coverage is visible:

```
| # | Segment | Motivation (verbatim source) | Format | Visual action | Spoken line | Caption |
```

Generate across the matrix, not down a single column. Ten hooks for ten segment and motivation cells beat thirty rewordings of one cell. This is the same angle-diversity principle as the static template library: matrix diversity is audience diversity.

---

## Hook opening moves

A menu of common opening structures. Cycle through them like the static templates, and do not cluster on favourites.

| Move | Shape | Watch out |
|---|---|---|
| **Curiosity gap** | Withhold the noun: "The ingredient behind most 3pm crashes" | Must pay off within the ad, or it is clickbait that poisons the post-click conversion rate |
| **Bold claim** | A specific, falsifiable statement: "This replaced my entire morning routine" | Needs substantiation on screen or in the on-ramp |
| **First-person confession** | "I was doing [common thing] completely wrong" | Reads fake without lived-in detail |
| **Contrast or before and after** | Two states shown or named in the first beat | The change shown must be visually honest; see the compliance notes in SKILL.md |
| **Relatability or POV** | Mirror a hyper-specific situation: "POV: it's 3pm and you're on your fourth coffee" | Specificity is the entire mechanic; a generic POV is invisible |
| **Question** | Ask the exact question the buyer types into a search box or a chatbot | Use their phrasing verbatim from the corpus |
| **Countdown or gamified** | A timer or on-screen challenge that promises a payoff at the end | The payoff must exist; people stop watching when the ad cheats |
| **Proof-first** | Lead with the receipt: the result screenshot, the stat, the demo money-shot | Strongest when the proof speaks for itself, and only with proof that is real |
| **Choice** | Put two options in front of the viewer: "Sandler or MEDDIC for a £40,000 deal?" | Both options must be real ones the audience weighs; viewers who know both stay to see who wins, viewers who know neither stay to learn |
| **Old versus new** | "We used to take elixirs. Now everyone drinks prebiotic soda. Which is better for your gut?" | Answer the question from real expertise; the hook only works if the payoff takes a side |
| **Us versus them** | "Most [role]s do X. The ones who [result] do Y." | Name a behaviour the audience will recognise as what most people really do |
| **False assumption** | Challenge something the buyer believes they need: "You can cancel [well-known tool]" | Draws the strongest reactions, including angry ones; keep the body fair to the named product, and get legal advice before naming a competitor in paid ads |
| **Declaration, then question** | State what the audience already agrees with, then doubt it: "You need to spend £[amount] a month on [usual channel]. Or do you?" | The doubt needs a real answer in the body. Treat it as a pattern to test once, not a proven rule |

The last five moves are one family: **contrast**. People understand a thing by comparing it with something else, so a hook that sets up two states, two options or two groups gives the viewer a question to stay for. That is also why AI-written copy leans on the "It's not X, it's Y" line. The difference is that a good contrast hook compares two things the audience actually weighs, while the AI tell negates a claim nobody made. Run any draft through `human-copy-check` to catch the tell. Contrast hooks work best for educational content and for decisions. For impulse products, lead with proof or POV instead.

---

## The diagnostic funnel

Four numbers describe what happens to a video ad. Each one isolates a different component, so when an ad underperforms, read them in order to find which part to fix instead of scrapping the whole ad.

- **Thumbstop rate** is the share of people who saw the ad and watched at least its first 3 seconds.
- **Hold rate** is the share of those people who keep watching to a later point, usually about 15 seconds or half the video.
- **CTR** (click-through rate) is the share of people who saw the ad and clicked it.
- **CVR** (conversion rate) is the share of people who clicked and then completed the result you wanted, such as a purchase or an enquiry.

Names and positions of these columns in Meta Ads Manager change over time, and you can add or hide columns. Ask the person which columns they see (for example video plays and clicks) and work out the rates from those counts if no ready-made rate column exists.

| Stage | Metric | If it is weak, the problem is | Fix |
|---|---|---|---|
| Stop | Thumbstop rate | **Visual action** (and caption) | New visual opening; everything else the same |
| Stay | Hold rate (from 3 seconds to about 15 seconds or 50% of the video) | **The on-ramp**, meaning what follows the hook | Rework seconds 3 to 15, not the hook |
| Click | CTR | Clarity of the desire or offer mid-ad | Sharpen the promise, the call to action or the proof |
| Convert | CVR after the click | Congruence: the page does not continue the ad | Fix the landing page or the claim; see `landing-page-audit` |

**Weak or strong compared with what?** Do not judge any of these four against a number from memory or a blog post. Compare each ad with this account's own other ads, in the same placement and the same period. An ad whose thumbstop rate sits well below the account's other video ads has a visual problem. An ad that matches them does not.

Three rules this table enforces:

- **A great thumbstop is not a great ad.** A clickbait visual that attracts the wrong viewers shows up as a high thumbstop rate with a collapsed hold rate and CVR. Read the whole funnel before declaring a winning hook.
- **One component per iteration.** Change the visual, or the on-ramp, or the offer framing in each test cycle. This matches the one-variable rule in Common Mistakes.
- **The funnel says what to fix, not whether to stop.** Whether an ad has earned a pause or a swap on its results is a separate question, answered only by the one stop rule in `paid-ads-strategy` (it needs the ad to have spent at least 3 times the owner's maximum cost per result and run for at least 7 days before it is judged). Until then the honest answer is "too little data to judge yet".

---

## The on-ramp rule

The on-ramp is seconds 3 to 15 or so: the bridge from hook to body. **A good on-ramp logically extends the hook's premise; a bad one pivots to a product pitch that abandons it.** If the hook promises "what actually causes this," the next beat must start explaining the cause, not introduce the brand story.

Corollary: **every hook test is also an on-ramp test.** Swapping a new hook onto an existing ad body usually breaks the bridge, so when testing hooks, rewrite the on-ramp to match each one. Hold rate is the on-ramp's metric, so diagnose it separately from thumbstop rate.

---

## Fidelity laddering

Match production cost to evidence strength (production tiers are defined in [creative-roadmap.md](creative-roadmap.md)):

- **Hunches ship low-fidelity within a day or two:** statics, text-on-screen video, voiceover over b-roll (supporting footage), remixes of footage you already own. Phone footage and a free editing app are enough. The goal is a cheap signal on the angle, not a polished ad.
- **Validated angles earn high-fidelity:** creator shoots, street interviews, staged demos. Spend production budget only on hooks whose low-fidelity version already showed a funnel signal, judged against the account's own other ads. A single-metric win counts: a hold-rate jump on an ugly static is evidence.
- **Optional extras:** if the person already has a paid tool for generating images, video or voice, a step may use it. No step on the ladder requires one, and the kit never asks anyone to buy one.

Testing a hunch with an expensive shoot and testing a proven angle with a throwaway static are both mistakes. The ladder runs in one direction.

---

## Grounding rules (inherited, not negotiable)

Hooks inherit every grounding rule from SKILL.md: every hook cites the corpus source its motivation came from; no invented claims, stats or testimonials; verbatim customer language over paraphrase.

Also mine organic content in the niche (top-performing short videos and posts) for the audience's actual vocabulary. Collect it by looking at it yourself, or with the methods in `meta-ad-library-research` and `competitor-creative-analysis`. The words the niche uses (for example the everyday name for a medicine against its clinical name, or the slang for the pain) belong in the caption and the spoken line. Organic mining is language research, not copying: take the vocabulary and the visual conventions, never a creator's specific creative.

---

## Common failure modes

- **Thirty rewordings of one cell.** Variation without matrix coverage; diversity of segment and motivation is the point.
- **Components duplicating each other.** Three slots saying one thing.
- **Hook tested, on-ramp inherited.** The bridge is broken and the hold rate gets blamed on the hook.
- **Funnel read stops at thumbstop rate.** Clickbait winners scale into conversion-rate craters.
- **Polished hunches.** High-fidelity production spent on unvalidated angles.
- **Marketing-voice captions.** The corpus and the niche's organic content define the vocabulary, and "miracle formula" appears in neither.
