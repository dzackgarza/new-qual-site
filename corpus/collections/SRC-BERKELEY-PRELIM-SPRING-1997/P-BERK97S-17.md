---
schema: qual/card@1
id: P-BERK97S-17
kind: problem
title: Order of $GL_2(\ZZ/p^n\ZZ)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $GL_2(\mathbb Z_m)$ be the multiplicative group of invertible $2\times2$ matrices over the ring of integers modulo $m$. Find
\[
|GL_2(\mathbb Z_{p^n})|
\]
for every prime $p$ and positive integer $n$.
:::

::: {.solution}
Put
$$
R_n\coloneqq\ZZ/p^n\ZZ,
\qquad
k\coloneqq\FF_p,
$$
and let
$$
\rho:GL_2(R_n)\longrightarrow GL_2(k)
$$
be reduction modulo $p$.

<1>1. The reduction map $\rho$ is surjective.

::: {.proof}
Let $A\in GL_2(k)$ and lift its four entries arbitrarily to a matrix
$\widetilde A\in M_2(R_n)$. Since
$$
\det(\widetilde A)\bmod p=\det(A)\neq0,
$$
the element $\det(\widetilde A)\in R_n$ is not divisible by $p$, hence is a
unit of $R_n$. The adjugate formula then shows that $\widetilde A$ is
invertible over $R_n$. Thus $\rho(\widetilde A)=A$.
:::

<1>2. The kernel of $\rho$ has order
$$
\lvert\ker\rho\rvert=p^{4(n-1)}.
$$

::: {.proof}
An element of $\ker\rho$ is exactly a matrix of the form
$$
I+X,
\qquad
X\in M_2(pR_n).
$$
Conversely, every such matrix is invertible because
$$
\det(I+X)\equiv1\pmod p,
$$
so its determinant is a unit of $R_n$. Therefore the map
$$
M_2(pR_n)\longrightarrow\ker\rho,
\qquad
X\longmapsto I+X,
$$
is a bijection.

The ideal $pR_n$ has $p^{n-1}$ elements, including the case $n=1$, when
$pR_1=\{0\}$. Hence
$$
\lvert\ker\rho\rvert
=\lvert pR_n\rvert^4
=p^{4(n-1)}.
$$
:::

<1>3. The group $GL_2(k)$ has order
$$
\lvert GL_2(k)\rvert=(p^2-1)(p^2-p).
$$

::: {.proof}
The first column of an invertible $2\times2$ matrix over $k$ can be any
nonzero vector in $k^2$, giving $p^2-1$ choices. Once the first column is
chosen, the second column can be any vector outside its one-dimensional
span, giving $p^2-p$ choices. These choices are exactly the ordered bases of
$k^2$.
:::

<1>4. For every prime $p$ and positive integer $n$,
$$
\boxed{
\lvert GL_2(\ZZ/p^n\ZZ)\rvert
=p^{4(n-1)}(p^2-1)(p^2-p)
}.
$$

::: {.proof}
By steps <1>1 and <1>2, reduction modulo $p$ gives a short exact sequence
$$
1\longrightarrow\ker\rho
\longrightarrow GL_2(R_n)
\overset{\rho}{\longrightarrow}GL_2(k)
\longrightarrow1.
$$
Taking orders and applying steps <1>2 and <1>3 gives the displayed formula.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required order.
:::
:::
