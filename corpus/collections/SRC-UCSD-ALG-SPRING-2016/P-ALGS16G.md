---
schema: qual/card@1
id: P-ALGS16G
kind: problem
title: Galois extension of $\QQ$ with cyclic Galois group of order $4$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Prove that there exists a Galois extension of $\QQ$ whose Galois group is a cyclic group of order $4$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\zeta_5$ be a primitive fifth root of unity and set $K=\QQ(\zeta_5)$.

::: pf-proof

The field $K$ is the splitting field over $\QQ$ of the fifth cyclotomic polynomial
$$
\Phi_5(x)=x^4+x^3+x^2+x+1,
$$
so $K/\QQ$ is Galois.

:::

:::

::: {.pf-step #s2}

Every automorphism of $K/\QQ$ is determined by
$$
\zeta_5\longmapsto\zeta_5^a,\qquad a\in(\ZZ/5\ZZ)^\times,
$$
and every such choice occurs.

::: pf-proof

The conjugates of $\zeta_5$ are exactly the primitive fifth roots $\zeta_5^a$ with $a$ invertible modulo $5$. The usual cyclotomic Galois action therefore gives an isomorphism
$$
\operatorname{Gal}(K/\QQ)\cong(\ZZ/5\ZZ)^\times.
$$

:::

:::

::: {.pf-step #s3}

The group $(\ZZ/5\ZZ)^\times$ is cyclic of order $4$.

::: pf-proof

Its four elements are $1,2,3,4$ modulo $5$, and $2$ has order $4$ because $2^2\equiv4\not\equiv1\pmod5$ while $2^4\equiv1\pmod5$.

:::

:::

::: pf-step

Hence $K/\QQ$ is a Galois extension with cyclic Galois group of order $4$.

::: pf-proof

Combine Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
