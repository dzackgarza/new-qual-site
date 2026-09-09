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

::: problem
Let $X$ be a topological space.
Prove that $X$ is **connected** if and only if the only subsets of $X$ that are both open and closed (clopen) are $\varnothing$ and $X$.
:::

::: solution
<1>1. Suppose $X$ is connected and $A\subseteq X$ is clopen. If $A$ were neither $\varnothing$ nor $X$, then
$$
X=A\sqcup(X\setminus A)
$$
would be a union of two disjoint nonempty open sets, contradicting connectedness. Hence the only clopen subsets are $\varnothing$ and $X$.

<1>2. Conversely, suppose the only clopen subsets are $\varnothing$ and $X$. If $X$ were disconnected, there would be disjoint nonempty open sets $U,V$ with $X=U\cup V$. Then
$$
X\setminus U=V
$$
is open, so $U$ is also closed. Thus $U$ is a nontrivial clopen subset, a contradiction.

<1>3. Therefore $X$ is connected if and only if its only clopen subsets are $\varnothing$ and $X$.
:::
