---
schema: qual/card@1
id: P-TRIV-LA07
kind: problem
title: First-order expansion of $\det(I+\epsilon B)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let $A = E + \epsilon B$, where $E$ is the identity matrix and $\epsilon \ll 1$. Expand $\det A$ to the first order in $\epsilon$.
:::

::: {.solution}

Write the columns of $B$ as
$$
b_1,\ldots,b_n,
$$
and the standard basis columns of the identity as
$$
e_1,\ldots,e_n.
$$

::: pf

::: pf-step

The columns of
$$
I+\epsilon B
$$
are
$$
e_j+\epsilon b_j,
\qquad
j=1,\ldots,n.
$$


::: pf-proof

This is the column-wise form of matrix addition and scalar multiplication.

:::

:::

::: {.pf-step #s1-2}

By multilinearity of the determinant,
$$
\det(I+\epsilon B)
=
1
+
\epsilon
\sum_{j=1}^n D_j
+
O(\epsilon^2),
$$
where $D_j$ is the determinant obtained from $I$ by replacing its $j$th
column by $b_j$.


::: pf-proof

Expand
$$
\det(e_1+\epsilon b_1,\ldots,e_n+\epsilon b_n)
$$
multilinearly. The term using only the $e_j$ is
$$
\det I=1.
$$
The terms linear in $\epsilon$ are exactly those in which one column $e_j$ is
replaced by $b_j$. Every term involving at least two columns from $B$ carries
at least two factors of $\epsilon$ and is therefore $O(\epsilon^2)$.

:::

:::

::: {.pf-step #s1-3}

For each $j$,
$$
D_j=b_{jj}.
$$


::: pf-proof

Expand $D_j$ along the $j$th column. Every cofactor vanishes except the one in
row $j$, because the remaining columns are standard basis vectors. The
surviving cofactor equals $1$, so the determinant is the $j$th entry of
$b_j$, namely $b_{jj}$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\sum_{j=1}^n D_j
=
\sum_{j=1}^n b_{jj}
=
\operatorname{Tr}B.
$$


::: pf-proof

Apply step [](#s1-3){.pf-ref} and the definition of trace.

:::

:::

::: {.pf-step #s1-5}

Hence the first-order expansion is
$$
\boxed{
\det(I+\epsilon B)
=
1
+
\epsilon\operatorname{Tr}B
+
O(\epsilon^2).
}
$$


::: pf-proof

Substitute step [](#s1-4){.pf-ref} into step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required first-order expansion.

:::

:::

:::
