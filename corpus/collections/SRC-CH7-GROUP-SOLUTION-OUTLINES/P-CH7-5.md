---
schema: qual/card@1
id: P-CH7-5
kind: problem
title: Equality of cosets of $3\mathbb Z$ in $\mathbb Z$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the subgroup H of Exercise 3 and moved the three coset pairs out of the solution block into the statement, per page 1 of Ch7Sltns.pdf.
---

::: {.problem}
Let $H = \{0, \pm 3, \pm 6, \pm 9, \ldots\}$ be as in Exercise 3. Decide whether or not the following cosets of $H$ are the same.

(a) $11 + H$ and $17 + H$.

(b) $-1 + H$ and $5 + H$.

(c) $7 + H$ and $23 + H$.
:::

::: {.solution}
To do this, we use that aH = bH iff $a ^ { - 1 } b \in H$ , which in additive notation is $( - a ) + b \in H$

(a) −11 + 17 = 6, and $6 \in H$ so yes, they are the same.

(b) −(−1) + 5 = 6, which is still in H so yes, they are the same.

(c) −7 + 23 = 16 but 16 is not a multiple of 3 so it is not in H. Hence these are different cosets.
:::
