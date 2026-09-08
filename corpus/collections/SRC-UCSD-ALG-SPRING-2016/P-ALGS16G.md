---
schema: qual/card@1
id: P-ALGS16G
kind: problem
title: Galois extension of $\mathbb{Q}$ with cyclic Galois group of order $4$
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

::: problem
Prove that there exists a Galois extension of $\mathbb{Q}$ whose Galois group is a cyclic group of order $4$.
:::


::: {.solution}
<1>1. Let $\zeta_5$ be a primitive fifth root of unity and set $K=\mathbf Q(\zeta_5)$.
::: {.proof}
The field $K$ is the splitting field over $\mathbf Q$ of the fifth cyclotomic polynomial
\[
\Phi_5(x)=x^4+x^3+x^2+x+1,
\]
so $K/\mathbf Q$ is Galois.
:::

<1>2. Every automorphism of $K/\mathbf Q$ is determined by
\[
\zeta_5\longmapsto\zeta_5^a,\qquad a\in(\mathbf Z/5\mathbf Z)^\times,
\]
and every such choice occurs.
::: {.proof}
The conjugates of $\zeta_5$ are exactly the primitive fifth roots $\zeta_5^a$ with $a$ invertible modulo $5$. The usual cyclotomic Galois action therefore gives an isomorphism
\[
\operatorname{Gal}(K/\mathbf Q)\cong(\mathbf Z/5\mathbf Z)^\times.
\]
:::

<1>3. The group $(\mathbf Z/5\mathbf Z)^\times$ is cyclic of order $4$.
::: {.proof}
Its four elements are $1,2,3,4$ modulo $5$, and $2$ has order $4$ because $2^2\equiv4\not\equiv1\pmod5$ while $2^4\equiv1\pmod5$.
:::

<1>4. Hence $K/\mathbf Q$ is a Galois extension with cyclic Galois group of order $4$.
::: {.proof}
Combine Steps <1>1--<1>3.
:::
:::
