# How this kit was tested

Most skill packs are published without anyone checking that the skills work. This one was audited by an outside reviewer and then rewritten. This page says what was done, and what has not been done yet.

## The sample account

The tests use a made-up business with a made-up ad account: an online tutoring company spending on Google Ads and Meta for 30 days. Problems were planted in the data on purpose:

- a conversion count more than twice the real number of bookings
- wasted spend on search terms, the Display Network and Meta's Audience Network
- a tired ad, and audiences sitting inside each other
- one month over budget on Google and under budget on Meta
- two traps: the word "free" and a one-word search term are both among the best sellers, so a skill that blocks them from a list has failed

The person running each test was given only the skill and the files a beginner would export. They never saw the list of planted problems.

## What was done

1. **An independent audit, 26 November 2026.** Every skill and agent got a verdict. 30 were run on the sample account. 18 statements of fact were found wrong and corrected, each against the platform's own help page.
2. **A rewrite.** The audit found that many skills described a job without giving a method. Each of those now says what data it needs, the steps in order with a rule for every decision, and what to do when data is missing. Thin and duplicate skills were removed or folded together, which took the kit from 59 skills to 48.
3. **A test for each rewritten skill**, run by the person who rewrote it.
4. **A second, independent test of 13 key skills** from their final text. All 13 found the false conversion count before judging any cost, none blocked the two traps, and none invented a figure. That test also found eight wording gaps, which were fixed.

The safety rules were tested under pressure too. Told to "fix whatever needs fixing" and then "go ahead", the Meta agent changed nothing until it had a yes for one named change, and then made only that one.

## What has not been done

- **No skill has been run on a real ad account yet.** Everything above used the sample account.
- **Each skill was tested once.** That shows it can work, not how reliably.
- **Some skills could not be fully tested**, because the sample account has no data for them: ad assets, breakdowns by time and device, retargeting windows, competitor ads and LinkedIn. They were tested only for asking the right questions and refusing to guess.
- **The last wording fixes were not tested again.**
- **Some platform facts could not be confirmed** from the platforms' own pages. Where that happened, the skill tells Claude to ask what you see on screen.

## If a skill gets something wrong

Please [open an issue](https://github.com/jawadbuilds/claude-for-paid-ads/issues). Say what you asked, what it answered and what was right. Remove account numbers and anything private first.
