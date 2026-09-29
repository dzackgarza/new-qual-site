---
schema: qual/card@1
id: E-5NREC
kind: problem
title: Images of locally compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a locally compact space.
If $f: X \to Y$ is continuous, does it follow that $f(X)$ is locally compact?
What if $f$ is both continuous and open?
Justify your answer.
:::

::: {.solution}
**Goal:** Determine whether the continuous image (and continuous open image) of a locally compact space is locally compact.

::: pf

::: pf-step
Question 1: Continuous images of locally compact spaces need NOT be locally compact.

::: pf-proof

::: pf-step
Let $X = \mathbb{R}$ with the discrete topology.
:::

::: pf-step
Since every singleton in $X$ is an open and compact neighborhood of itself, $X$ is locally compact.
:::

::: pf-step
Let $Y = \mathbb{Q}$ with the standard subspace topology inherited from $\mathbb{R}$.
:::

::: pf-step
Let $f: X \to Y$ be any surjective function (for example, mapping $\mathbb{R} \setminus \mathbb{Q}$ onto $0$ and acting as the identity on $\mathbb{Q}$).
:::

::: pf-step
Since $X$ has the discrete topology, $f$ is continuous, and $f(X) = \mathbb{Q}$.
:::

::: pf-step
The rational numbers $\mathbb{Q}$ are not locally compact at any point: every compact subset of $\mathbb{Q}$ has empty interior, so no point of $\mathbb{Q}$ possesses a compact neighborhood.
:::

::: pf-step
Thus the continuous image $f(X)$ is not locally compact.
:::

:::

:::

::: pf-step
Question 2: If $f$ is continuous and open, then $f(X)$ IS locally compact.

::: pf-proof

::: pf-step
Let $y \in f(X)$. Since $f: X \to f(X)$ is surjective, choose $x \in X$ such that $f(x) = y$.
:::

::: pf-step
Because $X$ is locally compact, there exists a compact subspace $C \subseteq X$ containing an open neighborhood $U \subseteq X$ of $x$, so $x \in U \subseteq C$.
:::

::: pf-step
Since $f$ is continuous, the image $f(C)$ is a compact subset of $f(X)$.
:::

::: pf-step
Since $f: X \to f(X)$ is an open map, $f(U)$ is an open subset of $f(X)$.
:::

::: pf-step
We have $y = f(x) \in f(U) \subseteq f(C)$, which exhibits $f(C)$ as a compact neighborhood of $y$ in $f(X)$.
:::

::: pf-step
Since $y \in f(X)$ was arbitrary, $f(X)$ is locally compact. Q.E.D.
:::

:::

:::

:::

:::
