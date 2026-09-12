---
schema: qual/card@1
id: P-APAS24C
kind: problem
title: Hermitian matrices are those with real quadratic forms $x^HAx$
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
---

::: problem
Let $A\in M_n(\mathbb{C})=\mathbb{C}^{n\times n}$.
Prove that $A$ is Hermitian if and only if $x^HAx\in\mathbb{R}$ for all $x\in\mathbb{C}^n$.

Note: $x^H=\overline{x^T}$.
:::

::: solution
If $A$ is Hermitian, then for every $x\in\mathbb C^n$,
\[
\overline{x^HAx}=x^HA^Hx=x^HAx,
\]
so $x^HAx$ is real.

Conversely, suppose
\[
x^HAx\in\mathbb R
\]
for every $x$. Then
\[
x^HAx=\overline{x^HAx}=x^HA^Hx,
\]
so
\[
x^H(A-A^H)x=0
\]
for every $x$.

Set $B=A-A^H$. We show $B=0$. Taking $x=e_i$ gives
\[
b_{ii}=0.
\]
For $i\ne j$, taking $x=e_i+e_j$ gives
\[
b_{ij}+b_{ji}=0,
\]
and taking $x=e_i+i e_j$ gives
\[
i b_{ij}-i b_{ji}=0.
\]
Thus $b_{ij}=b_{ji}=0$. Therefore every entry of $B$ vanishes, so
\[
A-A^H=0.
\]
Hence $A=A^H$, i.e. $A$ is Hermitian.
:::
