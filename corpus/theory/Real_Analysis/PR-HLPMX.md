---
schema: qual/card@1
id: PR-HLPMX
kind: proposition
title: Integrals of nonnegative functions are subadditive over covers and additive over disjoint unions
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(Y,\mcm,\mu)$ be a [[D-QYLPH|measure space]], $f\in$ [[D-BF5L2|$L^+$]], and $X,A,B\in\mcm$.
If $X\subseteq A\cup B$, then
$$
\int_X f\dmu \leq \int_A f\dmu + \int_B f\dmu,
$$
with equality when $X=A\cup B$ and $A\cap B=\emptyset$.
:::

::: {.proof}
If $A\cap B=\emptyset$, then $\chi_{A\cup B}=\chi_A+\chi_B$, and additivity of the integral on $L^+$ gives $\int_{A\cup B}f\dmu=\int_A f\dmu+\int_B f\dmu$.
In general $X\subseteq A\cup(B\setminus A)$ with $A\cap(B\setminus A)=\emptyset$, so, since $f\geq0$,
$$
\int_X f\dmu\leq\int_{A\cup(B\setminus A)}f\dmu=\int_A f\dmu+\int_{B\setminus A}f\dmu\leq\int_A f\dmu+\int_B f\dmu .
$$
:::
