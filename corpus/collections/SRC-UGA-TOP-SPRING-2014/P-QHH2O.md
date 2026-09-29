---
schema: qual/card@1
id: P-QHH2O
kind: problem
title: Cellular homology of $S^n\times S^m$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 7 of the official UGA Spring 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified the product CW structure and cellular tensor-product differential, including the n=m multiplicity and the S^0 edge cases.
---

::: {.problem}
Use cellular homology to calculate the homology groups of $S^n \times S^m$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Assume first that $n,m\ge1$.
Give each sphere its standard CW structure with one $0$-cell and one top-dimensional cell.

::: pf-proof

Write
\[
S^n=e^0\cup e^n,
\qquad
S^m=e^0\cup e^m.
\]
The cellular chain complexes are
\[
C_k(S^n)
\cong
\begin{cases}
\mathbb Z,&k=0,n,\\
0,&\text{otherwise},
\end{cases}
\qquad
C_k(S^m)
\cong
\begin{cases}
\mathbb Z,&k=0,m,\\
0,&\text{otherwise}.
\end{cases}
\]
All cellular boundary maps are zero.
For dimensions greater than $1$ this follows because there are no cells in the preceding dimension; for $S^1$, the unique $1$-cell has both endpoints attached to the same $0$-cell, so its cellular boundary is also zero.

:::

:::

::: {.pf-step #s2}

The product CW structure on $S^n\times S^m$ has exactly the four product cells
\[
e^0\times e^0,
\qquad
e^n\times e^0,
\qquad
e^0\times e^m,
\qquad
e^n\times e^m,
\]
of dimensions
\[
0,
\qquad
n,
\qquad
m,
\qquad
n+m.
\]

::: pf-proof

The product of CW complexes carries the product CW structure whose cells are products of cells, with
\[
\dim(e^p\times e^q)=p+q.
\]
Applying this to the two-cell structures in step [](#s1){.pf-ref} yields precisely the displayed cells.

:::

:::

::: {.pf-step #s3}

Every cellular differential of $S^n\times S^m$ is zero.

::: pf-proof

For product CW structures, cellular chains identify with the graded tensor product
\[
C_*(S^n\times S^m)
\cong
C_*(S^n)\otimes C_*(S^m),
\]
and the differential on a homogeneous tensor satisfies
\[
\partial(a\otimes b)
=
(\partial a)\otimes b
+
(-1)^{\deg a}a\otimes(\partial b).
\]
By step [](#s1){.pf-ref} both factor differentials vanish.
Hence the right-hand side is zero for every product cell, so
\[
\partial=0
\]
on the entire cellular chain complex of $S^n\times S^m$.

:::

:::

::: {.pf-step #s4}

If $n\ne m$, then
\[
H_k(S^n\times S^m;\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&k=0,n,m,n+m,\\
0,&\text{otherwise}.
\end{cases}
\]

::: pf-proof

By step [](#s2){.pf-ref} there is one cell in each of the four distinct dimensions
\[
0,n,m,n+m.
\]
By step [](#s3){.pf-ref} every differential is zero.
Therefore cellular homology equals the cellular chain group in each degree, giving the displayed formula.

:::

:::

::: {.pf-step #s5}

If $n=m\ge1$, then
\[
H_k(S^n\times S^n;\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&k=0,2n,\\
\mathbb Z^2,&k=n,\\
0,&\text{otherwise}.
\end{cases}
\]

::: pf-proof

When $n=m$, the two middle product cells
\[
e^n\times e^0
\qquad\text{and}\qquad
e^0\times e^n
\]
have the same dimension $n$.
Thus
\[
C_n(S^n\times S^n)\cong\mathbb Z^2,
\]
while $C_0$ and $C_{2n}$ are each $\mathbb Z$.
Again step [](#s3){.pf-ref} makes all differentials zero.

:::

:::

::: pf-step

Equivalently, for $n,m\ge1$ the answer can be written uniformly as
\[
H_k(S^n\times S^m;\mathbb Z)
\cong
\bigoplus_{j\in\{0,n,m,n+m\}\,:\,j=k}\mathbb Z,
\]
where repeated dimensions contribute separate summands.

::: pf-proof

This is exactly steps [](#s4){.pf-ref} and [](#s5){.pf-ref} written without separating the case $n=m$.

:::

:::

::: pf-step

If the notation is allowed to include $S^0$, the corresponding edge cases are obtained directly from the fact that $S^0$ has two points.

::: pf-proof

For $m\ge1$,
\[
S^0\times S^m\cong S^m\amalg S^m,
\]
so
\[
H_k(S^0\times S^m;\mathbb Z)
\cong
\begin{cases}
\mathbb Z^2,&k=0,m,\\
0,&\text{otherwise}.
\end{cases}
\]
The same holds with $n$ and $m$ interchanged.
Finally,
\[
S^0\times S^0
\]
is a four-point discrete space, so its only nonzero homology group is
\[
H_0(S^0\times S^0;\mathbb Z)\cong\mathbb Z^4.
\]

:::

:::

:::

:::
