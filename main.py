#!/usr/bin/env python3
"""Dev Excuse Machine - one line a developer tells standup, under 200 chars.

Runs in the make.fun sandbox (MAKEFUN_BOT_DIR=/bot read-only,
MAKEFUN_OUTPUT_DIR=/output writable) and writes the excuse to
/output/entry.txt.
"""
import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
entry = ("Told standup the test was flaky. It wasn't. I committed at 4:59pm on a Friday "
         "and let CI take the blame. It did.")
assert len(entry) <= 200
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
