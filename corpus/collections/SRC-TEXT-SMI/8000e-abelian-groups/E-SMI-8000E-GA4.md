---
schema: qual/card@1
id: E-SMI-8000E-GA4
kind: problem
title: Hom from a free abelian group into Q is a rational vector space of the same rank
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Hom and Duality
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Prove that $\Hom(\ZZ^s, \QQ)$ is isomorphic as a $\QQ$-vector space to $\QQ^s$, by sending the map $f: \ZZ^s \to \QQ$ to the vector $(f(e_1), \ldots, f(e_s))$ — where we multiply maps by rational numbers by multiplying their values, to make $\Hom(\ZZ^s, \QQ)$ into a $\QQ$-vector space.
[Hint: one proof would be to find a $\QQ$-basis for $\Hom(\ZZ^s, \QQ)$ consisting of exactly $s$ elements.]
:::

::: {.solution}
Let $e_1, \ldots, e_s$ be the standard basis of $\ZZ^s$, and define $\Phi\colon \Hom(\ZZ^s, \QQ) \to \QQ^s$ by $\Phi(f) = (f(e_1), \ldots, f(e_s))$.

::: pf

::: {.pf-step #s1}

$\Phi$ is $\QQ$-linear.

::: pf-proof

Addition and rational scalar multiplication of homomorphisms are pointwise, so $\Phi(f + g) = (f(e_1) + g(e_1), \ldots, f(e_s) + g(e_s)) = \Phi(f) + \Phi(g)$ and $\Phi(qf) = (qf(e_1), \ldots, qf(e_s)) = q\Phi(f)$ for $q \in \QQ$.

:::

:::

::: {.pf-step #s2}

$\Phi$ is injective.

::: pf-proof

If $\Phi(f) = 0$, then $f(e_i) = 0$ for all $i$; since $e_1, \ldots, e_s$ generate $\ZZ^s$, $f = 0$.

:::

:::

::: {.pf-step #s3}

$\Phi$ is surjective.

::: pf-proof

Given $(q_1, \ldots, q_s) \in \QQ^s$, define $f\colon \ZZ^s \to \QQ$ by $f(\sum_i n_i e_i) = \sum_i n_i q_i$. Since $e_1, \ldots, e_s$ is a basis, $f$ is a well-defined homomorphism, and $\Phi(f) = (q_1, \ldots, q_s)$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}, $\Phi$ is a $\QQ$-linear isomorphism $\Hom(\ZZ^s, \QQ) \cong \QQ^s$.

:::

:::

:::
