---
schema: qual/card@1
id: P-APAF22B
kind: problem
title: Schur eigenvalues versus singular values; equality implies normality
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Normal Operators
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
Let $V$ be a finite-dimensional complex inner product space of dimension $n$, and $\phi \colon V \to V$ a linear map.
Suppose that $B$ is an orthonormal basis for $V$ such that the matrix
\[
A = \mathcal{M}(\phi, B, B)
=
\begin{pmatrix}
\lambda_1 & * & \cdots & * \\
0 & \lambda_2 & \cdots & * \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{pmatrix}
\]
is upper-triangular, i.e., a Schur decomposition.
Finally let $\sigma_1 \geq \cdots \geq \sigma_n$ denote the singular values of $\phi$, with multiplicity.

(a) By considering $\|\phi\|_{\mathrm{Frob}}$, or otherwise, prove that $\sum_{i=1}^{n} |\lambda_i|^2 \leq \sum_{i=1}^{n} \sigma_i^2$.

(b) Suppose now that $\sum_{i=1}^{n} |\lambda_i|^2 = \sum_{i=1}^{n} \sigma_i^2$.
By considering $A$, or otherwise, prove that $\phi$ is normal.
:::

::: {.solution}
<1>1. The squared Frobenius norm of $A$ is
\[
\|A\|_{\mathrm{Frob}}^2
=\sum_{i=1}^n|\lambda_i|^2+
\sum_{1\le i<j\le n}|a_{ij}|^2.
\]
::: {.proof}
Because $A$ is upper triangular, its only possibly nonzero entries are the diagonal entries $\lambda_i$ and the entries $a_{ij}$ with $i<j$. By definition,
\[
\|A\|_{\mathrm{Frob}}^2=\sum_{i,j}|a_{ij}|^2,
\]
which gives the displayed decomposition.
:::

<1>2. One also has
\[
\|A\|_{\mathrm{Frob}}^2=\sum_{i=1}^n\sigma_i^2.
\]
::: {.proof}
Since $B$ is orthonormal, $A$ is the matrix of $\phi$ in an orthonormal basis. The Frobenius norm is unitarily invariant, and
\[
\|A\|_{\mathrm{Frob}}^2
=\operatorname{tr}(A^*A).
\]
The eigenvalues of $A^*A$ are the squares $\sigma_1^2,\ldots,\sigma_n^2$ of the singular values, counted with multiplicity. Therefore
\[
\operatorname{tr}(A^*A)=\sum_{i=1}^n\sigma_i^2.
\]
:::

<1>3. Hence
\[
\boxed{\sum_{i=1}^n|\lambda_i|^2\le\sum_{i=1}^n\sigma_i^2}.
\]
::: {.proof}
Combine <1>1 and <1>2:
\[
\sum_{i=1}^n\sigma_i^2
=\sum_{i=1}^n|\lambda_i|^2+\sum_{i<j}|a_{ij}|^2.
\]
The second sum on the right is nonnegative, which gives the inequality.
:::

<1>4. If equality holds in <1>3, then $A$ is diagonal.
::: {.proof}
Under the equality hypothesis,
\[
0=\sum_{i<j}|a_{ij}|^2.
\]
Every summand is nonnegative, so each $a_{ij}=0$ for $i<j$. Since $A$ is already upper triangular, all off-diagonal entries vanish and
\[
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n).
\]
:::

<1>5. Therefore $\phi$ is normal.
::: {.proof}
By <1>4, the matrix of $\phi$ in the orthonormal basis $B$ is diagonal. A diagonal matrix commutes with its adjoint:
\[
AA^*=A^*A.
\]
Normality is invariant under unitary change of orthonormal basis, so
\[
\phi\phi^*=\phi^*\phi.
\]
Hence $\phi$ is normal.
:::
:::
