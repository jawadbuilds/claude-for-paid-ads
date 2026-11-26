# The creative strategy loop

Writing (Paths A to C in the skill) answers "make me ads." This reference answers the question that comes first: which ads are worth making, in what order, at what production cost. It also covers the retro (a short review of what the last month taught you) that turns each month's results into next month's plan. It is the standing operating loop of a creative strategist, run by an agent with a human deciding.

```
Signals, then Concepts (ranked by evidence), then Roadmap (tiered, capacity-checked), then Briefs, then [Paths A to C produce], then Monthly retro, then back into the icebox
```

**If you are a one-person business:** you do not need the team version of this loop. Keep one roadmap page, take one monthly look at what happened (the retro), and plan 2 to 3 new ads a month, within the number your budget can judge (see the capacity check in step 4). The weekly and quarterly rhythms below are for teams; a solo owner can skip them.

---

## Step 1: Read the three signals

Creative direction comes from combining three independent sources. One source alone misleads: the account tells you what worked among the things you have tried, customers tell you why they buy in their own words, and organic content tells you what the audience chooses to watch when nobody is paying.

| Signal | What to pull | How |
|---|---|---|
| **Account performance** | Winners and losers by angle, hook and format; funnel numbers per concept (see the diagnostic funnel in [hook-system.md](hook-system.md)); fatigue state | The platform's own reports, exported as the kit's guide `docs/use-exports.md` describes, or a connector if one is set up |
| **Customer and brand** | Verbatim pain, desire and objection language; unexpected use cases; who is actually buying compared with who is targeted | The reviews and comments you have collected, sales-call notes and support themes; see `icp-research-assistant` |
| **External organic** | What the niche watches unpaid: top organic content, its hooks, formats and vocabulary; competitor ads that have run for a long time (a sign they may be working) | `meta-ad-library-research`, `competitor-creative-analysis` and `competitor-teardown` |

**Cadence for a team:** a monthly deep dive (60 to 90 minutes, all three sources, feeding the monthly roadmap) plus a weekly refresh of about 20 minutes (what changed: new winners and losers, new review themes, anything spiking organically). Research beyond what the next decision needs is busywork, so every session should end in concepts, not notes.

**Trust rule:** every insight the agent surfaces must carry its receipt: which review, which ad's numbers, which organic post. An insight without a source does not enter the icebox. (Same grounding rules as everything else in this skill.)

---

## Step 2: Turn signals into concepts ranked by evidence

A **concept** is one testable creative hypothesis: segment, motivation, angle and format, with its evidence attached. "UGC for mums" is not a concept (UGC is user-generated content: ads that look like ordinary customer posts). A concept looks like this. Example: new-parent insomniacs (per [number] reviews mentioning 3am feeds), motivation "quiet enough to not wake the baby", before-and-after demo angle, POV night-shot video format.

Rank every concept by the strongest evidence behind it:

| Tier | Evidence | Weight |
|---|---|---|
| 1 | Your own account: a converting ad with the same angle or segment | Strongest. Iterate and extend |
| 2 | Your customers verbatim: recurring review or call language | Strong. Build new creative on it |
| 3 | Competitor creative that has run for a long time (rule of thumb: about 60 days or more, so presumed working) | Good. Adapt the angle, never the ad |
| 4 | Organic engagement in the niche (unpaid views or saves on the theme) | Moderate. Validate cheaply first |
| 5 | Cross-niche pattern (worked in an adjacent category) | Weak. Icebox until corroborated |
| 6 | Team hunch, no external signal | Weakest. Low-fidelity test or drop |

Higher evidence earns roadmap priority, meaning an earlier slot in the slate. Production tier is a separate call, set by validation strength, existing assets, capacity and risk: even a tier 2 customer-language concept starts low-fidelity until it shows a funnel signal. Hunches are not banned. They are just cheap and last.

---

## Step 3: Branch on account state

The right creative mix depends on which of two states the account is in. Diagnose before roadmapping, because a plan built for the wrong state wastes the month.

**Exploration state** means nothing (or nothing new) is working:
- Go wide, not deep: mostly net-new concepts across different segments and angles, with iterations kept to a small minority. Iterating on losers multiplies losers.
- Redefine "win" per metric. With no full-funnel winners, a single-metric improvement on any test (a hold-rate lift, a lower cost per click, a better conversion rate), measured against this account's own earlier ads, is a hit worth pulling on. See the diagnostic funnel.
- Iterate only on hits; everything else stays exploratory.
- Common root causes to check while testing: the creative is boring (safe, seen before), the message is overcomplicated, the offer is unclear, or CPMs (cost per 1,000 views) are punishing a too-narrow audience.

**Scaling state** means one or more concepts are converting profitably:
- Go deep on the winner while it is open. Build a winner-led slate of visually distinct variations of the winning concept (same message, new execution; near-duplicates mostly compete with the original for the same viewers and teach you nothing new, so variations must look meaningfully different), plus a remix lane (tonal or emotional re-executions of it) and sub-angle probes that drill into the winning segment. Tune the split to budget, fatigue speed and production speed.
- Keep a small exploration allocation alive even mid-scale. Winners fatigue, and the next winner is rarely an iteration of the current one.
- Speed matters more in this state, because a scaling window is finite.

---

## Step 4: The roadmap artifact

Maintain one living document (suggested: `roadmap.md`, kept with the reviews, comments and past ads you have collected) with three horizons:

```
## Icebox        every concept, evidence tier and source attached, nothing scheduled
## This quarter  2 to 4 themes chosen from the icebox (the bets), with why-now
## This month    the slate: concept | evidence tier | production tier | owner | status
```

Each concept on the monthly slate gets a **production tier**:

| Tier | Cost | What it is | Use for |
|---|---|---|---|
| **T1: Iteration** | Hours | New hook, caption or crop on an existing asset | Extending proven winners |
| **T2: Remix** | Days | New creative from existing footage and assets (a paid generation tool is optional, never required) | Concepts with decent evidence or a first low-fidelity signal |
| **T3: Production** | Weeks | Net-new shoot, creators, full build | Only angles with own-account proof or a prior low-fidelity funnel signal (fidelity ladder in [hook-system.md](hook-system.md)) |

**Capacity check, the rule that keeps roadmaps honest.** There are two limits, and the slate must fit under both.

1. **What you can produce at quality this month.** Count what the team (or the pipeline) can make well and roadmap to that number. A 20-concept slate against 8 concepts of real capacity does not produce 20 ads. It produces 20 compromised ones and a tired team.
2. **What the budget can judge.** An ad cannot be judged on results until it has spent at least 3 times the owner's maximum cost per result (the most they can pay for one result and not lose money). So the number of ads the budget can judge in about two weeks is:

```
ads the budget can judge = (daily budget x 14) / (3 x maximum cost per result)
```

Example: a daily budget of £30 and a maximum cost per result of £20 gives (30 x 14) / (3 x 20) = 420 / 60 = 7 ads judged in two weeks. A slate of 20 new ads on that budget would leave most of them with too little data to judge. Cut by evidence rank until the slate fits both limits. The 3-times rule is the kit's rule of thumb, set out in the one stop rule in `paid-ads-strategy`.

From the slate, generate **one brief per concept** (segment, motivation with verbatim source, angle, format, hook matrix rows, production tier, success metric) and hand each to Paths A to C for writing.

---

## Step 5: The monthly creative retro

The last step of the loop and the first input of the next one. One artifact per month (suggested: `retros/YYYY-MM.md`):

```
## Winners      concept, the funnel numbers, and the WHY (which element earned it)
## Losers       concept, where in the funnel it died, hypothesis for why
## Metric wins  full-funnel losers with one strong metric (these are leads, not losses)
## Learnings    pattern-level notes, written back into the icebox as new or revised concepts
## Kills        concepts retired from the icebox, with reason
## Next slate   first draft of next month, with updated evidence ranks
```

Retro rules:

- **Judge concepts, not ads.** Three executions of one concept failing says the concept is wrong. One failing says the execution was.
- **Read the funnel, and look beyond the return-on-ad-spend column.** The diagnostic funnel says what to fix, while return on ad spend alone says only that something is broken.
- **Enough data before verdicts.** Whether an ad or concept has earned a stop is decided only by the one stop rule in `paid-ads-strategy`. A two-day read is a coin flip, and the honest verdict is "too little data to judge yet".
- **Every learning lands somewhere:** an icebox update, an evidence re-rank or a kill. A retro that changes nothing in the roadmap was a meeting, not a retro.

There is no scheduler in this kit: run the retro by hand on the first of each month. Teams can add a weekly refresh on Mondays. A solo owner needs only the monthly look.

---

## Failure modes

- **Roadmapping without a diagnosis.** A slate built before reading the three signals is a wish list, and testing without a diagnosis is not strategy.
- **Iteration-heavy slates in exploration state.** Polishing losers while the real problem (angle, offer, audience) goes untested.
- **Ignoring capacity.** A plan the team cannot produce at quality, or the budget cannot judge, is a plan to produce slop.
- **Evidence-free concepts jumping the queue.** The loudest stakeholder's hunch ships as a T3 shoot while tier 2 customer language sits in the icebox.
- **Retro as theatre.** Winners celebrated, nothing re-ranked, icebox untouched.
- **Scaling-state complacency.** The whole slate goes on winner variations, and when the winner fatigues the pipeline is empty.
