---
schema: qual/card@1
id: P-ZYJDF
kind: problem
title: A polynomial with Galois group $\ZZ/3\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Construct an explicit polynomial over $\mathbb{Q}$ whose Galois group is the cyclic group of order 3:
$$\operatorname{Gal}(f/\mathbb{Q}) \cong \mathbb{Z}/3\mathbb{Z}.$$
Prove that your polynomial satisfies this condition.
:::

::: solution
**Goal:** Prove that the cubic polynomial $f(x) = x^3 - 3x + 1 \in \mathbb{Q}[x]$ (or $x^3 + x^2 - 2x - 1$) has Galois group $\operatorname{Gal}(f/\mathbb{Q}) \cong \mathbb{Z}/3\mathbb{Z}$.

<1>1. Selection of the Polynomial $f(x) = x^3 - 3x + 1$:
    *Proof:*
    <2>1. Consider the cubic polynomial:
        $$f(x) = x^3 - 3x + 1 \in \mathbb{Q}[x].$$
    <2>2. This polynomial arises naturally from the triple-angle formula $\cos(3\theta) = 4\cos^3(\theta) - 3\cos(\theta)$ for $\theta = 2\pi/9$: setting $x = 2\cos(2\pi/9)$ gives $x^3 - 3x = 2\cos(2\pi/3) = -1 \implies x^3 - 3x + 1 = 0$.

<1>2. Irreducibility of $f(x)$ over $\mathbb{Q}$:
    *Proof:*
    <2>1. By the **Rational Root Theorem**, any rational root of $f(x) = x^3 - 3x + 1$ must divide the constant term $1$, so the only possible rational roots are $\pm 1$.
    <2>2. We test both candidates:
        - $f(1) = 1^3 - 3(1) + 1 = -1 \ne 0$.
        - $f(-1) = (-1)^3 - 3(-1) + 1 = -1 + 3 + 1 = 3 \ne 0$.
    <2>3. Since $f(x)$ is a cubic polynomial with no rational roots, $f(x)$ is **irreducible over $\mathbb{Q}$**.
    <2>4. Therefore, the splitting field $L$ of $f(x)$ satisfies $[L : \mathbb{Q}] \in \{3, 6\}$, so $\operatorname{Gal}(f/\mathbb{Q}) \le S_3$ is a transitive subgroup of $S_3$, which means:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong A_3 \cong \mathbb{Z}_3 \quad \text{or} \quad \operatorname{Gal}(f/\mathbb{Q}) \cong S_3.$$

<1>3. Computation of the Discriminant $\Delta(f)$:
    *Proof:*
    <2>1. For a depressed cubic $x^3 + px + q$, the discriminant is given by the standard formula:
        $$\Delta = -4 p^3 - 27 q^2.$$
    <2>2. Here $p = -3$ and $q = 1$:
        $$\Delta = -4(-3)^3 - 27(1)^2 = -4(-27) - 27 = 108 - 27 = 81.$$
    <2>3. We observe that:
        $$\Delta = 81 = 9^2 = (3^2)^2 \in (\mathbb{Q}^\times)^2.$$
    <2>4. The discriminant $\Delta$ is a **perfect square** in $\mathbb{Q}$.

<1>4. Galois Group Classification for Irreducible Cubics:
    *Proof:*
    <2>1. By the fundamental classification theorem for Galois groups of irreducible cubic polynomials over $\mathbb{Q}$:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong \begin{cases} A_3 \cong \mathbb{Z}/3\mathbb{Z} & \text{if } \Delta \in (\mathbb{Q}^\times)^2, \\ S_3 & \text{if } \Delta \notin (\mathbb{Q}^\times)^2. \end{cases}$$
    <2>2. Since $\Delta = 81 = 9^2 \in (\mathbb{Q}^\times)^2$, the square root of the discriminant $\delta = \sqrt{\Delta} = 9$ already lies in $\mathbb{Q}$.
    <2>3. Therefore, every permutation in the Galois group must be an **even permutation**, which forces:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong A_3 \cong \mathbb{Z}/3\mathbb{Z}.$$

<1>5. Alternative Cyclic Cubic from $\mathbb{Q}(\zeta_7)$:
    *Proof:*
    <2>1. The polynomial $g(x) = x^3 + x^2 - 2x - 1$ has roots $2\cos(2\pi/7), 2\cos(4\pi/7), 2\cos(6\pi/7)$ generating the real subfield $\mathbb{Q}(\zeta_7)^+ \subset \mathbb{Q}(\zeta_7)$.
    <2>2. Its discriminant is $\Delta = 49 = 7^2$, giving another example with $\operatorname{Gal}(g/\mathbb{Q}) \cong \mathbb{Z}/3\mathbb{Z}$.

<1>6. Conclusion:
    $f(x) = x^3 - 3x + 1$ is irreducible with discriminant $\Delta = 81 = 9^2$, so $\operatorname{Gal}(f/\mathbb{Q}) \cong \mathbb{Z}/3\mathbb{Z}$. Q.E.D.
:::
