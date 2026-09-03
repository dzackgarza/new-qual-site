---
schema: qual/card@1
id: E-2KJEL
kind: problem
title: "The Jordan canonical form of a matrix"
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Matrices
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

:::{.exercise}
Determine $\operatorname{JCF}(B)$ for
\[
B :=
\begin{pmatrix}
5 & -1 & 0 & 0 \\
9 & -1 & 0 & 0 \\
0 & 0 & 7 & -2 \\
0 & 0 & 12 & -3
\end{pmatrix}
.\]

:::

::: solution
**Goal:** Determine the Jordan Canonical Form $\operatorname{JCF}(B)$ of the block-diagonal matrix $B = B_1 \oplus B_2$.

<1>1. Block decomposition:
    The matrix $B$ is block diagonal:
    $$B = \begin{pmatrix} B_1 & 0 \\ 0 & B_2 \end{pmatrix}, \quad \text{where } B_1 = \begin{pmatrix} 5 & -1 \\ 9 & -1 \end{pmatrix} \text{ and } B_2 = \begin{pmatrix} 7 & -2 \\ 12 & -3 \end{pmatrix}.$$
    Hence $\operatorname{JCF}(B) = \operatorname{JCF}(B_1) \oplus \operatorname{JCF}(B_2)$.

<1>2. Jordan form of $B_1$:
    $\operatorname{JCF}(B_1) = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
    *Proof:*
    <2>1. Characteristic polynomial of $B_1$:
        $$p_1(\lambda) = \det(\lambda I - B_1) = (\lambda - 5)(\lambda + 1) - (-1)(9) = \lambda^2 - 4\lambda + 4 = (\lambda - 2)^2.$$
        Thus $\lambda = 2$ is the unique eigenvalue with algebraic multiplicity 2.
    <2>2. Eigenspace and geometric multiplicity:
        $$B_1 - 2I = \begin{pmatrix} 3 & -1 \\ 9 & -3 \end{pmatrix}.$$
        Since $\operatorname{rank}(B_1 - 2I) = 1$, the geometric multiplicity is $\operatorname{nullity}(B_1 - 2I) = 2 - 1 = 1$.
    <2>3. Since the geometric multiplicity is 1, there is a single Jordan block of size 2 associated with $\lambda = 2$, so $J(B_1) = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.

<1>3. Jordan form of $B_2$:
    $\operatorname{JCF}(B_2) = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$.
    *Proof:*
    <2>1. Characteristic polynomial of $B_2$:
        $$p_2(\lambda) = \det(\lambda I - B_2) = (\lambda - 7)(\lambda + 3) - (-2)(12) = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3).$$
    <2>2. The eigenvalues are $\lambda_1 = 1$ and $\lambda_2 = 3$, both having algebraic multiplicity 1.
    <2>3. Since all eigenvalues are distinct, $B_2$ is diagonalizable, giving two $1 \times 1$ Jordan blocks $J_1(1)$ and $J_1(3)$.

<1>4. Conclusion:
    Combining the Jordan blocks of $B_1$ and $B_2$, the Jordan Canonical Form of $B$ (unique up to ordering of blocks) is:
    $$\operatorname{JCF}(B) = \begin{pmatrix}
    2 & 1 & 0 & 0 \\
    0 & 2 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 3
    \end{pmatrix}.$$
    Q.E.D.
:::

