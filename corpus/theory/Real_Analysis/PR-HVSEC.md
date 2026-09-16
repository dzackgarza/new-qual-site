---
schema: qual/card@1
id: PR-HVSEC
kind: proposition
title: Integrals of nonnegative functions are subadditive over covers and additive over disjoint unions
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations:
- kind: variant-of
  target: PR-HLPMX
review: draft
---

::: {.proposition}
Let $(Y,\mcm,\mu)$ be a [[D-QYLPH|measure space]], $f\in$ [[D-BF5L2|$L^+$]], and $X,A,B\in\mcm$ with $A\cap B=\emptyset$.
Then
$$
\begin{aligned}
X \subseteq A \cup B &\implies \int_X f\dmu \leq \int_A f\dmu + \int_B f\dmu, \\
X = A \cup B &\implies \int_X f\dmu = \int_A f\dmu + \int_B f\dmu .
\end{aligned}
$$
:::
