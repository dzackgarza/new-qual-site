---
schema: qual/card@1
id: P-BKS77-5
kind: problem
title: The sum of two elements algebraic over a field is algebraic
classification: {areas: [prelim], topics: []}
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
<1>1. The extension $F(a)/F$ is finite.

::: {.proof}
Since $a$ is algebraic over $F$, its minimal polynomial over $F$ has finite degree. Therefore
$$
[F(a):F]<\infty.
$$
:::

<1>2. The element $b$ is algebraic over $F(a)$.

::: {.proof}
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

<1>3. The extension $F(a,b)/F$ is finite.

::: {.proof}
By step <1>2,
$$
[F(a,b):F(a)]<\infty.
$$
Together with step <1>1, the tower law gives
$$
[F(a,b):F]
=
[F(a,b):F(a)]\,[F(a):F]
<\infty.
$$
:::

<1>4. Every element of $F(a,b)$ is algebraic over $F$.

::: {.proof}
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
Hence $x$ is algebraic over $F$. Apply this with $L=F(a,b)$, which is finite by step <1>3.
:::

<1>5. The element $a+b$ is algebraic over $F$.

::: {.proof}
One has
$$
a+b\in F(a,b).
$$
Apply step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
