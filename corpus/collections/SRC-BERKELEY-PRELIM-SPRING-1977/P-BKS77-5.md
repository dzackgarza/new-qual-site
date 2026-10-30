---
schema: qual/card@1
id: P-BKS77-5
kind: problem
title: The sum of two elements algebraic over a field is algebraic
classification: {areas: [prelim], topics: [Abstract Algebra]}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let $F\subset K$ be fields and let $a,b\in K$ be algebraic over $F$.
Show that $a+b$ is algebraic over $F$.
:::

::: {.solution}
::: pf

::: {.pf-step #first-finite-extension}
The extension $F(a)/F$ is finite.

::: pf-proof
Since $a$ is algebraic over $F$, its minimal polynomial over $F$ has finite degree. Therefore
$$
[F(a):F]<\infty.
$$
:::

:::

::: {.pf-step #algebraic-over-intermediate-field}
The element $b$ is algebraic over $F(a)$.

::: pf-proof
Because $b$ is algebraic over $F$, there is a nonzero polynomial
$$
p(x)\in F[x]
$$
with $p(b)=0$. Since
$$
F[x]\subseteq F(a)[x],
$$
the same polynomial shows that $b$ is algebraic over $F(a)$.
:::

:::

::: {.pf-step #composite-finite-extension}
The extension $F(a,b)/F$ is finite.

::: pf-proof
By [](#algebraic-over-intermediate-field){.pf-ref},
$$
[F(a,b):F(a)]<\infty.
$$
Together with [](#first-finite-extension){.pf-ref}, the tower law gives
$$
[F(a,b):F]
=
[F(a,b):F(a)]\,[F(a):F]
<\infty.
$$
:::

:::

::: {.pf-step #finite-implies-algebraic}
Every element of $F(a,b)$ is algebraic over $F$.

::: pf-proof
Let $L/F$ be any finite extension and let $x\in L$. The vectors
$$
1,x,x^2,\ldots,x^{[L:F]}
$$
lie in the finite-dimensional $F$-vector space $L$, so they are linearly dependent over $F$. Thus there exist coefficients, not all zero,
$$
c_0,\ldots,c_m\in F
$$
such that
$$
c_0+c_1x+\cdots+c_mx^m=0.
$$
Hence $x$ is algebraic over $F$. Apply this with $L=F(a,b)$, which is finite by [](#composite-finite-extension){.pf-ref}.
:::

:::

::: pf-step
The element $a+b$ is algebraic over $F$.

::: pf-proof
One has
$$
a+b\in F(a,b).
$$
Apply [](#finite-implies-algebraic){.pf-ref}.
:::

:::

:::

:::
