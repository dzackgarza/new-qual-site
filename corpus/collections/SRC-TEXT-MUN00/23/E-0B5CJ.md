---
schema: qual/card@1
id: E-0B5CJ
kind: problem
title: Punctured products of connected spaces are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $A$ be a proper subset of $X$, and let $B$ be a proper subset of $Y$.
If $X$ and $Y$ are connected, show that

$$
(X \times Y) - (A \times B)
$$

is connected.
:::

::: {.solution}
Let $Z=(X\times Y)-(A\times B)$, and choose $x_0\in X-A$ and $y_0\in Y-B$. A union of connected subspaces with a point in common is connected.

<1>1. For $x\in X-A$ the slice $\{x\}\times Y$, and for $y\in Y-B$ the slice $X\times\{y\}$, is a connected subset of $Z$.

::: {.proof}
The slices are homeomorphic to $Y$ and $X$ by [[E-OTJ9S]], hence connected.
If $x\notin A$, no point $(x,y)$ lies in $A\times B$; similarly if $y\notin B$.
:::

<1>2. The cross $C_0=(\{x_0\}\times Y)\cup(X\times\{y_0\})$ is a connected subset of $Z$.

::: {.proof}
By step <1>1, both slices are connected subsets of $Z$, and they share $(x_0,y_0)$.
:::

<1>3. Every point $(x,y)\in Z$ lies in a connected subset of $Z$ that contains $C_0$.

::: {.proof}
Since $(x,y)\notin A\times B$, either $x\notin A$ or $y\notin B$.
If $x\notin A$, the slice $\{x\}\times Y$ meets $C_0$ at $(x,y_0)$, so $C_0\cup(\{x\}\times Y)$ is connected by step <1>1.
If $y\notin B$, the slice $X\times\{y\}$ meets $C_0$ at $(x_0,y)$, so $C_0\cup(X\times\{y\})$ is connected.
:::

<1>4. Q.E.D.

::: {.proof}
By step <1>3, $Z$ is a union of connected subsets that all contain $(x_0,y_0)$, so $Z$ is connected.
:::
:::
