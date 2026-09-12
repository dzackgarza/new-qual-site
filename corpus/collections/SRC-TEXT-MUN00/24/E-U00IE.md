---
schema: qual/card@1
id: E-U00IE
kind: problem
title: Well-ordered sets times the half-open interval are linear continua
classification:
  areas:
  - topology
  topics:
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that if $X$ is a well-ordered set, then $X \times [0, 1)$ in the dictionary order is a linear continuum.
:::

::: {.solution}
Let
\[
L=X\times[0,1)
\]
with dictionary order, where $X$ is well ordered.

First we prove the least-upper-bound property. Let $A\subseteq L$ be nonempty and bounded above. Let
\[
C=\{x\in X:\text{some }(x,t)\text{ is an upper bound of }A\}.
\]
The set $C$ is nonempty, so it has a least element $x_0$.

If $A$ contains points with first coordinate $x_0$, let
\[
T=\{t:(x_0,t)\in A\}.
\]
Because some $(x_0,s)$ is an upper bound, $T$ is bounded above by $s<1$. Let $t_0=\sup T$. Then $(x_0,t_0)$ is the least upper bound of $A$.

If $A$ contains no point with first coordinate $x_0$, then every point of $A$ has first coordinate $<x_0$, and $(x_0,0)$ is the least upper bound. Thus $L$ has the least-upper-bound property.

Now let $(x,s)<(y,t)$. If $x=y$, choose $u$ with $s<u<t$. If $x<y$, choose $u$ with $s<u<1$; then
\[
(x,s)<(x,u)<(y,t).
\]
Hence the order is dense. Therefore $X\times[0,1)$ is a linear continuum.
:::
