# Document queue A: Wiki files with `title="?"` (defect 3)

**RESOLVED** (2026-08-30). Zero `title="?"` instances remain in wiki source.

The original queue listed 95 files with `:::{.proof title="?"}` (or `.example title="?"`). All instances were resolved — verified with fixed-string grep (`grep -rF 'title="?"' wiki/` returns 0 matches).
The earlier count of 102 was a regex escaping artifact.

All `:::{.proof title=...}` blocks now carry real titles.
No action needed.
