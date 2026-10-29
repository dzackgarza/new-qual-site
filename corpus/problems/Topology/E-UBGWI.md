---
schema: qual/card@1
id: E-UBGWI
kind: problem
title: The closure is the smallest closed set containing $A$
classification:
  areas:
  - topology
  topics:
  - Closure
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

::: {.exercise}
Let $X$ be a topological space and $A \subseteq X$ an arbitrary subset.
Prove that the topological closure $\operatorname{cl}_X(A)$ (or $\overline{A}$) is the smallest closed subset of $X$ containing $A$:
$$\overline{A} = \bigcap \{F \subseteq X \mid F \text{ is closed and } A \subseteq F\}.$$
:::

::: {.solution}
Here $\overline A$ is the set of points $x\in X$ such that every open neighborhood of $x$ meets $A$. Let
$$K=\bigcap\{F\subseteq X:F\text{ is closed and }A\subseteq F\}.$$

::: pf

::: {.pf-step #closed}

The closure $\overline A$ is closed and contains $A$.

::: pf-proof

Every neighborhood of a point of $A$ meets $A$, so $A\subseteq\overline A$. If $x\notin\overline A$, some open neighborhood $U$ of $x$ misses $A$; $U$ is then an open neighborhood of each of its points that misses $A$, so $U\subseteq X\setminus\overline A$. Thus $X\setminus\overline A$ is open.

:::

:::

::: {.pf-step #upper}

$K\subseteq\overline A$.

::: pf-proof

By step [](#closed){.pf-ref}, $\overline A$ is one of the closed sets in the intersection defining $K$.

:::

:::

::: {.pf-step #lower}

Every closed $F\supseteq A$ contains $\overline A$, so $\overline A\subseteq K$.

::: pf-proof

If $x\notin F$, then $X\setminus F$ is an open neighborhood of $x$ that misses $A$, so $x\notin\overline A$.

:::

:::

::: pf-step

$\overline A=K$, and $\overline A$ is the smallest closed subset of $X$ containing $A$.

::: pf-proof

Steps [](#upper){.pf-ref} and [](#lower){.pf-ref} give the equality, and steps [](#closed){.pf-ref} and [](#lower){.pf-ref} give minimality.

:::

:::

:::

:::
