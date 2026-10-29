---
schema: qual/card@1
id: P-BKS77-7
kind: problem
title: Vandermonde invertibility and polynomial interpolation
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let
$$
V=\begin{pmatrix}
1&a_0&a_0^2&\cdots&a_0^n\\
1&a_1&a_1^2&\cdots&a_1^n\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&a_n&a_n^2&\cdots&a_n^n
\end{pmatrix}.
$$

1. Prove that $V$ is invertible if $a_0,\ldots,a_n$ are distinct.
2. If the $a_i$ are distinct and $b_0,\ldots,b_n\in\CC$, prove that there is a unique complex polynomial $f$ of degree at most $n$ satisfying $f(a_i)=b_i$ for all $i$.
:::

::: {.solution}
::: pf

::: {.pf-step #kernel-polynomial}
If
$$
Vc=0,
\qquad
c=(c_0,\ldots,c_n)^T,
$$
then the polynomial
$$
p(x)\coloneqq
\sum_{j=0}^n c_jx^j
$$
satisfies
$$
p(a_i)=0
$$
for every $i=0,\ldots,n$.

::: pf-proof
The $i$-th row of the equation $Vc=0$ is
$$
c_0+c_1a_i+c_2a_i^2+\cdots+c_na_i^n=0,
$$
which is exactly $p(a_i)=0$.
:::

:::

::: {.pf-step #trivial-kernel}
If the numbers $a_0,\ldots,a_n$ are distinct, then
$$
\ker V=\{0\}.
$$

::: pf-proof
Let $c\in\ker V$ and define $p$ as in [](#kernel-polynomial){.pf-ref}. Then $p$ has the $n+1$ distinct roots
$$
a_0,\ldots,a_n.
$$
But $\deg p\leq n$. A nonzero polynomial of degree at most $n$ has at most $n$ roots, so $p$ must be the zero polynomial. Hence
$$
c_0=\cdots=c_n=0.
$$
:::

:::

::: {.pf-step #vandermonde-invertible}
Under the distinctness hypothesis,
$$
\boxed{V\text{ is invertible}}.
$$

::: pf-proof
The matrix $V$ is square of size $n+1$. [](#trivial-kernel){.pf-ref} shows that the associated linear map has trivial kernel, hence is injective. A linear endomorphism of a finite-dimensional vector space is injective if and only if it is invertible.
:::

:::

::: {.pf-step #evaluation-map}
Let
$$
\mathcal P_n
\coloneqq
\{f\in\CC[x]:\deg f\leq n\}.
$$
The evaluation map
$$
E:\mathcal P_n\longrightarrow\CC^{n+1},
\qquad
E(f)=\bigl(f(a_0),\ldots,f(a_n)\bigr),
$$
has matrix $V$ in the basis
$$
1,x,\ldots,x^n
$$
of $\mathcal P_n$.

::: pf-proof
If
$$
f(x)=c_0+c_1x+\cdots+c_nx^n,
$$
then
$$
E(f)
=
V
\begin{pmatrix}
c_0\\
c_1\\
\vdots\\
c_n
\end{pmatrix}.
$$
This is exactly the matrix representation of $E$ in the stated bases.
:::

:::

::: pf-step
For every
$$
(b_0,\ldots,b_n)\in\CC^{n+1},
$$
there is a unique polynomial $f\in\mathcal P_n$ such that
$$
f(a_i)=b_i
\qquad
(0\leq i\leq n).
$$

::: pf-proof
By [](#vandermonde-invertible){.pf-ref}, the matrix $V$ is invertible, so the linear map $E$ in [](#evaluation-map){.pf-ref} is bijective. Hence the vector
$$
(b_0,\ldots,b_n)
$$
has exactly one preimage $f\in\mathcal P_n$.
:::

:::

:::

:::
