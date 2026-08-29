---
schema: qual/card@1
id: P-QX43E
kind: problem
title: Solving $\exp(A)=B$ over $\CC$ and over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Jordan Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
When and how can we solve the matrix equation $\exp(A) = B$?
Do it over the complex numbers and over the real numbers.
Give a counterexample with real entries.
:::

::: solution
**Goal:** Characterize the solvability of $\exp(A) = B$ over $\mathbb{C}$ and $\mathbb{R}$, describe the construction, and give a real counterexample.

<1>1. Solvability over the complex numbers $\mathbb{C}$:
    *Proof:*
    <2>1. **Necessary condition:** For any matrix $A \in M_n(\mathbb{C})$, $\det(\exp(A)) = e^{\operatorname{tr}(A)} \ne 0$. Thus $B$ must be invertible: $B \in \operatorname{GL}_n(\mathbb{C})$.
    <2>2. **Sufficiency:** Every invertible matrix $B \in \operatorname{GL}_n(\mathbb{C})$ has a matrix logarithm $A = \log(B) \in M_n(\mathbb{C})$ such that $\exp(A) = B$.
    <2>3. **Construction via Jordan Canonical Form:**
        - Put $B = P J P^{-1}$ where $J = \operatorname{diag}(J_{k_1}(\lambda_1), \dots, J_{k_m}(\lambda_m))$. Since $B$ is invertible, each eigenvalue $\lambda_j \ne 0$.
        - For each Jordan block $J_k(\lambda) = \lambda (I + N)$ where $N = \frac{1}{\lambda} (J_k(\lambda) - \lambda I)$ is nilpotent ($N^k = 0$):
            $$\log(J_k(\lambda)) = (\log\lambda) I + \sum_{m=1}^{k-1} \frac{(-1)^{m-1}}{m} N^m$$
            where $\log\lambda$ is any chosen branch of the natural logarithm of $\lambda \in \mathbb{C}^\times$.
        - Then $A = P \operatorname{diag}(\log(J_{k_1}(\lambda_1)), \dots, \log(J_{k_m}(\lambda_m))) P^{-1}$ satisfies $\exp(A) = B$.

<1>2. Solvability over the real numbers $\mathbb{R}$:
    *Proof:*
    <2>1. **Necessary condition:** $B \in \operatorname{GL}_n(\mathbb{R})$ and $\det(B) = \det(\exp(A)) = e^{\operatorname{tr}(A)} > 0$ (if $A$ is real, $\operatorname{tr}(A) \in \mathbb{R}$, so $e^{\operatorname{tr}(A)} > 0$).
    <2>2. **Full classification criterion (Culver's Theorem, 1966):**
        $B \in \operatorname{GL}_n(\mathbb{R})$ has a real logarithm $A \in M_n(\mathbb{R})$ if and only if $B$ is invertible and, in the Jordan decomposition of $B$, every Jordan block corresponding to a negative real eigenvalue occurs an even number of times with the same size.
    <2>3. **Construction when valid:**
        - Pair conjugate complex eigenvalues and pair identical negative real Jordan blocks:
            Two identical $1 \times 1$ blocks $[-a]$ and $[-a]$ ($a > 0$) combine to $\begin{pmatrix} -a & 0 \\ 0 & -a \end{pmatrix} = \exp\begin{pmatrix} \ln a & \pi \\ -\pi & \ln a \end{pmatrix}$.
        - Positive eigenvalues use the standard real Mercator series on their Jordan blocks.

<1>3. Counterexample with real entries:
    *Proof:*
    <2>1. Consider $B = \begin{pmatrix} -1 & 0 \\ 0 & -2 \end{pmatrix} \in \operatorname{GL}_2(\mathbb{R})$.
    <2>2. Note $\det(B) = 2 > 0$, so the determinant condition alone is not sufficient.
    <2>3. The eigenvalues of $B$ are $\lambda_1 = -1$ and $\lambda_2 = -2$, both negative, but they have distinct eigenvalues (different sizes/values, so they cannot be paired into a $2 \times 2$ block with complex conjugate logarithm).
    <2>4. If $\exp(A) = B$ for real $A$, the eigenvalues $\mu_1, \mu_2$ of $A$ must satisfy $e^{\mu_1} = -1$ and $e^{\mu_2} = -2$.
    <2>5. This forces $\mu_1 = i(2k+1)\pi$ and $\mu_2 = \ln 2 + i(2m+1)\pi$ for some $k, m \in \mathbb{Z}$.
    <2>6. Since $A$ is a real $2 \times 2$ matrix, its non-real eigenvalues must occur in complex conjugate pairs: $\mu_2 = \overline{\mu_1}$.
    <2>7. But $\operatorname{Re}(\mu_1) = 0 \ne \ln 2 = \operatorname{Re}(\mu_2)$, so $\mu_1$ and $\mu_2$ cannot be conjugates.
    <2>8. Thus no such real matrix $A$ exists.

<1>4. Conclusion:
    $\exp(A) = B$ is always solvable over $\mathbb{C}$ for any $B \in \operatorname{GL}_n(\mathbb{C})$, and solvable over $\mathbb{R}$ iff negative Jordan blocks pair up identically. $B = \operatorname{diag}(-1, -2)$ is a real counterexample. Q.E.D.
:::
