---
schema: qual/card@1
id: E-7GKPR
kind: problem
title: Compact subsets of metric spaces are bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
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
Show that if $X$ is a metric space and $A\subseteq X$ is compact then $A$ is bounded.
:::

::: solution
If $A=\varnothing$, it is bounded. Assume $A\ne\varnothing$ and fix $x_0\in A$.

<1>1. The nested balls
$$
B(x_0,1),B(x_0,2),\dots
$$
form an open cover of $A$.

<1>2. Compactness gives a finite subcover. If $N$ is the largest radius occurring, then
$$
A\subseteq B(x_0,N).
$$

<1>3. Therefore for all $x,y\in A$,
$$
d(x,y)\le d(x,x_0)+d(x_0,y)<2N.
$$
Thus $A$ is bounded.
:::
