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

Every biholomorphic self-map of $\DD$ has the form $e^{i\theta}\psi_a$ for some $a\in\DD$ and $\theta\in\RR$, where $\psi_a$ is the Blaschke factor below.

## Blaschke factors

[[D-MFPYG]]

[[PR-ULJAJ]]

[[FF-4GUYL]]

::: {.remark}
For $a\neq 0$, $\psi_a(z) = (a-z)/(1-\bar a z)$ has a simple zero at $z=a$ and a simple pole at $z = 1/\bar a$, the reflection of $a$ in the unit circle.

:::

::: {.proof title="Properties"}
For $\abs z=1$, $\abs{1-\bar a z} = \abs{\bar z}\abs{1-\bar a z} = \abs{\bar z - \bar a} = \abs{a-z}$, so $\abs{\psi_a(z)} = 1$ and $\psi_a$ maps $S^1$ to $S^1$.
Since $\psi_a$ is holomorphic on a neighborhood of $\overline\DD$ (its pole $1/\bar a$ lies outside $\overline\DD$) and $\abs{\psi_a}=1$ on $S^1$, the maximum modulus principle gives $\psi_a(\DD)\subseteq\DD$.

Inverting: set $\psi_a(z) = w$ and solve.
$$
\begin{aligned}
{a-z \over 1 - \bar{a}z} &= w \\
\implies a-z - w(1-\bar{a} z) &= 0 \\
\implies z&= {w-a \over \bar a w - 1} = {a-w\over 1-\bar a w}
\end{aligned},$$
so $\psi_a\circ\psi_a=\id$, and $\psi_a$ is an automorphism of $\DD$.

Differentiating, by the quotient rule:
$$
\psi'_a(z)
= {-(1-\bar a z) + \bar a(a-z) \over \qty{1-\bar a z}^2}
= {-1 + \abs{a}^2 \over \qty{1-\bar a z}^2}
.$$

Scaling: for $\abs\lambda = 1$, insert $1 = \bar\lambda\lambda$,
$$
\begin{aligned}
\psi_a(\lambda z)
&=
{a - \lambda z \over 1 - \bar a \lambda z}\\
&=
{\lambda\bar\lambda a - \lambda z \over 1 - \bar a \lambda z} \\
&= \lambda {\bar\lambda a - z \over 1 - \bar{\bar\lambda a} z} \\
&= \lambda \psi_{\bar \lambda a}(z)
\end{aligned}.$$

:::

## The automorphism group of the disc

[[T-W26VL]]

::: {.proof title="Sketch"}
\envlist

- The maps $\lambda\psi_a$ are automorphisms, being compositions of the rotation $z\mapsto \lambda z$ with $\psi_a$.
- Let $f \in \Aut(\DD)$ and let $a\coloneqq f\inv(0)$.
- Then $g\coloneqq f\circ \psi_a \in \Aut(\DD)$ fixes $0$.
  The Schwarz lemma applied to $g$ and to $g\inv$ gives $\abs{g(z)}\leq\abs z$ and $\abs z = \abs{g\inv(g(z))}\leq\abs{g(z)}$, so $g(z) = \lambda z$ with $\abs\lambda = 1$.
- Hence $f = g\circ\psi_a = \lambda\psi_a$.

:::

[[T-VGDFW]]

## Exercises

[[E-IVHVW]]
[[E-XQ4BA]]
[[E-CFTRQ]]
