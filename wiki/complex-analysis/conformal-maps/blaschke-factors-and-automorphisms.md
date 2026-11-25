---
title: Blaschke factors and automorphisms
order: 30
topics:
- Blaschke Factors
- Blaschke Products
- Automorphisms
- Automorphisms of the Disc
- Disc Automorphisms
- Biholomorphisms
- Biholomorphic Maps
---

# Blaschke factors and automorphisms

A finite product of [[D-MFPYG|Blaschke factors]] is a self-map of $\DD$ with prescribed zeros, and every biholomorphic self-map of $\DD$ is a Blaschke factor followed by a rotation ([[T-W26VL]]).

## Blaschke factors

[[D-MFPYG]]

::: {.remark}
For $a\neq 0$ the Blaschke factor $\psi_a$ has a simple zero at $a$ and a simple pole at $1/\bar a$, the reflection of $a$ in the unit circle.

:::

::: {.example title="The Blaschke factor at $1/2$, in numbers"}
$\psi_{1/2}(z) = \dfrac{1/2-z}{1-z/2}$ exchanges $0$ and $1/2$: $\psi_{1/2}(0) = 1/2$ and $\psi_{1/2}(1/2) = 0$.
It is its own inverse — $\psi_{1/2}\!\left(\psi_{1/2}(z)\right) = z$, checked at $z = 0.3+0.4i$, which returns $0.3+0.4i$ — and it is unimodular on the boundary: at $z = i$ it takes the value $4/5-3i/5$, of modulus $1$.
So $\abs{\psi_{1/2}}\leq 1$ on $\DD$ with equality only on $S^1$, which is [[T-BYNL5|the maximum modulus principle]] for a function that is not constant.
The automorphism of $\DD$ carrying $i/2$ to $0$ is $\psi_{i/2}(z) = \dfrac{i/2-z}{1+iz/2}$; at $z = 0.3+0.1i$ it takes the value $-0.2432\ldots+0.4595\ldots i$, of modulus $0.5199\ldots$
Composing the two, $\psi_{i/2}\circ\psi_{1/2}$ carries $1/2$ to $i/2$, since $\psi_{1/2}(1/2) = 0$ and $\psi_{i/2}(0) = i/2$.
:::

## The automorphism group of the disc

[[T-W26VL]]

[[T-VGDFW]]

## Problems

[[E-IVHVW]] [[P-ZRVTI]] [[E-CFTRQ]]
