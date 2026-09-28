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
Suppose $\mathbb{C}^3$ is given its usual inner product, and $\psi\colon\mathbb{C}^3\to\mathbb{C}^3$ is a linear map.
Further suppose that the singular values of $\psi$ are $\sigma_1=3$, $\sigma_2=2$ and $\sigma_3=1$.

(a) Determine, with justification, the norms $\|\psi\|_{\mathrm{op}}$ and $\|\psi\|_{\mathrm{Frob}}$.

(b) Let $\lambda\in\mathbb{C}$ be an eigenvalue of $\psi$.
Prove that $|\lambda|\in[1,3]$.

(c) Suppose now that $\psi$ is self-adjoint.
Prove that $\lambda\in\{-3,-2,-1,1,2,3\}$.
:::

::: {.solution}
<1>1. The operator norm is
\[
\boxed{\|\psi\|_{\mathrm{op}}=3}.
\]
::: {.proof}
For a linear map on a finite-dimensional Hermitian space, the operator norm induced by the Euclidean norm equals the largest singular value. Since the singular values are $3,2,1$, the largest is $3$.
:::

<1>2. The Frobenius norm is
\[
\boxed{\|\psi\|_{\mathrm{Frob}}=\sqrt{14}}.
\]
::: {.proof}
The squared Frobenius norm is the trace of $\psi^*\psi$, equivalently the sum of the squares of the singular values. Hence
\[
\|\psi\|_{\mathrm{Frob}}^2=3^2+2^2+1^2=14.
\]
:::

<1>3. For every vector $v\in\mathbb C^3$,
\[
\|v\|\le \|\psi v\|\le3\|v\|.
\]
::: {.proof}
Choose a singular value decomposition
\[
\psi=U\Sigma V^*,
\qquad
\Sigma=\operatorname{diag}(3,2,1).
\]
Since $U$ and $V$ are unitary,
\[
\|\psi v\|=\|\Sigma V^*v\|.
\]
Writing $w=V^*v=(w_1,w_2,w_3)^T$ gives
\[
\|\Sigma w\|^2
=9|w_1|^2+4|w_2|^2+|w_3|^2.
\]
Therefore
\[
\|w\|^2\le \|\Sigma w\|^2\le9\|w\|^2.
\]
Because $\|w\|=\|v\|$, taking square roots yields the claimed inequalities.
:::

<1>4. If $\lambda$ is an eigenvalue of $\psi$, then
\[
\boxed{1\le|\lambda|\le3}.
\]
::: {.proof}
Let $0\ne v$ satisfy
\[
\psi v=\lambda v.
\]
Applying <1>3 gives
\[
\|v\|\le\|\psi v\|=|\lambda|\|v\|\le3\|v\|.
\]
Since $v\ne0$, divide by $\|v\|$ to obtain the result.
:::

<1>5. If $\psi$ is self-adjoint, then every eigenvalue belongs to
\[
\boxed{\{-3,-2,-1,1,2,3\}}.
\]
::: {.proof}
A self-adjoint operator is unitarily diagonalizable with real eigenvalues, say
\[
\psi=Q\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)Q^*,
\qquad \lambda_i\in\mathbb R.
\]
Then
\[
\psi^*\psi=\psi^2
=Q\operatorname{diag}(\lambda_1^2,\lambda_2^2,\lambda_3^2)Q^*.
\]
Thus the singular values of $\psi$, which are the nonnegative square roots of the eigenvalues of $\psi^*\psi$, are
\[
|\lambda_1|,|\lambda_2|,|\lambda_3|.
\]
Their multiset is $\{3,2,1\}$ by hypothesis. Hence each real eigenvalue has absolute value $1$, $2$, or $3$, so each lies in the displayed set.
:::
:::
