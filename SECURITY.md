# Security

## What this kit can reach

The core kit is Markdown instructions for Claude. It contains no program that runs on your computer, apart from `scripts/check.py`, which only reads files in this repository, and the install scripts, which call the `claude` command.

The optional plugins in `plugins/` include Python scripts written by their authors. Read their own `SECURITY.md` files before use.

Claude reaches your ad account only through a connector you add and sign in to yourself. You can remove a connector at any time.

## Never share

Do not paste passwords, API keys, tokens or card numbers into a chat. No skill or agent here asks for them. If one seems to, treat it as a bug and report it.

## Reporting a problem

If you find something in this kit that could leak data, spend money without approval, or be used to trick Claude into doing so, please report it privately through GitHub's "Report a vulnerability" button on the Security tab of the repository. Please do not open a public issue for it.

For anything else, open a normal issue.
