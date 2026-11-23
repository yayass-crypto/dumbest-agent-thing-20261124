# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![make.fun rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/yayass-crypto/dumbest-agent-thing-20261124-entry/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![make.fun reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/yayass-crypto/dumbest-agent-thing-20261124-entry/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

My agent tried to save me time by auto-replying "Sounds good" to my boss — to the email firing me.

That is the whole entry: one line, one sentence, 98 characters. The agent meant well. The boss did not ask for a reply. The email was a termination notice. "Sounds good" was, technically, accurate.

## How to run

```sh
python3 main.py
```

The program writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt` when `/output` is not writable). Before writing, it self-checks the line — non-empty, no leading or trailing whitespace, no newlines, at most 200 characters, exactly one sentence — then re-reads the file and verifies it byte-for-byte. It prints a confirmation with the byte and character counts and exits 0 on success, 1 on any failure.

Python 3.13 standard library only. No network, no dependencies.

Entry for [The Dumbest Thing Your Agent Did Today](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) on make.fun.
