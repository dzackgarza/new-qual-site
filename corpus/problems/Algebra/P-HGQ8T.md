---
schema: qual/card@1
id: P-HGQ8T
kind: problem
title: For symmetric $A,B$, the product $AB$ is symmetric iff $AB=BA$; $BB^t$ and
  $B+B^t$ are symmetric
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Bilinear Forms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $A, B \in M_n(R)$ be $n \times n$ matrices over a commutative ring $R$.
(1) Prove that if $A$ and $B$ are symmetric matrices ($A^t = A, B^t = B$), then the product $AB$ is symmetric if and only if $A$ and $B$ commute ($AB = BA$). (2) For an arbitrary matrix $B \in M_n(R)$, prove that $B B^t$ and $B + B^t$ are symmetric, and $B - B^t$ is skew-symmetric.
:::

::: solution
**Goal:** Prove the symmetry condition for products of symmetric matrices and symmetry of algebraic combinations of arbitrary matrices.

<1>1. Part (1): For symmetric $A, B$, $AB$ is symmetric $\iff AB = BA$: *Proof:* <2>1. Assume $A^t = A$ and $B^t = B$.
<2>2. By the transpose property of matrix multiplication: $$(AB)^t = B^t A^t = B A.$$ <2>3. **Direction $(\implies)$:** Suppose $AB$ is symmetric, so $(AB)^t = AB$.
Substituting $(AB)^t = BA$ gives $BA = AB$, so $A$ and $B$ commute.
<2>4. **Direction $(\impliedby)$:** Suppose $AB = BA$.
Then $(AB)^t = B^t A^t = BA = AB$, which proves $AB$ is symmetric.

<1>2. Part (2): Symmetry of $B B^t$, $B + B^t$, and skew-symmetry of $B - B^t$: *Proof:* <2>1. Let $B \in M_n(R)$ be an arbitrary matrix.
<2>2. **$B B^t$ is symmetric:** $$(B B^t)^t = (B^t)^t B^t = B B^t.$$ Thus $B B^t$ is symmetric.
(Similarly, $B^t B$ is symmetric).
<2>3. **$B + B^t$ is symmetric:** $$(B + B^t)^t = B^t + (B^t)^t = B^t + B = B + B^t.$$ Thus $B + B^t$ is symmetric.
<2>4. **$B - B^t$ is skew-symmetric:** $$(B - B^t)^t = B^t - (B^t)^t = B^t - B = -(B - B^t).$$ Thus $B - B^t$ is skew-symmetric.

<1>3. Conclusion: $AB$ is symmetric iff $AB = BA$; $B B^t$ and $B + B^t$ are symmetric, while $B - B^t$ is skew-symmetric.
Q.E.D.
:::
