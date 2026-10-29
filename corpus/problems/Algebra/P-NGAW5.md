---
schema: qual/card@1
id: P-NGAW5
kind: problem
title: Eisenstein's criterion
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
State and prove Eisenstein's criterion.
:::

::: {.solution}
Bars denote reduction modulo $p$, from $\ZZ[x]$ to $\FF_p[x]$.

::: pf

::: pf-step
Eisenstein's criterion: let $f(x)=a_nx^n+\cdots+a_1x+a_0\in\ZZ[x]$ with $n\ge1$, and let $p$ be a prime with $p\nmid a_n$, $p\mid a_i$ for $0\le i<n$, and $p^2\nmid a_0$.
Then $f$ is irreducible in $\QQ[x]$.

::: pf-proof

::: {.pf-step #gauss}
If $f$ is reducible in $\QQ[x]$, then $f=gh$ with $g,h\in\ZZ[x]$ of degrees $r,s\ge1$.

::: pf-proof
This is Gauss's lemma.
:::

:::

::: {.pf-step #reduce}
In such a factorization, $\bar g=cx^r$ and $\bar h=dx^s$ with $c,d\in\FF_p$ nonzero.

::: pf-proof
The leading coefficients of $g$ and $h$ multiply to $a_n$, which $p$ does not divide, so $\deg\bar g=r$ and $\deg\bar h=s$.
By hypothesis $\bar f=\bar a_nx^n$, and $\bar g\bar h=\bar f$; since $\FF_p[x]$ is a UFD and $x$ is irreducible, the divisors of $\bar a_nx^n$ are unit multiples of powers of $x$.
:::

:::

::: pf-step
$f$ is irreducible in $\QQ[x]$.

::: pf-proof
Otherwise take $g,h$ as in step [](#gauss){.pf-ref}.
By step [](#reduce){.pf-ref} and $r,s\ge1$, $p$ divides the constant terms of $g$ and of $h$, so $p^2$ divides their product $a_0$, contrary to the hypothesis.
:::

:::

:::

:::

:::

:::
