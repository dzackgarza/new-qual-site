---
schema: qual/card@1
id: P-L3WZM
kind: problem
title: $\GF(p^n)$ is the splitting field of $x^{p^n}-x$ over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Galois Theory
relations: []
review: draft
---

::: {.problem}
Show that $\GF(p^n)$ is the splitting field of $x^{p^n}-x$ over $\FF_p$.
:::

::: {.solution}
Let $q=p^n$, $f=x^q-x$, and fix an algebraic closure $\overline{\FF}_p$.

::: pf

::: {.pf-step #separable}
$f$ has $q$ distinct roots in $\overline{\FF}_p$.

::: pf-proof
$f'=qx^{q-1}-1=-1$, so $\gcd(f,f')=1$ and $f$ has no repeated root.
:::

:::

::: {.pf-step #roots-field}
The set $K$ of roots of $f$ is a subfield of $\overline{\FF}_p$ with $q$ elements.

::: pf-proof
$K$ is the fixed set of $\phi^n$, where $\phi(x)=x^p$ is the Frobenius endomorphism, and the fixed set of a field endomorphism is a subfield. It has $q$ elements by step [](#separable){.pf-ref}.
:::

:::

::: pf-step
$\GF(q)$ is the splitting field of $f$ over $\FF_p$.

::: pf-proof
By step [](#roots-field){.pf-ref}, $K$ is generated over $\FF_p$ by the roots of $f$, so it is a splitting field of $f$, and it has $q$ elements. Conversely, every field $F$ with $q$ elements satisfies $a^{q-1}=1$ for $a\in F^\times$, so every element of $F$ is a root of $f$; thus $F$ consists of the $q$ roots of $f$ and is a splitting field of $f$. Splitting fields are unique up to isomorphism, so $\GF(q)\cong K$.
:::

:::

:::

:::
