---
schema: qual/card@1
id: P-TRIV-CA22
kind: problem
title: $\int_0^1 (x^2-x^3)^{-1/3}\,dx$ by a dogbone contour
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 22, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source hint refers to Figure 4, whose graphical content is absent from Flash. The integral itself is fully extracted; only the hinted contour is unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the missing-figure note with a description of Figure 4, against Complex Analysis Problem 22 on pages 15-16 of the source PDF.
---

::: {.problem}
Compute $\displaystyle\int_0^1 \frac{1}{\left(x^2 - x^3\right)^{1/3}}$ (**hint:** use the contour in figure 4);

Figure 4 of the source (integration contour for exercise 22) shows a dogbone contour around the segment $[0, 1]$: a segment just above $[0, 1]$ traversed from $0$ to $1$, a small circle around $1$, a segment just below $[0, 1]$ traversed from $1$ to $0$, and a small circle around $0$; this dogbone is enclosed by a large circle traversed counterclockwise.
:::
