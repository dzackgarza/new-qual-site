---
schema: qual/card@1
id: E-WADQN
kind: problem
title: Extreme value theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
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

::: exercise
Show that if $f: X \to \mathbb{R}$ is continuous and $X$ is a nonempty compact topological space, then $f(X)$ is bounded and $f$ attains its minimum and maximum on $X$.
:::

::: solution
<1>1. Since $f$ is continuous and $X$ is compact, $f(X)$ is compact.
::: proof
If $\{V_\alpha\}$ is an open cover of $f(X)$, then $\{f^{-1}(V_\alpha)\}$ is an open cover of $X$. A finite subcover of $X$ pushes forward to a finite subcover of $f(X)$.
:::

<1>2. By Heine--Borel, the compact subset $f(X)\subset\mathbb R$ is bounded and closed.

<1>3. Because $X$ is nonempty, $f(X)$ is nonempty. Since it is bounded, let
$$
m=\inf f(X),\qquad M=\sup f(X).
$$
Both $m$ and $M$ lie in the closure of $f(X)$; since $f(X)$ is closed, they lie in $f(X)$ itself.

<1>4. Hence there are $x_{\min},x_{\max}\in X$ such that
$$
f(x_{\min})=m,\qquad f(x_{\max})=M.
$$
Thus $f$ is bounded and attains both extrema.
:::
