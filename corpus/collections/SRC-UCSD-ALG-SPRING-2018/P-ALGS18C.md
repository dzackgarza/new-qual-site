---
schema: qual/card@1
id: P-ALGS18C
kind: problem
title: "Jordan form of a matrix with minimal polynomial t^p - 1"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $p$ is a prime number and the minimal polynomial of $g \in \operatorname{GL}_p(F)$ is $t^p - 1$.

(a) Find the Jordan form of $g$ if $F = \mathbb{C}$.

(b) Find the Jordan form of $g$ if $F = \overline{\mathbb{F}}_p$ is an algebraic closure of the finite field $\mathbb{F}_p$.
:::

::: {.solution}
**(a). Case $F = \mathbb{C}$:**

::: pf

::: pf-step

Factor the minimal polynomial over $\mathbb{C}$:
\[
t^p - 1 = \prod_{k=0}^{p-1} (t - \zeta^k), \quad \text{where } \zeta = e^{2\pi i/p}.
\]

::: pf-proof

over $\mathbb{C}$, the $p$-th roots of unity are distinct.

:::

:::

::: {.pf-step #s2}

The minimal polynomial $m_g(t) = t^p - 1$ has $p$ distinct roots over $\mathbb{C}$, so $g$ is diagonalizable.

::: pf-proof

a matrix is diagonalizable over an algebraically closed field if and only if its minimal polynomial has no repeated roots.

:::

:::

::: {.pf-step #s3}

Since $g \in \operatorname{GL}_p(\mathbb{C})$ is a $p \times p$ matrix and has $p$ distinct eigenvalues $\{1, \zeta, \zeta^2, \dots, \zeta^{p-1}\}$, each eigenvalue has algebraic and geometric multiplicity 1.

::: pf-proof

the sum of the multiplicities is $\deg(\operatorname{char}_g(t)) = p$, and each of the $p$ roots of $m_g(t)$ must be an eigenvalue.

:::

:::

::: {.pf-step #s4}

Therefore the Jordan canonical form of $g$ is the diagonal matrix:
\[
J = \begin{pmatrix}
1 & 0 & 0 & \cdots & 0 \\
0 & \zeta & 0 & \cdots & 0 \\
0 & 0 & \zeta^2 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \zeta^{p-1}
\end{pmatrix}.
\]

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

**(b). Case $F = \overline{\mathbb{F}}_p$:**

:::

:::

::: pf-step

Factor the minimal polynomial in characteristic $p$:
\[
t^p - 1 = (t - 1)^p.
\]

::: pf-proof

in characteristic $p$, the Frobenius identity $(a - b)^p = a^p - b^p$ gives $(t - 1)^p = t^p - 1^p = t^p - 1$.

:::

:::

::: pf-step

The only eigenvalue of $g$ is $\lambda = 1$.

::: pf-proof

the roots of the minimal polynomial are the eigenvalues of $g$.

:::

:::

::: {.pf-step #s7}

The size of the largest Jordan block for eigenvalue $1$ is the power of $(t - 1)$ in the minimal polynomial, which is $p$.

::: pf-proof

for any eigenvalue $\lambda$, the degree of $(t - \lambda)$ in the minimal polynomial equals the size of the largest Jordan block associated with $\lambda$.

:::

:::

::: {.pf-step #s8}

Since $g$ is a $p \times p$ matrix, there is a single Jordan block of size $p$:
\[
J = J_p(1) = \begin{pmatrix}
1 & 1 & 0 & \cdots & 0 \\
0 & 1 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & \cdots & 1 & 1 \\
0 & 0 & \cdots & 0 & 1
\end{pmatrix}.
\]

::: pf-proof

Step [](#s7){.pf-ref} and the matrix dimension is $p$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} (a) and step [](#s8){.pf-ref} (b).

:::

:::

:::
