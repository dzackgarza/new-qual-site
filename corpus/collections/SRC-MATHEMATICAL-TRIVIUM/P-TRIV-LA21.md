---
schema: qual/card@1
id: P-TRIV-LA21
kind: problem
title: No commutator of real matrices is a nonzero multiple of the identity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the linear transformations A, B of the vector space $\mathbb { R } ^ { n }$ . Prove that $[ A , B ] \neq c E$ , where E is the identity matrix, $c \in \mathbb { R }$
:::

::: {.remark}
As printed, the statement is false for $c=0$: if $A$ and $B$ commute, then
$[A,B]=0$. The intended assertion is that a commutator cannot equal a
nonzero scalar multiple $cI$ with $c\neq0$.
:::

::: pf

::: pf-step

For any two $n\times n$ matrices $A$ and $B$,
$$
\operatorname{Tr}(AB)=\operatorname{Tr}(BA).
$$


::: pf-proof

Writing entries,
$$
\operatorname{Tr}(AB)
=
\sum_{i=1}^n\sum_{j=1}^n a_{ij}b_{ji}.
$$
Interchanging the dummy indices $i$ and $j$ gives
$$
\sum_{j=1}^n\sum_{i=1}^n b_{ji}a_{ij}
=
\operatorname{Tr}(BA).
$$

:::

:::

::: pf-step

Every commutator has trace zero:
$$
\operatorname{Tr}[A,B]=0.
$$


::: pf-proof

By definition,
$$
[A,B]=AB-BA.
$$
Therefore, using step <1>1,
$$
\operatorname{Tr}[A,B]
=
\operatorname{Tr}(AB)-\operatorname{Tr}(BA)
=0.
$$

:::

:::

::: pf-step

If
$$
[A,B]=cI,
$$
then
$$
cn=0.
$$


::: pf-proof

Take traces and use step <1>2:
$$
0
=
\operatorname{Tr}[A,B]
=
\operatorname{Tr}(cI)
=
cn.
$$

:::

:::

::: pf-step

Over $\mathbb R$, if $n\geq1$, the equality
$$
[A,B]=cI
$$
forces
$$
c=0.
$$


::: pf-proof

Since $n$ is a positive integer, it is nonzero in $\mathbb R$. Thus step
<1>3 implies $c=0$.

:::

:::

::: pf-step

Therefore no commutator of real matrices can be a nonzero scalar
multiple of the identity:
$$
\boxed{[A,B]\neq cI\quad\text{for every }c\neq0.}
$$


::: pf-proof

If such an equality held, step <1>4 would force $c=0$, a contradiction.

:::

:::

::: pf-qed

Step <1>5 is the corrected intended conclusion.

:::

:::
