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
Let $\alpha,\beta\in\mathbb C$ be algebraic over $\mathbb Q$.

::: pf

::: {.pf-step #first-finite-extension}
The field extension $\mathbb Q(\alpha)/\mathbb Q$ is finite.

::: pf-proof
Since $\alpha$ is algebraic, it has a nonzero minimal polynomial over $\mathbb Q$ of finite degree. The standard basis theorem for a simple algebraic extension gives
$$
[\mathbb Q(\alpha):\mathbb Q]<\infty.
$$
:::

:::

::: {.pf-step #algebraic-over-intermediate-field}
The number $\beta$ is algebraic over $\mathbb Q(\alpha)$.

::: pf-proof
There is a nonzero polynomial
$$
p(x)\in\mathbb Q[x]
$$
with $p(\beta)=0$. Since
$$
\mathbb Q[x]\subseteq\mathbb Q(\alpha)[x],
$$
the same polynomial witnesses that $\beta$ is algebraic over $\mathbb Q(\alpha)$.
:::

:::

::: {.pf-step #composite-finite-extension}
The extension
$$
\mathbb Q(\alpha,\beta)/\mathbb Q
$$
is finite.

::: pf-proof
[](#algebraic-over-intermediate-field){.pf-ref} gives
$$
[\mathbb Q(\alpha,\beta):\mathbb Q(\alpha)]<\infty.
$$
Combining this with [](#first-finite-extension){.pf-ref} and the tower law,
$$
[\mathbb Q(\alpha,\beta):\mathbb Q]
=
[\mathbb Q(\alpha,\beta):\mathbb Q(\alpha)]
[\mathbb Q(\alpha):\mathbb Q]
<\infty.
$$
:::

:::

::: {.pf-step #finite-implies-algebraic}
Every element of a finite extension of $\mathbb Q$ is algebraic over $\mathbb Q$.

::: pf-proof
Let $L/\mathbb Q$ be finite and let $\gamma\in L$. If
$$
d=[L:\mathbb Q],
$$
then the $d+1$ elements
$$
1,\gamma,\gamma^2,\ldots,\gamma^d
$$
are linearly dependent over $\mathbb Q$. Hence there are rational coefficients, not all zero, such that
$$
c_0+c_1\gamma+\cdots+c_d\gamma^d=0.
$$
Thus $\gamma$ is a root of a nonzero polynomial in $\mathbb Q[x]$.
:::

:::

::: pf-step
The sum $\alpha+\beta$ is algebraic.

::: pf-proof
One has
$$
\alpha+\beta\in\mathbb Q(\alpha,\beta).
$$
The field on the right is finite over $\mathbb Q$ by [](#composite-finite-extension){.pf-ref}, so [](#finite-implies-algebraic){.pf-ref} applies.
:::

:::

:::

:::
