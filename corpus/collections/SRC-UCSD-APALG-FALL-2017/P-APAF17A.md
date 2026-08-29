---
schema: qual/card@1
id: P-APAF17A
kind: problem
title: Rank inequalities for powers when $\operatorname{rank} A^2\leq\operatorname{rank} A^3$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $A \in \mathbb{R}^{n \times n}$ be a square matrix such that:
$$\operatorname{rank}(A^2) \le \operatorname{rank}(A^3).$$
Show that:
$$\operatorname{rank}(A^k) \le \operatorname{rank}(A^{k+1})$$
(and in fact, $\operatorname{rank}(A^k) = \operatorname{rank}(A^{k+1}) = \operatorname{rank}(A^2)$) for all integers $k \ge 3$.
:::

::: solution
**Goal:** Prove that the descending chain of images $\operatorname{im}(A) \supseteq \operatorname{im}(A^2) \supseteq \operatorname{im}(A^3) \supseteq \cdots$ stabilizes once $\operatorname{rank}(A^2) = \operatorname{rank}(A^3)$.

<1>1. Monotonicity of Ranks of Matrix Powers:
    *Proof:*
    <2>1. For any matrix $A \in M_n(\mathbb{R})$ and any integer $j \ge 1$, we have:
        $$\operatorname{im}(A^{j+1}) = A(\operatorname{im}(A^j)) \subseteq \operatorname{im}(A^j).$$
    <2>2. Since the image space of $A^{j+1}$ is a subspace of the image space of $A^j$, their dimensions (ranks) satisfy:
        $$\operatorname{rank}(A^{j+1}) \le \operatorname{rank}(A^j) \quad \text{for all } j \ge 1.$$

<1>2. Stabilization at Step 2:
    *Proof:*
    <2>1. By Step 1 with $j = 2$:
        $$\operatorname{rank}(A^3) \le \operatorname{rank}(A^2).$$
    <2>2. Combining this with the given hypothesis $\operatorname{rank}(A^2) \le \operatorname{rank}(A^3)$:
        $$\operatorname{rank}(A^2) = \operatorname{rank}(A^3).$$
    <2>3. Since $\operatorname{im}(A^3) \subseteq \operatorname{im}(A^2)$ are finite-dimensional subspaces of $\mathbb{R}^n$ with identical dimension:
        $$\operatorname{im}(A^3) = \operatorname{im}(A^2).$$

<1>3. Induction for All $k \ge 3$:
    *Proof:*
    <2>1. **Inductive Claim:** $\operatorname{im}(A^k) = \operatorname{im}(A^2)$ for all $k \ge 2$.
    <2>2. **Base Case:** For $k = 2, 3$, we already proved $\operatorname{im}(A^3) = \operatorname{im}(A^2)$.
    <2>3. **Inductive Step:** Suppose $\operatorname{im}(A^k) = \operatorname{im}(A^{k-1})$ for some $k \ge 3$.
        Applying the linear transformation $A$ to both equal subspaces:
        $$\operatorname{im}(A^{k+1}) = A(\operatorname{im}(A^k)) = A(\operatorname{im}(A^{k-1})) = \operatorname{im}(A^k).$$
    <2>4. Thus $\operatorname{im}(A^k) = \operatorname{im}(A^{k+1})$ for all $k \ge 2$.
    <2>5. Taking dimensions:
        $$\operatorname{rank}(A^k) = \operatorname{rank}(A^{k+1}) \quad \text{for all } k \ge 2.$$
    <2>6. In particular:
        $$\operatorname{rank}(A^k) \le \operatorname{rank}(A^{k+1}) \quad \text{for all } k \ge 3.$$

<1>4. Conclusion:
    $\operatorname{im}(A^3) = \operatorname{im}(A^2) \implies \operatorname{im}(A^{k+1}) = A^{k-2}(\operatorname{im}(A^3)) = A^{k-2}(\operatorname{im}(A^2)) = \operatorname{im}(A^k)$, so $\operatorname{rank}(A^k) \le \operatorname{rank}(A^{k+1})$ holds with equality. Q.E.D.
:::
