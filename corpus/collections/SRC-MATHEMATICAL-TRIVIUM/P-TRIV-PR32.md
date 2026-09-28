---
schema: qual/card@1
id: P-TRIV-PR32
kind: problem
title: Almost sure convergence of the random harmonic series $\sum \xi_n/n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 32, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the values +1 or -1 and removed stray residue against Probability Problem 32 on page 32 of the source PDF.
---

::: {.problem}
It is known that the series $\sum_{n=1}^\infty \frac{1}{n}$ diverges while the series $\sum_{n=1}^\infty \frac{(-1)^n}{n}$ converges.
One may ask about the convergence or divergence of the series $\sum_{n=1}^\infty \frac{\xi_n}{n}$, where $\xi_n$ are independent random variables taking the values $+1$ or $-1$ with the probabilities $p$ and $q = 1 - p$ correspondingly.

(a) Show that if $p = q = \frac{1}{2}$, the series converges with the unit probability.

(b) Show that otherwise the series diverges with the unit probability.
:::
