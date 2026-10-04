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
$\mathbb R^n$.

<1>1. The first column $v_1$ has $n-1$ independent parameters.

::: {.proof}
The vector $v_1$ lies on the unit sphere
$$
S^{n-1}\subset\mathbb R^n,
$$
which has dimension $n-1$.
:::

<1>2. Once $v_1$ is fixed, the second column $v_2$ has $n-2$ independent
parameters.

::: {.proof}
The vector $v_2$ must be a unit vector in the orthogonal complement
$$
v_1^\perp,
$$
which is an $(n-1)$-dimensional vector space. Its unit sphere therefore has
dimension $n-2$.
:::

<1>3. More generally, once
$$
v_1,\ldots,v_{k-1}
$$
have been chosen, the column $v_k$ has
$$
n-k
$$
independent parameters.

::: {.proof}
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

<1>4. Hence the total number of independent parameters is
$$
\sum_{k=1}^{n}(n-k)
=
(n-1)+(n-2)+\cdots+1+0.
$$

::: {.proof}
Add the independent choices from step <1>3 for all columns.
:::

<1>5. Therefore
$$
\boxed{
\frac{n(n-1)}2
}
$$
independent real parameters are needed to specify an $n\times n$ orthogonal
matrix.

::: {.proof}
The arithmetic sum in step <1>4 is
$$
\frac{n(n-1)}2.
$$
Equivalently,
$$
\dim O(n)=\frac{n(n-1)}2.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required count.
:::
:::
