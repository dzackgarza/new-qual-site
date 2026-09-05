---
schema: qual/card@1
id: P-KCN2B
kind: problem
title: $X$ is Hausdorff iff the diagonal is closed in $X\times X$
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
  date: 2026-09-05
  note: Checked the statement against problem 1 of the official UGA Spring 2021 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Rewrote and verified both implications directly from the Hausdorff condition and the product-topology basis.
---

:::{.problem}
Let $X$ be a topological space and let
$$
\Delta = \theset{(x, y) \in X \times X \mid x = y}
.$$

Show that $X$ is a Hausdorff space if and only if $\Delta$ is closed in $X \times X$.

:::

::: {.solution}
<1>1. If $X$ is Hausdorff, then $\Delta$ is closed in $X\times X$.
::: {.proof}
It is enough to show that
\[
(X\times X)\setminus\Delta
\]
is open.
Let
\[
(x,y)\in (X\times X)\setminus\Delta.
\]
Then $x\ne y$.
Because $X$ is Hausdorff, there are disjoint open neighborhoods $U,V\subseteq X$ with
\[
x\in U,
\qquad
y\in V.
\]
The set $U\times V$ is an open neighborhood of $(x,y)$ in the product topology.
Moreover,
\[
(U\times V)\cap\Delta=\emptyset:
\]
if $(z,z)\in U\times V$, then $z\in U\cap V$, contradicting $U\cap V=\emptyset$.
Thus every point of $(X\times X)\setminus\Delta$ has an open neighborhood contained in that complement, so the complement is open and $\Delta$ is closed.
:::

<1>2. If $\Delta$ is closed in $X\times X$, then $X$ is Hausdorff.
::: {.proof}
Let $x,y\in X$ with $x\ne y$.
Then
\[
(x,y)\in (X\times X)\setminus\Delta.
\]
Since $\Delta$ is closed, its complement is open.
By the basis defining the product topology, there are open sets $U,V\subseteq X$ such that
\[
x\in U,
\qquad
y\in V,
\qquad
U\times V\subseteq (X\times X)\setminus\Delta.
\]
We claim that $U\cap V=\emptyset$.
Indeed, if $z\in U\cap V$, then
\[
(z,z)\in U\times V,
\]
while $(z,z)\in\Delta$, contradicting the displayed containment.
Hence $U$ and $V$ are disjoint open neighborhoods of $x$ and $y$.
Therefore $X$ is Hausdorff.
:::

<1>3. Hence
\[
X\text{ is Hausdorff}
\quad\Longleftrightarrow\quad
\Delta\text{ is closed in }X\times X.
\]
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
