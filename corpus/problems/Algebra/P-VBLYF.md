---
schema: qual/card@1
id: P-VBLYF
kind: problem
title: Conjugacy classes in $\mathrm{GL}_2(\CC)$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Jordan Canonical Form
  - Matrix Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What are the conjugacy classes in $\operatorname{GL}_2(\mathbb{C})$?
:::

::: solution
**Goal:** Classify all conjugacy classes in $\operatorname{GL}_2(\mathbb{C})$ using the Jordan Canonical Form.

<1>1. General principle of conjugacy in $\operatorname{GL}_n(\mathbb{C})$:
    *Proof:*
    <2>1. Two matrices $A, B \in \operatorname{GL}_n(\mathbb{C})$ are conjugate (similar) if and only if there exists $P \in \operatorname{GL}_n(\mathbb{C})$ such that $B = P A P^{-1}$.
    <2>2. By Jordan Canonical Form theory over an algebraically closed field ($\mathbb{C}$), every matrix $A \in \operatorname{GL}_n(\mathbb{C})$ is conjugate to a unique Jordan matrix (up to permutation of Jordan blocks).
    <2>3. Since $A \in \operatorname{GL}_2(\mathbb{C})$ is invertible, its eigenvalues $\lambda_1, \lambda_2 \in \mathbb{C}^\times$ are non-zero.

<1>2. Classification of $2 \times 2$ Jordan forms:
    *Proof:*
    <2>1. The characteristic polynomial is $p_A(t) = (t - \lambda_1)(t - \lambda_2)$ with $\lambda_1, \lambda_2 \in \mathbb{C}^\times$.
    <2>2. We have three distinct geometric cases:
    <2>3. **Type I: Distinct eigenvalues ($\lambda_1 \ne \lambda_2$ in $\mathbb{C}^\times$):**
        - The matrix is diagonalizable with Jordan form:
            $$J = \begin{pmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{pmatrix}, \qquad \lambda_1 \ne \lambda_2 \in \mathbb{C}^\times.$$
        - Permuting $\lambda_1 \leftrightarrow \lambda_2$ gives the same conjugacy class: these classes are parameterized by unordered pairs of distinct non-zero complex numbers $\{\lambda_1, \lambda_2\}$.
    <2>4. **Type II: Equal eigenvalues, diagonalizable ($\lambda_1 = \lambda_2 = \lambda \in \mathbb{C}^\times$, scalar matrices):**
        - The matrix has two $1 \times 1$ Jordan blocks:
            $$J = \begin{pmatrix} \lambda & 0 \\ 0 & \lambda \end{pmatrix} = \lambda I_2, \qquad \lambda \in \mathbb{C}^\times.$$
        - These are central elements in $\operatorname{GL}_2(\mathbb{C})$, so each scalar matrix forms a singleton conjugacy class $\{\lambda I_2\}$.
    <2>5. **Type III: Equal eigenvalues, non-diagonalizable ($\lambda_1 = \lambda_2 = \lambda \in \mathbb{C}^\times$, one $2 \times 2$ Jordan block):**
        - The matrix has a single $2 \times 2$ Jordan block:
            $$J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}, \qquad \lambda \in \mathbb{C}^\times.$$
        - Each $\lambda \in \mathbb{C}^\times$ gives a distinct conjugacy class.

<1>3. Parametrization summary:
    *Proof:*
    <2>1. The conjugacy classes in $\operatorname{GL}_2(\mathbb{C})$ are precisely:
        1. $\operatorname{diag}(\lambda_1, \lambda_2)$ with $\lambda_1 \ne \lambda_2 \in \mathbb{C}^\times$ (parameterized by $(\mathbb{C}^\times \times \mathbb{C}^\times \setminus \Delta) / S_2$).
        2. $\operatorname{diag}(\lambda, \lambda)$ with $\lambda \in \mathbb{C}^\times$ (parameterized by $\mathbb{C}^\times$).
        3. $\begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$ with $\lambda \in \mathbb{C}^\times$ (parameterized by $\mathbb{C}^\times$).

<1>4. Conclusion:
    Every conjugacy class in $\operatorname{GL}_2(\mathbb{C})$ is represented by exactly one matrix of the form $\operatorname{diag}(\lambda_1, \lambda_2)$ ($\lambda_1 \le \lambda_2$ in some order), $\lambda I_2$, or $\begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$ with $\lambda_i, \lambda \in \mathbb{C}^\times$. Q.E.D.
:::
