---
title: The Galois correspondence
order: 10
topics:
- Galois Theory
- Irreducibility Criteria
---

# The Galois correspondence

## Galois extensions

[[D-5JYEI]]

[[FD-YJEDU]]

[[FE-Z4VF2]]

[[PR-QDRB4]]

## The fundamental theorem

[[T-NLPZY]]

[[T-SGY3O]]

[[PR-FM5FN]]

## Criteria for Galois extensions

**Irreducibility of $f\in\QQ[x]$.** Apply [[T-CF6S3|Eisenstein's criterion]] to $f(x)$, to $f(x+a)$ for some $a\in\ZZ$, or to the reversed polynomial $x^nf(1/x)$. If $f\in\ZZ[x]$ has leading coefficient prime to $p$ and $f\bmod p$ is irreducible over $\FF_p$, then $f$ is irreducible over $\QQ$. A polynomial of degree $2$ or $3$ is irreducible if and only if it has no root.

**Separability.** [[PR-TLBPS|The derivative detects separability]]; [[PR-25FLW|algebraic extensions of perfect fields are separable]]; [[PR-3VQBI|characterizations of separability for finite extensions]]; separable extensions form a [[D-JMATC|distinguished class]].

**Normality.** [[PR-TZN4M|Finite normal extensions are splitting fields]].

**Galois.** [[D-5JYEI|Galois extension]]; [[PR-ZCKLJ|separable splitting fields are Galois]]. Every finite extension of finite fields is Galois: $\FF_{p^n}$ is the splitting field of the separable polynomial $x^{p^n}-x$ over every subfield.

## Irreducibility

[[PR-PB6UE]]

::: {.remark}
Over a finite field $\FF_p$, a polynomial of degree $d$ is irreducible if and only if it has no monic irreducible factor of degree at most $d/2$, which can be checked by dividing by each monic irreducible polynomial of degree at most $d/2$.
:::

::: {.example title="Irreducibility modulo $2$"}
$f(x) \definedas x^4 + x + 1$ is irreducible over $\QQ$.
Modulo $2$, $f(0)=f(1)=1$, so $f$ has no linear factor, and the only monic irreducible quadratic over $\FF_2$ is $x^2+x+1$, which leaves remainder $1$ on dividing $f$; hence $f$ is irreducible over $\FF_2$.
:::

[[T-CF6S3]]

::: {.remark title="Shifting"}
For $a\in\ZZ$, $g(x)\mapsto g(x+a)$ is a ring automorphism of $\QQ[x]$, so if $f(x+a)$ satisfies Eisenstein's criterion at $p$, then $f$ is irreducible.
For monic $f$ of degree $n\geq2$, in that case $f(x+a)\equiv x^n \pmod p$, so $f \bmod p$ has a repeated root, and $p$ divides $\Delta_f = \Delta_{f(x+a)}$; the primes to test are among the prime divisors of the discriminant.
:::

[[T-AILFB]]
