---
schema: qual/card@1
id: D-KQFIV
kind: definition
title: Perfect fields
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

::: {.definition}
A field $k$ is \dfn{perfect} if either $k$ has [[D-JNCUB|characteristic]] $0$, or $k$ has characteristic $p>0$ and the Frobenius map $k\to k$, $a\mapsto a^p$, is surjective, that is, $k^p = k$.
:::

::: {.proposition}
For a field $k$, the following are equivalent:

1. $k$ is perfect;

2. every irreducible polynomial in $k[x]$ is [[D-ZT46D|separable]];

3. every finite extension $F/k$ is [[D-JGYLA|separable]].
:::

::: {.proof}
An irreducible $f\in k[x]$ has a repeated root if and only if $\gcd(f,f')\neq 1$, which for irreducible $f$ happens if and only if $f'=0$.
In characteristic $0$ this never happens for nonconstant $f$, so (1), (2), and (3) all hold.

Let $\characteristic k=p>0$.
If $k^p=k$ and $f'=0$, then $f(x)=\sum_i a_ix^{pi}$ with $a_i=b_i^p$ for some $b_i\in k$, so $f=\bigl(\sum_i b_ix^i\bigr)^p$ is not irreducible; hence (1) implies (2).
If $a\in k\setminus k^p$, then $x^p-a$ is irreducible over $k$ and equals $(x-\alpha)^p$ over a splitting field, where $\alpha^p=a$, so it is not separable; hence (2) implies (1).
Finally, (2) implies (3) because the minimal polynomial of each element of $F$ is irreducible over $k$, and (3) implies (2) because a root $\alpha$ of an irreducible $f$ generates the finite extension $k(\alpha)/k$, in which $\alpha$ is separable exactly when $f$ is separable.
:::
