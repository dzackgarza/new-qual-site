---
schema: qual/card@1
id: P-UCLAB11S-02
kind: problem
title: Powers of a diagonalizable invertible matrix
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Show that if an invertible complex matrix is diagonalizable, then every positive power of it is diagonalizable.
:::

::: {.solution}
<1>1. Since $A$ is diagonalizable, there exists an invertible matrix $P$ and a diagonal matrix
\[
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
\]
such that
\[
\boxed{A=PDP^{-1}}.
\]

::: {.proof}
This is the definition of diagonalizability over $\mathbb C$.
Because $A$ is invertible, none of the diagonal entries $\lambda_i$ is zero, although this is not needed for the positive-power conclusion.
:::

<1>2. For every positive integer $m$,
\[
A^m
=
PD^mP^{-1}.
\]

::: {.proof}
Using
\[
A=PDP^{-1},
\]
one has
\[
\begin{aligned}
A^m
&=
(PDP^{-1})^m\\
&=
PD(P^{-1}P)D\cdots(P^{-1}P)DP^{-1}\\
&=
PD^mP^{-1}.
\end{aligned}
\]
All intermediate factors
\[
P^{-1}P
\]
cancel.
:::

<1>3. The matrix $D^m$ is diagonal.

::: {.proof}
Since
\[
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\]
raising $D$ to the $m$th power gives
\[
\boxed{
D^m
=
\operatorname{diag}
(\lambda_1^m,\ldots,\lambda_n^m).
}
\]
:::

<1>4. Therefore $A^m$ is diagonalizable for every positive integer $m$.

::: {.proof}
By step <1>2,
\[
A^m
\]
is similar to the diagonal matrix
\[
D^m,
\]
which is diagonal by step <1>3.
Hence
\[
\boxed{A^m\text{ is diagonalizable}.}
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
