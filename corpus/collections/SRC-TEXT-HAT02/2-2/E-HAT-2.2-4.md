---
schema: qual/card@1
id: E-HAT-2.2-4
kind: problem
title: Surjective map $S^n \to S^n$ of degree zero
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 4; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed using degree theory and orthogonal-group homotopies.
---

Construct a surjective map $S^n \to S^n$ of degree zero, for each $n \geq 1$.

::: {.solution}
Choose an embedded equatorial $(n-1)$-sphere in $S^n$ and collapse it to a point. This gives the pinch map
\[
p:S^n\longrightarrow S^n\vee S^n.
\]
Let
\[
g:S^n\vee S^n\longrightarrow S^n
\]
be the identity on the first summand and a reflection on the second summand. Set
\[
f=g\circ p.
\]

<1>1. The map $f$ is surjective.
::: {.proof}
The first wedge summand is mapped by $g$ via the identity onto all of $S^n$. Hence the composite $f$ is onto.
:::

<1>2. The degree of $f$ is zero.
::: {.proof}
On top homology, the pinch map sends a fundamental class to the sum of the fundamental classes of the two wedge summands:
\[
p_*[S^n]=([S^n],[S^n]).
\]
The identity has degree $+1$, while a reflection has degree $-1$. Therefore
\[
f_*[S^n]=(1+(-1))[S^n]=0,
\]
so
\[
\boxed{\deg f=0.}
\]
:::

Thus for every $n\ge1$ there is a surjective degree-zero map $S^n\to S^n$.
:::
