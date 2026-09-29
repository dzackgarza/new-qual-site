---
schema: qual/card@1
id: P-BKS15-7B
kind: problem
title: Low-rank approximation of the exponential kernel matrix
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
  note: Independently checked the exponential-tail estimate and the decomposition of B as a sum of m rank-one matrices.
---

::: {.problem}
Fix $N\ge1$.
Let $s_1,\ldots,s_N,t_1,\ldots,t_N$ be $2N$ complex numbers of magnitude at most $1$, and let $A$ be the $N\times N$ matrix
$$
A_{ij}=\exp(t_is_j).
$$
Show that $A$ can be approximated by matrices of small rank in the following sense: for every $m\ge1$, the matrix $B$ with entries
$$
B_{ij}=\sum_{n=0}^{m-1}\frac{(t_is_j)^n}{n!}
$$
satisfies
$$
|A_{ij}-B_{ij}|\le\frac2{m!}
$$
for all $i,j$, and has rank at most $m$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every integer $m\geq1$,
$$
\sum_{n=m}^{\infty}\frac1{n!}
\leq
\frac2{m!}.
$$

::: pf-proof

Write $n=m+k$. For $k\geq0$,
$$
(m+k)!
=
m!(m+1)(m+2)\cdots(m+k)
\geq
m!2^k,
$$
where the empty product for $k=0$ is $1$. Hence
$$
\sum_{n=m}^{\infty}\frac1{n!}
\leq
\frac1{m!}\sum_{k=0}^{\infty}\frac1{2^k}
=
\frac2{m!}.
$$

:::

:::

::: {.pf-step #s2}

If $\abs{z}\leq1$, then
$$
\left|
e^z-
\sum_{n=0}^{m-1}\frac{z^n}{n!}
\right|
\leq
\frac2{m!}.
$$

::: pf-proof

The exponential power series gives
$$
e^z-
\sum_{n=0}^{m-1}\frac{z^n}{n!}
=
\sum_{n=m}^{\infty}\frac{z^n}{n!}.
$$
Therefore, by the triangle inequality and $\abs{z}\leq1$,
$$
\left|
e^z-
\sum_{n=0}^{m-1}\frac{z^n}{n!}
\right|
\leq
\sum_{n=m}^{\infty}\frac{\abs{z}^n}{n!}
\leq
\sum_{n=m}^{\infty}\frac1{n!}.
$$
Apply step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

For every $i,j$,
$$
\abs{A_{ij}-B_{ij}}
\leq
\frac2{m!}.
$$

::: pf-proof

Since $\abs{t_i}\leq1$ and $\abs{s_j}\leq1$,
$$
\abs{t_is_j}\leq1.
$$
Apply step [](#s2){.pf-ref} with $z=t_is_j$ and use the definitions of $A_{ij}$ and $B_{ij}$.

:::

:::

::: {.pf-step #s4}

The matrix $B$ is a sum of $m$ matrices of rank at most $1$.

::: pf-proof

For $0\leq n\leq m-1$, define column vectors
$$
u_n
\coloneqq
\begin{pmatrix}
t_1^n/n!\\
\vdots\\
t_N^n/n!
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
Then the $(i,j)$ entry of $u_nv_n^T$ is
$$
\frac{t_i^ns_j^n}{n!}
=
\frac{(t_is_j)^n}{n!}.
$$
Hence
$$
B
=
\sum_{n=0}^{m-1}u_nv_n^T.
$$
Each outer product $u_nv_n^T$ has rank at most $1$.

:::

:::

::: {.pf-step #s5}

One has
$$
\rank B\leq m.
$$

::: pf-proof

By step [](#s4){.pf-ref} and subadditivity of matrix rank,
$$
\rank B
\leq
\sum_{n=0}^{m-1}\rank(u_nv_n^T)
\leq
m.
$$

:::

:::

::: {.pf-step #s6}

Therefore $B$ has the required entrywise approximation and rank bound.

::: pf-proof

Step [](#s3){.pf-ref} gives
$$
\boxed{
\abs{A_{ij}-B_{ij}}
\leq
\frac2{m!}
}
$$
for every $i,j$, and step [](#s5){.pf-ref} gives
$$
\boxed{\rank B\leq m}.
$$

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is exactly the required conclusion.

:::

:::

:::
