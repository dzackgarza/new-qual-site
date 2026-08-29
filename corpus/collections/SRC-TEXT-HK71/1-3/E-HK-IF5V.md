---
schema: qual/card@1
id: E-HK-IF5V
kind: exercise
title: Solutions to a homogeneous system over $\CC$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Find all solutions in $\mathbb{C}^2$ to the homogeneous linear system:
$$
\begin{aligned}
(1 - i) x_1 - i x_2 &= 0 \\
2 x_1 + (1 - i) x_2 &= 0.
\end{aligned}
$$
:::

::: solution
**Goal:** Solve the $2 \times 2$ homogeneous complex linear system $A x = 0$ by determining the determinant and row echelon reduction.

<1>1. Matrix Form and Determinant Computation:
    *Proof:*
    <2>1. The system can be written as $A x = 0$ where $x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \in \mathbb{C}^2$ and:
        $$A = \begin{bmatrix} 1 - i & -i \\ 2 & 1 - i \end{bmatrix}.$$
    <2>2. We compute the determinant of the coefficient matrix $A$:
        $$\det(A) = (1 - i)(1 - i) - (-i)(2) = (1 - i)^2 + 2i.$$
    <2>3. Expanding the complex square:
        $$(1 - i)^2 = 1 - 2i + i^2 = 1 - 2i - 1 = -2i.$$
    <2>4. Substituting this into the determinant:
        $$\det(A) = -2i + 2i = 0.$$
    <2>5. Since $\det(A) = 0$, the matrix $A$ is singular ($\operatorname{rank}(A) < 2$), so the system has non-trivial solutions.

<1>2. Row Reduction and Parametric Solution:
    *Proof:*
    <2>1. Multiplying the first equation by $(1 + i)$:
        $$(1 + i)(1 - i) x_1 - (1 + i) i x_2 = 0 \implies 2 x_1 - (i - 1) x_2 = 0 \implies 2 x_1 + (1 - i) x_2 = 0.$$
    <2>2. This is identical to the second equation! Thus the second row is linearly dependent on the first.
    <2>3. The single independent equation is:
        $$(1 - i) x_1 - i x_2 = 0 \implies i x_2 = (1 - i) x_1.$$
    <2>4. Multiplying both sides by $-i$ (since $-i \cdot i = 1$):
        $$x_2 = -i (1 - i) x_1 = (-i - 1) x_1 = -(1 + i) x_1.$$
    <2>5. Setting $x_1 = t \in \mathbb{C}$ as the free parameter:
        $$x_2 = -(1 + i) t.$$

<1>3. Solution Space:
    *Proof:*
    <2>1. The complete solution set is the 1-dimensional complex subspace:
        $$\operatorname{Sol} = \left\{ t \begin{bmatrix} 1 \\ -(1 + i) \end{bmatrix} \;\middle|\; t \in \mathbb{C} \right\} = \operatorname{span}_\mathbb{C} \left\{ \begin{bmatrix} 1 \\ -1 - i \end{bmatrix} \right\}.$$

<1>4. Conclusion:
    The solutions are all scalar multiples $x = t \begin{bmatrix} 1 \\ -1 - i \end{bmatrix}$ for $t \in \mathbb{C}$. Q.E.D.
:::
