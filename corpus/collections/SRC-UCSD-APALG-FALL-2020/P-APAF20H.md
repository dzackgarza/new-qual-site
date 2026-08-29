---
schema: qual/card@1
id: P-APAF20H
kind: problem
title: Orthogonal complement of a $G$-invariant subspace is $G$-invariant
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $U\colon G\to\mathrm{U}(H)$ be a unitary representation of a compact group $G$ on a Hilbert space $H$.
Prove that, if $K$ is a closed subspace of $H$ invariant under the action of $G$, so is $K^\perp$.
:::

::: {.solution}
<1>1. Let $v \in K^\perp$ and $g \in G$.
Proof: take an arbitrary element of $K^\perp$ and an arbitrary group element.

<1>2. For any $w \in K$, $\langle U(g)v, w \rangle = \langle v, U(g)^* w \rangle = \langle v, U(g)^{-1} w \rangle = \langle v, U(g^{-1}) w \rangle$.
Proof: $U(g)$ is unitary, so $U(g)^* = U(g)^{-1} = U(g^{-1})$.

<1>3. $U(g^{-1}) w \in K$ (since $K$ is $G$-invariant).
Proof: hypothesis.

<1>4. Hence $\langle U(g)v, w \rangle = \langle v, U(g^{-1})w \rangle = 0$ (since $v \in K^\perp$).
Proof: <1>2 and <1>3.

<1>5. Therefore $U(g)v \in K^\perp$ for all $g \in G$, so $K^\perp$ is $G$-invariant.
Proof: <1>4 (for arbitrary $w \in K$).

<1>6. Q.E.D.
Proof: <1>5.
:::
