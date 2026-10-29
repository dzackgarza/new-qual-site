---
schema: qual/card@1
id: E-OB3LO
kind: problem
title: $x^{\ell}-1$ divides $x^{m}-1$ if and only if $\ell$ divides $m$
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Factorization
  - Roots of Unity
relations: []
review: draft
---

::: {.exercise}
Show 
$$
x^\ell - 1 \divides x^m-1 \iff \ell\divides m
.$$
:::

::: {.solution}
Work in $\ZZ[x]$ with positive integers $\ell,m$, and write $m=\ell q+r$ with $0\le r<\ell$.

::: pf

::: {.pf-step #z-minus-one}
$x^\ell-1$ divides $x^{\ell q}-1$.

::: pf-proof
With $z=x^\ell$, one has $z^q-1=(z-1)(z^{q-1}+\cdots+z+1)$.
:::

:::

::: {.pf-step #remainder}
$x^m-1=x^r(x^{\ell q}-1)+(x^r-1)$.

::: pf-proof
Expand the right-hand side: $x^{\ell q+r}-x^r+x^r-1=x^m-1$.
:::

:::

::: pf-step
If $x^\ell-1\divides x^m-1$, then $\ell\divides m$.

::: pf-proof
By steps [](#z-minus-one){.pf-ref} and [](#remainder){.pf-ref}, $x^\ell-1$ divides $x^r-1$. Since $x^\ell-1$ is monic of degree $\ell>r\ge\deg(x^r-1)$, this forces $x^r-1=0$, so $r=0$ and $\ell\divides m$.
:::

:::

::: pf-step
If $\ell\divides m$, then $x^\ell-1\divides x^m-1$.

::: pf-proof
Then $r=0$, and $x^m-1=x^{\ell q}-1$ is divisible by $x^\ell-1$ by step [](#z-minus-one){.pf-ref}.
:::

:::

:::

:::
