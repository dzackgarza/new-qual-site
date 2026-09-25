---
schema: qual/card@1
id: P-BKS15-7A
kind: problem
title: Determinant of the Pascal matrix $\left[\binom{i+j}{i}\right]$
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the descending column and row operations, the Pascal-identity reductions, and the determinant recurrence.
---

::: {.problem}
Compute
\[
\Delta_n=
\det\left[\binom{i+j}{i}\right]_{0\le i,j\le n-1}.
\]
:::

::: {.solution}
Let
$$
A_n
\coloneqq
\left[\binom{i+j}{i}\right]_{0\leq i,j\leq n-1},
$$
so that $\Delta_n=\det A_n$.

<1>1. Starting with $A_n$, for $j=n-1,n-2,\ldots,1$ replace column $j$ by
$$
C_j-C_{j-1}.
$$
The resulting matrix $B_n=(b_{ij})$ has
$$
b_{i0}=1,
$$
and, for $j\geq1$,
$$
b_{0j}=0,
\qquad
b_{ij}=\binom{i+j-1}{i-1}
\quad(i\geq1).
$$

::: {.proof}
Each column replacement preserves the determinant. The columns are changed in descending order, so when column $j$ is replaced, column $j-1$ still has its original entries. Thus, for $j\geq1$ and $i\geq1$,
$$
\begin{aligned}
b_{ij}
&=
\binom{i+j}{i}
-
\binom{i+j-1}{i}\\
&=
\binom{i+j-1}{i-1}
\end{aligned}
$$
by Pascal's identity. For $i=0$ the same column difference is
$$
1-1=0.
$$
Column $0$ is unchanged and consists entirely of $1$'s.
:::

<1>2. Starting with $B_n$, for $i=n-1,n-2,\ldots,1$ replace row $i$ by
$$
R_i-R_{i-1}.
$$
The resulting matrix is
$$
\begin{pmatrix}
1&0\\
0&A_{n-1}
\end{pmatrix}.
$$

::: {.proof}
Again, each row replacement preserves the determinant, and descending order ensures that row $i-1$ is still unchanged when it is subtracted from row $i$.

By step <1>1, the first row of $B_n$ is $(1,0,\ldots,0)$ and the first column consists of $1$'s. Hence after the row differences, the first column becomes $(1,0,\ldots,0)^T$ while the first row stays fixed.

For $i\geq2$ and $j\geq1$, the new $(i,j)$ entry is
$$
\begin{aligned}
\binom{i+j-1}{i-1}
-
\binom{i+j-2}{i-2}
&=
\binom{i+j-2}{i-1},
\end{aligned}
$$
by Pascal's identity. For $i=1$ and $j\geq1$, the new entry is
$$
\binom{j}{0}-0
=
1
=
\binom{j-1}{0},
$$
so the same final formula holds for every $i,j\geq1$. Reindexing by
$$
i'=i-1,
\qquad
j'=j-1
$$
shows that the lower-right block has entries
$$
\binom{i'+j'}{i'},
$$
which is exactly $A_{n-1}$.
:::

<1>3. For every $n\geq2$,
$$
\Delta_n=\Delta_{n-1}.
$$

::: {.proof}
The column and row operations in steps <1>1 and <1>2 preserve determinant. Therefore
$$
\Delta_n
=
\det
\begin{pmatrix}
1&0\\
0&A_{n-1}
\end{pmatrix}
=
\det A_{n-1}
=
\Delta_{n-1}.
$$
:::

<1>4. One has
$$
\Delta_1=1.
$$

::: {.proof}
The matrix $A_1$ is the $1\times1$ matrix
$$
\left[\binom{0}{0}\right]=[1].
$$
:::

<1>5. Therefore, for every $n\geq1$,
$$
\boxed{\Delta_n=1}.
$$

::: {.proof}
Apply step <1>3 repeatedly until reaching the base case in step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested determinant.
:::
:::
