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

::: pf

::: {.pf-step #s1-1}

One has
$$
\operatorname{im}(MM^T)
\subseteq
\operatorname{im}M.
$$


::: pf-proof

Every vector in the range of $MM^T$ has the form
$$
MM^Tx
$$
for some $x\in\RR^n$.
But
$$
MM^Tx
=
M(M^Tx),
$$
which lies in the range of $M$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{
\ker(MM^T)
=
\ker M^T.
}
$$


::: pf-proof

If
$$
M^Tx=0,
$$
then clearly
$$
MM^Tx=0.
$$
Thus
$$
\ker M^T
\subseteq
\ker(MM^T).
$$

Conversely, suppose
$$
MM^Tx=0.
$$
Then
$$
0
=
x^TMM^Tx
=
(M^Tx)^T(M^Tx)
=
\|M^Tx\|_2^2.
$$
Hence
$$
M^Tx=0.
$$
Thus the reverse inclusion also holds.

:::

:::

::: {.pf-step #s1-3}

The two matrices have the same rank:
$$
\boxed{
\operatorname{rank}(MM^T)
=
\operatorname{rank}M.
}
$$


::: pf-proof

By rank-nullity and step [](#s1-2){.pf-ref},
$$
\begin{aligned}
\operatorname{rank}(MM^T)
&=
n-\dim\ker(MM^T)\\
&=
n-\dim\ker M^T\\
&=
\operatorname{rank}M^T.
\end{aligned}
$$
The row rank equals the column rank, so
$$
\operatorname{rank}M^T
=
\operatorname{rank}M.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\operatorname{im}(MM^T)
=
\operatorname{im}M.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives an inclusion of finite-dimensional subspaces.
Step [](#s1-3){.pf-ref} shows that the two subspaces have the same dimension.
Hence the inclusion is equality.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
