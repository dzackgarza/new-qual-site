---
schema: qual/card@1
id: P-WXTVX
kind: problem
title: A space is connected iff its only clopen subsets are $\emptyset$ and $X$
classification:
  areas:
  - topology
  topics:
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
Let $X$ be a topological space.
Prove that $X$ is **connected** if and only if the only subsets of $X$ that are both open and closed (clopen) are $\varnothing$ and $X$.
:::

::: {.solution}

::: pf

::: pf-step
If $X$ is connected, then its only clopen subsets are $\varnothing$ and $X$.

::: pf-proof
Let $A\subseteq X$ be clopen.
Then $A$ and $X\setminus A$ are disjoint open sets with union $X$, so connectedness forces one of them to be empty, that is, $A=\varnothing$ or $A=X$.
:::

:::

::: pf-step
If the only clopen subsets of $X$ are $\varnothing$ and $X$, then $X$ is connected.

::: pf-proof
Suppose $X=U\cup V$ with $U,V$ disjoint open sets.
Then $X\setminus U=V$ is open, so $U$ is clopen, and hence $U=\varnothing$ or $V = X \setminus U=\varnothing$.
So $X$ admits no separation.
:::

:::

:::

:::
