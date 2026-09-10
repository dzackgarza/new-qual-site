---
schema: qual/card@1
id: P-APAF07A
kind: problem
title: Singular Value Decomposition Theorem
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
State and prove the Singular Value Decomposition Theorem.
(If you use the Polar Decomposition Theorem, then also state and prove it.)
:::

::: {.solution}
<1>1. **Hermitian spectral theorem.** If $H\in M_n(\mathbb C)$ is Hermitian, then $\mathbb C^n$ has an orthonormal basis of eigenvectors of $H$, and all eigenvalues are real.
::: {.proof}
Because the characteristic polynomial of $H$ splits over $\mathbb C$, choose an eigenvector $0\ne v$ with $Hv=\lambda v$.
Then
\[
\lambda\langle v,v\rangle
=\langle Hv,v\rangle
=\langle v,Hv\rangle
=\overline\lambda\langle v,v\rangle,
\]
so $\lambda\in\mathbb R$.
Normalize $v$.
If $w\perp v$, then
\[
\langle Hw,v\rangle
=\langle w,Hv\rangle
=\lambda\langle w,v\rangle=0,
\]
so $v^\perp$ is $H$-invariant. The restriction of $H$ to $v^\perp$ is again Hermitian.
Induction on $n$ therefore gives an orthonormal eigenbasis of $v^\perp$; adjoining $v$ gives an orthonormal eigenbasis of $\mathbb C^n$.
:::

<1>2. **Singular Value Decomposition.** For every $A\in M_{m,n}(\mathbb C)$ there exist unitary matrices
\[
U\in U(m),\qquad V\in U(n)
\]
and nonnegative real numbers
\[
\sigma_1\ge\cdots\ge\sigma_r>0,
\qquad r=\operatorname{rank}A,
\]
such that
\[
A=U\Sigma V^*,
\]
where $\Sigma\in M_{m,n}(\mathbb C)$ has diagonal entries $\sigma_1,\ldots,\sigma_r$ and all other entries zero.
The numbers $\sigma_i$ are the positive square roots of the nonzero eigenvalues of $A^*A$ and are called the singular values of $A$.
::: {.proof}
The construction is given in the following steps.
:::

<1>3. The matrix $A^*A$ is Hermitian positive semidefinite. Hence there is an orthonormal basis $v_1,\ldots,v_n$ of $\mathbb C^n$ such that
\[
A^*Av_i=\sigma_i^2v_i,
\]
with
\[
\sigma_1\ge\cdots\ge\sigma_r>0,
\qquad
\sigma_{r+1}=\cdots=\sigma_n=0,
\]
and $r=\operatorname{rank}A$.
::: {.proof}
Hermitianity follows from
\[
(A^*A)^*=A^*A.
\]
For every $x\in\mathbb C^n$,
\[
\langle A^*Ax,x\rangle=\langle Ax,Ax\rangle=\|Ax\|^2\ge0,
\]
so every eigenvalue is nonnegative. Apply <1>1 and order the eigenvalues decreasingly, writing them as $\sigma_i^2$.
Finally,
\[
\ker(A^*A)=\ker A,
\]
because
\[
A^*Ax=0
\Longleftrightarrow
0=\langle A^*Ax,x\rangle=\|Ax\|^2
\Longleftrightarrow
Ax=0.
\]
Thus
\[
r=\operatorname{rank}A=n-\dim\ker A
=n-\dim\ker(A^*A),
\]
which is exactly the number of positive eigenvalues counted with multiplicity.
:::

<1>4. For $1\le i\le r$, define
\[
u_i=\frac{Av_i}{\sigma_i}.
\]
Then $u_1,\ldots,u_r$ is an orthonormal set in $\mathbb C^m$.
::: {.proof}
For $1\le i,j\le r$,
\[
\langle u_i,u_j\rangle
=\frac{1}{\sigma_i\sigma_j}\langle Av_i,Av_j\rangle
=\frac{1}{\sigma_i\sigma_j}\langle v_i,A^*Av_j\rangle
=\frac{\sigma_j^2}{\sigma_i\sigma_j}\langle v_i,v_j\rangle.
\]
If $i\ne j$, this is $0$; if $i=j$, it is $1$. Hence the $u_i$ are orthonormal.
:::

<1>5. Extend $u_1,\ldots,u_r$ to an orthonormal basis $u_1,\ldots,u_m$ of $\mathbb C^m$. Let
\[
U=[u_1\ \cdots\ u_m],
\qquad
V=[v_1\ \cdots\ v_n].
\]
Then $U$ and $V$ are unitary and
\[
Av_i=\sigma_i u_i\quad(1\le i\le r),
\qquad
Av_i=0\quad(i>r).
\]
::: {.proof}
Every orthonormal set in a finite-dimensional inner-product space extends to an orthonormal basis, so the extension exists. A matrix whose columns form an orthonormal basis is unitary.
For $i\le r$, the first formula is the definition of $u_i$. For $i>r$, <1>3 gives $A^*Av_i=0$, hence $v_i\in\ker(A^*A)=\ker A$, so $Av_i=0$.
:::

<1>6. With $\Sigma$ as in <1>2,
\[
AV=U\Sigma,
\]
and therefore
\[
A=U\Sigma V^*.
\]
::: {.proof}
The $i$-th column of $AV$ is $Av_i$. By <1>5, this column equals $\sigma_i u_i$ for $i\le r$ and $0$ for $i>r$. These are exactly the columns of $U\Sigma$, so $AV=U\Sigma$.
Since $V$ is unitary, $V^{-1}=V^*$, and right multiplication by $V^*$ gives the stated factorization.
:::

<1>7. The positive singular values are uniquely determined by $A$.
::: {.proof}
From any decomposition $A=U\Sigma V^*$,
\[
A^*A
=V\Sigma^*\Sigma V^*.
\]
Thus $A^*A$ is unitarily similar to $\Sigma^*\Sigma$, whose eigenvalues are
\[
\sigma_1^2,\ldots,\sigma_r^2,0,\ldots,0.
\]
Therefore the multiset of singular values is determined uniquely by the spectrum of $A^*A$.
:::
:::
