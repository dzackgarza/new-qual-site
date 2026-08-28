---
schema: qual/card@1
id: P-S04KT
kind: problem
title: The kernel of a linear map $\mathbb{R}^n\to\mathbb{R}^m$ is a subspace
classification:
  areas:
  - prelim
  topics:
  - Linear Maps
  - Vector Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
a) Give the definition for a function $L: \mathbb{R}^n \to \mathbb{R}^m$ to be a linear transformation.

b) Prove that the kernel of a linear transformation $L: \mathbb{R}^n \to \mathbb{R}^m$ is a subspace of $\mathbb{R}^n$.
:::

::: {.solution}
**Goal.** Define a linear transformation and prove its kernel is a subspace.

<1>1. (a) $L: \RR^n \to \RR^m$ is linear iff $L(x + y) = L(x) + L(y)$ and $L(cx) = cL(x)$ for all $x, y \in \RR^n$ and $c \in \RR$.
Proof: definition of a linear transformation.

<1>2. (b) $\ker L = \theset{x \in \RR^n : L(x) = 0}$ is a subspace.
<2>1. $0 \in \ker L$.
Proof: $L(0) = L(0 + 0) = L(0) + L(0)$, so $L(0) = 0$.
<2>2. Closed under addition: if $x, y \in \ker L$, then $L(x + y) = L(x) + L(y) = 0 + 0 = 0$, so $x + y \in \ker L$.
Proof: linearity.
<2>3. Closed under scalar multiplication: if $x \in \ker L$ and $c \in \RR$, then $L(cx) = cL(x) = c \cdot 0 = 0$, so $cx \in \ker L$.
Proof: linearity.
<2>4. Hence $\ker L$ is a subspace.
Proof: <1>2.1, <1>2.2, <1>2.3 verify the three subspace axioms.

<1>3. Q.E.D.
Proof: <1>2.4 is the claim.
:::
