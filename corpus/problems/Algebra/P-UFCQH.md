---
schema: qual/card@1
id: P-UFCQH
kind: problem
title: Whether real matrices conjugate over $\CC$ are conjugate over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Canonical Forms
  - Matrices
relations: []
review: draft
---

::: {.problem}
Let $A,B\in M_n(\RR)$. If $A$ and $B$ are similar in $M_n(\CC)$, must they already be similar in $M_n(\RR)$?
:::

::: {.solution}
Suppose $AX=XB$ with $X\in\GL_n(\CC)$, and write $X=P+iQ$ with $P,Q\in M_n(\RR)$.

::: pf

::: {.pf-step #real-parts}
$A(P+tQ)=(P+tQ)B$ for every $t\in\RR$.

::: pf-proof
Since $A$ and $B$ are real, comparing real and imaginary parts of $AX=XB$ gives $AP=PB$ and $AQ=QB$.
:::

:::

::: {.pf-step #invertible}
$P+tQ$ is invertible for some $t\in\RR$.

::: pf-proof
$f(t)=\det(P+tQ)$ is a polynomial in $t$ with real coefficients, and $f(i)=\det X\ne0$, so $f$ is not identically zero and has finitely many roots.
:::

:::

::: pf-step
$\boxed{\text{Yes}}$: $A$ and $B$ are similar in $M_n(\RR)$.

::: pf-proof
With $t$ as in step [](#invertible){.pf-ref}, $Y=P+tQ\in\GL_n(\RR)$, and step [](#real-parts){.pf-ref} gives $A=YBY^{-1}$.
:::

:::

:::

:::
