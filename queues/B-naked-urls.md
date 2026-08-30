# Document queue B: Wiki files with naked URLs (defect 16)

**RESOLVED** (2026-08-30). Zero bare `<https://...>` links remain in wiki source.

The original queue listed 17 files with bare URL link text.
All 161 URL conversions were committed.
Verified with fixed-string grep (`grep -rF '<https://' wiki/` returns 0 matches).
No action needed.
