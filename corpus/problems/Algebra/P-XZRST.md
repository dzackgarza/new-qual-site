---
schema: qual/card@1
id: P-XZRST
kind: problem
title: Whether $L^1$ has a natural multiplication making it an algebra
classification:
  areas:
  - algebra
  topics:
  - Convolution
  - Algebras
  - Function Spaces
relations: []
review: draft
---

::: {.problem}
Does $L^1$ have a natural multiplication making it an algebra? Distinguish pointwise multiplication on a general measure space from convolution on a locally compact group.
:::

::: {.solution}
The multiplication depends on the structure underlying $L^1$: a measure space alone, or a locally compact group with Haar measure.

::: pf

::: pf-step
Pointwise multiplication does not make a general $L^1(X,\mu)$ an algebra.

::: pf-proof
On $(0,1)$ with Lebesgue measure, $f(x)=x^{-2/3}$ lies in $L^1(0,1)$, but $f(x)^2=x^{-4/3}\notin L^1(0,1)$.
Pointwise multiplication does make $L^1\cap L^\infty$ an algebra, since $\norm{fg}_1\le\norm{f}_1\norm{g}_\infty$ and $\norm{fg}_\infty\le\norm{f}_\infty\norm{g}_\infty$.
:::

:::

::: pf-step
For a locally compact group $G$ with left Haar measure, $L^1(G)$ is a Banach algebra under convolution $(f*g)(x)=\int_G f(y)g(y^{-1}x)\,dy$; it is commutative when $G$ is abelian, and it is $\ell^1(G)$ when $G$ is discrete.

::: pf-proof
By Tonelli and left invariance of Haar measure, $\int_G\int_G\abs{f(y)}\abs{g(y^{-1}x)}\,dx\,dy=\norm{f}_1\norm{g}_1$, so $f*g$ is defined almost everywhere, lies in $L^1(G)$, and $\norm{f*g}_1\le\norm{f}_1\norm{g}_1$.
Associativity follows from Fubini, which is justified by the same absolute bound, and bilinearity is clear.
If $G$ is abelian, the substitution $y\mapsto xy^{-1}$, which preserves Haar measure on an abelian group, gives $f*g=g*f$.
On a discrete group with counting measure the integral is the sum $\sum_y f(y)g(y^{-1}x)$.
:::

:::

:::

:::
