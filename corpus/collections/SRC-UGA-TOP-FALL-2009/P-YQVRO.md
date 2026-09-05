---
schema: qual/card@1
id: P-YQVRO
kind: problem
title: Homotopy classes of self-maps of $S^1\times\DD^2$ in which every map has a
  fixed point
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Fall 2009 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Classified self-map homotopy classes by the degree on the core circle, computed the Lefschetz number as 1-k, and exhibited a fixed-point-free rotation in the unique exceptional class k=1.
---

::: problem
Find all homotopy classes of maps from $S^1 \times \DD^2$ to itself such that every element of the homotopy class has a fixed point.
:::

::: {.solution}
Put
\[
M=S^1\times\DD^2.
\]

<1>1. Homotopy classes of self-maps of $M$ are indexed by an integer
\[
k\in\ZZ,
\]
the degree induced on the core circle.
::: {.proof}
Let
\[
i:S^1\longrightarrow M,
\qquad
i(z)=(z,0),
\]
and let
\[
r:M\longrightarrow S^1,
\qquad
r(z,w)=z.
\]
Then
\[
r\circ i=\operatorname{id}_{S^1},
\]
while $i\circ r$ is homotopic to the identity on $M$ by radial contraction in the disk factor.

For a self-map $f:M\to M$, set
\[
h_f=r\circ f\circ i:S^1\longrightarrow S^1.
\]
Using the two deformation-retraction homotopies,
\[
f\simeq i\circ h_f\circ r.
\]
Thus the homotopy class of $f$ is determined by the homotopy class of $h_f$.
Maps $S^1\to S^1$ are classified up to homotopy by their degree, so define
\[
k=\deg(h_f)\in\ZZ.
\]
Conversely, for every $k\in\ZZ$, the map
\[
(z,w)\longmapsto(z^k,0)
\]
represents the corresponding class.
Hence
\[
[M,M]\cong\ZZ.
\]
:::

<1>2. If $f$ represents the class indexed by $k$, then its Lefschetz number is
\[
L(f)=1-k.
\]
::: {.proof}
The solid torus deformation retracts onto $S^1$, so with rational coefficients
\[
H_j(M;\QQ)\cong
\begin{cases}
\QQ,&j=0,1,\\
0,&j\ge2.
\end{cases}
\]
Because $M$ is connected, the induced map on $H_0$ is the identity and has trace $1$.
Under the generator supplied by the oriented core circle, the induced map on $H_1$ is multiplication by $k$, so its trace is $k$.
Therefore
\[
L(f)
=\sum_{j\ge0}(-1)^j\operatorname{tr}(f_*|H_j(M;\QQ))
=1-k.
\]
:::

<1>3. Every map in a class with
\[
k\ne1
\]
has a fixed point.
::: {.proof}
If $g\simeq f$, homotopy invariance of the induced homology maps gives
\[
L(g)=L(f)=1-k.
\]
When $k\ne1$, this Lefschetz number is nonzero.
The Lefschetz fixed-point theorem for the finite CW complex $M$ therefore implies that $g$ has a fixed point.
Since $g$ was arbitrary in the homotopy class, every representative has a fixed point.
:::

<1>4. The class
\[
k=1
\]
does not have the required property.
::: {.proof}
Choose a unit complex number
\[
\lambda\ne1
\]
and define
\[
R_\lambda:M\longrightarrow M,
\qquad
R_\lambda(z,w)=(\lambda z,w).
\]
The map on the core circle is the rotation
\[
z\longmapsto\lambda z,
\]
which has degree $1$.
Thus $R_\lambda$ lies in the class $k=1$ by <1>1.

It has no fixed point: if
\[
R_\lambda(z,w)=(z,w),
\]
then $\lambda z=z$, and since $z\in S^1$ is nonzero this forces $\lambda=1$, contrary to the choice of $\lambda$.
Hence the degree-one class contains a fixed-point-free representative.
:::

<1>5. Therefore the required homotopy classes are exactly
\[
\boxed{\{k\in\ZZ:k\ne1\}}.
\]
::: {.proof}
Step <1>3 proves that every class with $k\ne1$ has the required fixed-point property, while <1>4 excludes the remaining class $k=1$.
:::
:::
