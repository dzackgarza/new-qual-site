---
schema: qual/card@1
id: E-6A0RO
kind: problem
title: Hausdorff spaces and the closed diagonal
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that $X$ is Hausdorff if and only if the diagonal $\Delta = \theset{x \times x \mid x \in X}$ is closed in $X \times X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $X$ is Hausdorff, then $\Delta$ is closed in $X\times X$.

::: pf-proof

Let $(x,y)\in(X\times X)-\Delta$, so $x\ne y$.
Choose disjoint open sets $U\ni x$ and $V\ni y$.
Then $U\times V$ is an open neighborhood of $(x,y)$, and a point $(z,z)\in U\times V$ would give $z\in U\cap V=\varnothing$.
So $U\times V\subseteq(X\times X)-\Delta$, and the complement of $\Delta$ is open.

:::

:::

::: {.pf-step #s2}

If $\Delta$ is closed in $X\times X$, then $X$ is Hausdorff.

::: pf-proof

Let $x\ne y$ in $X$.
Then $(x,y)$ lies in the open set $(X\times X)-\Delta$, so by the definition of the product topology there are open $U,V\subseteq X$ with $(x,y)\in U\times V\subseteq(X\times X)-\Delta$.
If $z\in U\cap V$, then $(z,z)\in(U\times V)\cap\Delta=\varnothing$; hence $U$ and $V$ are disjoint open neighborhoods of $x$ and $y$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the two implications.

:::

:::

:::
