---
schema: qual/card@1
id: P-APAF20B
kind: problem
title: Operator and Frobenius norms, eigenvalue bounds, and self-adjoint spectrum from singular values
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
  - Singular Values
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Suppose $\CC^3$ is given its usual inner product, and $\psi\colon\CC^3\to\CC^3$ is a linear map.
Further suppose that the singular values of $\psi$ are $\sigma_1=3$, $\sigma_2=2$ and $\sigma_3=1$.

(a) Determine, with justification, the norms $\norm{\psi}_{\mathrm{op}}$ and $\norm{\psi}_{\mathrm{Frob}}$.

(b) Let $\lambda\in\CC$ be an eigenvalue of $\psi$.
Prove that $\abs{\lambda}\in[1,3]$.

(c) Suppose now that $\psi$ is self-adjoint.
Prove that $\lambda\in\{-3,-2,-1,1,2,3\}$.
:::

::: {.solution}

::: pf

::: pf-step
The operator norm is
$$
\boxed{\norm{\psi}_{\mathrm{op}}=3}.
$$

::: pf-proof
For a linear map on a finite-dimensional Hermitian space, the operator norm induced by the Euclidean norm equals the largest singular value. Since the singular values are $3,2,1$, the largest is $3$.
:::

:::

::: pf-step
The Frobenius norm is
$$
\boxed{\norm{\psi}_{\mathrm{Frob}}=\sqrt{14}}.
$$

::: pf-proof
The squared Frobenius norm is the trace of $\psi^*\psi$, equivalently the sum of the squares of the singular values. Hence
$$
\norm{\psi}_{\mathrm{Frob}}^2=3^2+2^2+1^2=14.
$$
:::

:::

::: {.pf-step #singular-value-bounds-on-image}
For every vector $v\in\CC^3$,
$$
\norm{v}\le \norm{\psi v}\le3\norm{v}.
$$

::: pf-proof
Choose a singular value decomposition
$$
\psi=U\Sigma V^*,
\qquad
\Sigma=\operatorname{diag}(3,2,1).
$$
Since $U$ and $V$ are unitary,
$$
\norm{\psi v}=\norm{\Sigma V^*v}.
$$
Writing $w=V^*v=(w_1,w_2,w_3)^T$ gives
$$
\norm{\Sigma w}^2
=9\abs{w_1}^2+4\abs{w_2}^2+\abs{w_3}^2.
$$
Therefore
$$
\norm{w}^2\le \norm{\Sigma w}^2\le9\norm{w}^2.
$$
Because $\norm{w}=\norm{v}$, taking square roots yields the claimed inequalities.
:::

:::

::: pf-step
If $\lambda$ is an eigenvalue of $\psi$, then
$$
\boxed{1\le\abs{\lambda}\le3}.
$$

::: pf-proof
Let $0\ne v$ satisfy
$$
\psi v=\lambda v.
$$
Applying step [](#singular-value-bounds-on-image){.pf-ref} gives
$$
\norm{v}\le\norm{\psi v}=\abs{\lambda}\norm{v}\le3\norm{v}.
$$
Since $v\ne0$, divide by $\norm{v}$ to obtain the result.
:::

:::

::: pf-step
If $\psi$ is self-adjoint, then every eigenvalue belongs to
$$
\boxed{\{-3,-2,-1,1,2,3\}}.
$$

::: pf-proof
A self-adjoint operator is unitarily diagonalizable with real eigenvalues, say
$$
\psi=Q\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)Q^*,
\qquad \lambda_i\in\RR.
$$
Then
$$
\psi^*\psi=\psi^2
=Q\operatorname{diag}(\lambda_1^2,\lambda_2^2,\lambda_3^2)Q^*.
$$
Thus the singular values of $\psi$, which are the nonnegative square roots of the eigenvalues of $\psi^*\psi$, are
$$
\abs{\lambda_1},\abs{\lambda_2},\abs{\lambda_3}.
$$
Their multiset is $\{3,2,1\}$ by hypothesis. Hence each real eigenvalue has absolute value $1$, $2$, or $3$, so each lies in the displayed set.
:::

:::

:::

:::
