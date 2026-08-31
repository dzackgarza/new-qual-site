---
schema: qual/card@1
id: P-RHIIP
kind: problem
title: Hungerford 7.1.5
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Bilinear Forms
relations: []
review: draft
---

::: problem
Let $R$ be a commutative ring and let $A, B \in M_n(R)$ be $n \times n$ matrices.

(a) Show that if $A$ and $B$ are symmetric (respectively, skew-symmetric), then $A + B$ is symmetric (respectively, skew-symmetric).

(b) Show that if $A$ and $B$ are symmetric, then the product $A B$ is symmetric if and only if $A B = B A$.

(c) Show that for any matrix $B \in M_n(R)$, the matrices $B B^t$ and $B + B^t$ are symmetric, and $B - B^t$ is skew-symmetric.
:::

::: solution
**Goal:** Prove closure properties and transpose identities for symmetric and skew-symmetric matrices over a commutative ring $R$.

<1>1. Properties of the matrix transpose:
    *Proof:*
    <2>1. For any matrices $X, Y \in M_n(R)$, $(X + Y)^t = X^t + Y^t$.
    <2>2. For any $X, Y \in M_n(R)$, $(X Y)^t = Y^t X^t$ (using commutativity of multiplication in $R$ when computing $(X Y)_{i, j}^t = \sum_k X_{j, k} Y_{k, i} = \sum_k Y_{k, i} X_{j, k} = (Y^t X^t)_{i, j}$).
    <2>3. For any $X \in M_n(R)$, $(X^t)^t = X$ and $(-X)^t = -X^t$.

<1>2. Part (a): Additive closure of symmetric and skew-symmetric matrices.
    *Proof:*
    <2>1. If $A$ and $B$ are symmetric ($A^t = A$ and $B^t = B$):
    $$(A + B)^t = A^t + B^t = A + B,$$
    so $A + B$ is symmetric.
    <2>2. If $A$ and $B$ are skew-symmetric ($A^t = -A$ and $B^t = -B$):
    $$(A + B)^t = A^t + B^t = (-A) + (-B) = -(A + B),$$
    so $A + B$ is skew-symmetric.

<1>3. Part (b): Symmetry of the product of symmetric matrices.
    *Proof:*
    <2>1. Assume $A^t = A$ and $B^t = B$.
    <2>2. Compute the transpose of the product:
    $$(A B)^t = B^t A^t = B A.$$
    <2>3. By definition, $A B$ is symmetric if and only if $(A B)^t = A B$.
    <2>4. Substituting $(A B)^t = B A$ gives:
    $$A B \text{ is symmetric } \iff B A = A B \iff A B = B A.$$

<1>4. Part (c): Symmetry of $B B^t$ and $B + B^t$, and skew-symmetry of $B - B^t$.
    *Proof:*
    <2>1. Transpose of $B B^t$:
    $$(B B^t)^t = (B^t)^t B^t = B B^t,$$
    so $B B^t$ is symmetric.
    <2>2. Transpose of $B + B^t$:
    $$(B + B^t)^t = B^t + (B^t)^t = B^t + B = B + B^t,$$
    so $B + B^t$ is symmetric.
    <2>3. Transpose of $B - B^t$:
    $$(B - B^t)^t = B^t - (B^t)^t = B^t - B = -(B - B^t),$$
    so $B - B^t$ is skew-symmetric.

<1>5. Conclusion:
    *Proof:*
    All requested transpose properties are proved.
:::
