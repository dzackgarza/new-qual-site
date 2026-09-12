---
schema: qual/card@1
id: P-APAS20H
kind: problem
title: Haar integrals of $\operatorname{Tr} U$ and $|u_{11}|^2$ over $U(2)$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Compute the integrals
\[
\int_{U(2)}\operatorname{Tr} U\,dU
\qquad\text{and}\qquad
\int_{U(2)}|u_{11}|^2\,dU,
\]
where the integration is over the group of $2\times 2$ unitary matrices
\[
U=\begin{bmatrix}u_{11}&u_{12}\\ u_{21}&u_{22}\end{bmatrix}
\]
against Haar measure.
:::

::: solution
Normalize Haar measure on \(U(2)\) to have total mass \(1\).

For the first integral, the function \(U\mapsto\operatorname{Tr}U\) is the character of the defining two-dimensional representation of \(U(2)\). Averaging a character over a compact group gives the dimension of the invariant subspace. The defining representation has no nonzero invariant vector: if \(v\ne0\), then the scalar matrix \(-I\in U(2)\) sends \(v\) to \(-v\ne v\). Therefore
\[
\boxed{\int_{U(2)}\operatorname{Tr}U\,dU=0.}
\]

For the second integral, each unitary matrix satisfies
\[
|u_{11}|^2+|u_{12}|^2=1.
\]
Integrating gives
\[
\int_{U(2)}|u_{11}|^2\,dU+
\int_{U(2)}|u_{12}|^2\,dU=1.
\]
Let
\[
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}\in U(2).
\]
Right multiplication by \(P\) interchanges the two columns. By right invariance of Haar measure,
\[
\int_{U(2)}|u_{11}|^2\,dU
=
\int_{U(2)}|u_{12}|^2\,dU.
\]
Thus the two integrals are equal and sum to \(1\), so each is \(1/2\). Hence
\[
\boxed{\int_{U(2)}|u_{11}|^2\,dU=\frac12.}
\]
:::
