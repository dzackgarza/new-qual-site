---
schema: qual/card@1
id: E-HOJKE
kind: problem
title: $A$ is a field iff $A$ is a simple ring iff every homomorphism from $A$ to
  a nonzero field is injective
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that TFAE:

- $A\in \Field$

- $A$ is a simple ring, so $\Id(A) = \theset{ 0, A }$.

- If $B\in \Field$ is nonzero then every ring morphism $A\to B$ is injective.
:::

::: {.solution}
Let $A$ be a commutative ring with $1\neq0$; ring homomorphisms preserve $1$.
Number the three conditions (1), (2), (3) in the order stated.

::: pf

::: {.pf-step #field-implies-simple}
(1) implies (2).

::: pf-proof
Let $I$ be a nonzero ideal of the field $A$ and $0\neq x\in I$.
Then $1=x^{-1}x\in I$, so $a=a\cdot1\in I$ for every $a\in A$ and $I=A$.
:::

:::

::: {.pf-step #simple-implies-injective}
(2) implies (3).

::: pf-proof
Let $\varphi\colon A\to B$ be a ring homomorphism to a field.
$\ker\varphi$ is an ideal, and $\varphi(1)=1\neq0$ gives $\ker\varphi\neq A$.
By (2), $\ker\varphi=0$, so $\varphi$ is injective.
:::

:::

::: {.pf-step #injective-implies-field}
(3) implies (1).

::: pf-proof
Let $0\neq x\in A$ and suppose $(x)\neq A$.
The proper ideal $(x)$ lies in a maximal ideal $\mathfrak m$ (Zorn's lemma), and $\pi\colon A\to A/\mathfrak m$ is a homomorphism to a field.
By (3), $\mathfrak m=\ker\pi=0$, so $x\in\mathfrak m=0$, a contradiction.
Hence $(x)=A$, so $x$ is a unit, and $A$ is a field.
:::

:::

::: pf-qed
Steps [](#field-implies-simple){.pf-ref}, [](#simple-implies-injective){.pf-ref} and [](#injective-implies-field){.pf-ref} give $(1)\Rightarrow(2)\Rightarrow(3)\Rightarrow(1)$.
:::

:::

:::
