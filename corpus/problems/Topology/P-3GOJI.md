---
schema: qual/card@1
id: P-3GOJI
kind: problem
title: One-point compactification is compact; path-connected implies connected
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
(1) Show that for $X$ an arbitrary topological space, the one-point (Alexandroff) compactification $X^* = X \cup \{\infty\}$ is compact.

(2) Prove that every path-connected topological space is connected.
:::

::: solution
<1>1. Let $X^*=X\cup\{\infty\}$ carry the Alexandroff topology: the open sets not containing $\infty$ are the open subsets of $X$, while a neighborhood of $\infty$ has the form
$$
\{\infty\}\cup(X\setminus K)
$$
with $K\subseteq X$ compact and closed.

<1>2. The space $X^*$ is compact.
::: proof
Let $\mathcal U$ be an open cover of $X^*$. Choose $U_\infty\in\mathcal U$ containing $\infty$. Then for some compact closed $K\subseteq X$,
$$
\{\infty\}\cup(X\setminus K)\subseteq U_\infty.
$$
The remaining points lie in $K$. The sets $U\cap X$, for $U\in\mathcal U$, cover $K$, so compactness of $K$ gives finitely many of them covering $K$. Together with $U_\infty$ they form a finite subcover of $X^*$.
:::

<1>3. Every path-connected space is connected.
::: proof
Fix $x_0\in X$. For each $x\in X$, choose a path from $x_0$ to $x$. Each path image is connected, all such images contain $x_0$, and their union is $X$. A union of connected subsets with a common point is connected.
:::
:::
