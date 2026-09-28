---
schema: qual/card@1
id: P-QSHZ6
kind: problem
title: Prime elements of $\ZZ[i]$
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Prime Ideals
  - Number Theory
relations: []
review: draft
---

::: {.problem}
Classify the prime elements of the Gaussian integers $\ZZ[i]$, up to multiplication by units.
:::

::: {.solution}
The units of $\ZZ[i]$ are
\[
\{\pm1,\pm i\}.
\]
Up to these units, the Gaussian primes are exactly the following.

<1>1. The ramified prime above $2$:
\[
1+i,
\]
with
\[
2=-i(1+i)^2.
\]

<1>2. Rational primes $p\equiv3\pmod4$.
::: {.proof}
Such a prime remains irreducible in $\ZZ[i]$. If it factored nontrivially, taking norms would write
\[
p^2=N(\alpha)N(\beta)
\]
with both norms greater than $1$, forcing one factor to have norm $p$. But
\[
a^2+b^2=p
\]
has no solution when $p\equiv3\pmod4$.
:::

<1>3. Gaussian integers $a+bi$ with both coordinates nonzero and
\[
a^2+b^2=p
\]
a rational prime.
::: {.proof}
Their norm is the rational prime $p$. Since the norm is multiplicative, any factorization would force one factor to have norm $1$, hence be a unit. Thus $a+bi$ is prime.
:::

For rational primes $p\equiv1\pmod4$, Fermat's two-squares theorem gives
\[
p=a^2+b^2=(a+bi)(a-bi),
\]
so $p$ itself is not Gaussian prime; the factors $a\pm bi$ are.

Equivalently, a nonunit $a+bi$ is Gaussian prime iff either
- one of $a,b$ is zero and the absolute value of the other is a rational prime congruent to $3\pmod4$, or
- both are nonzero and $a^2+b^2$ is a rational prime.
:::
