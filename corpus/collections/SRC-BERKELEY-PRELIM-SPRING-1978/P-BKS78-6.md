---
schema: qual/card@1
id: P-BKS78-6
kind: problem
title: The sum of two algebraic numbers is algebraic
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Prove that the sum of two algebraic numbers is algebraic.
Here an algebraic number means a complex root of a polynomial with rational coefficients.
:::

::: {.solution}
Let $\alpha,\beta\in\CC$ be algebraic over $\QQ$.

::: pf

::: {.pf-step #first-finite-extension}
The field extension $\QQ(\alpha)/\QQ$ is finite.

::: pf-proof
Since $\alpha$ is algebraic, it has a nonzero minimal polynomial over $\QQ$ of finite degree. The standard basis theorem for a simple algebraic extension gives
$$
[\QQ(\alpha):\QQ]<\infty.
$$
:::

:::

::: {.pf-step #algebraic-over-intermediate-field}
The number $\beta$ is algebraic over $\QQ(\alpha)$.

::: pf-proof
There is a nonzero polynomial
$$
p(x)\in\QQ[x]
$$
with $p(\beta)=0$. Since
$$
\QQ[x]\subseteq\QQ(\alpha)[x],
$$
the same polynomial witnesses that $\beta$ is algebraic over $\QQ(\alpha)$.
:::

:::

::: {.pf-step #composite-finite-extension}
The extension
$$
\QQ(\alpha,\beta)/\QQ
$$
is finite.

::: pf-proof
[](#algebraic-over-intermediate-field){.pf-ref} gives
$$
[\QQ(\alpha,\beta):\QQ(\alpha)]<\infty.
$$
Combining this with [](#first-finite-extension){.pf-ref} and the tower law,
$$
[\QQ(\alpha,\beta):\QQ]
=
[\QQ(\alpha,\beta):\QQ(\alpha)]
[\QQ(\alpha):\QQ]
<\infty.
$$
:::

:::

::: {.pf-step #finite-implies-algebraic}
Every element of a finite extension of $\QQ$ is algebraic over $\QQ$.

::: pf-proof
Let $L/\QQ$ be finite and let $\gamma\in L$. If
$$
d=[L:\QQ],
$$
then the $d+1$ elements
$$
1,\gamma,\gamma^2,\ldots,\gamma^d
$$
are linearly dependent over $\QQ$. Hence there are rational coefficients, not all zero, such that
$$
c_0+c_1\gamma+\cdots+c_d\gamma^d=0.
$$
Thus $\gamma$ is a root of a nonzero polynomial in $\QQ[x]$.
:::

:::

::: pf-step
The sum $\alpha+\beta$ is algebraic.

::: pf-proof
One has
$$
\alpha+\beta\in\QQ(\alpha,\beta).
$$
The field on the right is finite over $\QQ$ by [](#composite-finite-extension){.pf-ref}, so [](#finite-implies-algebraic){.pf-ref} applies.
:::

:::

:::

:::
