---
schema: qual/card@1
id: E-VYIZJ
kind: problem
title: A holomorphic self-map of $\DD$ with two fixed points is the identity
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
---

::: {.exercise}
Show that the only holomorphic map $f:\DD\to \DD$ with two distinct fixed points $a\neq b$ is the identity.
:::

::: {.solution}
For $a\in\DD$ let $\psi_a(z) = \frac{a-z}{1-\bar a z}$, an automorphism of $\DD$ with $\psi_a(a) = 0$ and $\psi_a\circ\psi_a = \id$.

::: pf

::: {.pf-step #conjugate}
$F \definedas \psi_a\circ f\circ\psi_a$ is a holomorphic self-map of $\DD$ with $F(0) = 0$ and $F(c) = c$, where $c \definedas \psi_a(b) \neq 0$.

::: pf-proof
$F(0) = \psi_a(f(a)) = \psi_a(a) = 0$ and $F(c) = \psi_a(f(b)) = \psi_a(b) = c$; $c\neq0$ because $\psi_a$ is injective and $b\neq a$.
:::

:::

::: {.pf-step #rotation}
$F = \id$.

::: pf-proof
By the Schwarz lemma $\abs{F(z)}\le\abs z$ on $\DD$, and equality holds at $z = c\neq0$, so $F(z) = \lambda z$ with $\abs\lambda = 1$.
Then $c = F(c) = \lambda c$ gives $\lambda = 1$.
:::

:::

::: pf-step
$f = \id$.

::: pf-proof
By step [](#rotation){.pf-ref}, $f = \psi_a\circ F\circ\psi_a = \psi_a\circ\psi_a = \id$.
:::

:::

:::

:::
