---
schema: qual/card@1
id: P-T7W8G
kind: problem
title: Irreducible polynomials over a field in which every element has a $p$th root are separable
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.problem}
Let $F$ be a field of characteristic $p>0$ such that every element of $F$ has a $p$th root in $F$. Show that every irreducible polynomial in $F[x]$ is separable.
:::

::: {.solution}
Let $f\in F[x]$ be irreducible, and suppose for contradiction that $f$ is inseparable.

::: pf

::: {.pf-step #derivative}
$f'=0$.

::: pf-proof
Since $f$ is irreducible and has a repeated root, $\gcd(f,f')$ is a nonconstant divisor of $f$, so $\gcd(f,f')=f$ up to a unit.
Thus $f$ divides $f'$, and since $\deg f'<\deg f$, this forces $f'=0$.
:::

:::

::: {.pf-step #p-power}
$f=g^p$ for a nonconstant $g\in F[x]$.

::: pf-proof
In characteristic $p$, $f'=0$ exactly when every exponent occurring in $f$ is divisible by $p$, so by step [](#derivative){.pf-ref} $f(x)=\sum_i a_i x^{pi}$ with $a_i\in F$.
By hypothesis $a_i=b_i^p$ for some $b_i\in F$, and the Frobenius identity in characteristic $p$ gives
$$
f(x)=\sum_i b_i^p x^{pi}=\Bigl(\sum_i b_i x^i\Bigr)^p.
$$
Since $f$ is nonconstant, $g=\sum_i b_i x^i$ is nonconstant.
:::

:::

::: pf-step
$f$ is separable.

::: pf-proof
By step [](#p-power){.pf-ref}, $f=g\cdot g^{p-1}$ with both factors nonconstant, which contradicts the irreducibility of $f$.
:::

:::

:::

:::
