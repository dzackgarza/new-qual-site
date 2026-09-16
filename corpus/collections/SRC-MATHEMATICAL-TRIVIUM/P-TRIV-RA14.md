---
schema: qual/card@1
id: P-TRIV-RA14
kind: problem
title: Double and iterated limits of $x+y\sin\frac1x$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the garbled iterated-limit notation against Real Analysis Problem 14 on page 9 of the source PDF.
---

::: problem
Find $\lim_{(x,y) \to (0,0)} f(x,y)$, where
$$
f(x,y) = \begin{cases} x + y \sin\frac{1}{x}, & x \neq 0, \\ 0, & x = 0. \end{cases}
$$
Do the limits $\lim_{x \to 0}\left(\lim_{y \to 0} f(x,y)\right)$ and $\lim_{y \to 0}\left(\lim_{x \to 0} f(x,y)\right)$ exist?
:::
