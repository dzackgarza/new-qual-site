---
schema: qual/card@1
id: E-TK5YY
kind: problem
title: Cayley-Hamilton theorem, cokernels of integer matrices, and diagonalizability
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Diagonalization
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
- Prove the Cayley-Hamilton theorem.

- Prove that the minimal polynomial divides the characteristic polynomial.

- Prove that the cokernel of $A\in \Mat(n\times n, \ZZ)$ is finite $\iff \det A \neq 0$, and show that in this case $\abs{\coker(A)} = \abs{\det(A)}$.

- Show that a nilpotent operator is diagonalizable.

- Show that if $A,B$ are diagonalizable and $[A, B] = 0$ then $A,B$ are simultaneously diagonalizable.

- Does diagonalizable imply invertible?
  The converse?

- Does diagonalizable imply distinct eigenvalues?

- Show that if a matrix is diagonalizable, its minimal polynomial is squarefree.

- Show that a matrix representing a linear map $T:V\to V$ is diagonalizable iff $V$ is a direct sum of eigenspaces $V = \bigoplus_i \ker(T -\lambda_i I)$.

- Show that if $\theset{\vector v_i}$ is a basis for $V$ where $\dim(V) = n$ and $T(\vector v_i) = \vector v_{i+1 \mod n}$ then $T$ is diagonalizable with minimal polynomial $x^n-1$.

- Show that if the minimal polynomial of a linear map $T$ is irreducible, then every $T\dash$invariant subspace has a $T\dash$invariant complement.
:::

::: {.solution}
Throughout, $A\in M_n(F)$ for a field $F$, with characteristic polynomial $p(t)=\det(tI-A)=\sum_{j=0}^nc_jt^j$.

::: pf

::: {.pf-step #cayley-hamilton}
$p(A)=0$ (Cayley--Hamilton).

::: pf-proof
Write $\operatorname{adj}(tI-A)=\sum_{j=0}^{n-1}B_jt^j$ with $B_j\in M_n(F)$.
The adjugate identity $(tI-A)\operatorname{adj}(tI-A)=p(t)I$ gives, on comparing coefficients of $t^j$, $$B_{n-1}=c_nI,\qquad B_{j-1}-AB_j=c_jI\ (1\le j\le n-1),\qquad -AB_0=c_0I .$$ Multiplying the equation for $t^j$ on the left by $A^j$ and summing over $j$, the right sides sum to $p(A)$ and the left sides telescope to $0$.
:::

:::

::: pf-step
The minimal polynomial $m_A$ divides $p$.

::: pf-proof
$m_A$ generates the ideal $\{f\in F[t]:f(A)=0\}$ of the PID $F[t]$, and $p$ lies in it by step [](#cayley-hamilton){.pf-ref}.
:::

:::

::: pf-step
For $A\in M_n(\ZZ)$, $\operatorname{coker}A$ is finite if and only if $\det A\neq0$, and then $|\operatorname{coker}A|=|\det A|$.

::: pf-proof
By Smith normal form there are $P,Q\in\operatorname{GL}_n(\ZZ)$ with $PAQ=D=\operatorname{diag}(d_1,\dots,d_n)$, $d_i\ge0$.
Since $P,Q$ are automorphisms of $\ZZ^n$, $\operatorname{coker}A\cong\operatorname{coker}D\cong\bigoplus_i\ZZ/d_i\ZZ$, which is finite if and only if every $d_i\neq0$, and then has order $\prod_id_i$.
Since $\det P,\det Q=\pm1$, $|\det A|=|\det D|=\prod_id_i$.
:::

:::

::: pf-step
A nilpotent operator $N$ is diagonalizable only if $N=0$.

::: pf-proof
If $N^k=0$ and $Nv=\lambda v$ with $v\neq0$, then $\lambda^kv=0$, so $\lambda=0$.
A diagonalizable $N$ is therefore similar to the zero matrix, hence $N=0$.
:::

:::

::: pf-step
If $A$ and $B$ are diagonalizable and $AB=BA$, then they are simultaneously diagonalizable.

::: pf-proof
For $v\in E_\lambda(A)=\ker(A-\lambda I)$, $A(Bv)=B(Av)=\lambda Bv$, so each eigenspace $E_\lambda(A)$ is $B$-invariant.
The minimal polynomial of $B|_{E_\lambda(A)}$ divides that of $B$, which has distinct linear factors, so $B|_{E_\lambda(A)}$ is diagonalizable.
The union over $\lambda$ of eigenbases of the restrictions is a basis of $V=\bigoplus_\lambda E_\lambda(A)$ of common eigenvectors.
:::

:::

::: pf-step
Diagonalizability neither implies nor is implied by invertibility, and does not imply distinct eigenvalues.

::: pf-proof
$\begin{pmatrix}1&0\\0&0\end{pmatrix}$ is diagonal and singular.
$\begin{pmatrix}1&1\\0&1\end{pmatrix}$ is invertible with minimal polynomial $(x-1)^2$, so it is not diagonalizable.
$I_n$ ($n\ge2$) is diagonal with the single eigenvalue $1$.
:::

:::

::: {.pf-step #diag-iff-eigenspace-decomp}
$T\colon V\to V$ is diagonalizable if and only if $V=\bigoplus_i\ker(T-\lambda_iI)$, and then $m_T=\prod_i(x-\lambda_i)$ is squarefree.

::: pf-proof
Eigenvectors for distinct eigenvalues are linearly independent, so the sum $\sum_i\ker(T-\lambda_iI)$ is direct.
$T$ is diagonalizable exactly when $V$ has a basis of eigenvectors, that is, when this sum is $V$.
In that case $\prod_i(T-\lambda_iI)$ kills every basis vector, so $m_T$ divides the squarefree polynomial $\prod_i(x-\lambda_i)$.
:::

:::

::: pf-step
If $T(v_i)=v_{i+1\bmod n}$ for a basis $v_0,\dots,v_{n-1}$, then $m_T=x^n-1$, and $T$ is diagonalizable over $\CC$.

::: pf-proof
$T^n=I$, so $m_T\mid x^n-1$; and $v_0,Tv_0,\dots,T^{n-1}v_0$ is a basis, so no nonzero polynomial of degree less than $n$ kills $T$.
Hence $m_T=x^n-1$.
Over $\CC$ it has the $n$ distinct roots $e^{2\pi ik/n}$, so by step [](#diag-iff-eigenspace-decomp){.pf-ref} $T$ is diagonalizable.
Over a field where $x^n-1$ has a repeated root or does not split, $T$ is not diagonalizable.
:::

:::

::: pf-step
If $m_T$ is irreducible, every $T$-invariant subspace $W$ has a $T$-invariant complement.

::: pf-proof
$E=F[x]/(m_T)$ is a field, and $V$ is an $E$-vector space with $x$ acting as $T$.
$T$-invariant subspaces are exactly the $E$-subspaces, and an $E$-linear complement of $W$ is $T$-invariant.
:::

:::

:::

:::

::: {.remark}
The fourth part states that a nilpotent operator is diagonalizable; by step <1>4 this holds only for the zero operator.
The tenth part holds over $\CC$, or over any field in which $x^n-1$ has $n$ distinct roots.
:::
