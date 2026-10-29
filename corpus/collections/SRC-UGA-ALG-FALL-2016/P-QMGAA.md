---
schema: qual/card@1
id: P-QMGAA
kind: problem
title: Number of monic irreducibles of prime degree $\ell$ over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-11
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-11
---

::: {.problem}
How many monic irreducible polynomials over $\FF_p$ of prime degree $\ell$ are there?
Justify your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #irreducible-splits-completely}
Every monic irreducible polynomial of degree $\ell$ over $\FF_p$ splits completely in $\FF_{p^\ell}$, and each of its roots has degree exactly $\ell$ over $\FF_p$.

::: pf-proof
Let $f\in\FF_p[x]$ be monic irreducible of degree $\ell$, and let $\alpha$ be a root. Then
$$
[\FF_p(\alpha):\FF_p]=\ell,
$$
so $\FF_p(\alpha)$ has $p^\ell$ elements and is therefore isomorphic to $\FF_{p^\ell}$.
Finite fields are perfect, so $f$ is separable. Its roots are
$$
\alpha,\alpha^p,\ldots,\alpha^{p^{\ell-1}},
$$
all lying in $\FF_{p^\ell}$ and all distinct.
:::

:::

::: {.pf-step #element-degree-divides-ell}
An element $\alpha\in\FF_{p^\ell}$ has degree over $\FF_p$ dividing $\ell$.
Since $\ell$ is prime, its degree is either $1$ or $\ell$.

::: pf-proof
The field $\FF_p(\alpha)$ is an intermediate field
$$
\FF_p\subseteq\FF_p(\alpha)\subseteq\FF_{p^\ell}.
$$
By the tower law,
$$
[\FF_p(\alpha):\FF_p]\mid [\FF_{p^\ell}:\FF_p]=\ell.
$$
Because $\ell$ is prime, the only possibilities are $1$ and $\ell$.
:::

:::

::: pf-step
Exactly
$$
p^\ell-p
$$
elements of $\FF_{p^\ell}$ have degree $\ell$ over $\FF_p$.

::: pf-proof
By step [](#element-degree-divides-ell){.pf-ref}, the elements of degree less than $\ell$ are precisely those of degree $1$, namely the elements of the base field $\FF_p$.
There are $p$ such elements, while $\FF_{p^\ell}$ has $p^\ell$ elements in total. Hence the number of degree-$\ell$ elements is $p^\ell-p$.
:::

:::

::: pf-step
Each monic irreducible polynomial of degree $\ell$ contributes exactly $\ell$ of these elements, namely its distinct roots, and two distinct monic irreducibles have disjoint root sets.

::: pf-proof
By step [](#irreducible-splits-completely){.pf-ref}, an irreducible polynomial of degree $\ell$ has exactly $\ell$ distinct roots in $\FF_{p^\ell}$.
Conversely, every element of degree $\ell$ has a unique monic minimal polynomial over $\FF_p$, which is irreducible of degree $\ell$. Thus the degree-$\ell$ elements partition into root sets of size $\ell$ indexed by the monic irreducible polynomials of degree $\ell$.
:::

:::

::: pf-step
Therefore the number of monic irreducible polynomials of degree $\ell$ over $\FF_p$ is
$$
\boxed{\frac{p^\ell-p}{\ell}}.
$$

:::

:::

:::
