---
title: Which kind of ring is this?
order: 0
topics:
- Rings
- Commutative Algebra
---

# Which kind of ring is this?

## The chain of inclusions

$$
\text{fields} \subset \text{Euclidean domains} \subset \text{PIDs} \subset \text{UFDs} \subset \text{integral domains} \subset \text{commutative rings}
$$

[[PR-LLBRB]]

::: {.remark title="Proofs of the inclusions"}
\envlist

- **Field $\implies$ Euclidean domain.** With the norm $d(x)=0$ for $x\neq0$, write $x = qy+r$ with $q = y\inv x$ and $r=0$.

- **Euclidean domain $\implies$ PID.** Let $I\neq 0$ be an ideal and $a\in I$ a nonzero element with $d(a)$ minimal.
  If $b\in I$, write $b = aq+r$ with $r=0$ or $d(r) < d(a)$; then $r = b-aq \in I$, so minimality forces $r=0$, and $I = \gens a$.

- **PID $\implies$ UFD.** A PID is Noetherian, so a nonzero nonunit that is not a product of irreducibles would give a strictly ascending chain $\gens a \subsetneq \gens{a_1}\subsetneq\cdots$ of principal ideals; hence factorizations exist.
  In a PID every irreducible element $p$ generates a maximal ideal, so $p$ is prime, and two factorizations into primes agree up to order and units by cancelling one prime at a time.
:::

## Strictness of the inclusions

::: {.example title="Each inclusion is strict"}
\envlist

- **Euclidean domain, not a field.** $k[x]$ for a field $k$: the division algorithm makes it Euclidean, and $x$ is not invertible.

- **PID, not a Euclidean domain.** $\ZZ\left[\frac{1 + \sqrt{-19}}{2}\right]$.

- **UFD, not a PID.** $\ZZ[x]$.
  Since $\ZZ$ is a UFD, so is $\ZZ[x]$.
  The ideal $\gens{2,x} = \ts{\sum r_ix^i \st r_0 \in 2\ZZ}$ is proper and not principal: a constant generator $\pm2$ generates only polynomials with even coefficients and misses $x$, and a generator of degree at least one misses $2$.

- **Integral domain, not a UFD.** $\ZZ[\sqrt{-5}]$, where $(2+\sqrt{-5})(2-\sqrt{-5}) = 9 = 3\cdot 3$ and all four factors are irreducible and pairwise nonassociate, by the multiplicativity of the norm $N(a+b\sqrt{-5})=a^2+5b^2$.

- **Commutative ring, not an integral domain.** $\ZZ/4$, where $[2]^2 = [0]$.
:::

[[E-XH2QU]]

## Quotients

[[PR-76BDN]]

::: {.remark title="Maximal and prime ideals through quotients"}
For an ideal $I$ of a commutative ring $R$,
$$
I \text{ maximal} \iff R/I \text{ is a field}, \qquad I \text{ prime} \iff R/I \text{ is an integral domain}.
$$
Every field is an integral domain, so every maximal ideal is prime, and $\mspec R \subseteq \spec R$.
:::

For a field $k$ and a nonconstant $f\in k[x]$, the following are equivalent: $\gens f$ is maximal in $k[x]$; $k[x]/\gens f$ is a field; $f$ is irreducible.

## Transporting properties

[[PR-GEHJF]]

::: {.fact}
If $\mfm\subseteq R$ is a maximal ideal and $x\in R\sm\mfm$, then $\mfm + Rx = R$, so $1 = m + rx$ for some $m\in\mfm$ and $r\in R$.
:::

## Gorenstein rings

[[D-DU4UQ]]

::: {.example title="Finite-dimensional graded Gorenstein algebras"}
Let $k$ be a field and $R = R_0 \oplus R_1 \oplus \cdots \oplus R_n$ a graded commutative $k$-algebra with $R_0 = k$, $\dim_k R < \infty$, and $R_n\neq0$.
Then $R$ is Gorenstein if and only if $R$ satisfies Poincaré duality: $\dim_k R_n = 1$, and for each $i$ the multiplication pairing $R_i \times R_{n-i} \to R_n$ is perfect.
:::
