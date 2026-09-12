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

::: exercise
Show that if $X$ is Hausdorff and $A\subseteq X$ is compact then $A$ is closed.
:::

::: solution
Let $x\in X\setminus A$.

<1>1. For each $a\in A$, Hausdorffness gives disjoint open sets $U_a,V_a$ with
$$
a\in U_a,\qquad x\in V_a.
$$
The sets $U_a$ cover $A$.

<1>2. Compactness gives $a_1,\dots,a_r\in A$ such that
$$
A\subseteq U_{a_1}\cup\cdots\cup U_{a_r}.
$$
Set
$$
V=V_{a_1}\cap\cdots\cap V_{a_r}.
$$
Then $V$ is an open neighborhood of $x$ and is disjoint from every $U_{a_i}$, hence from $A$.

<1>3. Thus every point of $X\setminus A$ has an open neighborhood contained in $X\setminus A$. Therefore $X\setminus A$ is open and $A$ is closed.
:::
