# The creative review page

A shareable, self-contained web page that presents generated ad concepts for a client or owner to review and pick. It is the visual upgrade to `INDEX.md`. The markdown outputs are built for the person running the ads. The review page is built for the person approving the spend: it shows each concept as an in-feed Instagram or Facebook mockup, breaks carousels into a labelled frame-by-frame storyboard, lets them switch between copy variations, and says which claims are real and which still need the owner's confirmation.

The template ships at [assets/creative-review-template.html](../assets/creative-review-template.html). It is one file with inline CSS and JS. It needs no build step, no extra software and no internet connection, and it loads nothing from the web (no fonts, no scripts, no tracking). The person reviewing only opens the file in a browser. Claude fills in the data; nobody has to edit code.

## When to produce one

- **Presenting a batch for approval.** After generating a batch of concepts, package the best ones into a review page instead of (or alongside) `INDEX.md`. Picking 5 of 50 is a visual decision, and an owner should not have to read markdown to make it.
- **Pitching a partnership ad with a creator.** Show the creator exactly what the ad looks like under each account (the brand's and the creator's), with the steps spelled out.
- **A monthly slate review.** Render the slate's concepts so the pick happens from one file.

Do not produce one for a single headline tweak or a quick gut-check, because the markdown output is faster. Use the review page when someone other than you needs to choose.

## How it is built

The template draws everything from a block of JSON near the top of the file: `<script type="application/json" id="review-data">`. Claude fills that block from the generated concepts and everything else renders from it: tabs, previews, storyboard and copy panel. Nobody edits the code below the data block. The annotated model below uses `//` comments for readability, but the file itself is strict JSON: no comments, no trailing commas (see "Filling in the data safely").

The sample data is a made-up business, "Brightpath Maths (sample)". Every sample claim is either true by construction or marked as a placeholder for the owner to confirm. Replace all of it with the real project, and never copy a sample claim into a real ad.

### Data model

```jsonc
{
  "project": {
    "brand": "Brightpath Maths (sample)",   // required
    "agency": "Sample Agency",              // optional: adds a "with" line and the partner label used when a concept has no handles
    "date": "2026-11-26",                   // optional
    "note": "one-line context"              // optional
  },
  "platforms": ["instagram", "facebook"],   // previews to offer; the first is the default. Supported: instagram, facebook
  "concepts": [                              // each concept is one strategic angle (see SKILL.md, "Define your angles")
    {
      "name": "Free trial lesson",           // required: the angle name
      "tagline": "Lead with the free 30-minute trial",   // one line on what makes this concept different
      "handles": [                           // optional. 1 entry = a normal post; 2 = the account toggle (see below)
        { "name": "brightpathmaths", "partner": "Paid partnership with samplecreator", "initials": "BM" },
        { "name": "Sample Creator", "partner": "Paid partnership with brightpathmaths", "initials": "SC" }
      ],
      "frames": [                            // 1 frame = single ad; several = carousel storyboard
        {
          "label": "Hook",                   // the frame's job in the story
          "prompt": "Teenager at a laptop, friendly teacher on screen",  // image description (shown as a placeholder if there is no image)
          "image": "images/free-trial-01.png",   // optional: local path or data URI; leave out for text-only concepts
          "headline": "Try a free 30-minute maths lesson, online.",       // optional text over the frame
          "headlineTheme": "dark"            // optional: "dark" (default, white text) or "light" (dark text on light imagery)
        }
        // one object per frame
      ],
      "headlines": [                         // selectable variations; the chosen one is shown on frame 1 of the preview
        "Try a free 30-minute maths lesson, online.",
        "Maths lessons for ages 11 to 16, one to one.",
        "Your first lesson is free. Lessons after that are £19."
      ],
      "primaryText": "The caption or body copy.",
      "likes": "1,000",                       // optional Instagram like count. Leave it out unless it is a real figure; with no value, no count is shown
      "destination": { "url": "brightpathmaths.example", "cta": "Book now", "offer": "Free 30-minute trial lesson" },
      "rollout": {                           // optional: the steps for how this runs (partnership ad, launch plan)
        "title": "How the partnership ad runs",
        "steps": ["step 1", "step 2"]
      },
      "grounding": "What is real, and what the owner must confirm. See below."
    }
    // 2 to 4 concepts is the sweet spot; more than that and the tabs stop being a decision
  ]
}
```

### The account toggle (partnership ads)

When a concept has two `handles`, the page shows a toggle that switches the preview between two accounts: the brand's own account and a creator's account. This shows how the ad would look if it were posted from the creator's account instead of the brand's. Running an ad from a creator's account needs that creator's permission. Meta calls these partnership ads (some people call the practice whitelisting). The creator gives the brand permission in their own account settings, and the ad then carries a "Paid partnership" label. With one handle, or none, there is no toggle and the ad shows as a normal post from the brand.

### The frame storyboard is a carousel story

A concept's `frames` are its storyboard. Label each frame by the job it does, not by what is pictured: `Hook`, `The worry`, `How it works`, `The ask`. A carousel works like a short story, so each frame should move the reader on to the next one. A common run is: a hook that stops the scroll, the problem the viewer recognises, how the product or service solves it, the proof (only if it is real), and a clear ask. Pick the run that fits the angle before writing frames.

### Images and placeholders

Every frame shows in one of two ways:
- **`image` given.** The real creative (from the batch's `images/` folder, or a data URI) fills the frame.
- **`image` left out.** A styled placeholder shows the frame `label` and `prompt`. This is the normal state for concepts that have copy and an image description but no finished image yet. The review page is useful before images exist and stays useful as they are added.

Remote and protocol-relative image URLs are blocked, including URL spellings the browser normalises. Keep image files in a local `images/` folder next to the page and use relative paths. This restriction applies to the image sources supplied in the data, not to arbitrary edits to the HTML.

Ship review pages with placeholders freely, because they communicate the concept. Swap in images as they are made.

## Grounding: the disclosure block is required

Every concept must carry a `grounding` line, and it must be true. It tells the owner exactly what is real, what is illustrative, and which claims the owner still has to confirm before the ad can run. In the page it appears under the heading "What is real, and what to confirm". Write it in two parts:

- **Real:** the facts the concept rests on (for example, "free 30-minute trial lesson", "ages 11 to 16, online", "lessons £19"), with where they came from.
- **Owner to confirm:** every claim that is a placeholder or has not been checked (for example, "qualified UK teachers"), so the owner can approve or remove it before launch.

Never present invented statistics, made-up test results, reviews, customer counts or stock imagery as the business's own. If a concept's proof is not real yet, the grounding line says so plainly. A review page that passes fiction off as fact is worse than no review page.

## Filling in the data safely

The data sits in a `<script type="application/json" id="review-data">` block. It is inert data (read with `JSON.parse`), not code, so a value can never run as a script. Claude follows two rules when writing it:

- **Valid JSON only.** Double-quoted keys and strings, no comments, no trailing commas. If the JSON is malformed, the page shows a clear error banner, so a typo fails loudly rather than silently.
- **Escape `<` as `<` in every text value.** A value that literally contains `</script>` would otherwise close the data block early. Apply this escape to every string value. All values are also HTML-escaped again when the page draws them, but the escape in the source is the one that matters.

## Producing and delivering it

1. Copy `assets/creative-review-template.html` into the batch's output folder as `review.html` (for example `outputs/YYYY-MM-DD/review.html`).
2. Replace the sample data with the real project: concepts, frames, copy and grounding. Add `image` paths for any frames that have been made, kept relative to the HTML file so the folder stays portable.
3. Check it: open it in a browser, click through every concept tab, both platform buttons, the account toggle and every frame in the storyboard.
4. Deliver it with no account or hosting needed. Either the person opens the file in their browser, or you send the file itself by email or shared drive. If the page uses image files, send the whole folder as a zip (the `.html` file plus `images/`), or embed the images in the file as data URIs so it stays a single file.

Keep the review page next to the markdown outputs, not instead of them. `INDEX.md` and the per-concept files remain the working record and the claims audit trail. `review.html` is the approval page built on top of them. Before anything goes live, run `ad-claims-check` on the final copy.

## Common mistakes

- **Too many concepts.** Two to four tabs is a decision; ten is a menu nobody finishes. Choose the best before presenting.
- **Frames labelled by content.** Label by the job the frame does (`The offer`), not by what is pictured (`Laptop photo`).
- **Missing or dishonest grounding.** Every concept says what is real and what the owner must confirm. Illustrative proof is labelled illustrative.
- **Editing the drawing code.** Everything is driven by the data. If something does not show, look at the data fields, not the JS.
- **Absolute image paths.** Keep image paths relative so the folder can be zipped, moved or sent intact.
- **Copying sample claims.** The sample business is made up. Replace every claim with the owner's own, checked facts.

Credit: the review-page idea and template are adapted from Corey Haines' MIT-licensed marketingskills pack, with the sample data and wording rewritten for this kit.
