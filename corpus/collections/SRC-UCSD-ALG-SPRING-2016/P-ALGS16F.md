---
schema: qual/card@1
id: P-ALGS16F
kind: problem
title: Solvability by radicals of $x^5 - 16x + 2 = 0$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Is the equation $x^5 - 16x + 2 = 0$ solvable in radicals?
:::

::: solution
**Goal:** Prove that the polynomial equation $f(x) = x^5 - 16x + 2 = 0$ is not solvable by radicals over $\mathbb{Q}$ by proving its Galois group is $S_5$.

<1>1. Irreducibility of $f(x)$ over $\mathbb{Q}$:
    *Proof:*
    <2>1. The polynomial $f(x) = x^5 - 16x + 2 \in \mathbb{Z}[x]$ is monic of degree 5.
    <2>2. The prime $p = 2$ divides all non-leading coefficients ($-16$ and $2$), but $p^2 = 4$ does not divide the constant term $2$.
    <2>3. By Eisenstein's Criterion at $p = 2$ and Gauss's Lemma, $f(x)$ is irreducible over $\mathbb{Q}$.
    <2>4. Therefore, the Galois group $G = \operatorname{Gal}(f/\mathbb{Q})$ acts transitively on the 5 complex roots of $f(x)$.
    <2>5. By the Orbit-Stabilizer Theorem, $5 \mid |G|$. By Cauchy's Theorem for groups, $G$ contains an element of order 5, which must be a 5-cycle in $S_5$.

<1>2. Number of real roots and existence of a 2-cycle:
    *Proof:*
    <2>1. Differentiating $f(x)$ on $\mathbb{R}$:
    $$f'(x) = 5x^4 - 16 = 0 \implies x = \pm \sqrt[4]{16/5} = \pm \frac{2}{\sqrt[4]{5}} \approx \pm 1.3374.$$
    <2>2. Evaluating $f(x)$ at key points:
    $$\lim_{x \to -\infty} f(x) = -\infty < 0,$$
    $$f(0) = 2 > 0,$$
    $$f(1) = 1 - 16 + 2 = -13 < 0,$$
    $$f(2) = 32 - 32 + 2 = 2 > 0.$$
    <2>3. By the Intermediate Value Theorem, $f(x)$ has at least 3 distinct real roots: one in $(-\infty, 0)$, one in $(0, 1)$, and one in $(1, 2)$.
    <2>4. By Rolle's Theorem, since $f'(x)$ has only 2 real roots, $f(x)$ can have at most 3 real roots.
    <2>5. Thus $f(x)$ has exactly 3 real roots and 2 non-real complex conjugate roots, say $\alpha, \bar{\alpha} \in \mathbb{C} \setminus \mathbb{R}$.
    <2>6. Complex conjugation $\tau: \mathbb{C} \to \mathbb{C}$ restricts to an automorphism in $G = \operatorname{Gal}(f/\mathbb{Q})$.
    <2>7. The map $\tau$ fixes each of the 3 real roots and transposes the 2 complex conjugate roots $\alpha \leftrightarrow \bar{\alpha}$.
    <2>8. Thus $\tau$ acts on the 5 roots as a 2-cycle (transposition).

<1>3. Identification of the Galois group as $S_5$:
    *Proof:*
    <2>1. A standard theorem in group theory states that for any prime $p$, any transitive subgroup of the symmetric group $S_p$ containing a transposition must be the entire symmetric group $S_p$.
    <2>2. By <1>1 and <1>2, $G \le S_5$ is a transitive subgroup containing a transposition $\tau$.
    <2>3. Therefore $G = \operatorname{Gal}(f/\mathbb{Q}) \cong S_5$.

<1>4. Solvability by radicals:
    *Proof:*
    <2>1. By the Galois Criterion for solvability by radicals, a polynomial $f(x) \in \mathbb{Q}[x]$ is solvable by radicals if and only if its Galois group $\operatorname{Gal}(f/\mathbb{Q})$ is a solvable group.
    <2>2. The alternating group $A_5$ is a simple non-abelian group of order 60, so $S_5$ is not a solvable group.
    <2>3. Therefore the equation $x^5 - 16x + 2 = 0$ is not solvable by radicals.
:::
