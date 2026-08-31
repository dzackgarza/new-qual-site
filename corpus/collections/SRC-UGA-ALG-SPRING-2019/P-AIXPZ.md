---
schema: qual/card@1
id: P-AIXPZ
kind: problem
title: Invertible matrices over $\CC$ with $A^{2019}$ diagonalizable are diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
  - Separability
relations: []
review: draft
---

::: problem
Let $A \in M_m(\mathbb{C})$ be an $m \times m$ matrix over the complex numbers. Suppose that $A$ is non-singular ($\det A \ne 0$) and that $A^k$ is diagonalizable over $\mathbb{C}$ for some integer $k \ge 1$ (for instance, $k = 2019$).

Show that $A$ is also diagonalizable over $\mathbb{C}$.
:::

::: solution
**Goal:** Prove that an invertible complex matrix whose power $A^k$ is diagonalizable must itself be diagonalizable, using the square-free criterion for minimal polynomials.

<1>1. Diagonalizability criterion and factorization of $m_{A^k}(x)$:
::: {.proof}
    <2>1. A matrix over $\mathbb{C}$ is diagonalizable if and only if its minimal polynomial is square-free (splits into distinct linear factors).
    <2>2. Since $A^k$ is diagonalizable over $\mathbb{C}$, its minimal polynomial $m_{A^k}(x) \in \mathbb{C}[x]$ factors as
    $$m_{A^k}(x) = \prod_{i=1}^r (x - \lambda_i),$$
    where $\lambda_1, \dots, \lambda_r \in \mathbb{C}$ are the distinct eigenvalues of $A^k$.

:::

<1>2. Non-zero eigenvalues:
::: {.proof}
    <2>1. Since $A$ is non-singular, $\det(A) \ne 0$.
    <2>2. By the multiplicative property of determinants, $\det(A^k) = (\det A)^k \ne 0$.
    <2>3. Since the determinant is the product of all eigenvalues with multiplicity, $0$ is not an eigenvalue of $A^k$.
    <2>4. Thus $\lambda_i \ne 0$ for each $i \in \{1, \dots, r\}$.

:::

<1>3. Annihilating polynomial $P(x) = m_{A^k}(x^k)$:
::: {.proof}
    <2>1. Define the polynomial $P(x) \in \mathbb{C}[x]$ by
    $$P(x) = m_{A^k}(x^k) = \prod_{i=1}^r (x^k - \lambda_i).$$
    <2>2. Evaluating $P$ on $A$:
    $$P(A) = m_{A^k}(A^k) = 0.$$
    <2>3. Since $P(A) = 0$, the minimal polynomial $m_A(x)$ of $A$ divides $P(x)$ in $\mathbb{C}[x]$.

:::

<1>4. $P(x)$ has distinct roots in $\mathbb{C}$:
::: {.proof}
    <2>1. For each $i \in \{1, \dots, r\}$, since $\lambda_i \ne 0$, the polynomial $x^k - \lambda_i$ has derivative $k x^{k-1} \ne 0$. The only root of the derivative is $x = 0$, which is not a root of $x^k - \lambda_i$ because $\lambda_i \ne 0$.
    <2>2. Thus $\gcd(x^k - \lambda_i, k x^{k-1}) = 1$, so each $x^k - \lambda_i$ has $k$ distinct roots in $\mathbb{C}$, given explicitly by
    $$\mu_{i, j} = \lambda_i^{1/k} e^{2\pi i j / k} \quad \text{for } j \in \{0, 1, \dots, k-1\}.$$
    <2>3. For $i \ne j$, the polynomials $x^k - \lambda_i$ and $x^k - \lambda_j$ share no roots: if $\alpha \in \mathbb{C}$ were a common root, then $\alpha^k = \lambda_i$ and $\alpha^k = \lambda_j$, implying $\lambda_i = \lambda_j$, a contradiction.
    <2>4. Therefore, $P(x) = \prod_{i=1}^r (x^k - \lambda_i)$ has exactly $k r$ distinct roots in $\mathbb{C}$.

:::

<1>5. Diagonalizability of $A$:
::: {.proof}
    <2>1. Since $m_A(x)$ divides $P(x)$ and $P(x)$ is a product of distinct linear factors over $\mathbb{C}$, $m_A(x)$ is also a product of distinct linear factors over $\mathbb{C}$.
    <2>2. By the criterion in <1>1, $A$ is diagonalizable over $\mathbb{C}$.

:::

<1>6. Conclusion:
::: {.proof}
    $A$ is diagonalizable over $\mathbb{C}$.
:::
:::
