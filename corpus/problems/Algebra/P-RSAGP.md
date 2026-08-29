---
schema: qual/card@1
id: P-RSAGP
kind: problem
title: Bilinear forms and orthogonal matrices
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Matrix Groups
  - Quadratic Forms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) What is a bilinear form on a vector space $V$ over a field $K$?
(2) When are two bilinear forms equivalent (congruent)?
(3) What is an orthogonal matrix $Q \in \operatorname{O}(n)$, and what are its special geometric and algebraic properties?
:::

::: solution
**Goal:** Define bilinear forms, classify their equivalence (congruence) via change of basis, and characterize orthogonal matrices.

<1>1. Definition of a Bilinear Form:
    *Proof:*
    <2>1. Let $V$ be a vector space over a field $K$.
    <2>2. A **bilinear form** on $V$ is a function $B: V \times V \to K$ that is linear in each argument separately:
        - $B(u_1 + c u_2, v) = B(u_1, v) + c B(u_2, v)$,
        - $B(u, v_1 + c v_2) = B(u, v_1) + c B(u, v_2)$,
        for all $u, u_1, u_2, v, v_1, v_2 \in V$ and $c \in K$.
    <2>3. If $V$ is finite-dimensional with ordered basis $\mathcal{B} = \{e_1, \dots, e_n\}$, the **Gram matrix** of $B$ with respect to $\mathcal{B}$ is $[B]_\mathcal{B} \in M_n(K)$ with entries:
        $$([B]_\mathcal{B})_{ij} = B(e_i, e_j).$$
    <2>4. For vectors $x, y \in V$ with coordinate vectors $[x]_\mathcal{B}, [y]_\mathcal{B} \in K^n$:
        $$B(x, y) = [x]_\mathcal{B}^t [B]_\mathcal{B} [y]_\mathcal{B}.$$

<1>2. Equivalence (Congruence) of Bilinear Forms:
    *Proof:*
    <2>1. Two bilinear forms $B_1, B_2$ on $V$ are **equivalent** (isomorphic) if there exists an invertible linear map (change of basis) $T \in \operatorname{GL}(V)$ such that:
        $$B_2(u, v) = B_1(T u, T v) \quad \text{for all } u, v \in V.$$
    <2>2. In terms of Gram matrices, two matrices $M_1, M_2 \in M_n(K)$ represent the same bilinear form with respect to different bases if and only if they are **congruent**:
        $$M_2 = P^t M_1 P \quad \text{for some invertible } P \in \operatorname{GL}_n(K).$$

<1>3. Definition of an Orthogonal Matrix:
    *Proof:*
    <2>1. A real square matrix $Q \in M_n(\mathbb{R})$ is **orthogonal** if its transpose equals its inverse:
        $$Q^t Q = Q Q^t = I_n.$$
    <2>2. The set of all $n \times n$ orthogonal matrices forms the **orthogonal group** $\operatorname{O}(n) \le \operatorname{GL}_n(\mathbb{R})$.

<1>4. Special Properties of Orthogonal Matrices:
    *Proof:*
    <2>1. **Isometry of Euclidean Space:** $Q$ preserves the standard Euclidean inner product $\langle u, v \rangle = u^t v$:
        $$\langle Q u, Q v \rangle = (Q u)^t (Q v) = u^t Q^t Q v = u^t I_n v = \langle u, v \rangle.$$
        Consequently, $Q$ preserves Euclidean lengths ($\|Q v\| = \|v\|$), distances, and angles.
    <2>2. **Orthonormal Columns/Rows:** The columns (and rows) of $Q$ form an orthonormal basis of $\mathbb{R}^n$.
    <2>3. **Determinant:** $\det(Q^t Q) = \det(I_n) \implies (\det Q)^2 = 1 \implies \det Q \in \{+1, -1\}$.
        - If $\det Q = +1$, $Q \in \operatorname{SO}(n)$ represents a pure rotation.
        - If $\det Q = -1$, $Q$ represents a reflection or rotoreflection.
    <2>4. **Eigenvalues:** All complex eigenvalues of $Q$ lie on the unit circle $S^1 \subset \mathbb{C}$ ($|\lambda| = 1$), and non-real eigenvalues appear in conjugate pairs $e^{\pm i\theta}$.
    <2>5. **Preservation of Congruence vs Similarity:** For orthogonal matrices, congruence coincides with similarity ($Q^t A Q = Q^{-1} A Q$), which enables simultaneous diagonalization of symmetric bilinear forms and self-adjoint operators (the Spectral Theorem).

<1>5. Conclusion:
    Bilinear forms transform via congruence $P^t A P$, and orthogonal matrices ($Q^t Q = I$) are the metric-preserving isometries where congruence and similarity coincide. Q.E.D.
:::
