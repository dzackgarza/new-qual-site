---
schema: qual/card@1
id: P-APAS13A
kind: problem
title: Schur decomposition; Hermitian quadratic forms determine a matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n\times n$ matrices with complex entries, $\CC^n$ is the set of column vectors with $n$ complex entries, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) Prove the Schur decomposition theorem for a matrix $A\in M_n$.

(b) Prove that for $A,B\in M_n$, if $x^HAx=x^HBx$ for all $x\in\CC^n$, then $A=B$.
:::

::: {.solution}

The argument is the card's own: the induction for Schur's theorem and the two-test polarization for (b). No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Write $U^{H}=\overline{U}^{T}$ for the Hermitian transpose.

::: pf

::: {.pf-step #schur}
(a) For every $A\in M_{n}$ there are a unitary $U$ and an upper triangular $T$ with $U^{H}AU=T$.

::: pf-proof

::: {.pf-step #eigenvector}
$A$ has an eigenvalue $\lambda\in\CC$ with a unit eigenvector $u_{1}$.

::: pf-proof
The characteristic polynomial $\det(A-tI)$ is monic of degree $n$ with complex coefficients, so it has a root $\lambda$ in $\CC$ (the fundamental theorem of algebra); then $A-\lambda I$ is singular, so its kernel is nonzero and contains a vector $u_{1}$, which may be divided by its norm to be made a unit vector.
:::

:::

::: {.pf-step #first-column}
If $u_{1},\ldots,u_{n}$ is an orthonormal basis with $u_{1}$ as above and $U_{1}$ has these as columns, then $U_{1}$ is unitary and
$$
U_{1}^{H}AU_{1}=\begin{pmatrix}\lambda & \ast\\ 0 & A_{1}\end{pmatrix}
$$
with $A_{1}\in M_{n-1}$.

::: pf-proof
The columns of $U_{1}$ being orthonormal means $U_{1}^{H}U_{1}=I$, so $U_{1}$ is unitary. The first column of $U_{1}^{H}AU_{1}$ is the coordinate vector of $Au_{1}=\lambda u_{1}$ in the basis, namely $(\lambda,0,\ldots,0)^{T}$, since $u_{1}$ is the first basis vector and the basis is orthonormal. The remaining columns form an $(n-1)\times(n-1)$ block $A_{1}$.
:::

:::

::: {.pf-step #wrapping}
If $V$ is unitary of size $n-1$ with $V^{H}A_{1}V$ upper triangular, then $W=\begin{pmatrix}1&0\\0&V\end{pmatrix}$ is unitary and $W^{H}\big(U_{1}^{H}AU_{1}\big)W=\begin{pmatrix}\lambda&\ast\\0&V^{H}A_{1}V\end{pmatrix}$.

::: pf-proof
$W^{H}W=\begin{pmatrix}1&0\\0&V^{H}V\end{pmatrix}=I$, so $W$ is unitary. Multiplying the block matrix of step [](#first-column){.pf-ref} on the left by $W^{H}=\begin{pmatrix}1&0\\0&V^{H}\end{pmatrix}$ and on the right by $W$ leaves the first row and column as they are, since $W$ fixes the first coordinate, and replaces the block $A_{1}$ by $V^{H}A_{1}V$. The $(1,1)$ entry stays $\lambda$, the lower-left block stays $0$, and the upper-right block stays some row $\ast$.
:::

:::

::: {.pf-qed}
Induct on $n$. For $n=1$ every $1\times1$ matrix is upper triangular and $U=1$ is unitary. For $n>1$, step [](#first-column){.pf-ref} produces $U_{1}$ and $A_{1}$, the induction hypothesis applied to $A_{1}$ produces a unitary $V$ with $V^{H}A_{1}V$ upper triangular, and step [](#wrapping){.pf-ref} then gives a block upper triangular matrix whose diagonal block $V^{H}A_{1}V$ is upper triangular, so the whole matrix $T$ is upper triangular. With $U=U_{1}W$, unitary as a product of unitaries, one has $U^{H}AU=T$.
:::

:::

:::

::: {.pf-step #diagonal}
(b) If $x^{H}Ax=x^{H}Bx$ for all $x\in\CC^{n}$ then every diagonal entry of $C=A-B$ is zero.

::: pf-proof
Put $C=A-B$; the hypothesis is $x^{H}Cx=0$ for all $x$. For $x=e_{i}$ the standard basis vector, $e_{i}^{H}Ce_{i}=c_{ii}$, so $c_{ii}=0$.
:::

:::

::: {.pf-step #sum}
(b) $c_{ij}+c_{ji}=0$ for $i\ne j$.

::: pf-proof
Take $x=e_{i}+e_{j}$. Expanding, $x^{H}Cx=e_{i}^{H}Ce_{i}+e_{i}^{H}Ce_{j}+e_{j}^{H}Ce_{i}+e_{j}^{H}Ce_{j}=c_{ii}+c_{ij}+c_{ji}+c_{jj}$, and the two diagonal entries vanish by step [](#diagonal){.pf-ref}. The hypothesis gives $c_{ij}+c_{ji}=0$.
:::

:::

::: {.pf-step #difference}
(b) $c_{ij}-c_{ji}=0$ for $i\ne j$.

::: pf-proof
Take $x=e_{i}+ie_{j}$, so $x^{H}=e_{i}^{H}-ie_{j}^{H}$. Then
$$
x^{H}Cx=c_{ii}+ic_{ij}-ic_{ji}+(-i)(i)c_{jj}=c_{ii}+ic_{ij}-ic_{ji}+c_{jj},
$$
using $(-i)(i)=1$; the diagonal entries vanish by step [](#diagonal){.pf-ref}, and the hypothesis gives $i(c_{ij}-c_{ji})=0$, that is $c_{ij}=c_{ji}$.
:::

:::

::: {.pf-step #equality}
(b) $C=0$, that is $A=B$.

::: pf-proof
For $i\ne j$, steps [](#sum){.pf-ref} and [](#difference){.pf-ref} give $c_{ij}+c_{ji}=0$ and $c_{ij}-c_{ji}=0$, hence $2c_{ij}=0$ and $c_{ij}=0$ in $\CC$, and then $c_{ji}=0$. Together with step [](#diagonal){.pf-ref} every entry of $C$ is zero, so $C=0$ and
$$
\boxed{A=B.}
$$
:::

:::

:::
:::
