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

::: {.problem}
(a) Show that for $X$ an arbitrary topological space, the one-point (Alexandroff) compactification $X^* = X \cup \{\infty\}$ is compact.

(b) Prove that every path-connected topological space is connected.
:::

::: {.solution}

In the Alexandroff topology on $X^*$, the open sets not containing $\infty$ are the open subsets of $X$, and the open sets containing $\infty$ are the sets $\{\infty\}\cup(X\setminus K)$ with $K\subseteq X$ compact and closed.

::: pf

::: pf-step

(a) $X^*$ is compact.

::: pf-proof

Let $\mathcal U$ be an open cover of $X^*$ and choose $U_\infty\in\mathcal U$ containing $\infty$. Then $U_\infty=\{\infty\}\cup(X\setminus K)$ for some compact closed $K\subseteq X$. The sets $U\cap X$, for $U\in\mathcal U$, are open in $X$ and cover $K$, so finitely many of them cover $K$. Together with $U_\infty$ the corresponding members of $\mathcal U$ form a finite subcover of $X^*$.

:::

:::

::: pf-step

(b) Every path-connected space $X$ is connected.

::: pf-proof

The empty space is connected. Otherwise fix $x_0\in X$ and, for each $x\in X$, a path $\gamma_x$ from $x_0$ to $x$. Each image $\gamma_x([0,1])$ is connected as a continuous image of $[0,1]$, all of them contain $x_0$, and their union is $X$. A union of connected subsets with a common point is connected.

:::

:::

:::

:::
