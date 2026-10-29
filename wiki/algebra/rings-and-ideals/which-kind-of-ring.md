---
title: Which kind of ring is this?
order: 0
topics:
- Rings
- Commutative Algebra
---

# Which kind of ring is this?

## The chain of inclusions

[[PR-LLBRB]]

::: {.remark title="Proofs of the inclusions"}
\envlist

- **Field $\implies$ Euclidean domain.** With the norm $d(x)=0$ for $x\neq0$, write $x = qy+r$ with $q = \inverseof{y} x$ and $r=0$.

- **Euclidean domain $\implies$ PID.** Let $I\neq 0$ be an ideal and $a\in I$ a nonzero element with $d(a)$ minimal.
  If $b\in I$, write $b = aq+r$ with $r=0$ or $d(r) < d(a)$; then $r = b-aq \in I$, so minimality forces $r=0$, and $I = \generators a$.

- **PID $\implies$ UFD.** A PID is Noetherian, so a nonzero nonunit that is not a product of irreducibles would give a strictly ascending chain $\generators a \subsetneq \generators{a_1}\subsetneq\cdots$ of principal ideals; hence factorizations exist.
  In a PID every irreducible element $p$ generates a maximal ideal, so $p$ is prime, and two factorizations into primes agree up to order and units by cancelling one prime at a time.
:::

[[E-XH2QU]]

## Quotients

[[PR-76BDN]]

::: {.remark}
Every field is an integral domain, so every maximal ideal is prime, and $\mspec R \subseteq \Spec R$.
:::

For a field $k$ and a nonconstant $f\in k[x]$, the following are equivalent: $\generators f$ is maximal in $k[x]$; $k[x]/\generators f$ is a field; $f$ is irreducible.

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
