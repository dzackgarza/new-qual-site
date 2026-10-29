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

::: pf

::: pf-step
The ideal $(x)\subset k[x,y]$ is prime and not maximal, and its variety is the $y$-axis $V(x)=\{(0,b):b\in k\}$.

::: pf-proof
$k[x,y]/(x)\cong k[y]$ is an integral domain and not a field, and a point $(a,b)$ is a zero of $x$ exactly when $a=0$.
:::

:::

::: pf-step
For every $(a,b)\in k^2$, the ideal $\mathfrak m_{a,b}\coloneqq(x-a,y-b)$ is maximal, and its variety is the point $\{(a,b)\}$. If $k$ is algebraically closed, these are all the maximal ideals of $k[x,y]$.

::: pf-proof
Evaluation at $(a,b)$ induces $k[x,y]/\mathfrak m_{a,b}\cong k$, a field. The only common zero of $x-a$ and $y-b$ is $(a,b)$. The last sentence is the weak Nullstellensatz.
:::

:::

::: pf-step
(Nullstellensatz.) Let $k$ be algebraically closed. Every maximal ideal of $k[x_1,\ldots,x_n]$ has the form $(x_1-a_1,\ldots,x_n-a_n)$ (weak form), and for every ideal $I\subseteq k[x_1,\ldots,x_n]$,
$$
I(V(I))=\sqrt I
$$
(strong form): a polynomial vanishes on every common zero of $I$ exactly when some power of it lies in $I$.

::: pf-proof
This is Hilbert's Nullstellensatz.
:::

:::

:::
:::
