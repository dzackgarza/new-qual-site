---
schema: qual/card@1
id: P-BKF84-2
kind: problem
title: Differentiate a matrix power and its trace
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the deterministic MinerU Flash extraction. Flash drops the arrow in the limit; the card restores $t\to0$.
---

::: {.problem}
Let $A,B$ be real $n\times n$ matrices and let $k$ be a positive integer. Find

1.
\[
\lim_{t\to0}\frac{(A+tB)^k-A^k}{t};
\]

2.
\[
\left.\frac d{dt}\operatorname{tr}(A+tB)^k\right|_{t=0}.
\]
:::
