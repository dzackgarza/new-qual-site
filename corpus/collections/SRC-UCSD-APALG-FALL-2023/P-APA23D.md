---
schema: qual/card@1
id: P-APA23D
kind: problem
title: Rayleigh quotient bounds; $p$-norm of a diagonal matrix; $\norm{aa^H}_2$ and a block companion
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Verified the Rayleigh, induced-norm, and spectral-norm computations.
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex entries, and $x^H$ denotes the Hermitian transpose of $x$.

(a) Consider any Hermitian $A \in M_n$ with eigenvalues ordered so that $\lambda_n(A) \le \cdots \le \lambda_2(A) \le \lambda_1(A)$.
Prove that:
$$\lambda_n(A) \le \frac{x^H A x}{x^H x} \le \lambda_1(A) \quad \text{for all nonzero } x \in \CC^n.$$

(b) Suppose that $D \in M_n$ with $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$.
Prove that for all $1 \le p \le \infty$, the induced operator $p$-norm of $D$ is given by $\norm{D}_p = \max_{1 \le i \le n} \abs{d_i}$.

(c) Given $a \in \CC^n$, find $\norm{A}_2$ for the matrices:
$$A_1 = a a^H \quad \text{and} \quad A_2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix}.$$
:::

::: {.solution}

**Goal:** Prove the Rayleigh quotient inequalities for Hermitian matrices, compute induced $p$-norms of diagonal matrices, and evaluate the spectral 2-norm of rank-one and symmetric block companion matrices.

::: pf

::: pf-step
Part (a): Rayleigh Quotient Bounds for Hermitian Matrices:

::: pf-proof
*Proof:*

::: pf-step
By the **Spectral Theorem**, there exists an orthonormal eigenbasis $\{u_1, u_2, \dots, u_n\}$ of $\CC^n$ such that $A u_i = \lambda_i(A) u_i$ and $u_i^H u_j = \delta_{ij}$.
:::

::: pf-step
Write any non-zero vector $x \in \CC^n \setminus \{0\}$ as $x = \sum_{i=1}^n c_i u_i$ with $c_i = u_i^H x \in \CC$.
:::

::: pf-step
Then:
$$x^H x = \sum_{i=1}^n \abs{c_i}^2 > 0, \qquad x^H A x = \sum_{i=1}^n \lambda_i(A) \abs{c_i}^2.$$
:::

::: pf-step
Since $\lambda_n(A) \le \lambda_i(A) \le \lambda_1(A)$ for each $i \in \{1, \dots, n\}$:
$$\lambda_n(A) \sum_{i=1}^n \abs{c_i}^2 \le \sum_{i=1}^n \lambda_i(A) \abs{c_i}^2 \le \lambda_1(A) \sum_{i=1}^n \abs{c_i}^2.$$
:::

::: pf-step
Dividing by $x^H x = \sum_{i=1}^n \abs{c_i}^2$:
$$\lambda_n(A) \le \frac{x^H A x}{x^H x} \le \lambda_1(A).$$
:::

:::

:::

::: pf-step
Part (b): $p$-Norm of a Diagonal Matrix $\norm{D}_p = \max_i \abs{d_i}$:

::: pf-proof
*Proof:*

::: pf-step
Let $M = \max_{1 \le i \le n} \abs{d_i}$.
:::

::: pf-step
For any $x \in \CC^n$ and $1 \le p < \infty$:
$$\norm{D x}_p^p = \sum_{i=1}^n \abs{d_i x_i}^p = \sum_{i=1}^n \abs{d_i}^p \abs{x_i}^p \le \sum_{i=1}^n M^p \abs{x_i}^p = M^p \sum_{i=1}^n \abs{x_i}^p = M^p \norm{x}_p^p.$$
Taking $p$-th roots gives $\norm{D x}_p \le M \norm{x}_p$, so $\norm{D}_p \le M$.
(For $p = \infty$: $\norm{D x}_\infty = \max_i \abs{d_i x_i} \le M \max_i \abs{x_i} = M \norm{x}_\infty$).
:::

::: pf-step
To show attainment, choose index $k$ such that $\abs{d_k} = M = \max_i \abs{d_i}$.
:::

::: pf-step
Let $e_k = (0, \dots, 0, 1, 0, \dots, 0)^T$ be the $k$-th standard basis vector.
:::

::: pf-step
$\norm{e_k}_p = 1$, and $D e_k = d_k e_k$, so $\norm{D e_k}_p = \abs{d_k} \norm{e_k}_p = M$.
:::

::: pf-step
Therefore:
$$\norm{D}_p = \sup_{x \ne 0} \frac{\norm{D x}_p}{\norm{x}_p} = M = \max_{1 \le i \le n} \abs{d_i}.$$
:::

:::

:::

::: pf-step
Part (c): Evaluation of $\norm{A}_2$ (Spectral Norm):

::: pf-proof
*Proof:*

::: pf-step
The matrix 2-norm is the largest singular value: $\norm{A}_2 = \sigma_1(A) = \sqrt{\lambda_1(A^H A)}$.
:::

::: pf-step
**For $A_1 = a a^H$ (where $a \in \CC^n$):**

- If $a = 0$, $\norm{A_1}_2 = 0 = \norm{a}_2^2$.
- If $a \ne 0$, $A_1 a = (a a^H) a = a (a^H a) = \norm{a}_2^2 a$, so $a$ is an eigenvector with eigenvalue $\norm{a}_2^2$.
- For any $v \perp a$, $A_1 v = a (a^H v) = 0$.
- Since $A_1$ is Hermitian and rank 1, its eigenvalues are $\norm{a}_2^2$ (multiplicity 1) and $0$ (multiplicity $n - 1$).
- Thus:
  $$\norm{A_1}_2 = \lambda_1(A_1) = \norm{a}_2^2.$$
:::

::: pf-step
**For $A_2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} \in M_{n+1}(\CC)$:**

- We compute $A_2^H A_2 = A_2^2$ (since $A_2$ is Hermitian):
  $$A_2^2 = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} = \begin{pmatrix} a^H a & 0 \\ 0 & a a^H \end{pmatrix} = \begin{pmatrix} \norm{a}_2^2 & 0 \\ 0 & a a^H \end{pmatrix}.$$
- The eigenvalues of the block diagonal matrix $A_2^2$ are:
  - From top block $1 \times 1$: $\norm{a}_2^2$.
  - From bottom block $n \times n$: eigenvalues of $a a^H$, which are $\norm{a}_2^2$ and $0$.
- Thus the largest eigenvalue of $A_2^2$ is $\lambda_{\max}(A_2^2) = \norm{a}_2^2$.
- Taking the square root gives the spectral norm:
  $$\norm{A_2}_2 = \sqrt{\lambda_{\max}(A_2^2)} = \sqrt{\norm{a}_2^2} = \norm{a}_2.$$
:::

:::

:::

::: pf-qed
Conclusion:

The Rayleigh quotient is bounded by $\lambda_n \le \frac{x^HAx}{x^Hx} \le \lambda_1$, $\norm{D}_p = \max_i \abs{d_i}$, $\norm{a a^H}_2 = \norm{a}_2^2$, and $\norm{ \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix} }_2 = \norm{a}_2$.
:::

:::

:::
