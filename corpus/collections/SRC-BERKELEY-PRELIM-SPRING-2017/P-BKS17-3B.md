---
schema: qual/card@1
id: P-BKS17-3B
kind: problem
title: Maximal degree of exactness and positive weights of quadrature rules
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
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 14 problem 3B.
---

::: {.problem}
The error of a quadrature rule with $p + 1$ distinct points $x_j$, weights $w_j$ is

$$
E_p(f) = \int_a^b f(x) \, dx - \sum_{j=0}^{p} w_j f(x_j).
$$

Suppose that $E_p(f) = 0$ whenever $f$ is a polynomial of degree $\leq q$. Show that $q \leq 2p + 1$ and if $q \geq 2p$ then $w_j > 0$ for all $j$.
:::
