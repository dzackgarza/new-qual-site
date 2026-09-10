---
schema: qual/card@1
id: P-APAF06A
kind: problem
title: Eigenpair of algebraic and geometric multiplicity one yields a complementary block form
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Assume that $(\lambda, x)$ is an eigenpair of $A \in M_n$ such that $am(\lambda) = gm(\lambda) = 1$.
Prove that there exists a nonsingular matrix $(x \quad X)$ with inverse $(y \quad Y)^*$ such that
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix} A (x \quad X) = \begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]
:::


::: {.solution}
<1>1. Let $V=\mathbb C^n$ and write the characteristic polynomial as
\[
\chi_A(t)=(t-\lambda)q(t).
\]
Since the algebraic multiplicity of $\lambda$ is one, $q(\lambda)\neq0$, so $t-\lambda$ and $q(t)$ are relatively prime.
::: {.proof}
Algebraic multiplicity one means exactly that $t-\lambda$ occurs to the first power in $\chi_A$ and does not divide $q$.
:::

<1>2. One has an $A$-invariant direct-sum decomposition
\[
V=\ker(A-\lambda I)\oplus\ker q(A).
\]
::: {.proof}
Choose polynomials $u,v$ with
\[
u(t)(t-\lambda)+v(t)q(t)=1.
\]
For $z\in V$,
\[
z=u(A)(A-\lambda I)z+v(A)q(A)z.
\]
By Cayley--Hamilton,
\[
(A-\lambda I)q(A)=\chi_A(A)=0.
\]
Hence $u(A)(A-\lambda I)z\in\ker q(A)$ and $v(A)q(A)z\in\ker(A-\lambda I)$, so the two kernels span $V$.
If $z$ lies in both kernels, the Bézout identity gives $z=0$, so the sum is direct.
Both kernels are $A$-invariant because they are kernels of polynomials in $A$.
:::

<1>3. Since the geometric multiplicity of $\lambda$ is one,
\[
\ker(A-\lambda I)=\mathbb Cx.
\]
Choose a matrix $X$ whose columns form a basis of $\ker q(A)$.
Then
\[
S=(x\quad X)
\]
is nonsingular.
::: {.proof}
The eigenspace for $\lambda$ is one-dimensional and contains the nonzero eigenvector $x$, so it is exactly $\mathbb Cx$.
By <1>2, adjoining a basis of the complementary summand $\ker q(A)$ to $x$ gives a basis of $V$.
:::

<1>4. Relative to the basis given by the columns of $S$, the matrix of $A$ is block diagonal:
\[
S^{-1}AS=
\begin{pmatrix}
\lambda&0\\
0&M
\end{pmatrix}
\]
for some $(n-1)\times(n-1)$ matrix $M$.
::: {.proof}
The first summand $\mathbb Cx$ is $A$-invariant and $Ax=\lambda x$, while the complementary summand $\ker q(A)$ is also $A$-invariant by <1>2. Therefore there are no off-diagonal blocks, and the restriction of $A$ to $\mathbb Cx$ is multiplication by $\lambda$.
:::

<1>5. Write the inverse of $S$ in block-row form as
\[
S^{-1}=\begin{pmatrix}y^*\\Y^*\end{pmatrix}.
\]
Then
\[
\begin{pmatrix}y^*\\Y^*\end{pmatrix}A(x\quad X)
=
\begin{pmatrix}\lambda&0\\0&M\end{pmatrix},
\]
which is the required form.
::: {.proof}
This is exactly the identity in <1>4 after naming the first row of $S^{-1}$ by $y^*$ and the remaining rows by $Y^*$.
:::
:::
