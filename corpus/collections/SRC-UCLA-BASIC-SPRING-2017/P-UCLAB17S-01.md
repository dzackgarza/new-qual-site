---
schema: qual/card@1
id: P-UCLAB17S-01
kind: problem
title: Range of a matrix and its Gram product
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $M$ be a real $n\times n$ matrix. Prove that $M$ and $MM^T$ have the same range.
:::

::: {.solution}
<1>1. One has
\[
\operatorname{im}(MM^T)
\subseteq
\operatorname{im}M.
\]

::: {.proof}
Every vector in the range of $MM^T$ has the form
\[
MM^Tx
\]
for some $x\in\mathbb R^n$.
But
\[
MM^Tx
=
M(M^Tx),
\]
which lies in the range of $M$.
:::

<1>2. One has
\[
\boxed{
\ker(MM^T)
=
\ker M^T.
}
\]

::: {.proof}
If
\[
M^Tx=0,
\]
then clearly
\[
MM^Tx=0.
\]
Thus
\[
\ker M^T
\subseteq
\ker(MM^T).
\]

Conversely, suppose
\[
MM^Tx=0.
\]
Then
\[
0
=
x^TMM^Tx
=
(M^Tx)^T(M^Tx)
=
\|M^Tx\|_2^2.
\]
Hence
\[
M^Tx=0.
\]
Thus the reverse inclusion also holds.
:::

<1>3. The two matrices have the same rank:
\[
\boxed{
\operatorname{rank}(MM^T)
=
\operatorname{rank}M.
}
\]

::: {.proof}
By rank-nullity and step <1>2,
\[
\begin{aligned}
\operatorname{rank}(MM^T)
&=
n-\dim\ker(MM^T)\\
&=
n-\dim\ker M^T\\
&=
\operatorname{rank}M^T.
\end{aligned}
\]
The row rank equals the column rank, so
\[
\operatorname{rank}M^T
=
\operatorname{rank}M.
\]
:::

<1>4. Therefore
\[
\boxed{
\operatorname{im}(MM^T)
=
\operatorname{im}M.
}
\]

::: {.proof}
Step <1>1 gives an inclusion of finite-dimensional subspaces.
Step <1>3 shows that the two subspaces have the same dimension.
Hence the inclusion is equality.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
