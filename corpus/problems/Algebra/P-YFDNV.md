---
schema: qual/card@1
id: P-YFDNV
kind: problem
title: Real division algebras
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Classification
  - Semisimplicity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State Frobenius's Theorem classifying all finite-dimensional associative division algebras over the real numbers $\mathbb{R}$, and state the generalized Hurwitz / Adams theorem for normed / alternative division algebras.
:::

::: solution
**Goal:** Classify real division algebras via Frobenius's Theorem ($\mathbb{R}, \mathbb{C}, \mathbb{H}$) and Hurwitz's Theorem ($\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$).

<1>1. Frobenius's Theorem (Associative Division Algebras over $\mathbb{R}$):
    *Proof:*
    <2>1. **Theorem (Frobenius, 1877):** Every finite-dimensional associative division algebra $D$ over the field of real numbers $\mathbb{R}$ is isomorphic to one of the following three algebras:
        1. $\mathbb{R}$ (the real numbers, dimension 1, commutative).
        2. $\mathbb{C}$ (the complex numbers, dimension 2, commutative).
        3. $\mathbb{H}$ (the Hamilton quaternions, dimension 4, non-commutative).
    <2>2. **Sketch of Proof:**
        - For any element $x \in D \setminus \mathbb{R}$, the commutative subalgebra $\mathbb{R}(x) \subset D$ is a finite field extension of $\mathbb{R}$.
        - Since $\mathbb{R}$ has algebraic closure $\mathbb{C}$, the minimal polynomial of $x$ has degree 1 or 2. If irreducible of degree 2, $\mathbb{R}(x) \cong \mathbb{C}$.
        - If $D = \mathbb{R}$ or $D \cong \mathbb{C}$, we are done.
        - Otherwise, $D$ contains a copy of $\mathbb{C} = \mathbb{R}(i)$ where $i^2 = -1$.
        - The linear operator $\operatorname{ad}_i(y) = i y i^{-1}$ on $D$ satisfies $(\operatorname{ad}_i)^2 = \operatorname{id}$, giving an eigenspace decomposition $D = D_+ \oplus D_-$.
        - $D_+ = C_D(i) \cong \mathbb{C}$, and choosing $j \in D_-$ with $j^2 = -1$ gives $ij = -ji = k$ and $k^2 = -1$.
        - This forces $D = \operatorname{span}_\mathbb{R}\{1, i, j, k\} \cong \mathbb{H}$.

<1>2. Hurwitz's Theorem (Normed / Composition Algebras):
    *Proof:*
    <2>1. If the associativity condition is relaxed to **alternative algebras** ($x(xy) = (xx)y$ and $(yx)x = y(xx)$) or **normed division algebras** ($\|xy\| = \|x\|\|y\|$):
    <2>2. **Theorem (Hurwitz, 1898):** There are exactly four finite-dimensional real normed division algebras up to isomorphism:
        1. $\mathbb{R}$ (Real numbers, dimension 1).
        2. $\mathbb{C}$ (Complex numbers, dimension 2).
        3. $\mathbb{H}$ (Quaternions, dimension 4).
        4. $\mathbb{O}$ (Octonions / Cayley numbers, dimension 8, non-associative, alternative).

<1>3. Adams's Hopf Invariant One Theorem (General Real Division Algebras):
    *Proof:*
    <2>1. By the Bott–Milnor–Kervaire Theorem (1958) and Adams's theorem on vector fields on spheres / Hopf invariant one, any finite-dimensional (possibly non-associative) real division algebra must have dimension:
        $$\dim_\mathbb{R}(D) \in \{1, 2, 4, 8\}.$$

<1>4. Conclusion:
    The associative real division algebras are $\mathbb{R}, \mathbb{C}, \mathbb{H}$ (Frobenius), and the alternative/normed ones include $\mathbb{O}$ (Hurwitz). Q.E.D.
:::
