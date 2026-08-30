---
schema: qual/card@1
id: E-HOJKE
kind: exercise
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

- $A$ is a simple ring, so $\Id(A) = \ts{ 0, A }$.

- If $B\in \Field$ is nonzero then every ring morphism $A\to B$ is injective.
:::

::: solution
**Goal:** Prove the three statements are equivalent.

<1> Show a field is simple and has injective maps to nonzero fields.
    *Proof:*
    <2>1. If $A$ is a field and $I\subseteq A$ is an ideal, then either $I=0$ or $1\in I$.
    <2>2. Since $I= A$ iff $1\in I$, every ideal is $0$ or $A$, so $A$ is simple.
    <2>3. Let $\varphi:A\to B$ with $B$ a nonzero field and $\varphi\ne0$.
    <2>4. If $a\in\ker\varphi$ is nonzero, then $a^{-1}$ exists and
        $$\varphi(1)=\varphi(a a^{-1})=\varphi(a)\varphi(a^{-1})=0,$$
        impossible. Thus $\ker\varphi=0$.

<1> Show simplicity implies injective maps to nonzero fields.
    *Proof:*
    <2>1. Let $A$ be simple and $\varphi:A\to B$ a nonzero homomorphism to a nonzero field.
    <2>2. $\ker\varphi$ is an ideal of $A$, and $\ker\varphi\neq A$ because $\varphi\ne0$.
    <2>3. Simplicity gives $\ker\varphi=0$, hence $\varphi$ is injective.

<1> Show injective maps to fields force field and simplicity.
    *Proof:*
    <2>1. Assume every nonzero homomorphism $A\to$ nonzero field is injective.
    <2>2. Let $0\ne a\in A$ and suppose $(a)$ is proper.
    <2>3. Choose a maximal ideal $\mathfrak m\supseteq(a)$.
    <2>4. The quotient map $\pi:A\to A/\mathfrak m$ is a nonzero map to a field.
    <2>5. By hypothesis, $\pi$ is injective, so $\mathfrak m=\ker\pi=0$.
    <2>6. This contradicts $a\in\mathfrak m$ and $a\ne0$. Hence every nonzero $a$ is a unit.
    <2>7. Thus $A$ is a field (commutative ring with unity is understood by context).
    <2>8. Then every nonzero ideal of $A$ is all of $A$, so $A$ is simple.

Authored by **Codex 5.3 Spark Extra High**.
:::
