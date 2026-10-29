---
schema: qual/card@1
id: P-Y4XPA
kind: problem
title: The ring of arithmetic functions under Dirichlet convolution
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Convolution
  - Number Theory
relations: []
review: draft
---

::: {.problem}
Let $\mathcal A$ be the set of functions $f:\NN\to\CC$, with pointwise addition and Dirichlet convolution
$$
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d).
$$
Show that $\mathcal A$ is a commutative ring. What further structure can be described?
:::

::: {.solution}
Here $\NN=\{1,2,3,\ldots\}$, and $\delta_1$ is the function with $\delta_1(1)=1$ and $\delta_1(n)=0$ for $n>1$.

::: pf

::: {.pf-step #ring}
$\mathcal A$ is a commutative ring with identity $\delta_1$.

::: pf-proof
Pointwise addition makes $\mathcal A$ an abelian group, and $*$ distributes over it term by term.
Replacing each divisor $d$ of $n$ by $n/d$ gives $f*g=g*f$.
Both $((f*g)*h)(n)$ and $(f*(g*h))(n)$ equal $\sum_{abc=n}f(a)g(b)h(c)$, so $*$ is associative.
Finally $(f*\delta_1)(n)=f(n)$, since only $d=n$ contributes.
:::

:::

::: pf-step
$f$ is a unit of $\mathcal A$ if and only if $f(1)\ne0$.

::: pf-proof
If $f*g=\delta_1$, then $f(1)g(1)=1$.
Conversely, if $f(1)\ne0$, define $g(1)=f(1)^{-1}$ and, recursively for $n>1$, $g(n)=-f(1)^{-1}\sum_{d\mid n,\,d>1}f(d)g(n/d)$; this is exactly the condition $(f*g)(n)=\delta_1(n)$.
:::

:::

::: pf-step
The map sending $f$ to the formal Dirichlet series $\sum_{n\ge1}f(n)n^{-s}$ is a ring isomorphism onto formal Dirichlet series, and products of absolutely convergent Dirichlet series are computed by $*$.

::: pf-proof
Collecting the terms of $\left(\sum_a f(a)a^{-s}\right)\left(\sum_b g(b)b^{-s}\right)$ with $ab=n$ gives coefficient $(f*g)(n)$; under absolute convergence the rearrangement is valid.
:::

:::

:::

:::
