---
schema: qual/card@1
id: P-BKS16-7B
kind: problem
title: Spectral radius bounds the norm of a symmetric matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Checked the statement against Problem 7B in the vendored Berkeley Spring 2016 exam and independently reviewed the supplied solution.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the orthonormal eigenbasis estimate and the nilpotent counterexample in the nonsymmetric case.
---

::: {.problem}
Let $A$ be a real square matrix and let $\rho$ be the maximum of the absolute values of its eigenvalues (i.e. its spectral radius).

(a) Show that if $A$ is symmetric then
$$
\norm{Ax}\le \rho\norm{x}
$$
for all $x\in\RR^n$, where $\norm{\cdot}$ denotes the Euclidean norm.

(b) Is this true when $A$ is not symmetric?
Prove or give a counterexample.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $A$ is symmetric, then
$$
\norm{ Ax}\leq\rho\norm{ x}
$$
for every $x\in\RR^n$.


::: pf-proof

By the spectral theorem, there is an orthonormal basis $u_1,\ldots,u_n$ of $\RR^n$ consisting of eigenvectors of $A$, with corresponding real eigenvalues $\lambda_1,\ldots,\lambda_n$. Write
$$
x=\sum_{i=1}^n c_i u_i.
$$
Then
$$
Ax=\sum_{i=1}^n \lambda_i c_i u_i.
$$
Orthogonality gives
$$
\norm{ Ax}^2
=
\sum_{i=1}^n \lambda_i^2c_i^2
\leq
\rho^2\sum_{i=1}^n c_i^2
=
\rho^2\norm{ x}^2,
$$
because $\abs{\lambda_i}\leq\rho$ for every $i$. Taking square roots gives the claimed inequality.

:::

:::

::: {.pf-step #s1-2}

For a nonsymmetric matrix, the assertion is $\boxed{\text{false}}$.


::: pf-proof

Consider
$$
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
Its characteristic polynomial is $t^2$, so both eigenvalues are $0$ and therefore $\rho=0$. But for the second standard basis vector $e_2$,
$$
Ae_2=e_1,
$$
so
$$
\norm{ Ae_2}=1>0=\rho\norm{ e_2}.
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and step [](#s1-2){.pf-ref} supplies the counterexample required in part (b).

:::

:::

:::
