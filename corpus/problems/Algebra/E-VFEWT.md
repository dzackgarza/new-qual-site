---
schema: qual/card@1
id: E-VFEWT
kind: problem
title: Radical, prime, and maximal ideals correspond under $R\to R/I$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that if $J\in \Id(R)$ (with $J\containing I$) is radical/prime/maximal iff $\bar J \in \Id(R/I)$ is radical/prime/maximal.
:::

::: {.solution}
Let $I\subseteq J$ be ideals of the commutative ring $R$, and write
\[
\overline J=J/I\subseteq R/I.
\]

::: pf

::: {.pf-step #quotient-iso}
The quotient correspondence gives
\[
(R/I)/(J/I)\cong R/J.
\]

::: pf-proof
Define
\[
\phi:R/I\longrightarrow R/J,
\qquad
r+I\longmapsto r+J.
\]
Because $I\subseteq J$, this map is well-defined and surjective. Its kernel is exactly $J/I$. The first isomorphism theorem therefore gives the displayed isomorphism.
:::

:::

::: {.pf-step #prime-correspondence}
The ideal $J$ is prime in $R$ if and only if $J/I$ is prime in $R/I$.

::: pf-proof
An ideal is prime exactly when its quotient ring is an integral domain. By step [](#quotient-iso){.pf-ref},
\[
R/J\cong (R/I)/(J/I).
\]
Hence one quotient is a domain exactly when the other is.
:::

:::

::: {.pf-step #maximal-correspondence}
The ideal $J$ is maximal in $R$ if and only if $J/I$ is maximal in $R/I$.

::: pf-proof
An ideal is maximal exactly when its quotient ring is a field. Again step [](#quotient-iso){.pf-ref} identifies the two quotient rings, so the two maximality conditions are equivalent.
:::

:::

::: {.pf-step #radical-correspondence}
The ideal $J$ is radical in $R$ if and only if $J/I$ is radical in $R/I$.

::: pf-proof
Suppose first that $J$ is radical. If
\[
(r+I)^n\in J/I,
\]
then $r^n+I\in J/I$, which means $r^n\in J$. Radicality of $J$ gives $r\in J$, hence $r+I\in J/I$. Thus $J/I$ is radical.

Conversely, suppose $J/I$ is radical and $r^n\in J$. Then
\[
(r+I)^n=r^n+I\in J/I.
\]
Hence $r+I\in J/I$, so $r\in J$. Therefore $J$ is radical.
:::

:::

::: pf-step
Thus radical, prime, and maximal ideals containing $I$ correspond to radical, prime, and maximal ideals of $R/I$ under $J\mapsto J/I$.

::: pf-proof
Combine steps [](#prime-correspondence){.pf-ref}, [](#maximal-correspondence){.pf-ref} and [](#radical-correspondence){.pf-ref} with the ordinary ideal correspondence for the quotient map $R\to R/I$.
:::

:::

:::

:::
