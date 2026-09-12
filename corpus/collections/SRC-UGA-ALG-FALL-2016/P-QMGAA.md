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

::: problem
How many monic irreducible polynomials over $\FF_p$ of prime degree $\ell$ are there?
Justify your answer.
:::

::: {.solution}
<1>1. Every monic irreducible polynomial of degree $\ell$ over $\mathbb F_p$ splits completely in $\mathbb F_{p^\ell}$, and each of its roots has degree exactly $\ell$ over $\mathbb F_p$.
::: {.proof}
Let $f\in\mathbb F_p[x]$ be monic irreducible of degree $\ell$, and let $\alpha$ be a root. Then
\[
[\mathbb F_p(\alpha):\mathbb F_p]=\ell,
\]
so $\mathbb F_p(\alpha)$ has $p^\ell$ elements and is therefore isomorphic to $\mathbb F_{p^\ell}$.
Finite fields are perfect, so $f$ is separable. Its roots are
\[
\alpha,\alpha^p,\ldots,\alpha^{p^{\ell-1}},
\]
all lying in $\mathbb F_{p^\ell}$ and all distinct.
:::

<1>2. An element $\alpha\in\mathbb F_{p^\ell}$ has degree over $\mathbb F_p$ dividing $\ell$.
Since $\ell$ is prime, its degree is either $1$ or $\ell$.
::: {.proof}
The field $\mathbb F_p(\alpha)$ is an intermediate field
\[
\mathbb F_p\subseteq\mathbb F_p(\alpha)\subseteq\mathbb F_{p^\ell}.
\]
By the tower law,
\[
[\mathbb F_p(\alpha):\mathbb F_p]\mid [\mathbb F_{p^\ell}:\mathbb F_p]=\ell.
\]
Because $\ell$ is prime, the only possibilities are $1$ and $\ell$.
:::

<1>3. Exactly
\[
p^\ell-p
\]
elements of $\mathbb F_{p^\ell}$ have degree $\ell$ over $\mathbb F_p$.
::: {.proof}
By <1>2, the elements of degree less than $\ell$ are precisely those of degree $1$, namely the elements of the base field $\mathbb F_p$.
There are $p$ such elements, while $\mathbb F_{p^\ell}$ has $p^\ell$ elements in total. Hence the number of degree-$\ell$ elements is $p^\ell-p$.
:::

<1>4. Each monic irreducible polynomial of degree $\ell$ contributes exactly $\ell$ of these elements, namely its distinct roots, and two distinct monic irreducibles have disjoint root sets.
::: {.proof}
By <1>1, an irreducible polynomial of degree $\ell$ has exactly $\ell$ distinct roots in $\mathbb F_{p^\ell}$.
Conversely, every element of degree $\ell$ has a unique monic minimal polynomial over $\mathbb F_p$, which is irreducible of degree $\ell$. Thus the degree-$\ell$ elements partition into root sets of size $\ell$ indexed by the monic irreducible polynomials of degree $\ell$.
:::

<1>5. Therefore the number of monic irreducible polynomials of degree $\ell$ over $\mathbb F_p$ is
\[
\boxed{\frac{p^\ell-p}{\ell}}.
\]
:::
:::
