---
schema: qual/card@1
id: P-BKF95-8
kind: problem
title: Strict diagonal dominance implies invertibility
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Assumed a nonzero kernel vector and chose a coordinate of maximal
    modulus; the corresponding row equation contradicts strict diagonal
    dominance.
---

::: {.problem}
Let $A=(a_{ij})$ be an $n\times n$ complex matrix satisfying
\[
|a_{ii}|>\sum_{j\ne i}|a_{ij}|
\]
for every $1\le i\le n$.
Prove that $A$ is invertible.
:::

::: {.solution}
<1>1. Suppose
$$
Ax=0
$$
for some nonzero vector
$$
x=(x_1,\ldots,x_n)^t\in\CC^n.
$$
Choose an index $i$ such that
$$
\abs{x_i}
=
\max_{1\leq j\leq n}\abs{x_j}.
$$
Then
$$
\abs{x_i}>0.
$$

::: {.proof}
Since $x\neq0$, at least one coordinate is nonzero. A finite set of
nonnegative real numbers has a maximum, so such an index $i$ exists, and
its maximal modulus is positive.
:::

<1>2. The $i$th row equation implies
$$
\abs{a_{ii}}\abs{x_i}
\leq
\left(
\sum_{j\neq i}\abs{a_{ij}}
\right)
\abs{x_i}.
$$

::: {.proof}
The equation $Ax=0$ gives
$$
a_{ii}x_i
=
-\sum_{j\neq i}a_{ij}x_j.
$$
Taking absolute values and using the triangle inequality,
$$
\abs{a_{ii}}\abs{x_i}
\leq
\sum_{j\neq i}
\abs{a_{ij}}\abs{x_j}.
$$
By the choice of $i$ in step <1>1,
$$
\abs{x_j}\leq\abs{x_i}
$$
for every $j$. Substitution gives the displayed bound.
:::

<1>3. The assumption $x\neq0$ is impossible.

::: {.proof}
Strict diagonal dominance gives
$$
\sum_{j\neq i}\abs{a_{ij}}
<
\abs{a_{ii}}.
$$
Since $\abs{x_i}>0$, step <1>2 therefore yields
$$
\abs{a_{ii}}\abs{x_i}
<
\abs{a_{ii}}\abs{x_i},
$$
a contradiction.
:::

<1>4. The kernel of $A$ is trivial.

::: {.proof}
Step <1>3 shows that no nonzero vector can satisfy $Ax=0$.
:::

<1>5. The matrix $A$ is invertible.

::: {.proof}
By step <1>4, the linear map
$$
A:\CC^n\longrightarrow\CC^n
$$
is injective. Since domain and codomain have the same finite dimension, it
is bijective, hence $A$ is invertible.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
