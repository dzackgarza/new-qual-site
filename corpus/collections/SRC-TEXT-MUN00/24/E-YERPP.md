---
schema: qual/card@1
id: E-YERPP
kind: problem
title: Order-preserving surjections are homeomorphisms
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Homeomorphisms
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

(a) Let $X$ and $Y$ be ordered sets in the order topology.
Show that if $f: X \to Y$ is order preserving and surjective, then $f$ is a homeomorphism.

(b) Let $X = Y = \mathbb{R}_+$.
Given a positive integer $n$, show that the function $f(x) = x^n$ is order preserving and surjective.
Conclude that its inverse, the $n$th root function, is continuous.

(c) Let $X$ be the subspace $(-\infty, -1) \cup [0, \infty)$ of $\mathbb{R}$.
Show that the function $f: X \to \mathbb{R}$ defined by setting $f(x) = x + 1$ if $x < -1$, and $f(x) = x$ if $x \geq 0$, is order preserving and surjective.
Is $f$ a homeomorphism?
Compare with (a).
:::

::: {.solution}
(a) An order-preserving map in the strict sense satisfies
\[
x<x'\implies f(x)<f(x'),
\]
so it is injective. Together with surjectivity, $f$ is bijective and its inverse is also order preserving. Order isomorphisms carry open intervals and open rays to open intervals and open rays. Hence both $f$ and $f^{-1}$ are continuous in the order topologies, so $f$ is a homeomorphism.

(b) On $\mathbb R_+=(0,\infty)$, the map
\[
f(x)=x^n
\]
is strictly increasing and maps onto $(0,\infty)$. By part (a) it is a homeomorphism. Therefore its inverse
\[
x\mapsto x^{1/n}
\]
is continuous.

(c) The displayed map
\[
f(x)=\begin{cases}x+1,&x<-1,\\x,&x\ge0\end{cases}
\]
is strictly order preserving and maps $(-\infty,-1)$ onto $(-\infty,0)$ and $[0,\infty)$ onto $[0,\infty)$, so it is surjective. But it is not a homeomorphism for the given subspace topology on $X$. Indeed $[0,\varepsilon)$ is open in $X$ for every $\varepsilon>0$, while its image $[0,\varepsilon)$ is not open in $\mathbb R$. Thus $f^{-1}$ is not continuous.

There is no contradiction with (a): the topology on $X$ in part (c) is the subspace topology inherited from $\mathbb R$, not the order topology of the ordered set $X$.
:::
