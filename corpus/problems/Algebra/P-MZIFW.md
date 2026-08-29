---
schema: qual/card@1
id: P-MZIFW
kind: problem
title: Operators to which the spectral theorem for symmetric matrices generalizes
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Inner Product Spaces
  - Functional Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
To which classes of operators does the classical Spectral Theorem for real symmetric matrices generalize? State the key theorems.
:::

::: solution
**Goal:** Outline the hierarchy of generalizations of the Spectral Theorem: Hermitian/Normal matrices, Compact self-adjoint operators, and Bounded/Unbounded Self-Adjoint operators on Hilbert spaces.

<1>1. Finite-Dimensional Generalizations:
    *Proof:*
    <2>1. **Complex Hermitian Matrices ($A = A^*$):**
        - Every Hermitian matrix $A \in M_n(\mathbb{C})$ possesses an orthonormal basis of eigenvectors with real eigenvalues $\lambda_i \in \mathbb{R}$.
        - $A = U \Lambda U^*$ with $U \in \operatorname{U}(n)$ and $\Lambda \in M_n(\mathbb{R})$ diagonal.
    <2>2. **Normal Matrices ($A A^* = A^* A$):**
        - A matrix $A \in M_n(\mathbb{C})$ is unitarily diagonalizable if and only if $A$ is **normal** ($A A^* = A^* A$).
        - Special subclasses: Unitary matrices ($U^* U = I$, $|\lambda| = 1$), Skew-Hermitian matrices ($A^* = -A$, $\lambda \in i\mathbb{R}$), Orthogonal matrices in $M_n(\mathbb{R})$ (block-diagonalized with $2 \times 2$ rotation blocks and $\pm 1$).

<1>2. Compact Operators on Hilbert Spaces (Hilbert–Schmidt Spectral Theorem):
    *Proof:*
    <2>1. **Compact Self-Adjoint Operators ($T = T^* \in \mathcal{K}(H)$):**
        - Let $H$ be a separable Hilbert space and $T: H \to H$ a compact self-adjoint operator.
        - Then $H$ has an orthonormal basis $\{e_n\}$ of eigenvectors of $T$ with real eigenvalues $\lambda_n \to 0$:
            $$T = \sum_{n=1}^\infty \lambda_n \langle \cdot, e_n \rangle e_n.$$
    <2>2. **Compact Normal Operators ($T T^* = T^* T \in \mathcal{K}(H)$):**
        - Similarly, compact normal operators admit an orthonormal basis of eigenvectors with complex eigenvalues tending to 0.

<1>3. Bounded Self-Adjoint Operators on Hilbert Spaces:
    *Proof:*
    <2>1. **Multiplication Operator Form:**
        - Every bounded self-adjoint operator $T \in \mathcal{B}(H)$ is unitarily equivalent to a multiplication operator $M_f: L^2(X, \mu) \to L^2(X, \mu)$ defined by $(M_f \psi)(x) = f(x)\psi(x)$ for a bounded real-valued measurable function $f \in L^\infty(X, \mu)$.
    <2>2. **Projection-Valued Measure (Spectral Measure) Form:**
        - There exists a unique projection-valued measure $E$ on the Borel $\sigma$-algebra of the spectrum $\sigma(T) \subset \mathbb{R}$ such that:
            $$T = \int_{\sigma(T)} \lambda \, dE(\lambda).$$
    <2>3. **Continuous Functional Calculus:**
        - Provides an isometric $*$-isomorphism $C(\sigma(T)) \to C^*(T) \subset \mathcal{B}(H)$ sending $f \mapsto f(T)$.

<1>4. Unbounded Self-Adjoint Operators (Quantum Mechanics / Differential Operators):
    *Proof:*
    <2>1. For densely defined unbounded self-adjoint operators $T: \mathcal{D}(T) \to H$ with $T = T^*$, the spectral theorem holds via projection-valued measures supported on the closed (possibly unbounded) spectrum $\sigma(T) \subseteq \mathbb{R}$:
        $$T = \int_{-\infty}^\infty \lambda \, dE(\lambda).$$
    <2>2. This applies to fundamental differential operators like the Laplacian $\Delta$, momentum $-i\nabla$, and Schrödinger Hamiltonians $H = -\Delta + V$.

<1>5. Conclusion:
    The spectral theorem generalizes from symmetric matrices $\to$ normal matrices $\to$ compact self-adjoint/normal operators $\to$ bounded self-adjoint operators (spectral measures / multiplication operators) $\to$ unbounded self-adjoint operators. Q.E.D.
:::
