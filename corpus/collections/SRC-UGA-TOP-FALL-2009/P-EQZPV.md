---
schema: qual/card@1
id: P-EQZPV
kind: problem
title: Homology of $S^2$ with three distinct points identified
classification:
  areas:
  - topology
  topics:
  - Homology
  - Quotient Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the quotient description and requested integral homology against problem 4 of the official UGA Fall 2009 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Computed the quotient homology as the relative homology of the CW pair consisting of S^2 and the three identified points, then evaluated the long exact sequence of the pair.
---

::: problem
Let $X$ be the topological space obtained by identifying three distinct points on $S^2$.
Calculate $H_*(X;\ZZ)$.
:::

::: {.solution}
Let
\[
A=\{p_1,p_2,p_3\}\subset S^2
\]
be the three points that are identified.
Then
\[
X=S^2/A.
\]

<1>1. For every $k\ge1$,
\[
\widetilde H_k(X;\ZZ)\cong H_k(S^2,A;\ZZ).
\]
::: {.proof}
Choose a CW structure on $S^2$ in which the three points $p_1,p_2,p_3$ are $0$-cells.
Then $A$ is a subcomplex.
For a CW pair, collapsing the subcomplex gives the quotient isomorphism
\[
\widetilde H_k(S^2/A;\ZZ)
\cong
H_k(S^2,A;\ZZ)
\]
for every $k$.
Since $S^2/A=X$, this gives the claim.
:::

<1>2. One has
\[
H_2(S^2,A;\ZZ)\cong\ZZ.
\]
::: {.proof}
The degree-$2$ portion of the long exact sequence of the pair $(S^2,A)$ is
\[
H_2(A)
\longrightarrow
H_2(S^2)
\longrightarrow
H_2(S^2,A)
\longrightarrow
H_1(A).
\]
Because $A$ is a discrete set of three points,
\[
H_2(A)=H_1(A)=0,
\]
while
\[
H_2(S^2)\cong\ZZ.
\]
Exactness therefore gives
\[
H_2(S^2,A)\cong\ZZ.
\]
:::

<1>3. One has
\[
H_1(S^2,A;\ZZ)\cong\ZZ^2.
\]
::: {.proof}
The next portion of the long exact sequence is
\[
0=H_1(S^2)
\longrightarrow
H_1(S^2,A)
\xrightarrow{\partial}
H_0(A)
\xrightarrow{i_*}
H_0(S^2)
\longrightarrow
H_0(S^2,A)
\longrightarrow0.
\]
Here
\[
H_0(A)\cong\ZZ^3,
\qquad
H_0(S^2)\cong\ZZ.
\]
Since all three points of $A$ lie in the same path component of $S^2$, the inclusion induces
\[
i_*:\ZZ^3\longrightarrow\ZZ,
\qquad
(a,b,c)\longmapsto a+b+c.
\]
This map is surjective and its kernel is
\[
\{(a,b,c)\in\ZZ^3:a+b+c=0\}
\cong\ZZ^2.
\]
Exactness therefore gives
\[
H_1(S^2,A)
\cong
\ker i_*
\cong\ZZ^2.
\]
It also gives $H_0(S^2,A)=0$.
:::

<1>4. For every $k\ge3$,
\[
H_k(S^2,A;\ZZ)=0.
\]
::: {.proof}
For $k\ge3$, the relevant part of the long exact sequence is
\[
H_k(A)
\longrightarrow
H_k(S^2)
\longrightarrow
H_k(S^2,A)
\longrightarrow
H_{k-1}(A).
\]
All three outside groups vanish: a finite discrete space has no positive-degree homology, and $S^2$ has no homology above degree $2$.
Thus the middle relative group vanishes.
:::

<1>5. The quotient $X$ is path connected, so
\[
H_0(X;\ZZ)\cong\ZZ.
\]
::: {.proof}
The sphere $S^2$ is path connected, and the quotient map
\[
S^2\longrightarrow X
\]
is continuous and surjective.
The continuous image of a path-connected space is path connected.
Therefore $X$ is path connected, and its zeroth homology is $\ZZ$.
:::

<1>6. Hence
\[
\boxed{
H_k(X;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,2,\\
\ZZ^2,&k=1,\\
0,&\text{otherwise}.
\end{cases}}
\]
::: {.proof}
For $k\ge1$, combine the quotient isomorphism in <1>1 with the relative-homology computations in <1>2--<1>4.
Degree zero is <1>5.
:::
:::
