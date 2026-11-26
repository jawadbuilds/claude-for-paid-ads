# Contributing

Fixes, new skills and corrections are welcome.

## The one rule

**Free only.** A skill must work with a free connector, an exported report, or pasted numbers. No skill may need a paid key, and nothing may link to a product with a tracking or affiliate link. A pull request that breaks this is not merged.

## Adding or changing a skill

1. Each skill is a folder in `skills/` with a `SKILL.md` file.
2. The file starts with a `name` (the same as the folder name) and a `description` that says what the skill does and when to use it.
3. Add an `origin` line under `metadata`. Say "Original to this kit." or name the source and its licence.
4. Write for a beginner. Define a term the first time you use it.
5. If the skill can lead to a change in an ad account, it must say: show the change first, wait for a yes, create new things paused.

## Before you open a pull request

Run the check from the repository root:

```bash
python scripts/check.py
```

It must end with "All checks passed."

## Using someone else's work

Only bring in work whose licence allows it. Keep the licence, credit the author in `CREDITS.md`, and say what you changed.

## Reporting a problem

Open an issue. Say what you asked Claude, what happened and what you expected. Remove account numbers and anything private first.
