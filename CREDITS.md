# Credits

Claude for Paid Ads is built and maintained by [Jawad Ahmed](https://github.com/jawadbuilds). It stands on open-source work by other people. This page says exactly what came from where, and what was changed.

## What is original

- All 8 agents in `agents/`
- 11 skills: `ad-assets-audit`, `ad-claims-check`, `cost-ceiling-planner`, `human-copy-check`, `launch-paused`, `meta-ad-library-research`, `meta-connector-field-notes`, `performance-breakdown`, `plain-language-coach`, `start-here`, `tracking-preflight`
- The setup guides in `docs/`, the checks in `scripts/`, the installer and the artwork in `assets/`

Every skill says where it came from in the `origin` line at the top of its `SKILL.md`.

## What is adapted

### Ryze AI: marketing-skills

- Source: https://github.com/irinabuht12-oss/marketing-skills (commit `b3bdcd6`)
- Licence: MIT, as declared by the authors. See `licenses/ryze-marketing-skills-NOTICE.md`.
- Used: its skills were the starting point for 35 skills here. 24 were rewritten with a new method and keep only the idea: `ab-test-setup-and-analysis`, `account-structure-review`, `ad-copy-variant-generator`, `ad-spend-allocator`, `ai-visibility-audit`, `anomaly-detection`, `audience-overlap-analysis`, `bid-strategy-recommendations`, `budget-scenario-planner`, `campaign-naming-convention-builder`, `client-report-narratives`, `competitor-creative-analysis`, `content-aeo-optimizer`, `conversion-path-analysis`, `cpa-diagnostics`, `creative-fatigue-detection`, `keyword-cannibalization-check`, `pacing-monitor`, `quality-score-breakdown`, `retargeting-window-analysis`, `roas-forecasting`, `search-term-mining`, `wasted-spend-finder`, `weekly-account-summary`. 11 keep much of the original text, corrected and extended: `ab-test-analyzer`, `competitor-teardown`, `content-repurposer`, `e2e-seo-assistant`, `email-sequence-writer`, `google-ads-audit`, `icp-research-assistant`, `landing-page-audit`, `linkedin-ads-audit`, `meta-ads-audit`, `utm-tracking-generator`.
- Changed: the "Data access (Ryze MCP)" section and every link to the Ryze product were removed from each skill. A "Getting the data" section (free connector, exported report or pasted numbers) and a "Rules" section were added. Numbering was removed from titles. `landing-page-audit-39` was renamed `landing-page-audit`. After an audit on 26 November 2026, factual errors were corrected and rules that could cost an advertiser money were replaced in several of these skills, among them `google-ads-audit`, `meta-ads-audit`, `landing-page-audit`, `utm-tracking-generator`, `ab-test-analyzer` and `attribution-model-comparison`.
- Left out, or folded into another skill after the audit: the shorter of its two landing page audits, `reddit-ads-audit`, `performance-benchmarking`, the two programmatic SEO skills, `channel-mix-optimizer`, the three separate breakdown skills (now `performance-breakdown`), `frequency-cap-recommendations`, `attribution-model-comparison`, `citation-source-gap-finder`, `brand-answer-monitoring`, and `ad-extension-audit` (now `ad-assets-audit`).

### Corey Haines: marketingskills

- Source: https://github.com/coreyhaines31/marketingskills (commit `8fd2fca`)
- Licence: MIT. See `licenses/coreyhaines31-marketingskills-LICENSE.txt`.
- Used: `ads` (here named `paid-ads-strategy`) and `ad-creative`, with their reference files.
- Changed: the "Tool Integrations" and "Related Skills" sections were removed and replaced with links to skills in this kit. Links to skills that are not part of this kit were turned into plain text. In `ad-creative`, the "Generating Ad Visuals" section and `generative-tools.md` (a list of paid generation tools) were removed. In `paid-ads-strategy`, the LinkedIn and account-based-marketing playbooks were left out, and a mention of paid scraping services was replaced with the free route. `motion-video-ads.md` and `imessage-video-ads.md` were removed because they depend on paid generation services or a production pipeline. After an audit on 26 November 2026 both skills were corrected and tightened: the strategy files now share one rule for when to stop an ad, rules of thumb are labelled as such, and the platform specifications were rewritten from Google's and Meta's own pages.

## What is copied whole

### Agrici Daniel: claude-ads, claude-seo and claude-blog

- Sources: https://github.com/AgriciDaniel/claude-ads at tag `v2.1.0`, https://github.com/AgriciDaniel/claude-seo at tag `v2.6.2`, and https://github.com/AgriciDaniel/claude-blog at tag `v2.3.2`
- Licence: MIT. Each copy keeps its own `LICENSE` and notice files, in `plugins/claude-ads`, `plugins/claude-seo` and `plugins/claude-blog`.
- Changed: the `.github` folders were removed. Links to a paid community were removed from the README, CONTRIBUTING and CONTRIBUTORS files, and the "Community Footer" section was removed from `plugins/claude-seo/skills/seo/SKILL.md` and from `plugins/claude-blog/skills/blog/references/blog-delivery-contract.md`. Nothing else was changed.
- These are separate plugins. They install beside the core kit and keep their own names and commands.
- Some of their features are optional and use services with their own keys or charges, such as paid SEO data sources in `claude-seo` and image or audio generation in `claude-blog`. Nothing in the core kit needs them, and they stay off unless you set them up.

## Recommended, not included

These are linked from the guides. None of their code is in this repository.

- [Meta's ads connector](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview), run by Meta
- [googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp), Google's open-source Google Ads connector (Apache-2.0)
- [athm793/meta-ads-scraper](https://github.com/athm793/meta-ads-scraper), a local Meta Ad Library research app (Apache-2.0)

## The free-only rule

No skill in the core kit needs a paid key. No paid product is installed by default. There are no affiliate or tracking links. `scripts/check.py` enforces this on every change.

If you are an author listed here and something is credited wrongly, please open an issue and it will be fixed.

Claude for Paid Ads is an independent community project. It is not affiliated with or endorsed by Anthropic, Meta or Google.
