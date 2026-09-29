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

::: {.problem}
Let $A \in M_m(\mathbb{C})$ be an $m \times m$ matrix over the complex numbers. Suppose that $A$ is non-singular ($\det A \ne 0$) and that $A^k$ is diagonalizable over $\mathbb{C}$ for some integer $k \ge 1$ (for instance, $k = 2019$).

Show that $A$ is also diagonalizable over $\mathbb{C}$.
:::

::: {.solution}
**Goal:** Prove that an invertible complex matrix whose power $A^k$ is diagonalizable must itself be diagonalizable, using the square-free criterion for minimal polynomials.

::: pf

::: {.pf-step #s1}
Diagonalizability criterion and factorization of $m_{A^k}(x)$:

::: pf-proof

::: pf-step
A matrix over $\mathbb{C}$ is diagonalizable if and only if its minimal polynomial is square-free (splits into distinct linear factors).
:::

::: pf-step
Since $A^k$ is diagonalizable over $\mathbb{C}$, its minimal polynomial $m_{A^k}(x) \in \mathbb{C}[x]$ factors as
$$m_{A^k}(x) = \prod_{i=1}^r (x - \lambda_i),$$
where $\lambda_1, \dots, \lambda_r \in \mathbb{C}$ are the distinct eigenvalues of $A^k$.
:::

:::

:::

::: pf-step
Non-zero eigenvalues:

::: pf-proof

::: pf-step
Since $A$ is non-singular, $\det(A) \ne 0$.
:::

::: pf-step
By the multiplicative property of determinants, $\det(A^k) = (\det A)^k \ne 0$.
:::

::: pf-step
Since the determinant is the product of all eigenvalues with multiplicity, $0$ is not an eigenvalue of $A^k$.
:::

::: pf-step
Thus $\lambda_i \ne 0$ for each $i \in \{1, \dots, r\}$.
:::

:::

:::

::: pf-step
Annihilating polynomial $P(x) = m_{A^k}(x^k)$:

::: pf-proof

::: pf-step
Define the polynomial $P(x) \in \mathbb{C}[x]$ by
$$P(x) = m_{A^k}(x^k) = \prod_{i=1}^r (x^k - \lambda_i).$$
:::

::: pf-step
Evaluating $P$ on $A$:
$$P(A) = m_{A^k}(A^k) = 0.$$
:::

::: pf-step
Since $P(A) = 0$, the minimal polynomial $m_A(x)$ of $A$ divides $P(x)$ in $\mathbb{C}[x]$.
:::

:::

:::

::: pf-step
$P(x)$ has distinct roots in $\mathbb{C}$:

::: pf-proof

::: pf-step
For each $i \in \{1, \dots, r\}$, since $\lambda_i \ne 0$, the polynomial $x^k - \lambda_i$ has derivative $k x^{k-1} \ne 0$. The only root of the derivative is $x = 0$, which is not a root of $x^k - \lambda_i$ because $\lambda_i \ne 0$.
:::

::: pf-step
Thus $\gcd(x^k - \lambda_i, k x^{k-1}) = 1$, so each $x^k - \lambda_i$ has $k$ distinct roots in $\mathbb{C}$, given explicitly by
$$\mu_{i, j} = \lambda_i^{1/k} e^{2\pi i j / k} \quad \text{for } j \in \{0, 1, \dots, k-1\}.$$
:::

::: pf-step
For $i \ne j$, the polynomials $x^k - \lambda_i$ and $x^k - \lambda_j$ share no roots: if $\alpha \in \mathbb{C}$ were a common root, then $\alpha^k = \lambda_i$ and $\alpha^k = \lambda_j$, implying $\lambda_i = \lambda_j$, a contradiction.
:::

::: pf-step
Therefore, $P(x) = \prod_{i=1}^r (x^k - \lambda_i)$ has exactly $k r$ distinct roots in $\mathbb{C}$.
:::

:::

:::

::: pf-step
Diagonalizability of $A$:

::: pf-proof

::: pf-step
Since $m_A(x)$ divides $P(x)$ and $P(x)$ is a product of distinct linear factors over $\mathbb{C}$, $m_A(x)$ is also a product of distinct linear factors over $\mathbb{C}$.
:::

::: pf-step
By the criterion in step [](#s1){.pf-ref}, $A$ is diagonalizable over $\mathbb{C}$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$A$ is diagonalizable over $\mathbb{C}$.
:::

:::

:::
:::
