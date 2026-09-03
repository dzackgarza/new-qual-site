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

:::{.remark title="What they do"}
For $\psi_a \da {a-z\over 1-\bar a z}$:

- $\psi_a(a) = 0$ and $\psi_a(0) = a$, so $\psi_a$ swaps the origin with $a$.
- It has a simple zero at $z=a$ and a simple pole at $z = 1/\bar a$, which is the reflection of $a$ in the unit circle.
- $\psi_a(\bd\DD) = \bd\DD$: the boundary is preserved.
- $\psi_a'(z) = {\abs a^2 - 1 \over (1-\bar a z)^2}$.

The zero and the pole being reflections of each other across $\bd\DD$ is what makes the boundary invariant, and it is the reason these are the right maps rather than an arbitrary Möbius transformation.

:::

:::{.proof title="of properties"}
Inverting: set $f(z) = w$ and solve.
\[
{a-z \over 1 - \bar{a}z} &= w \\
\implies a-z - w(1-\bar{a} z) &= 0 \\
\implies z&= {w-a \over \bar a w - 1} = {a-w\over 1-\bar a w}
,\]
so $\psi_a$ is its own inverse.

Differentiating, by the quotient rule:
\[
\psi'_a(z)
= {-(1-\bar a z) + \bar a(a-z) \over \qty{1-\bar a z}^2}
= {-1 + \abs{a}^2 \over \qty{1-\bar a z}^2}
.\]

Scaling: insert $1 = \bar\lambda\lambda$,
\[
\psi_a(\lambda z)
&=
{a - \lambda z \over 1 - \bar a \lambda z}\\
&=
{\lambda\bar\lambda a - \lambda z \over 1 - \bar a \lambda z} \\
&= \lambda {\bar\lambda a - z \over 1 - \bar{\bar\lambda a} z} \\
&= \lambda \psi_{\bar \lambda a}(z)
.\]

Being an involution: $\psi_a\circ\psi_a$ satisfies the Schwarz lemma and has two fixed points, which forces it to be the identity.

:::

## The automorphism group of the disc

[[T-W26VL]]

:::{.proof title="sketch"}
\envlist

- These maps are biholomorphisms, being compositions of $z\mapsto \lambda z$ with $z\mapsto {z-a\over 1-\bar a z}$.
- Let $f \in \BiHol(\DD)$ and fix $a$ with $f(a) = 0$.
- Write $M(z) = {z-a\over 1-\bar a z}$, so $M(a) = 0$ and $M$ is a biholomorphism.
- Then $g\da f\circ M\inv \in \BiHol(\DD)$ fixes $0$, so the Schwarz lemma applied to $g$ and to $g\inv$ forces $g$ to be a rotation, $g(z) = \lambda z$.
- Hence $f = g\circ M$, which is the claimed form.
- Uniqueness: $f'$ determines $\Arg\lambda$.

:::

:::{.remark title="Why Schwarz is the engine"}
The only step with content is that a biholomorphism of the disc fixing the origin is a rotation, and that is Schwarz applied twice: once to $g$, giving $\abs{g(z)}\leq\abs z$, and once to $g\inv$, giving the reverse.
Equality in Schwarz is the rigidity that collapses the group to rotations and Blaschke factors.

:::

[[T-HSWGS]]

[[T-VGDFW]]

## Exercises

[[E-IVHVW]]
[[E-XQ4BA]]
[[E-CFTRQ]]
