---
schema: qual/card@1
id: P-TRIV-LA15
kind: problem
title: Number of independent entries of an orthogonal matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 15, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let A be $n \times n$ real orthogonal matrix.
Calculate the number of independent elements of A.
:::

::: {.solution}

Write the columns of $A$ as
$$
v_1,\ldots,v_n.
$$
Since $A$ is orthogonal, these columns form an orthonormal basis of
$\RR^n$.

::: pf

::: pf-step

The first column $v_1$ has $n-1$ independent parameters.


::: pf-proof

The vector $v_1$ lies on the unit sphere
$$
S^{n-1}\subset\RR^n,
$$
which has dimension $n-1$.

:::

:::

::: pf-step

Once $v_1$ is fixed, the second column $v_2$ has $n-2$ independent
parameters.


::: pf-proof

The vector $v_2$ must be a unit vector in the orthogonal complement
$$
v_1^\perp,
$$
which is an $(n-1)$-dimensional vector space. Its unit sphere therefore has
dimension $n-2$.

:::

:::

::: {.pf-step #s1-3}

More generally, once
$$
v_1,\ldots,v_{k-1}
$$
have been chosen, the column $v_k$ has
$$
n-k
$$
independent parameters.


::: pf-proof

The vector $v_k$ must be a unit vector in
$$
\operatorname{span}(v_1,\ldots,v_{k-1})^\perp,
$$
which has dimension
$$
n-(k-1)=n-k+1.
$$
The unit sphere in that space has dimension $n-k$.

:::

:::

::: {.pf-step #s1-4}

Hence the total number of independent parameters is
$$
\sum_{k=1}^{n}(n-k)
=
(n-1)+(n-2)+\cdots+1+0.
$$


::: pf-proof

Add the independent choices from step [](#s1-3){.pf-ref} for all columns.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\frac{n(n-1)}2
}
$$
independent real parameters are needed to specify an $n\times n$ orthogonal
matrix.


::: pf-proof

The arithmetic sum in step [](#s1-4){.pf-ref} is
$$
\frac{n(n-1)}2.
$$
Equivalently,
$$
\dim O(n)=\frac{n(n-1)}2.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required count.

:::

:::

:::
