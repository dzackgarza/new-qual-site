---
schema: qual/card@1
id: P-HFD24
kind: problem
title: $X$ is Hausdorff if and only if the diagonal is closed in $X\times X$
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 2 of the official UGA Spring 2014 topology exam and restored this source problem to the collection after it had been removed as a cross-collection phantom.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified both implications directly from the Hausdorff definition and the product-topology basis.
---

::: problem
Let $X$ be a topological space, and let
\[
\Delta=\{(x,y)\in X\times X\mid x=y\}.
\]
Show that $X$ is Hausdorff if and only if $\Delta$ is closed in $X\times X$.
:::

::: {.solution}
<1>1. If $X$ is Hausdorff, then $\Delta$ is closed in $X\times X$.
::: {.proof}
It is enough to prove that
\[
(X\times X)\setminus\Delta
\]
is open.
Let
\[
(x,y)\in(X\times X)\setminus\Delta.
\]
Then $x\ne y$.
Since $X$ is Hausdorff, there are disjoint open sets $U,V\subseteq X$ such that
\[
x\in U,
\qquad
y\in V.
\]
The set $U\times V$ is an open neighborhood of $(x,y)$ in $X\times X$.
Moreover,
\[
(U\times V)\cap\Delta=\varnothing,
\]
because if $(z,z)\in U\times V$, then $z\in U\cap V$, contradicting $U\cap V=\varnothing$.
Hence
\[
(x,y)\in U\times V\subseteq(X\times X)\setminus\Delta.
\]
Every point of the complement therefore has an open neighborhood contained in the complement, so the complement is open and $\Delta$ is closed.
:::

<1>2. If $\Delta$ is closed in $X\times X$, then $X$ is Hausdorff.
::: {.proof}
Let $x,y\in X$ with $x\ne y$.
Then
\[
(x,y)\in(X\times X)\setminus\Delta.
\]
Since $\Delta$ is closed, its complement is open.
By the definition of the product topology, there are open sets $U,V\subseteq X$ such that
\[
x\in U,
\qquad
y\in V,
\qquad
U\times V\subseteq(X\times X)\setminus\Delta.
\]
We claim that $U\cap V=\varnothing$.
Indeed, if $z\in U\cap V$, then
\[
(z,z)\in U\times V.
\]
But $(z,z)\in\Delta$, contradicting
\[
U\times V\subseteq(X\times X)\setminus\Delta.
\]
Thus $U$ and $V$ are disjoint open neighborhoods of $x$ and $y$.
Since every pair of distinct points admits such neighborhoods, $X$ is Hausdorff.
:::

<1>3. Therefore
\[
\boxed{X\text{ is Hausdorff}\iff\Delta\text{ is closed in }X\times X}.
\]
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
