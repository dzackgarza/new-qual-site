---
schema: qual/card@1
id: P-BKF06-8B
kind: problem
title: Simultaneous diagonalization of a Hermitian and a positive-definite matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained congruence argument using the positive
    Hermitian square root B^(1/2) and the spectral theorem.
---

::: {.problem}
Let $A$ be an $n\times n$ Hermitian matrix and $B$ an $n\times n$ positive-definite complex matrix.
Prove that there is an invertible complex $n\times n$ matrix $S$ such that
\[
S^*AS
\]
is diagonal and
\[
S^*BS=I.
\]
:::

::: {.solution}
<1>1. There exists an invertible Hermitian matrix
$$
Q=B^{-1/2}
$$
such that
$$
Q^*BQ=I.
$$

::: {.proof}
Since $B$ is positive definite, the spectral theorem gives a unitary
matrix $V$ and a diagonal matrix
$$
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad
\lambda_j>0,
$$
such that
$$
B=VDV^*.
$$
Define
$$
Q=VD^{-1/2}V^*,
$$
where
$$
D^{-1/2}
=
\operatorname{diag}(\lambda_1^{-1/2},\ldots,\lambda_n^{-1/2}).
$$
Then $Q$ is Hermitian and invertible, and
$$
\begin{aligned}
Q^*BQ
&=
VD^{-1/2}V^*\,VDV^*\,VD^{-1/2}V^*
\\
&=
VIV^*
\\
&=
I.
\end{aligned}
$$
:::

<1>2. The matrix
$$
H=Q^*AQ
$$
is Hermitian.

::: {.proof}
Using $A^*=A$,
$$
H^*
=(Q^*AQ)^*
=
Q^*A^*Q
=
Q^*AQ
=
H.
$$
:::

<1>3. There exists a unitary matrix $U$ such that
$$
U^*HU=\Lambda
$$
is diagonal.

::: {.proof}
This is the spectral theorem for the Hermitian matrix $H$ from step
<1>2.
:::

<1>4. Set
$$
S=QU.
$$
Then $S$ is invertible and
$$
S^*BS=I.
$$

::: {.proof}
Both $Q$ and $U$ are invertible, so $S$ is invertible. By step <1>1
and unitarity of $U$,
$$
\begin{aligned}
S^*BS
&=
U^*Q^*BQU
\\
&=
U^*IU
\\
&=
I.
\end{aligned}
$$
:::

<1>5. The same matrix $S$ satisfies
$$
\boxed{S^*AS=\Lambda},
$$
which is diagonal.

::: {.proof}
By the definitions of $S$ and $H$ and by step <1>3,
$$
\begin{aligned}
S^*AS
&=
U^*Q^*AQU
\\
&=
U^*HU
\\
&=
\Lambda.
\end{aligned}
$$
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>4 and <1>5 give the required invertible matrix $S$.
:::
:::
