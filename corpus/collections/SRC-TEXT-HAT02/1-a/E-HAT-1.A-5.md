---
schema: qual/card@1
id: E-HAT-1.A-5
kind: problem
title: Maps $fg = \mathrm{id}$ without inducing isomorphisms on $\pi_1$
classification:
  areas:
  - topology
  topics:
  - Graphs
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the countable rose with right-shift and left-shift maps, giving a literal split epimorphism on the space and nonisomorphic induced free-group endomorphisms.
---

Construct a connected graph $X$ and maps $f, g: X \to X$ such that $fg = \mathbb{1}$ but $f$ and $g$ do not induce isomorphisms on $\pi_1$.
[Note that $f_*g_* = \mathbb{1}$ implies that $f_*$ is surjective and $g_*$ is injective.]


::: {.solution}
Let
\[
X=\bigvee_{n=0}^{\infty} C_n
\]
be the CW wedge of countably many circles at a common basepoint $x_0$.
Choose orientation-preserving homeomorphisms
\[
h_n:C_n\to C_{n+1}
\]
fixing $x_0$.

<1>1. Define
\[
g:X\to X
\]
by
\[
g|_{C_n}=h_n
\]
for every $n\ge0$.
Define
\[
f:X\to X
\]
by collapsing $C_0$ to $x_0$ and, for $n\ge0$, setting
\[
f|_{C_{n+1}}=h_n^{-1}.
\]
::: {.proof}
Each map is continuous on every closed cell and fixes the common $0$-cell.
By the weak topology of the CW wedge, the resulting maps are continuous on $X$.
:::

<1>2. One has
\[
f\circ g=\operatorname{id}_X.
\]
::: {.proof}
For every $n\ge0$,
\[
(f\circ g)|_{C_n}=h_n^{-1}\circ h_n=\operatorname{id}_{C_n}.
\]
The wedgepoint is fixed as well.
:::

<1>3. The fundamental group is
\[
\pi_1(X,x_0)\cong F(a_0,a_1,a_2,\dots),
\]
where $a_n$ is represented by $C_n$.
The induced maps satisfy
\[
g_*(a_n)=a_{n+1},
\]
and
\[
f_*(a_0)=1,
\qquad
f_*(a_{n+1})=a_n.
\]
::: {.proof}
The fundamental group of a graph is free on the edges outside a maximal tree; here the $0$-skeleton itself is a maximal tree, so the circles give the stated free basis.
The formulas follow directly from the definitions of $f$ and $g$ on each circle.
:::

<1>4. Neither $f_*$ nor $g_*$ is an isomorphism.
::: {.proof}
The map $g_*$ is injective but not surjective, since no reduced word in its image contains the generator $a_0$.
The map $f_*$ is surjective but not injective, since
\[
a_0\ne1
\]
while
\[
f_*(a_0)=1.
\]
Nevertheless
\[
f_*g_*=(fg)_*=\operatorname{id}.
\]
Thus $f,g$ have the required properties.
:::
:::
