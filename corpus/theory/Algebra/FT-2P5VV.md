---
schema: qual/card@1
id: FT-2P5VV
kind: theorem
title: Eisenstein's criterion
prompts:
- State Eisenstein's criterion.
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
---

::: {.theorem}
Let $f(x)=\sum_{i=0}^na_ix^i\in\ZZ[x]$ with $n\ge1$, and let $p$ be a prime such that

- $p\nmid a_n$,

- $p\divides a_i$ for $0\le i\le n-1$, and

- $p^2\nmid a_0$.

Then $f$ is [[D-BVMTZ|irreducible]] in $\QQ[x]$.
:::

::: {.proof}
Suppose $f=gh$ with $g,h\in\QQ[x]$ nonconstant.
By [[FT-OXN3Y|Gauss' lemma]] we may take $g,h\in\ZZ[x]$ with $\deg g,\deg h\ge1$.
Reducing modulo $p$ gives $\overline g\,\overline h=\overline{a_n}x^n$ in $\FF_p[x]$ with $\overline{a_n}\ne0$.
The leading coefficients of $g$ and $h$ multiply to $a_n$, so neither is divisible by $p$, and $\deg\overline g=\deg g\ge1$, $\deg\overline h=\deg h\ge1$.
Since $\FF_p[x]$ is a unique factorization domain, $\overline g$ and $\overline h$ are nonzero multiples of positive powers of $x$, so $p$ divides the constant terms of $g$ and $h$.
Then $p^2$ divides their product $a_0$, a contradiction.
:::
