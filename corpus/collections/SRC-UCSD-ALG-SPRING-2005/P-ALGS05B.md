---
schema: qual/card@1
id: P-ALGS05B
kind: problem
title: "A triangular matrix is normal if and only if it is diagonal"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Prove that a triangular matrix is normal if and only if it is diagonal.
:::

::: {.solution}
<1>1. It suffices to treat the case in which \(A=(a_{ij})\) is upper triangular; the lower triangular case follows by applying the argument to \(A^*\).
::: {.proof}
The adjoint of a lower triangular matrix is upper triangular, and \(A\) is normal exactly when \(A^*\) is normal.
:::

<1>2. If \(A\) is upper triangular and normal, then \(a_{1j}=0\) for every \(j>1\).
::: {.proof}
Normality gives \(AA^*=A^*A\). Comparing the \((1,1)\)-entries,
\[
(AA^*)_{11}=\sum_{j=1}^n |a_{1j}|^2,
\qquad
(A^*A)_{11}=\sum_{j=1}^n |a_{j1}|^2.
\]
Because \(A\) is upper triangular, \(a_{j1}=0\) for every \(j>1\). Hence
\[
\sum_{j=1}^n |a_{1j}|^2=|a_{11}|^2,
\]
so
\[
\sum_{j=2}^n |a_{1j}|^2=0.
\]
Therefore \(a_{1j}=0\) for all \(j>1\).
:::

<1>3. Thus \(A\) has block form
\[
A=\begin{pmatrix}a_{11}&0\\0&B\end{pmatrix},
\]
where \(B\) is upper triangular and normal.
::: {.proof}
Upper triangularity already gives \(a_{j1}=0\) for \(j>1\), and <1>2 gives \(a_{1j}=0\) for \(j>1\), so the displayed block form holds.
Then
\[
AA^*=\begin{pmatrix}|a_{11}|^2&0\\0&BB^*\end{pmatrix},
\qquad
A^*A=\begin{pmatrix}|a_{11}|^2&0\\0&B^*B\end{pmatrix}.
\]
Since \(AA^*=A^*A\), one has \(BB^*=B^*B\), so \(B\) is normal.
:::

<1>4. By induction on the matrix size, every upper triangular normal matrix is diagonal.
::: {.proof}
The assertion is immediate for \(1\times1\) matrices.
For \(n>1\), <1>3 reduces the problem to the \((n-1)\times(n-1)\) upper triangular normal matrix \(B\), which is diagonal by the induction hypothesis.
Hence \(A\) is diagonal.
:::

<1>5. Conversely, every diagonal matrix is normal.
::: {.proof}
If \(A=\operatorname{diag}(\lambda_1,\dots,\lambda_n)\), then
\[
AA^*=A^*A=\operatorname{diag}(|\lambda_1|^2,\dots,|\lambda_n|^2).
\]
:::

<1>6. Therefore a triangular matrix is normal if and only if it is diagonal.
::: {.proof}
Combine <1>1--<1>5.
:::
:::
