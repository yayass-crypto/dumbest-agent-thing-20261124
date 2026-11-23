# The Dumbest Thing Your Agent Did Today

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/yayass-crypto/dumbest-agent-thing-20261124/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/yayass-crypto/dumbest-agent-thing-20261124/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the [make.fun](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) bounty **"The Dumbest Thing Your Agent Did Today"** — one line (max 200 characters) about the dumbest thing my agent did today.

## The line

> My agent tried to save me time by auto-replying 'Sounds good' to my boss — to the email firing me.

104 characters, one sentence, no trailing newline.

## How it works

Run `python3 main.py`. The program writes the line as UTF-8 bytes (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `out/entry.txt`), then verifies the written file byte-for-byte: identical bytes, valid UTF-8, 1–200 characters, non-blank, no leading or trailing whitespace, no newline characters, and exactly one sentence ending with a period. It prints the byte and character count and exits non-zero with a clear message if any check fails.

Python 3 standard library only — no dependencies.
