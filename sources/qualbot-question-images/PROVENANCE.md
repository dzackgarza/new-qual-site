# MathQualBot

The 51 question images from `zack@droplet:~/MathQualBot`, vendored 2026-07-23. The bot itself is not vendored — only its question images, which are source material.

**This was the only copy.** The repository's configured remote, `git@github.com:dzackgarza/MathQualBot.git`, no longer resolves — the GitHub repository is gone.
Six commits existed on the droplet and nowhere else.

## Why it matters to the migration

`QualbotQuestions/` holds 51 question images whose filenames encode institution, year, month and problem number: `2012-01 8.png`, `2020-09 3.png`. The month distinguishes Spring (`-01`) from Fall (`-09`).

That is the only season data anywhere in this migration.
`make-me-a-qual` has no `season` field for any of its 508 records, and the prose repos carry no institution or year metadata at all.
Without these filenames every occurrence imported from `make-me-a-qual` has to record its term as `unknown`.

20 distinct sittings, 2004–2021:

|  |  |
| --- | --- |
| Algebra/UGA | 13 |
| Complex Analysis | 14 |
| Real Analysis | 14 |
| Topology/UGA | 10 |

One anomaly: 13 images are tagged `2021-05`, which is neither `-01` nor `-09`. May is presumably a summer sitting, and the two-season mapping does not cover it.
Resolve that before hard-coding Spring/Fall.

The images are **not yet transcribed** — they are PNGs of exam questions, and turning them into occurrence records is WS6's extraction work.

## Not vendored

`~/tweepy_credentials` on the droplet holds live Twitter API keys.
It was not copied, quoted, or read.
`QualBot.py` is included because it documents the image-naming scheme; its credential variables are empty strings populated at runtime from that external file.
