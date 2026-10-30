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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Show that a nilpotent operator is diagonalizable", which is false for nonzero nilpotents; part (d) now asks to show that a diagonalizable nilpotent operator is zero. The source states part (j) over an unspecified field, where it fails when x^n-1 has a repeated root; part (j) now works over the complex numbers. The bulleted parts are labelled (a) to (k).'
---

::: {.exercise}
(a) Prove the Cayley-Hamilton theorem.

(b) Prove that the minimal polynomial divides the characteristic polynomial.

(c) Prove that the cokernel of $A\in \Mat(n\times n, \ZZ)$ is finite $\iff \det A \neq 0$, and show that in this case $\abs{\coker(A)} = \abs{\det(A)}$.

(d) Show that a nilpotent operator is diagonalizable only if it is zero.

(e) Show that if $A,B$ are diagonalizable and $[A, B] = 0$ then $A,B$ are simultaneously diagonalizable.

(f) Does diagonalizable imply invertible?
The converse?

(g) Does diagonalizable imply distinct eigenvalues?

(h) Show that if a matrix is diagonalizable, its minimal polynomial is squarefree.

(i) Show that a matrix representing a linear map $T:V\to V$ is diagonalizable iff $V$ is a direct sum of eigenspaces $V = \bigoplus_i \ker(T -\lambda_i I)$.

(j) Let $V$ be a complex vector space. Show that if $\theset{\vector v_i}$ is a basis for $V$ where $\dim(V) = n$ and $T(\vector v_i) = \vector v_{i+1 \mod n}$ then $T$ is diagonalizable with minimal polynomial $x^n-1$.

(k) Show that if the minimal polynomial of a linear map $T$ is irreducible, then every $T$-invariant subspace has a $T$-invariant complement.
:::

::: {.solution}
Throughout, $A\in M_n(F)$ for a field $F$, with characteristic polynomial $p(t)=\det(tI-A)=\sum_{j=0}^nc_jt^j$.

::: pf

::: {.pf-step #cayley-hamilton}
(a) $p(A)=0$.

::: pf-proof
Write $\operatorname{adj}(tI-A)=\sum_{j=0}^{n-1}B_jt^j$ with $B_j\in M_n(F)$.
The adjugate identity $(tI-A)\operatorname{adj}(tI-A)=p(t)I$ gives, on comparing coefficients of $t^j$, $$B_{n-1}=c_nI,\qquad B_{j-1}-AB_j=c_jI\ (1\le j\le n-1),\qquad -AB_0=c_0I .$$ Multiplying the equation for $t^j$ on the left by $A^j$ and summing over $j$, the right sides sum to $p(A)$ and the left sides telescope to $0$.
:::

:::

::: pf-step
(b) The minimal polynomial $m_A$ divides $p$.

::: pf-proof
$m_A$ generates the ideal $\{f\in F[t]:f(A)=0\}$ of the PID $F[t]$, and $p$ lies in it by step [](#cayley-hamilton){.pf-ref}.
:::

:::

::: pf-step
(c) For $A\in M_n(\ZZ)$, $\coker A$ is finite if and only if $\det A\neq0$, and then $\abs{\coker A}=\abs{\det A}$.

::: pf-proof
By Smith normal form there are $P,Q\in\GL_n(\ZZ)$ with $PAQ=D=\diag(d_1,\ldots,d_n)$, $d_i\ge0$.
Since $P,Q$ are automorphisms of $\ZZ^n$, $\coker A\cong\coker D\cong\bigoplus_i\ZZ/d_i\ZZ$, which is finite if and only if every $d_i\neq0$, and then has order $\prod_id_i$.
Since $\det P,\det Q=\pm1$, $\abs{\det A}=\abs{\det D}=\prod_id_i$.
:::

:::

::: pf-step
(d) A nilpotent operator $N$ is diagonalizable only if $N=0$.

::: pf-proof
If $N^k=0$ and $Nv=\lambda v$ with $v\neq0$, then $\lambda^kv=0$, so $\lambda=0$.
A diagonalizable $N$ is therefore similar to the zero matrix, hence $N=0$.
:::

:::

::: pf-step
(e) If $A$ and $B$ are diagonalizable and $AB=BA$, then they are simultaneously diagonalizable.

::: pf-proof
For $v\in E_\lambda(A)=\ker(A-\lambda I)$, $A(Bv)=B(Av)=\lambda Bv$, so each eigenspace $E_\lambda(A)$ is $B$-invariant.
The minimal polynomial of $B\restrict_{E_\lambda(A)}$ divides that of $B$, which has distinct linear factors, so $B\restrict_{E_\lambda(A)}$ is diagonalizable.
The union over $\lambda$ of eigenbases of the restrictions is a basis of $V=\bigoplus_\lambda E_\lambda(A)$ of common eigenvectors.
:::

:::

::: pf-step
(f), (g) Diagonalizability neither implies nor is implied by invertibility, and does not imply distinct eigenvalues.

::: pf-proof
$\begin{pmatrix}1&0\\0&0\end{pmatrix}$ is diagonal and singular.
$\begin{pmatrix}1&1\\0&1\end{pmatrix}$ is invertible with minimal polynomial $(x-1)^2$, so it is not diagonalizable.
$I_n$ ($n\ge2$) is diagonal with the single eigenvalue $1$.
:::

:::

::: pf-step
(h) If $T$ is diagonalizable, its minimal polynomial $m_T$ is squarefree.

::: pf-proof
Let $\lambda_1,\ldots,\lambda_r$ be the distinct eigenvalues of $T$. A basis of eigenvectors is killed by $\prod_i(T-\lambda_iI)$, so $m_T$ divides the squarefree polynomial $\prod_i(x-\lambda_i)$.
:::

:::

::: {.pf-step #diag-iff-eigenspace-decomp}
(i) $T\colon V\to V$ is diagonalizable if and only if $V=\bigoplus_i\ker(T-\lambda_iI)$.

::: pf-proof
Eigenvectors for distinct eigenvalues are linearly independent, so the sum $\sum_i\ker(T-\lambda_iI)$ is direct.
$T$ is diagonalizable exactly when $V$ has a basis of eigenvectors, that is, when this sum is $V$.
:::

:::

::: pf-step
(j) If $T(v_i)=v_{i+1\bmod n}$ for a basis $v_0,\ldots,v_{n-1}$ of a complex vector space, then $m_T=x^n-1$ and $T$ is diagonalizable.

::: pf-proof
$T^n=I$, so $m_T\mid x^n-1$; and $v_0,Tv_0,\ldots,T^{n-1}v_0$ is a basis, so no nonzero polynomial of degree less than $n$ kills $T$.
Hence $m_T=x^n-1$.
Over $\CC$ it has the $n$ distinct roots $\zeta_k=e^{2\pi ik/n}$, so $x^n-1=\prod_k(x-\zeta_k)$ is a product of pairwise coprime factors and the kernel decomposition theorem gives $V=\bigoplus_k\ker(T-\zeta_kI)$. By step [](#diag-iff-eigenspace-decomp){.pf-ref}, $T$ is diagonalizable.
:::

:::

::: pf-step
(k) If $m_T$ is irreducible, every $T$-invariant subspace $W$ has a $T$-invariant complement.

::: pf-proof
$E=F[x]/(m_T)$ is a field, and $V$ is an $E$-vector space with $x$ acting as $T$.
$T$-invariant subspaces are exactly the $E$-subspaces, and an $E$-linear complement of $W$ is $T$-invariant.
:::

:::

:::

:::

::: {.remark}
Part (j) holds over any field in which $x^n-1$ has $n$ distinct roots, and fails over a field in which it has a repeated root.
:::
