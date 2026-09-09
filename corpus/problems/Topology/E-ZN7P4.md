---
schema: qual/card@1
id: E-ZN7P4
kind: problem
title: Continuous images of connected sets are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
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
Prove that if $f: X \to Y$ is a continuous map between topological spaces and $X$ is connected, then the image $f(X)$ is connected in $Y$.
:::

::: solution
Give $f(X)$ the subspace topology. Suppose $f(X)$ were disconnected. Then there would be nonempty disjoint open subsets $U,V\subseteq f(X)$ with
\[
f(X)=U\cup V.
\]

<1>1. The map
\[
f:X\longrightarrow f(X)
\]
is continuous, so $f^{-1}(U)$ and $f^{-1}(V)$ are open in $X$.

<1>2. They are disjoint and cover $X$:
\[
f^{-1}(U)\cap f^{-1}(V)=\varnothing,
\qquad
f^{-1}(U)\cup f^{-1}(V)=X.
\]

<1>3. Both are nonempty because $U$ and $V$ consist of points in the image of $f$. Thus they form a separation of $X$, contradicting connectedness.

Therefore $f(X)$ is connected.
:::
