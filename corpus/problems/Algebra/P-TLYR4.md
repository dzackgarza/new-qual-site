---
schema: qual/card@1
id: P-TLYR4
kind: problem
title: Finite-dimensional division algebras over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Semisimplicity
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Classify all finite-dimensional (associative) **division algebras** over the field of real numbers $\mathbb{R}$ (Frobenius' Theorem).
:::

::: solution
**Goal:** State Frobenius' Theorem and prove that every finite-dimensional associative division algebra over $\mathbb{R}$ is isomorphic to $\mathbb{R}$, $\mathbb{C}$, or the Hamilton quaternions $\mathbb{H}$.

<1>1. Frobenius' Theorem (1877):
    *Proof:*
    <2>1. **Theorem:** Let $D$ be a finite-dimensional associative division algebra over $\mathbb{R}$.
        Then $D$ is isomorphic to exactly one of the following three division algebras:
        1. The field of real numbers $\mathbb{R}$ (dimension 1, commutative).
        2. The field of complex numbers $\mathbb{C}$ (dimension 2, commutative).
        3. The division ring of Hamilton quaternions $\mathbb{H}$ (dimension 4, non-commutative).

<1>2. Proof Step 1: Commutative Division Algebras over $\mathbb{R}$:
    *Proof:*
    <2>1. Suppose $D$ is commutative. Then $D$ is a field extension of $\mathbb{R}$ of finite degree $[D : \mathbb{R}] = n < \infty$.
    <2>2. Since $D/\mathbb{R}$ is algebraic and finite, by the Primitive Element Theorem $D \cong \mathbb{R}(\alpha) \cong \mathbb{R}[x]/(p(x))$ where $p(x) \in \mathbb{R}[x]$ is an irreducible polynomial.
    <2>3. By the **Fundamental Theorem of Algebra**, the only irreducible polynomials in $\mathbb{R}[x]$ have degree 1 (yielding $D \cong \mathbb{R}$) or degree 2 with negative discriminant (yielding $D \cong \mathbb{R}[x]/(x^2 + 1) \cong \mathbb{C}$).
    <2>4. Thus, if $D$ is commutative, $D \cong \mathbb{R}$ or $D \cong \mathbb{C}$.

<1>3. Proof Step 2: Non-Commutative Division Algebras over $\mathbb{R}$:
    *Proof:*
    <2>1. Suppose $D$ is non-commutative.
    <2>2. The center $Z(D)$ is a commutative division algebra over $\mathbb{R}$, and since $\mathbb{C}$ has no non-trivial central simple division algebras (as $\mathbb{C}$ is algebraically closed and Brauer group $\operatorname{Br}(\mathbb{C}) = 0$), we must have $Z(D) \cong \mathbb{R}$.
    <2>3. For any $x \in D \setminus \mathbb{R}$, the commutative subfield $\mathbb{R}(x) \subset D$ is isomorphic to $\mathbb{C}$.
    <2>4. In particular, the minimal polynomial of $x$ over $\mathbb{R}$ is a quadratic $x^2 - 2a x + (a^2 + b^2) = 0$ with $b > 0$.
    <2>5. Setting $i = (x - a)/b$, we find $i^2 = -1$.
    <2>6. Consider the linear operator $\operatorname{ad}_i: D \to D$ given by $\operatorname{ad}_i(y) = i y - y i$.
    <2>7. Since $\operatorname{ad}_i^2(y) + 4y = (i \cdot (i y - y i) - (i y - y i) \cdot i) = -2y - 2 i y i$, decomposing $D$ under the involution $y \mapsto i y i$ splits $D = D^+ \oplus D^-$ where $D^+ = \{y \in D \mid i y = y i\} = \mathbb{C}$ and $D^- = \{y \in D \mid i y = -y i\}$.
    <2>8. Since $D \ne \mathbb{C}$, there exists a non-zero $j \in D^-$ with $i j = -j i$.
    <2>9. $j^2$ commutes with $i$ ($i j^2 = -j i j = j^2 i$), so $j^2 \in \mathbb{C}$. But $j^2 \in \mathbb{R}$ and $j^2 < 0$. Normalizing $j$, we get $j^2 = -1$.
    <2>10. Defining $k = i j = -j i$, we obtain $k^2 = (i j)(i j) = -i j^2 i = i^2 = -1$.
    <2>11. The elements $\{1, i, j, k\}$ form an $\mathbb{R}$-basis of a 4-dimensional subalgebra of $D$ isomorphic to $\mathbb{H}$.
    <2>12. Since $\mathbb{H}$ has no non-trivial commutators in $D$, $D = \mathbb{H}$.

<1>4. Non-Associative Extension (Hurwitz Theorem):
    *Proof:*
    <2>1. (If associativity is relaxed, the only finite-dimensional alternative division algebra is the 8-dimensional Octonions $\mathbb{O}$).

<1>5. Conclusion:
    The only finite-dimensional associative division algebras over $\mathbb{R}$ are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$. Q.E.D.
:::
