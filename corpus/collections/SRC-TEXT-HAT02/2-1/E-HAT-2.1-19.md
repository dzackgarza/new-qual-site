---
schema: qual/card@1
id: E-HAT-2.1-19
kind: problem
title: Homology of subspace of $I \times I$ with rational first coordinate
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 19; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used a two-set Mayer--Vietoris cover whose intersection deformation retracts to Q intersect I; this gives countably generated free H_1 and no higher homology.
---

Compute the homology groups of the subspace of $I \times I$ consisting of the four boundary edges plus all points in the interior whose first coordinate is rational.

::: {.solution}
Let $X$ be the specified subspace of $I\times I$. Thus $X$ contains the whole boundary square and, for each rational $q\in(0,1)$, the vertical segment $\{q\}\times I$.

Define open subsets of $X$
\[
U=X\cap\{y<3/4\},
\qquad
V=X\cap\{y>1/4\}.
\]

<1>1. Both $U$ and $V$ are contractible.
::: {.proof}
The vertical homotopy
\[
(x,y)\longmapsto(x,(1-t)y)
\]
deformation retracts $U$ onto the bottom edge. It stays in $X$ because an interior point of $X$ either has rational first coordinate or lies on a vertical boundary edge, and the homotopy preserves the first coordinate. Similarly $V$ deformation retracts onto the top edge.
:::

<1>2. The intersection $U\cap V$ deformation retracts onto
\[
Q=(\mathbb Q\cap I)\times\{1/2\},
\]
so
\[
\widetilde H_0(U\cap V)
\cong
\bigoplus_{q\in(\mathbb Q\cap I)\setminus\{0\}}\mathbb Z
\]
and
\[
H_k(U\cap V)=0\quad(k>0).
\]
::: {.proof}
On $U\cap V$ the vertical contraction to height $1/2$ is well-defined and stays in $X$. At heights strictly between $1/4$ and $3/4$, points of $X$ have rational first coordinate, except that the side edges have first coordinates $0,1$, which are rational anyway. Hence the retract is precisely the copy of $\mathbb Q\cap I$ displayed above.

Every path-component of $\mathbb Q\cap I$ is a single point, so its $H_0$ is free on the rational points and the reduced group is the augmentation kernel, with basis $[q]-[0]$ for $q\ne0$. Any singular simplex of positive dimension in $\mathbb Q\cap I$ has connected image and is therefore constant, so the positive-dimensional homology vanishes.
:::

<1>3. The space $X$ is path connected, and
\[
H_1(X)\cong\widetilde H_0(U\cap V).
\]
::: {.proof}
Every point can be joined vertically to the top or bottom boundary and then along the boundary to any other point, so $X$ is path connected.

The reduced Mayer--Vietoris sequence for $X=U\cup V$ contains
\[
0=\widetilde H_1(U)\oplus\widetilde H_1(V)
\to\widetilde H_1(X)
\to\widetilde H_0(U\cap V)
\to\widetilde H_0(U)\oplus\widetilde H_0(V)=0.
\]
Thus the middle arrow is an isomorphism.
:::

<1>4. All homology in dimensions at least two vanishes.
::: {.proof}
For $k\ge2$, Mayer--Vietoris gives
\[
\widetilde H_k(X)\cong\widetilde H_{k-1}(U\cap V)=0
\]
by <1>2.
:::

<1>5. Therefore
\[
\boxed{
H_0(X)\cong\mathbb Z,
\qquad
H_1(X)\cong
\bigoplus_{q\in(\mathbb Q\cap I)\setminus\{0\}}\mathbb Z,
\qquad
H_k(X)=0\ (k\ge2).
}
\]
::: {.proof}
Combine <1>2--<1>4.
:::
:::
