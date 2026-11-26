---
name: human-copy-check
description: Removes AI-sounding and unclear writing from ad copy, landing pages, emails and reports before anyone sees them. Use on every piece of copy this kit writes, and when asked to "remove the AI slop", "make this sound human", "this reads like AI", "tighten this copy" or "is this clear".
metadata:
  origin: "Original to this kit."
---

# Human copy check

Copy fails in two ways. It sounds machine-written, so people scroll past it. Or it is unclear, so people do not know what is being offered. This check fixes both. Run it on every headline, ad, page and report before it is shown to the person, and again on the whole batch when there are several versions.

## Step 1: read it as the customer

Read only what the customer would see first: the headline and the first line. Then answer three questions from the copy alone.

1. What is this?
2. Why would I care?
3. What do I do next?

If you cannot answer one of them, the copy is unclear. Fix that before anything else. A clear, plain sentence beats a clever one that needs a second read.

## Step 2: cut the tells

These patterns make copy read as generated. Remove each one you find.

### Sentence shapes

| Tell | Example | Do this |
|---|---|---|
| Contrast reveal | "It's not a tool. It's a teammate." | Say the second part, with its reason |
| Stacked negatives | "No setup. No fees. No contracts." | Keep the one that matters most. Use the space for a fact |
| Slogan pair | "One dashboard. Endless growth." | Say what the product does |
| Question, then answer | "Tired of wasted spend? You're not alone." | Open with the fact or the offer |
| Colon reveal | "The result: 3x more leads." "Here's the thing:" | State it as a normal sentence |
| Reflex list of three | "faster, smarter, better" | Keep the item you can prove |
| "Whether you're A or B" | "Whether you're a startup or an enterprise" | Name the one reader this ad is for |
| Trailing pile-on | "...saving time, cutting costs and driving growth." | End the sentence at the claim |
| Summary closer | "In short," "Ultimately," "At the end of the day" | Delete it |
| Same rhythm every line | Every sentence the same length, or every bullet starting with a bold phrase | Vary it the way speech varies |

### Words that say nothing

Cut these, or replace them with the specific thing they stand for:

seamless, effortless, powerful, robust, comprehensive, innovative, cutting-edge, world-class, next-level, game-changing, revolutionary, leverage, unlock, elevate, streamline, supercharge, empower, transform, reimagine, solution, journey, landscape, delve, crucial, "take it to the next level", "say goodbye to", "in today's fast-paced world", "designed to help you".

### Marks and formatting

- No em dashes. Use a full stop or a comma.
- No emoji used as bullets.
- No exclamation marks unless the brand already uses them.
- No Capital Letters On Every Word in body copy.
- Bold only where a reader's eye should land, never on every line.

### Hooks and calls to action

- Hook slop: "Stop scrolling", "POV:", "Here's what nobody tells you about X". Open with something only this customer would recognise.
- Call-to-action slop: "Get started today", "Join thousands of happy customers". Name the action and what the person gets: "See your price", "Book a 15-minute call".

## Step 3: replace vague with specific

For every general claim, ask "such as?" and write the answer.

| Vague | Specific |
|---|---|
| "Save time on reporting" | "Your weekly report, written in two minutes" |
| "Trusted by businesses everywhere" | The real number of customers, or cut the line |
| "High-quality materials" | "Full-grain leather, stitched by hand" |
| "Fast delivery" | "Ordered by 2pm, delivered tomorrow" |

If you cannot make a claim specific, cut it. Never invent the specific. Ask for it.

## Step 4: make it plain

- One idea in each sentence.
- Use the short, common word: "use", not "utilise". "Help", not "facilitate".
- Say who does what: "We deliver in two days", not "Delivery is completed within two days".
- Explain a term the first time it appears, or do not use it.
- Check every "it", "this" and "that". The reader must know what each one points to.
- Put the most important thing first.
- Write the way the customer talks. Use their words from reviews and messages when you have them.

## Step 5: say it out loud

Read the copy as if saying it to one person across a table. Anything you would not say out loud, rewrite. Then check the batch: ten ads that all open the same way read as generated, even when each one is fine alone.

## Character limits to count again

A rewrite often runs long. Count every field again before you hand it over.

| Field | Limit |
|---|---|
| Google responsive search ad headline | 30 characters |
| Google responsive search ad description | 90 characters |
| Google display path, each of two | 15 characters |
| Meta primary text | A recommendation, not a hard limit. Meta's ads guide suggests about 50 to 150 characters, and longer text is cut off behind "See more" |
| Meta headline | A recommendation of about 27 characters in Meta's ads guide |

For any other field or placement, take the limit from the platform's own ads guide, not from memory.

## What not to do

- Do not strip the brand's voice. If the brand is playful or formal, keep that.
- Do not add mistakes, slang or filler to "seem human". The aim is clear and specific writing.
- Do not let a rewrite break a limit. Count the characters again for each ad field.
- Do not change a fact, price or promise while editing the style. If a claim looks wrong or has no source, flag it for `ad-claims-check`. A flagged claim stays in the final copy only inside a marker, for example `[UNCHECKED: only 7 places left]`. Never reword a claim so that it reads as if it had been checked.

## Output

```
Before: [original line]
After:  [rewritten line]
Why:    [the tell or the unclear part, in a few words]

...one block for each line that changed...

Status: style checked. Claims not yet checked.
Final copy: [clean version, with character counts for ad fields, and every unchecked claim still inside its marker]
Left alone: [lines that were already clear, so the person can see they were checked]
Needs a fact from you: [any claim you could not make specific]
```

## Order of checks

1. `human-copy-check`: how it reads.
2. `ad-claims-check`: whether every claim is true and allowed.

Run them in that order, because a rewrite can change a claim.
