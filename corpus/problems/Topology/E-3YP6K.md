---
schema: qual/card@1
id: E-3YP6K
kind: problem
title: Compact subsets of Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $X$ is Hausdorff and $A\subseteq X$ is compact then $A$ is closed.
:::

::: {.solution}

Let $x\in X\setminus A$.

::: pf

::: {.pf-step #cover}

There are $a_1,\dots,a_r\in A$ and disjoint pairs of open sets $U_{a_i} \ni a_i$, $V_{a_i} \ni x$ with $A\subseteq U_{a_1}\cup\cdots\cup U_{a_r}$.

::: pf-proof

For each $a\in A$, since $a \ne x$ and $X$ is Hausdorff, there are disjoint open sets $U_a \ni a$ and $V_a \ni x$. The sets $U_a$ cover $A$, and compactness of $A$ gives a finite subcover.

:::

:::

::: pf-step

$V=V_{a_1}\cap\cdots\cap V_{a_r}$ is an open neighborhood of $x$ disjoint from $A$, so $X \setminus A$ is open and $A$ is closed.

::: pf-proof

$V$ is a finite intersection of open neighborhoods of $x$. Each $V_{a_i}$ is disjoint from $U_{a_i}$, so $V$ is disjoint from $U_{a_1}\cup\cdots\cup U_{a_r} \supseteq A$ by step [](#cover){.pf-ref}. As $x$ was arbitrary, every point of $X\setminus A$ has an open neighborhood inside $X\setminus A$.

:::

:::

:::

:::
