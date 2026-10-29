---
schema: qual/card@1
id: P-OVRL2
kind: problem
title: Finite integral domains are fields
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Fields
relations: []
review: draft
---

::: {.problem}
Show that every finite integral domain is a field.
:::

::: {.solution}
Let $R$ be a finite integral domain, let $0\ne a\in R$, and let
$$
\mu_a\colon R\to R,\qquad x\mapsto ax.
$$

::: pf

::: {.pf-step #bijective}

$\mu_a$ is bijective.

::: pf-proof

If $ax=ay$, then $a(x-y)=0$, so $x=y$ because $R$ has no zero divisors. An injective map from a finite set to itself is surjective.

:::

:::

::: pf-step

$a$ is invertible, so $R$ is a field.

::: pf-proof

By step [](#bijective){.pf-ref} there is $b\in R$ with $ab=\mu_a(b)=1$, and $ba=ab$ because $R$ is commutative.

:::

:::

:::

:::
