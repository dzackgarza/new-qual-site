---
schema: qual/card@1
id: P-QWP3H
kind: problem
title: Prime ideals in $k[x,y]$ and the Nullstellensatz
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Geometry
relations: []
review: draft
---

::: {.problem}
Give examples of prime and maximal ideals in $k[x,y]$, describe the corresponding varieties, and state the Nullstellensatz.
:::

::: {.solution}
Let $k$ be a field.

<1>1. Prime ideal example.
::: {.proof}
The ideal
\[
(x)\subset k[x,y]
\]
is prime because
\[
k[x,y]/(x)\cong k[y]
\]
is an integral domain. Its affine variety is the $y$-axis
\[
V(x)=\{(0,b):b\in k\}.
\]
:::

<1>2. Maximal ideals over an algebraically closed field.
::: {.proof}
Assume now that $k$ is algebraically closed. For every $(a,b)\in k^2$,
\[
\mathfrak m_{a,b}=(x-a,y-b)
\]
is maximal because
\[
k[x,y]/\mathfrak m_{a,b}\cong k.
\]
The weak Nullstellensatz says that these are all maximal ideals of $k[x,y]$.
:::

<1>3. Strong Nullstellensatz.
::: {.proof}
For any ideal $I\subseteq k[x_1,\dots,x_n]$ with $k$ algebraically closed,
\[
I(V(I))=\sqrt I.
\]
Equivalently, a polynomial vanishes on every common zero of $I$ exactly when some power of it lies in $I$.
:::
:::
