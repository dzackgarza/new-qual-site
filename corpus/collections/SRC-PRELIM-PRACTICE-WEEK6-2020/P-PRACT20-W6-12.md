---
schema: qual/card@1
id: P-PRACT20-W6-12
kind: problem
title: The discrete metric on $\mathbb R$
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
  note: Restored the arrow lost from choice (D) and separated the choices, checked against Week6_solns.pdf (Problem 12).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow lost from the identity map in the solution, checked against Week6_solns.pdf (Problem 12).
---

::: {.problem}
Let $d(x, y) = \begin{cases} 0, & x = y, \\ 1, & x \neq y. \end{cases}$ Which of the following hold in the metric space $(\RR, d)$?

(A) $\{x\}$ is open for each $x \in \RR$.

(B) Every subset of $\RR$ is closed.

(C) If $d'$ is the ordinary metric on $\RR$, then the identity map $(\RR, d) \to (\RR, d')$ is continuous.

(D) If $d'$ is the ordinary metric on $\RR$, then the identity map $(\RR, d') \to (\RR, d)$ is continuous.
:::

::: {.solution}
This is the discrete metric which generates the discrete topology on R; thus every set is open.
If every set is open, then every set is closed as well.
Thus (A) and (B) are true.

For (C) and (D), consider any space X with two topologies $\tau _ { 1 } , \tau _ { 2 }$ Recall the identity $\iota :$ $( X , \tau _ { 1 } ) \to ( X , \tau _ { 2 } )$ is continuous iff $\iota ^ { - 1 } ( V ) \in \tau _ { 1 }$ whenever $V \in \tau _ { 2 }$ But $\iota ^ { - 1 } ( V ) = V$ Thus the identity is continuous iff $V \in \tau _ { 1 }$ whenever $V \in \tau _ { 2 }$ . rephrasing yet again, the identity is continuous iff $\tau _ { 2 } \subset \tau _ { 1 }$ which is true iff $\tau _ { 1 }$ is finer than $\tau _ { 2 }$ . The discrete topology is finer than any other topology on R so (D) is false while (C) is true.
:::
