---
schema: qual/card@1
id: P-APAF21F
kind: problem
title: 'Indecomposable versus irreducible complex representations of $\mathbb{Z}$'
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Modules
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

::: {.problem}
Let $\mathbb{Z}$ be the additive group of integers.
Is every indecomposable $\mathbb{Z}$-module over the complex numbers irreducible?
:::

::: {.solution}
No.

<1>1. Let $V=\mathbb C^2$ and let the generator $1\in\mathbb Z$ act by
\[
T=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]
This defines a complex representation of $\mathbb Z$.
::: {.proof}
The matrix $T$ is invertible, with determinant $1$. Define
\[
\rho(n)=T^n
\qquad(n\in\mathbb Z).
\]
Then
\[
\rho(m+n)=T^{m+n}=T^mT^n=\rho(m)\rho(n),
\]
so $\rho$ is a representation of the additive group $\mathbb Z$.
:::

<1>2. The representation is reducible.
::: {.proof}
The line
\[
W=\mathbb C e_1
\]
is nonzero and proper, and
\[
Te_1=e_1.
\]
Thus $W$ is invariant under $T$, hence under every $T^n=\rho(n)$. Therefore $V$ has a proper nonzero $\mathbb Z$-submodule.
:::

<1>3. The representation is nevertheless indecomposable.
::: {.proof}
Suppose
\[
V=V_1\oplus V_2
\]
were a direct sum of two nonzero $\mathbb Z$-submodules. Since $\dim V=2$, both $V_1$ and $V_2$ would be one-dimensional and invariant under $T$. Thus each would be spanned by an eigenvector of $T$, giving a basis of eigenvectors of $T$. Hence $T$ would be diagonalizable.

But
\[
T-I=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}\ne0,
\qquad
(T-I)^2=0.
\]
Thus the minimal polynomial of $T$ is $(x-1)^2$, which has a repeated root, so $T$ is not diagonalizable. This contradiction shows that no such direct-sum decomposition exists.
:::

<1>4. Therefore an indecomposable complex representation of $\mathbb Z$ need not be irreducible.
::: {.proof}
The representation in <1>1 is reducible by <1>2 and indecomposable by <1>3.
:::
:::
