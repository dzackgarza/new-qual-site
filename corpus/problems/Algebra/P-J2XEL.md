---
schema: qual/card@1
id: P-J2XEL
kind: problem
title: Diagonalizable matrices are dense over $\CC$ and Zariski-dense over an algebraically
  closed field
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Matrices
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) Prove that the set of diagonalizable $N \times N$ matrices over $\mathbb{C}$ is **dense** in $M_N(\mathbb{C})$ in the standard Euclidean/metric topology.
(2) Prove that over any algebraically closed field $K$, the set of diagonalizable matrices is **Zariski dense** in $M_N(K) \cong \mathbb{A}^{N^2}$.
:::

::: solution
**Goal:** Prove density of diagonalizable matrices in both metric topology over $\mathbb{C}$ and Zariski topology over algebraically closed $K$.

<1>1. Criterion for Diagonalizability (Distinct Eigenvalues):
    *Proof:*
    <2>1. Let $A \in M_N(K)$ be an $N \times N$ matrix.
    <2>2. The characteristic polynomial of $A$ is $p_A(t) = \det(t I_N - A) = t^N - c_1 t^{N-1} + \dots + (-1)^N c_N \in K[t]$.
    <2>3. If $p_A(t)$ has $N$ **distinct roots** (eigenvalues) in $K$, then $A$ has $N$ linearly independent eigenvectors, which implies that $A$ is **diagonalizable**.
    <2>4. The condition that $p_A(t)$ has distinct roots is equivalent to the non-vanishing of its **discriminant**:
        $$\Delta(A) \coloneqq \operatorname{Disc}(p_A) = \prod_{1 \le i < j \le N} (\lambda_i - \lambda_j)^2 \ne 0.$$
    <2>5. Since the coefficients of $p_A(t)$ are polynomials in the entries $a_{i, j}$ of $A$, the discriminant $\Delta(A) = \mathcal{D}(a_{1, 1}, \dots, a_{N, N})$ is a **non-zero polynomial** in the $N^2$ matrix variables:
        $$\mathcal{D} \in K[x_{1, 1}, x_{1, 2}, \dots, x_{N, N}] \setminus \{0\}.$$
    <2>6. (Non-zeroness: for the diagonal matrix $D = \operatorname{diag}(1, 2, \dots, N)$, $\Delta(D) = \prod_{i < j} (i - j)^2 \ne 0$).

<1>2. Proof of Metric Density over $\mathbb{C}$:
    *Proof:*
    <2>1. By Schur's Triangularization Theorem, every matrix $A \in M_N(\mathbb{C})$ is unitarily similar to an upper triangular matrix:
        $$A = U T U^*$$
        where $U \in \operatorname{U}(N)$ is unitary and $T$ is upper triangular with diagonal entries $\lambda_1, \lambda_2, \dots, \lambda_N$ (the eigenvalues of $A$).
    <2>2. For each $\varepsilon > 0$, choose small perturbations $\delta_1, \delta_2, \dots, \delta_N \in \mathbb{C}$ such that $|\delta_k| < \varepsilon$ and all numbers $\lambda_k + \delta_k$ are **mutually distinct**.
    <2>3. Let $T_\varepsilon = T + \operatorname{diag}(\delta_1, \dots, \delta_N)$, and define $A_\varepsilon = U T_\varepsilon U^*$.
    <2>4. Then $A_\varepsilon$ has $N$ distinct eigenvalues, so $A_\varepsilon$ is **diagonalizable**.
    <2>5. Furthermore, $\|A - A_\varepsilon\|_2 = \|U (T - T_\varepsilon) U^*\|_2 = \|\operatorname{diag}(\delta_1, \dots, \delta_N)\|_2 = \max |\delta_k| < \varepsilon$.
    <2>6. Since $\varepsilon > 0$ was arbitrary, the diagonalizable matrices are **dense in $M_N(\mathbb{C})$**.

<1>3. Proof of Zariski Density over an Algebraically Closed Field $K$:
    *Proof:*
    <2>1. In the Zariski topology on the affine space $\mathbb{A}^{N^2} \cong M_N(K)$, the closed sets are algebraic zero sets $V(S)$ of polynomial ideals.
    <2>2. Consider the principal open set (distinguished open set):
        $$U_\Delta \coloneqq \{A \in M_N(K) \mid \Delta(A) \ne 0\}.$$
    <2>3. By Step <1>1, every matrix in $U_\Delta$ has distinct eigenvalues, hence is diagonalizable:
        $$U_\Delta \subseteq \operatorname{Diag}_N(K) \subseteq M_N(K).$$
    <2>4. Since $\Delta$ is not the zero polynomial, $U_\Delta$ is a **non-empty Zariski open set**.
    <2>5. Over an algebraically closed field $K$, affine space $\mathbb{A}^{N^2}$ is an **irreducible algebraic variety**.
    <2>6. In an irreducible variety, every non-empty open set is **dense**:
        $$\overline{U_\Delta}^{\text{Zar}} = \mathbb{A}^{N^2} = M_N(K).$$
    <2>7. Since $U_\Delta \subseteq \operatorname{Diag}_N(K)$, the Zariski closure of the diagonalizable matrices contains $\overline{U_\Delta}^{\text{Zar}} = M_N(K)$.
    <2>8. Thus $\overline{\operatorname{Diag}_N(K)}^{\text{Zar}} = M_N(K)$, so diagonalizable matrices are **Zariski dense**.

<1>4. Conclusion:
    Matrices with distinct eigenvalues form a dense set under both Euclidean and Zariski topologies. Q.E.D.
:::
