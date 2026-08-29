---
schema: qual/card@1
id: P-5IZ2K
kind: problem
title: A non-symmetric polynomial whose square is symmetric
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Find a non-symmetric polynomial in several variables whose square is symmetric, and prove its properties.
:::

::: solution
**Goal:** Exhibit an alternating polynomial $P(x_1, \dots, x_n)$ that is not symmetric, but whose square $P^2$ is symmetric (the Vandermonde polynomial / discriminant).

<1>1. Example in 2 variables: $P(x, y) = x - y$:
    *Proof:*
    <2>1. Let $P(x, y) = x - y \in \mathbb{R}[x, y]$.
    <2>2. **$P$ is not symmetric:** Under the transposition $(x \ y)$, the polynomial becomes:
        $$(x \ y) \cdot P(x, y) = P(y, x) = y - x = -(x - y) = -P(x, y) \ne P(x, y).$$
    <2>3. **$P^2$ is symmetric:**
        $$(P(x, y))^2 = (x - y)^2 = x^2 - 2xy + y^2.$$
        Under $(x \ y)$:
        $$(y - x)^2 = (-(x - y))^2 = (x - y)^2.$$
        Since $(x \ y)$ generates the symmetric group $S_2$, $P^2$ is invariant under all of $S_2$, hence symmetric.

<1>2. General example in $n \ge 2$ variables: The Vandermonde polynomial $\Delta$:
    *Proof:*
    <2>1. Define the Vandermonde polynomial (square root of the discriminant):
        $$\Delta(x_1, \dots, x_n) = \prod_{1 \le i < j \le n} (x_i - x_j).$$
    <2>2. **$\Delta$ is not symmetric (it is alternating):**
        - For any transposition $\tau = (a \ b) \in S_n$:
            $$\tau \cdot \Delta = \operatorname{sgn}(\tau) \Delta = -\Delta.$$
        - Since $-\Delta \ne \Delta$ (in characteristic $\ne 2$), $\Delta$ is not symmetric.
    <2>3. **$\Delta^2$ is symmetric (the discriminant):**
        - For any permutation $\sigma \in S_n$:
            $$\sigma \cdot (\Delta^2) = (\sigma \cdot \Delta)^2 = (\operatorname{sgn}(\sigma) \Delta)^2 = (\operatorname{sgn}(\sigma))^2 \Delta^2 = (+1) \Delta^2 = \Delta^2.$$
        - Thus $\Delta^2 = \prod_{i < j} (x_i - x_j)^2$ is invariant under all permutations $\sigma \in S_n$, so it is symmetric.

<1>3. Conclusion:
    $P(x, y) = x - y$ (and more generally the Vandermonde polynomial $\Delta = \prod_{i<j} (x_i - x_j)$) is non-symmetric, but its square $(x-y)^2$ (resp. the discriminant $\Delta^2$) is symmetric. Q.E.D.
:::
