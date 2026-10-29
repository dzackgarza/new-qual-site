---
schema: qual/card@1
id: P-5KZDX
kind: problem
title: Finite fields are perfect
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Finite Fields
relations: []
review: draft
---

::: {.problem}
Define a perfect field. Prove that every finite field is perfect.
:::

::: {.solution}
Let $F$ be a finite field of characteristic $p>0$.

::: pf

::: pf-step
A field $F$ is a [[D-KQFIV|perfect field]] if every irreducible polynomial in $F[x]$ is separable.

::: pf-proof
This is the definition.
:::

:::

::: {.pf-step #frobenius-onto}
Every $a\in F$ has a $p$th root in $F$.

::: pf-proof
The Frobenius map $a\mapsto a^p$ is a ring homomorphism $F\to F$, and it is injective because $F$ is a field. An injective map from the finite set $F$ to itself is surjective.
:::

:::

::: pf-step
Every irreducible $f\in F[x]$ is separable, so $F$ is perfect.

::: pf-proof
Suppose $f$ is irreducible and inseparable. Then $\gcd(f,f')\ne1$, and irreducibility forces $f'=0$, so every exponent in $f$ is divisible by $p$ and $f(x)=\sum_i a_i x^{pi}$. By step [](#frobenius-onto){.pf-ref}, choose $b_i\in F$ with $b_i^p=a_i$. In characteristic $p$,
$$
f(x)=\left(\sum_i b_i x^i\right)^p,
$$
which is reducible because $f$ is nonconstant. This contradicts irreducibility.
:::

:::

:::

:::
