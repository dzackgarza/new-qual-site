---
schema: qual/card@1
id: P-AZOFF-H08
kind: problem
title: Zeros of the exponential partial sums $P_n$ and $P_n-1$ in a disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the OCR-garbled radius to |z| < 10 and cleaned the LaTeX against Rouché’s theorem, Problem 8, of Azoff Problems by Topic.pdf (pdftotext layer reads |z| < 10).
---

::: {.problem}
For each integer $n \ge 1$, let $P_n(z) = 1 + z + \frac{1}{2!}z^2 + \frac{1}{3!}z^3 + \cdots + \frac{1}{n!}z^n$. Show that all sufficiently large $n$, the polynomial $P_n$ has no zeros in $\abs{z} < 10$, while the polynomial $P_n(z) - 1$ has exactly 3 zeros there.
:::
