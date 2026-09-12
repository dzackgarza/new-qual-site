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

::: problem
Throughout, $M_n$ denotes the set of $n\times n$ matrices with complex entries, $\mathbb{C}^n$ is the set of column vectors with $n$ complex entries, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) Prove the Schur decomposition theorem for a matrix $A\in M_n$.

(b) Prove that for $A,B\in M_n$, if $x^HAx=x^HBx$ for all $x\in\mathbb{C}^n$, then $A=B$.
:::

::: solution
For (a), we prove by induction on $n$ that there is a unitary matrix $U$ and an upper-triangular matrix $T$ such that
\[
U^HAU=T,
\]
equivalently $A=UTU^H$.

The assertion is trivial for $n=1$. Suppose $n>1$. Since the characteristic polynomial of $A$ splits over $\mathbb C$, choose an eigenvalue $\lambda$ and a unit eigenvector $u_1$ with
\[
Au_1=\lambda u_1.
\]
Extend $u_1$ to an orthonormal basis $u_1,\ldots,u_n$ of $\mathbb C^n$, and let $U_1$ be the unitary matrix having these vectors as columns. In this basis,
\[
U_1^HAU_1=
\begin{pmatrix}
\lambda & *\\
0&A_1
\end{pmatrix}
\]
for some $(n-1)\times(n-1)$ matrix $A_1$: the zero block occurs because the first column represents $Au_1=\lambda u_1$.

By the induction hypothesis there is a unitary $(n-1)\times(n-1)$ matrix $V$ such that $V^HA_1V$ is upper triangular. Set
\[
W=\begin{pmatrix}1&0\\0&V\end{pmatrix}.
\]
Then $W$ is unitary and
\[
W^*U_1^HAU_1W
=
\begin{pmatrix}
\lambda&*\\
0&V^HA_1V
\end{pmatrix}
\]
is upper triangular. Thus $U=U_1W$ gives the desired Schur decomposition.

For (b), set $C=A-B$. The hypothesis is
\[
x^HCx=0\qquad\text{for every }x\in\mathbb C^n.
\]
Write $C=(c_{ij})$. Taking $x=e_i$ gives
\[
c_{ii}=0
\]
for every $i$.

For $i\ne j$, take $x=e_i+e_j$. Since the diagonal entries vanish,
\[
0=(e_i+e_j)^HC(e_i+e_j)=c_{ij}+c_{ji}.
\]
Now take $x=e_i+i e_j$. Again using $c_{ii}=c_{jj}=0$,
\[
0=(e_i+i e_j)^HC(e_i+i e_j)=i c_{ij}-i c_{ji},
\]
so
\[
c_{ij}-c_{ji}=0.
\]
Together with $c_{ij}+c_{ji}=0$, this yields
\[
c_{ij}=c_{ji}=0.
\]
Hence every entry of $C$ is zero, so $C=0$ and therefore $A=B$.
:::
