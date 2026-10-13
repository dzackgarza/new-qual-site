---
schema: qual/card@1
id: P-LATEST2-35
kind: problem
title: Rank of the matrix containing 1 through 25
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Find the rank of
\[
\begin{pmatrix}
1&2&3&4&5\\
6&7&8&9&10\\
11&12&13&14&15\\
16&17&18&19&20\\
21&22&23&24&25
\end{pmatrix}.
\]

(A) $1$  (B) $2$  (C) $3$  (D) $4$  (E) $5$
:::

::: {.solution}
Let the rows be $r_1,\ldots,r_5$, and set
$$
u=(1,1,1,1,1).
$$

<1>1. Every row lies in the span of $r_1$ and $u$.

::: {.proof}
The first row is
$$
r_1=(1,2,3,4,5).
$$
For $k=0,1,2,3,4$, the $(k+1)$st row is
$$
r_{k+1}=r_1+5k,u.
$$
Indeed, each entry increases by $5k$ from the corresponding entry of the first row.
Thus all rows belong to
$$
\operatorname{span}\{r_1,u\}.
$$
:::

<1>2. Therefore the rank is at most $2$.

::: {.proof}
The row space is contained in the span of two vectors by step <1>1.
Hence its dimension is at most $2$.
:::

<1>3. The vectors $r_1$ and $u$ are linearly independent.

::: {.proof}
If
$$
r_1=cu
$$
for some scalar $c$, then all five entries of $r_1$ would be equal to $c$.
But
$$
r_1=(1,2,3,4,5)
$$
has unequal entries.
Thus $r_1$ is not a scalar multiple of $u$.
:::

<1>4. Therefore the rank is at least $2$.

::: {.proof}
The row space contains the linearly independent vectors $r_1$ and
$$
u=\frac15(r_2-r_1).
$$
Hence its dimension is at least $2$.
:::

<1>5. Consequently,
$$
\boxed{\operatorname{rank}=2}.
$$

::: {.proof}
Combine steps <1>2 and <1>4.
This is answer choice $\boxed{\text{(B)}}$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required rank.
:::
:::
