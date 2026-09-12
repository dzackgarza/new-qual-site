---
schema: qual/card@1
id: P-APAS20F
kind: problem
title: Scalar products $\langle e_1^n,e_1^n\rangle$ and $\langle h_3 p_6,s_{5,4}\rangle$
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
relations: []
review: draft
---

::: problem
Let $\langle\,\cdot\,,\,\cdot\,\rangle$ be the scalar product on the ring of symmetric functions.

(a) Evaluate $\langle e_1^n,e_1^n\rangle$.

(b) Evaluate $\langle h_3 p_6,s_{5,4}\rangle$.
:::

::: solution
We use the Hall inner product, for which the power-sum basis satisfies
\[
\langle p_\lambda,p_\mu\rangle=\delta_{\lambda\mu}z_\lambda.
\]
Since \(e_1=p_1\),
\[
e_1^n=p_1^n=p_{(1^n)}.
\]
For the partition \((1^n)\),
\[
z_{(1^n)}=1^n n!=n!.
\]
Therefore
\[
\boxed{\langle e_1^n,e_1^n\rangle=n!.}
\]

For (b), \(h_3=s_{(3)}\). The Murnaghan--Nakayama rule says that the coefficient of \(s_\lambda\) in \(p_6s_{(3)}\) is the signed sum over ways of obtaining \(\lambda\) from \((3)\) by adding a border strip of size \(6\). For \(\lambda=(5,4)\), the skew diagram
\[
(5,4)/(3)
\]
consists of two boxes in the first row and four in the second row. It is connected, contains no \(2\times2\) block, and occupies two rows, so it is a border strip of height \(1\). Thus its Murnaghan--Nakayama sign is
\[
(-1)^1=-1.
\]
There is exactly one such skew shape, hence
\[
[h_3p_6:s_{(5,4)}]=-1.
\]
Because the Schur functions are orthonormal for the Hall inner product,
\[
\boxed{\langle h_3p_6,s_{(5,4)}\rangle=-1.}
\]
:::
