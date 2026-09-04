---
schema: qual/card@1
id: P-6PQRO
kind: problem
title: A suspension is a union of two contractible subspaces, with $\pi_1(SX)=0$ and
  $H_n(X)\cong H_{n+1}(SX)$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Homology
  - Fundamental Group
  - Quotient Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked all three parts against problem 3 of the official UGA Spring 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the two-pole open cover, the explicit contractions, the van Kampen argument, and the exact Mayer–Vietoris segment giving the degree shift for every n>=1.
---

::: problem
Recall that the **suspension** of a topological space, denoted $SX$, is the quotient space formed from $X \times [-1, 1]$ by identifying $(x, 1)$ with $(y, 1)$ for all $x, y \in X$, and also identifying $(x, -1)$ with $(y, -1)$ for all $x, y \in X$.

a. Show that $SX$ is the union of two contractible subspaces.

b. Prove that if $X$ is path-connected then $\pi_1(SX)=\{0\}$.

c. For all $n\geq1$, prove that $H_n(X)\cong H_{n+1}(SX)$.
:::

::: {.solution}
Let
\[
q:X\times[-1,1]\longrightarrow SX
\]
be the quotient map, and write
\[
N=q(X\times\{1\}),
\qquad
S=q(X\times\{-1\})
\]
for the north and south suspension points.

<1>1. The subspaces
\[
U=SX\setminus\{S\},
\qquad
V=SX\setminus\{N\}
\]
are open, contractible, and satisfy $SX=U\cup V$.
::: {.proof}
The sets are open because
\[
q^{-1}(U)=X\times(-1,1],
\qquad
q^{-1}(V)=X\times[-1,1)
\]
are open in the product $X\times[-1,1]$ with its relative topology.
Their union is all of $SX$.

On $U$, define
\[
H_U([x,t],s)=[x,(1-s)t+s],
\qquad 0\le s\le1.
\]
For $t>-1$ the second coordinate remains greater than $-1$, and when $t=1$ the expression stays at the north pole, so the formula is well defined on the quotient.
It is induced by a continuous map on $X\times(-1,1]\times[0,1]$, hence is continuous.
At $s=0$ it is the identity and at $s=1$ it is the constant map to $N$.
Thus $U$ is contractible.

Similarly,
\[
H_V([x,t],s)=[x,(1-s)t-s]
\]
contracts $V$ to $S$.
This proves part (a).
:::

<1>2. The intersection $U\cap V$ is homeomorphic to $X\times(-1,1)$ and hence homotopy equivalent to $X$.
::: {.proof}
One has
\[
q^{-1}(U\cap V)=X\times(-1,1).
\]
No two distinct points of this set are identified by the suspension quotient, since the only nontrivial identifications occur at the levels $t=\pm1$.
The restriction of $q$ to this saturated open subset is therefore a bijective quotient map, hence a homeomorphism
\[
X\times(-1,1)\xrightarrow{\cong}U\cap V.
\]
Projection onto $X$ is a homotopy equivalence because $(-1,1)$ is contractible.
:::

<1>3. If $X$ is path-connected, then
\[
\boxed{\pi_1(SX)=\{0\}}.
\]
::: {.proof}
If $X$ is path-connected, then <1>2 implies that $U\cap V$ is path-connected.
The sets $U$ and $V$ are open and contractible by <1>1, hence path-connected and simply connected.
The Seifert–van Kampen theorem gives
\[
\pi_1(SX)
\cong
\pi_1(U)*_{\pi_1(U\cap V)}\pi_1(V).
\]
Both outer groups are trivial, so their amalgamated product is trivial.
This proves part (b).
:::

<1>4. For every $n\ge1$ there is an isomorphism
\[
\boxed{H_{n+1}(SX)\cong H_n(X)}.
\]
::: {.proof}
Apply the Mayer–Vietoris sequence to the open cover $SX=U\cup V$.
For $n\ge1$, contractibility of $U$ and $V$ gives
\[
H_{n+1}(U)\oplus H_{n+1}(V)=0,
\qquad
H_n(U)\oplus H_n(V)=0.
\]
Hence the relevant exact segment is
\[
0
\longrightarrow H_{n+1}(SX)
\xrightarrow{\partial}
H_n(U\cap V)
\longrightarrow0.
\]
Thus $\partial$ is an isomorphism.
By <1>2,
\[
H_n(U\cap V)\cong H_n(X).
\]
Combining the two isomorphisms yields
\[
H_{n+1}(SX)\cong H_n(X)
\]
for every $n\ge1$, which is part (c).
:::
:::
