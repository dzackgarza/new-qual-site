---
schema: qual/card@1
id: P-BKF03-9A
kind: problem
title: Hölder continuity of the Cantor function with exponent $\log2/\log3$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in f and math delimiters against f03.pdf page 1 problem 9A.
---

::: {.problem}
Let $f : [0, 1] \to [0, 1]$ be an increasing (not strictly increasing) function such that

$$
f\left( \sum_{j=1}^{\infty} a_j 3^{-j} \right) = \sum_{j=1}^{\infty} \frac{a_j}{2} 2^{-j}
$$

whenever the $a_j$ are $0$ or $2$. Prove that there is a constant $C_0$ such that

$$
|f(x) - f(y)| \leq C_0 |x - y|^{(\log 2)/(\log 3)}
$$

for all $x, y \in [0, 1]$.
:::
