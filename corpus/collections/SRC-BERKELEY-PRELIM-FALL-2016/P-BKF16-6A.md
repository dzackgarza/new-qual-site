---
schema: qual/card@1
id: P-BKF16-6A
kind: problem
title: Low-rank approximation of the matrix $(\exp(t_is_j))$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: truncating
    the exponential series after m terms gives an error at most 2/m!, and
    the truncation matrix is a sum of m rank-one outer products.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the factorial tail estimate uniformly for |t_i s_j|<=1 and the
    rank bound from the explicit outer-product decomposition.
---

::: {.problem}
Fix $N \geq 1$ . Let $s _ { 1 } , \ldots , s _ { N } , t _ { 1 } , \ldots , t _ { N }$ be 2N complex numbers of magnitude less than or equal to 1. Let A be the $N \times N$ matrix with entries

$$
A _ { i j } = \exp { ( t _ { i } s _ { j } ) } .
$$

Show that for every $m \geq 1$ there is an $N \times N$ matrix B with rank less than or equal to m such that

$$
\vert A _ { i j } - B _ { i j } \vert \le \frac { 2 } { m ! }
$$

for all i and $j .$
:::

::: {.solution}
For
$$
0\le n\le m-1,
$$
define vectors
$$
u_n
\coloneqq
\begin{pmatrix}
t_1^n\\
\vdots\\
t_N^n
\end{pmatrix},
\qquad
v_n
\coloneqq
\begin{pmatrix}
s_1^n\\
\vdots\\
s_N^n
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

If $\abs z\le1$, then
$$
\left|
e^z-\sum_{n=0}^{m-1}\frac{z^n}{n!}
\right|
\le
\frac2{m!}.
$$

::: pf-proof

The exponential series gives
$$
\left|
e^z-\sum_{n=0}^{m-1}\frac{z^n}{n!}
\right|
\le
\sum_{n=m}^{\infty}\frac{\abs z^n}{n!}
\le
\sum_{n=m}^{\infty}\frac1{n!}.
$$
For $k\ge0$,
$$
\frac1{(m+k)!}
\le
\frac1{m!}\frac1{(m+1)^k},
$$
because each of the $k$ factors after $m!$ is at least $m+1$.
Therefore
$$
\begin{aligned}
\sum_{n=m}^{\infty}\frac1{n!}
&\le
\frac1{m!}
\sum_{k=0}^{\infty}\frac1{(m+1)^k}\\
&=
\frac1{m!}\frac{m+1}{m}\\
&\le
\frac2{m!},
\end{aligned}
$$
since $m\ge1$.

:::

:::

::: {.pf-step #s2}

Define the matrix $B$ by
$$
B_{ij}
\coloneqq
\sum_{n=0}^{m-1}
\frac{(t_i s_j)^n}{n!}.
$$
Then
$$
\abs{A_{ij}-B_{ij}}
\le
\frac2{m!}
$$
for every $i,j$.

::: pf-proof

The hypotheses give
$$
\abs{t_i s_j}
\le
\abs{t_i}\abs{s_j}
\le
1.
$$
Apply step [](#s1){.pf-ref} to
$$
z=t_i s_j.
$$
Since
$$
A_{ij}=e^{t_i s_j},
$$
the displayed estimate follows.

:::

:::

::: {.pf-step #s3}

The matrix $B$ has the decomposition
$$
B
=
\sum_{n=0}^{m-1}
\frac1{n!}u_nv_n^T.
$$

::: pf-proof

The $(i,j)$ entry of the right-hand side is
$$
\sum_{n=0}^{m-1}
\frac1{n!}
(u_n)_i(v_n)_j
=
\sum_{n=0}^{m-1}
\frac{t_i^ns_j^n}{n!}
=
B_{ij}.
$$
Thus the matrices are equal.

:::

:::

::: {.pf-step #s4}

One has
$$
\operatorname{rank}B\le m.
$$

::: pf-proof

Each outer product
$$
u_nv_n^T
$$
has rank at most $1$. By subadditivity of matrix rank and step [](#s3){.pf-ref},
$$
\operatorname{rank}B
\le
\sum_{n=0}^{m-1}
\operatorname{rank}(u_nv_n^T)
\le
m.
$$

:::

:::

::: {.pf-step #s5}

Thus for every $m\ge1$ there is a matrix $B$ satisfying
$$
\boxed{
\operatorname{rank}B\le m
\quad\text{and}\quad
\abs{A_{ij}-B_{ij}}\le\frac2{m!}
}
$$
for all $i,j$.

::: pf-proof

Take the matrix $B$ from step [](#s2){.pf-ref}. The entrywise estimate is step
[](#s2){.pf-ref}, and the rank estimate is step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required construction.

:::

:::

:::
