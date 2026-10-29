---
schema: qual/card@1
id: PR-LLBRB
kind: proposition
title: Inclusions among fields, Euclidean domains, PIDs, UFDs, and integral domains
slogan: 'Field implies Euclidean implies PID implies UFD implies domain, with every implication strict.'
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Integral Domains
  - Factorization
relations: []
review: draft
---

::: {.proposition}
Every [[D-UI6CU|field]] is a [[D-NKRGN|Euclidean domain]], every Euclidean domain is a [[D-HTIL5|principal ideal domain]], every principal ideal domain is a [[D-INULL|unique factorization domain]], every unique factorization domain is an [[D-QJ3QL|integral domain]], and every integral domain is a commutative [[D-GURUB|ring]]:
$$
\text{Fields} \subset \text{Euclidean domains} \subset \text{PIDs} \subset \text{UFDs} \subset \text{Integral domains} \subset \text{Commutative rings}.
$$
:::

::: {.example title="Each inclusion is strict"}
\envlist

- **Euclidean domain, not a field.** $\ZZ$, or $k[x]$ for a field $k$: the division algorithm makes each Euclidean, and $2$, respectively $x$, is not invertible.

- **PID, not a Euclidean domain.** $\ZZ\left[\frac{1 + \sqrt{-19}}{2}\right]$.

- **UFD, not a PID.** $\ZZ[x]$.
  Since $\ZZ$ is a UFD, so is $\ZZ[x]$.
  The ideal $\generators{2,x} = \theset{\sum r_ix^i \st r_0 \in 2\ZZ}$ is proper and not principal: a constant generator $\pm2$ generates only polynomials with even coefficients and misses $x$, and a generator of degree at least one misses $2$.

- **Integral domain, not a UFD.** $\ZZ[\sqrt{-5}]$, where $(2+\sqrt{-5})(2-\sqrt{-5}) = 9 = 3\cdot 3$ and $2\pm\sqrt{-5}$ and $3$ are irreducible and $3$ is associate to neither $2+\sqrt{-5}$ nor $2-\sqrt{-5}$, by the multiplicativity of the norm $N(a+b\sqrt{-5})=a^2+5b^2$.

- **Commutative ring, not an integral domain.** $\ZZ/4$, where $[2]^2 = [0]$.
:::
