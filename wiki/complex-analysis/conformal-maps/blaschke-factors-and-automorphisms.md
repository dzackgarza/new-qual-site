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

Every biholomorphic self-map of $\DD$ has the form $e^{i\theta}\psi_a$ for some $a\in\DD$ and $\theta\in\RR$, where $\psi_a(z) \coloneqq (a-z)/(1-\bar a z)$ is the Blaschke factor.

## Blaschke factors

[[D-MFPYG]]

::: {.remark}
For $a\neq 0$, $\psi_a(z) = (a-z)/(1-\bar a z)$ has a simple zero at $z=a$ and a simple pole at $z = 1/\bar a$, the reflection of $a$ in the unit circle.

:::

## The automorphism group of the disc

[[T-W26VL]]

::: {.proof title="Sketch"}
\envlist

- The maps $\lambda\psi_a$ are automorphisms, being compositions of the rotation $z\mapsto \lambda z$ with $\psi_a$.

- Let $f \in \Aut(\DD)$ and let $a\coloneqq \inverseof{f}(0)$.

- Then $g\coloneqq f\circ \psi_a \in \Aut(\DD)$ fixes $0$.
  The Schwarz lemma applied to $g$ and to $\inverseof{g}$ gives $\abs{g(z)}\leq\abs z$ and $\abs z = \abs{\inverseof{g}(g(z))}\leq\abs{g(z)}$, so $g(z) = \lambda z$ with $\abs\lambda = 1$.

- Hence $f = g\circ\psi_a = \lambda\psi_a$.

:::

[[T-VGDFW]]

## Problems

[[E-IVHVW]] [[E-TJ3WM]] [[E-CFTRQ]]
