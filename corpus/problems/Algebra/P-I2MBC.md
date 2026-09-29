---
schema: qual/card@1
id: P-I2MBC
kind: problem
title: $\ZZ/p\ZZ\otimes\ZZ/q\ZZ$ for distinct primes $p$ and $q$
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Abelian Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Now we'll take the tensor product of two abelian groups, that is, $\ZZ\dash$modules.
Take $\ZZ/p\ZZ$ and $\ZZ/q\ZZ$, where $p$ and $q$ are distinct primes.
What is their tensor product?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$\ZZ/p\otimes\ZZ/q=0$ for $p\neq q$.

::: pf-proof

$a\otimes b = p(a/p)\otimes b = a\otimes pb = a\otimes0=0$ using $p$ invertible mod $q$; more directly $1\otimes1 = q(1\otimes1/q)=0$ and $p(1\otimes1)=0$, so $\gcd(p,q)=1$ gives $1\otimes1=0$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref}.

:::

:::

:::
