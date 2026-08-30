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
---

::: problem
Suppose $p$ is a prime number and the minimal polynomial of $g \in \operatorname{GL}_p(F)$ is $t^p - 1$.

(a) Find the Jordan form of $g$ if $F = \mathbb{C}$.

(b) Find the Jordan form of $g$ if $F = \overline{\mathbb{F}}_p$ is an algebraic closure of the finite field $\mathbb{F}_p$.
:::

::: {.solution}
**(a). Case $F = \mathbb{C}$:**

<1>1. Factor the minimal polynomial over $\mathbb{C}$:
\[
t^p - 1 = \prod_{k=0}^{p-1} (t - \zeta^k), \quad \text{where } \zeta = e^{2\pi i/p}.
\]
Proof: over $\mathbb{C}$, the $p$-th roots of unity are distinct.

<1>2. The minimal polynomial $m_g(t) = t^p - 1$ has $p$ distinct roots over $\mathbb{C}$, so $g$ is diagonalizable.
Proof: a matrix is diagonalizable over an algebraically closed field if and only if its minimal polynomial has no repeated roots.

<1>3. Since $g \in \operatorname{GL}_p(\mathbb{C})$ is a $p \times p$ matrix and has $p$ distinct eigenvalues $\{1, \zeta, \zeta^2, \dots, \zeta^{p-1}\}$, each eigenvalue has algebraic and geometric multiplicity 1. Proof: the sum of the multiplicities is $\deg(\operatorname{char}_g(t)) = p$, and each of the $p$ roots of $m_g(t)$ must be an eigenvalue.

<1>4. Therefore the Jordan canonical form of $g$ is the diagonal matrix:
\[
J = \begin{pmatrix}
1 & 0 & 0 & \cdots & 0 \\
0 & \zeta & 0 & \cdots & 0 \\
0 & 0 & \zeta^2 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \zeta^{p-1}
\end{pmatrix}.
\]
Proof: <1>2 and <1>3.

**(b). Case $F = \overline{\mathbb{F}}_p$:**

<1>5. Factor the minimal polynomial in characteristic $p$:
\[
t^p - 1 = (t - 1)^p.
\]
Proof: in characteristic $p$, the Frobenius identity $(a - b)^p = a^p - b^p$ gives $(t - 1)^p = t^p - 1^p = t^p - 1$.

<1>6. The only eigenvalue of $g$ is $\lambda = 1$.
Proof: the roots of the minimal polynomial are the eigenvalues of $g$.

<1>7. The size of the largest Jordan block for eigenvalue $1$ is the power of $(t - 1)$ in the minimal polynomial, which is $p$.
Proof: for any eigenvalue $\lambda$, the degree of $(t - \lambda)$ in the minimal polynomial equals the size of the largest Jordan block associated with $\lambda$.

<1>8. Since $g$ is a $p \times p$ matrix, there is a single Jordan block of size $p$:
\[
J = J_p(1) = \begin{pmatrix}
1 & 1 & 0 & \cdots & 0 \\
0 & 1 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & \cdots & 1 & 1 \\
0 & 0 & \cdots & 0 & 1
\end{pmatrix}.
\]
Proof: <1>7 and the matrix dimension is $p$.

<1>9. Q.E.D. Proof: <1>4 (a) and <1>8 (b).
:::
