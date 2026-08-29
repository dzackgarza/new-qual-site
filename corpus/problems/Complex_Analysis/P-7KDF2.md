---
schema: qual/card@1
id: P-7KDF2
kind: problem
title: The parallelogram identity for complex numbers and its geometric meaning
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$ for any two complex numbers $z_1, z_2 \in \mathbb{C}$, and explain the geometric meaning of this identity.
:::

::: solution
**Goal:** Prove the Parallelogram Law for complex numbers and explain its geometric interpretation.

<1>1. Algebraic Proof:
    *Proof:*
    <2>1. For any complex number $w \in \mathbb{C}$, $|w|^2 = w \overline{w}$.
    <2>2. Expand $|z_1 + z_2|^2$:
        $$|z_1 + z_2|^2 = (z_1 + z_2)(\overline{z_1 + z_2}) = (z_1 + z_2)(\overline{z_1} + \overline{z_2}) = |z_1|^2 + z_1 \overline{z_2} + z_2 \overline{z_1} + |z_2|^2.$$
    <2>3. Expand $|z_1 - z_2|^2$:
        $$|z_1 - z_2|^2 = (z_1 - z_2)(\overline{z_1 - z_2}) = (z_1 - z_2)(\overline{z_1} - \overline{z_2}) = |z_1|^2 - z_1 \overline{z_2} - z_2 \overline{z_1} + |z_2|^2.$$
    <2>4. Summing the two equations:
        $$\begin{aligned}
        |z_1 + z_2|^2 + |z_1 - z_2|^2 &= \left( |z_1|^2 + z_1 \overline{z_2} + z_2 \overline{z_1} + |z_2|^2 \right) + \left( |z_1|^2 - z_1 \overline{z_2} - z_2 \overline{z_1} + |z_2|^2 \right) \\
        &= 2|z_1|^2 + 2|z_2|^2 + (z_1 \overline{z_2} - z_1 \overline{z_2}) + (z_2 \overline{z_1} - z_2 \overline{z_1}) \\
        &= 2(|z_1|^2 + |z_2|^2).
        \end{aligned}$$

<1>2. Geometric Interpretation (The Parallelogram Law in Euclidean Geometry):
    *Proof:*
    <2>1. In the complex plane (or $\mathbb{R}^2$), let $0, z_1, z_1 + z_2, z_2$ be the four vertices of the parallelogram spanned by the vectors $z_1$ and $z_2$.
    <2>2. **Sides of the parallelogram:** The four sides have lengths:
        - Two sides have length $|z_1|$.
        - Two sides have length $|z_2|$.
        - The sum of the squares of the lengths of all four sides is:
            $$|z_1|^2 + |z_2|^2 + |z_1|^2 + |z_2|^2 = 2(|z_1|^2 + |z_2|^2).$$
    <2>3. **Diagonals of the parallelogram:**
        - The main diagonal connects $0$ to $z_1 + z_2$, with length $|z_1 + z_2|$.
        - The other diagonal connects $z_2$ to $z_1$, with length $|z_1 - z_2|$.
        - The sum of the squares of the lengths of the two diagonals is:
            $$|z_1 + z_2|^2 + |z_1 - z_2|^2.$$
    <2>4. **Geometric Theorem:** The identity asserts that in any Euclidean parallelogram, the sum of the squares of the lengths of the two diagonals is equal to the sum of the squares of the lengths of all four sides.

<1>3. Conclusion:
    The identity $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$ holds algebraically and geometrically expresses the classical Parallelogram Law. Q.E.D.
:::
