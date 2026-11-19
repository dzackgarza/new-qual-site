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
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the four containers state why their subsections suffice, and the 15
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: $A^k$ has a separable minimal polynomial, non-singularity keeps every
    eigenvalue away from $0$ so that each $x^k-\lambda_i$ is separable and the factors are pairwise
    coprime, hence $P(x)=m_{A^k}(x^k)$ is a product of distinct linear factors, and its divisor
    $m_A$ is too. Checked against the statement on the card, from the UGA Spring 2019 algebra qualifying
    exam. Nothing in the statement was changed.

---
::: {.problem}
Let $A \in M_m(\CC)$ be an $m \times m$ matrix over the complex numbers. Suppose that $A$ is non-singular ($\det A \ne 0$) and that $A^k$ is diagonalizable over $\CC$ for some integer $k \ge 1$ (for instance, $k = 2019$).

Show that $A$ is also diagonalizable over $\CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The minimal polynomial of $A^k$ has the form
$$
m_{A^k}(x)=\prod_{i=1}^r(x-\lambda_i)
$$
for pairwise distinct nonzero complex numbers $\lambda_i$.

::: pf-proof

::: pf-step

A matrix over $\CC$ is diagonalizable if and only if its minimal polynomial is square-free (splits into distinct linear factors).


::: pf-proof
This is the standard criterion for diagonalizability over an algebraically closed field.
:::

:::

::: pf-step

Since $A^k$ is diagonalizable over $\CC$, its minimal polynomial $m_{A^k}(x) \in \CC[x]$ factors as


::: pf-proof
The criterion applied to the matrix $A^k$.
:::

:::

$$m_{A^k}(x) = \prod_{i=1}^r (x - \lambda_i),$$
where $\lambda_1, \dots, \lambda_r \in \CC$ are the distinct eigenvalues of $A^k$.

:::

:::

::: pf-step

Every eigenvalue $\lambda_i$ in step [](#s1){.pf-ref} is nonzero.

::: pf-proof

::: pf-step

Since $A$ is non-singular, $\det(A) \ne 0$.


::: pf-proof
This is the definition of non-singularity.
:::

:::

::: pf-step

By the multiplicative property of determinants, $\det(A^k) = (\det A)^k \ne 0$.


::: pf-proof
The determinant is multiplicative.
:::

:::

::: pf-step

Since the determinant is the product of all eigenvalues with multiplicity, $0$ is not an eigenvalue of $A^k$.


::: pf-proof
The determinant is the product of the eigenvalues counted with algebraic multiplicity.
:::

:::

::: pf-step

Thus $\lambda_i \ne 0$ for each $i \in \{1, \dots, r\}$.


::: pf-proof
If some eigenvalue vanished the product would vanish, contradicting $\det A\neq0$.
:::

:::

:::

:::

::: pf-step

The polynomial $P(x)=m_{A^k}(x^k)$ annihilates $A$.

::: pf-proof

::: pf-step

Define the polynomial $P(x) \in \CC[x]$ by
    $$P(x) = m_{A^k}(x^k) = \prod_{i=1}^r (x^k - \lambda_i).$$


::: pf-proof
This is a definition: the polynomial obtained by substituting $x^k$ into the minimal polynomial of $A^k$.
:::

:::

::: pf-step

Evaluating $P$ on $A$:
    $$P(A) = m_{A^k}(A^k) = 0.$$


::: pf-proof
Powers of $A$ commute, so substituting $A$ gives $m_{A^k}(A^k)$, which is zero.
:::

:::

::: pf-step

Since $P(A) = 0$, the minimal polynomial $m_A(x)$ of $A$ divides $P(x)$ in $\CC[x]$.


::: pf-proof
The minimal polynomial divides every polynomial that annihilates $A$.
:::

:::

:::

:::

::: pf-step

The polynomial $P$ has no repeated complex root.

::: pf-proof

::: pf-step

For each $i \in \{1, \dots, r\}$, since $\lambda_i \ne 0$, the polynomial $x^k - \lambda_i$ has derivative $k x^{k-1} \ne 0$. The only root of the derivative is $x = 0$, which is not a root of $x^k - \lambda_i$ because $\lambda_i \ne 0$.


::: pf-proof
The derivative $kx^{k-1}$ vanishes only at $0$, and $0$ is not a root because $\lambda_i\neq0$.
:::

:::

::: pf-step

Thus $\gcd(x^k - \lambda_i, k x^{k-1}) = 1$, so each $x^k - \lambda_i$ has $k$ distinct roots in $\CC$, given explicitly by
    $$\mu_{i, j} = \lambda_i^{1/k} e^{2\pi i j / k} \quad \text{for } j \in \{0, 1, \dots, k-1\}.$$


::: pf-proof
A polynomial is separable exactly when it is coprime to its derivative.
:::

:::

::: pf-step

For $i \ne j$, the polynomials $x^k - \lambda_i$ and $x^k - \lambda_j$ share no roots: if $\alpha \in \CC$ were a common root, then $\alpha^k = \lambda_i$ and $\alpha^k = \lambda_j$, implying $\lambda_i = \lambda_j$, a contradiction.


::: pf-proof
Their difference is the non-zero constant $\lambda_j-\lambda_i$, so any common factor is constant.
:::

:::

::: pf-step

Therefore, $P(x) = \prod_{i=1}^r (x^k - \lambda_i)$ has exactly $k r$ distinct roots in $\CC$.


::: pf-proof
Each factor is separable with $k$ distinct roots, and distinct factors share no root.
:::

:::

:::

:::

::: {.pf-step #s5}

The matrix $A$ is diagonalizable over $\CC$.

::: pf-proof

::: pf-step

Since $m_A(x)$ divides $P(x)$ and $P(x)$ is a product of distinct linear factors over $\CC$, $m_A(x)$ is also a product of distinct linear factors over $\CC$.


::: pf-proof
A divisor of a separable polynomial is separable.
:::

:::

::: pf-step

By the criterion in step [](#s1){.pf-ref}, $A$ is diagonalizable over $\CC$.


::: pf-proof
Its minimal polynomial has distinct linear factors.
:::

:::

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} establishes the required conclusion.

:::

:::

:::
