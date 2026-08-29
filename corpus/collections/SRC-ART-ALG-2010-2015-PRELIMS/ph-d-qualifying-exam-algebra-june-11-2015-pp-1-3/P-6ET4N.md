---
schema: qual/card@1
id: P-6ET4N
kind: problem
title: Rational and Jordan canonical forms of a $3\times 3$ real matrix; abelian groups
  of order $360$
classification:
  areas:
  - prelim
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
(a) Find a **Rational Canonical Form** and a **Jordan Canonical Form** for the following $3 \times 3$ matrix with real entries:
$$A = \begin{pmatrix} 0 & -1 & 2 \\ 3 & -4 & 6 \\ 2 & -2 & 3 \end{pmatrix}.$$

(b) Describe all distinct isomorphism classes of **Abelian groups of order 360**.
:::

::: solution
**Goal:** Compute the characteristic polynomial, minimal polynomial, rational/Jordan canonical forms of $A$, and classify abelian groups of order $360 = 2^3 \cdot 3^2 \cdot 5$.

<1>1. Part (a): Characteristic and Minimal Polynomial of $A$:
    *Proof:*
    <2>1. Compute the characteristic polynomial $p_A(\lambda) = \det(\lambda I - A)$:
        $$\lambda I - A = \begin{pmatrix} \lambda & 1 & -2 \\ -3 & \lambda + 4 & -6 \\ -2 & 2 & \lambda - 3 \end{pmatrix}.$$
    <2>2. We compute the determinant by expanding along row 1:
        $$\det(\lambda I - A) = \lambda \left( (\lambda+4)(\lambda-3) - (-12) \right) - 1 \left( -3(\lambda-3) - 12 \right) - 2 \left( -6 - (-2)(\lambda+4) \right)$$
        $$= \lambda (\lambda^2 + \lambda - 12 + 12) - (-3\lambda + 9 - 12) - 2 (-6 + 2\lambda + 8)$$
        $$= \lambda (\lambda^2 + \lambda) - (-3\lambda - 3) - 2(2\lambda + 2)$$
        $$= \lambda^3 + \lambda^2 + 3\lambda + 3 - 4\lambda - 4$$
        $$= \lambda^3 + \lambda^2 - \lambda - 1 = \lambda^2(\lambda + 1) - (\lambda + 1) = (\lambda^2 - 1)(\lambda + 1) = (\lambda - 1)(\lambda + 1)^2.$$
    <2>3. The eigenvalues of $A$ are $\lambda_1 = 1$ (multiplicity 1) and $\lambda_2 = -1$ (multiplicity 2).
    <2>4. We compute the eigenspace for $\lambda = -1$:
        $$-I - A = \begin{pmatrix} -1 & 1 & -2 \\ -3 & 3 & -6 \\ -2 & 2 & -4 \end{pmatrix} \xrightarrow{\text{RREF}} \begin{pmatrix} 1 & -1 & 2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
    <2>5. The nullity is $\operatorname{nullity}(-I - A) = 3 - 1 = 2$.
    <2>6. Since the geometric multiplicity of $\lambda = -1$ equals its algebraic multiplicity (2), the matrix $A$ is **diagonalizable**!
    <2>7. The minimal polynomial is square-free:
        $$m_A(\lambda) = (\lambda - 1)(\lambda + 1) = \lambda^2 - 1.$$

<1>2. Part (a): Canonical Forms:
    *Proof:*
    <2>1. **Jordan Canonical Form $J$:**
        Since $A$ is diagonalizable over $\mathbb{R}$ with eigenvalues $1, -1, -1$:
        $$J = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix}.$$
    <2>2. **Rational Canonical Form $R$:**
        - The invariant factors $d_1(\lambda) \mid d_2(\lambda)$ must satisfy $d_2(\lambda) = m_A(\lambda) = \lambda^2 - 1$ and $d_1(\lambda) d_2(\lambda) = p_A(\lambda) = (\lambda+1)(\lambda^2-1)$.
        - Thus the invariant factors are:
          $$d_1(\lambda) = \lambda + 1, \qquad d_2(\lambda) = \lambda^2 - 1.$$
        - The companion matrix for $d_1(\lambda) = \lambda + 1$ is $[-1]$.
        - The companion matrix for $d_2(\lambda) = \lambda^2 - 1$ is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
        - Thus the Rational Canonical Form (in companion block form) is:
          $$R = \begin{pmatrix} -1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}.$$

<1>3. Part (b): Abelian Groups of Order $360$:
    *Proof:*
    <2>1. Factor $360 = 2^3 \cdot 3^2 \cdot 5^1$.
    <2>2. By the Fundamental Theorem of Finitely Generated Abelian Groups, $G \cong P_2 \times P_3 \times P_5$ where:
        - $P_2$ is an abelian group of order $2^3 = 8$. The partitions of 3 are:
          1. $3 \implies \mathbb{Z}_8$,
          2. $2 + 1 \implies \mathbb{Z}_4 \times \mathbb{Z}_2$,
          3. $1 + 1 + 1 \implies \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2$ (3 possibilities).
        - $P_3$ is an abelian group of order $3^2 = 9$. The partitions of 2 are:
          1. $2 \implies \mathbb{Z}_9$,
          2. $1 + 1 \implies \mathbb{Z}_3 \times \mathbb{Z}_3$ (2 possibilities).
        - $P_5$ is an abelian group of order $5^1 = 5$:
          1. $1 \implies \mathbb{Z}_5$ (1 possibility).
    <2>3. Total number of isomorphism classes:
        $$p(3) \cdot p(2) \cdot p(1) = 3 \cdot 2 \cdot 1 = 6.$$
    <2>4. The 6 distinct isomorphism classes are:
        1. $\mathbb{Z}_8 \times \mathbb{Z}_9 \times \mathbb{Z}_5 \cong \mathbb{Z}_{360}$
        2. $\mathbb{Z}_8 \times \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_5 \cong \mathbb{Z}_3 \times \mathbb{Z}_{120}$
        3. $\mathbb{Z}_4 \times \mathbb{Z}_2 \times \mathbb{Z}_9 \times \mathbb{Z}_5 \cong \mathbb{Z}_2 \times \mathbb{Z}_{180}$
        4. $\mathbb{Z}_4 \times \mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_5 \cong \mathbb{Z}_6 \times \mathbb{Z}_{60}$
        5. $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_9 \times \mathbb{Z}_5 \cong \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_{90}$
        6. $\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_3 \times \mathbb{Z}_5 \cong \mathbb{Z}_2 \times \mathbb{Z}_6 \times \mathbb{Z}_{30}$.

<1>4. Conclusion:
    (a) $J = \operatorname{diag}(1, -1, -1)$, $R = \operatorname{diag}([-1], \begin{pmatrix}0&1\\1&0\end{pmatrix})$;
    (b) Exactly 6 isomorphism classes of abelian groups of order 360. Q.E.D.
:::
