---
schema: qual/card@1
id: P-BKS17-6B
kind: problem
title: Low-rank approximation of the matrix $f(t_is_j)$ for analytic $f$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 17 problem 6B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 Taylor-truncation argument. Its entrywise estimate is correct, but the printed solution does not justify the requested rank bound; the solution below exhibits the truncation as a sum of $r$ rank-one matrices.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified Taylor convergence at every $t_is_j$, the rank-one decomposition, and the factorial-tail estimate by a geometric bound.
---

::: {.problem}
Let $D$ be the unit disk in the complex plane $\CC$, $f : D \to \CC$ an analytic function with

$$
\abs{f^{(k)}(0)} \leq M
$$

for all $k \geq 0$, and let $t_p \in D$, $s_p \in D$ for $1 \leq p \leq n$. For each $n \geq 1$ define $A_{ij} = f(t_i s_j)$ for $1 \leq i, j \leq n$. For each $r \geq 1$ find an $n \times n$ matrix $B$ with rank $\leq r$ and

$$
\abs{A_{ij} - B_{ij}} \leq \frac{2M}{r!}
$$

for $1 \leq i, j \leq n$.
:::

::: {.solution}

For $k\geq0$, set
$$
a_k\coloneqq\frac{f^{(k)}(0)}{k!},
\qquad
u_k\coloneqq(t_1^k,\ldots,t_n^k)^T,
\qquad
v_k\coloneqq(s_1^k,\ldots,s_n^k)^T.
$$

::: pf

::: {.pf-step #s1-1}

Define the matrix $B$ by
$$
\boxed{
B_{ij}
=
\sum_{k=0}^{r-1}a_k(t_is_j)^k
}.
$$
Equivalently,
$$
B=\sum_{k=0}^{r-1}a_k u_kv_k^T.
$$


::: pf-proof

The $(i,j)$ entry of $u_kv_k^T$ is $t_i^ks_j^k=(t_is_j)^k$, so the two displayed definitions agree.

:::

:::

::: {.pf-step #s1-2}

The matrix $B$ has rank at most $r$.


::: pf-proof

Each outer product $u_kv_k^T$ has rank at most $1$. Therefore
$$
\operatorname{rank}(B)
\leq
\sum_{k=0}^{r-1}\operatorname{rank}(a_ku_kv_k^T)
\leq r.
$$

:::

:::

::: {.pf-step #s1-3}

For every $1\leq i,j\leq n$,
$$
\abs{A_{ij}-B_{ij}}
\leq
M\sum_{k=r}^{\infty}\frac1{k!}.
$$


::: pf-proof

Since $\abs{t_i}<1$ and $\abs{s_j}<1$, one has $\abs{t_is_j}<1$. The Taylor series of $f$ at $0$ therefore converges to $f(t_is_j)$:
$$
A_{ij}
=
f(t_is_j)
=
\sum_{k=0}^{\infty}a_k(t_is_j)^k.
$$
Subtracting the truncation from step [](#s1-1){.pf-ref} and using $\abs{f^{(k)}(0)}\leq M$ gives
$$
\begin{aligned}
\abs{A_{ij}-B_{ij}}
&\leq
\sum_{k=r}^{\infty}\frac{\abs{f^{(k)}(0)}}{k!}\abs{t_is_j}^k\\
&\leq
M\sum_{k=r}^{\infty}\frac1{k!}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

For every integer $r\geq1$,
$$
\sum_{k=r}^{\infty}\frac1{k!}\leq\frac2{r!}.
$$


::: pf-proof

Writing $k=r+m$,
$$
\sum_{k=r}^{\infty}\frac1{k!}
=
\frac1{r!}
\left(
1+
\sum_{m=1}^{\infty}
\frac1{(r+1)(r+2)\cdots(r+m)}
\right).
$$
Because $r\geq1$, every factor $r+j$ is at least $2$, so
$$
\frac1{(r+1)(r+2)\cdots(r+m)}\leq2^{-m}.
$$
Hence the parenthesized expression is at most
$$
1+\sum_{m=1}^{\infty}2^{-m}=2.
$$

:::

:::

::: {.pf-step #s1-5}

The matrix $B$ from step [](#s1-1){.pf-ref} satisfies
$$
\boxed{
\operatorname{rank}(B)\leq r,
\qquad
\abs{A_{ij}-B_{ij}}\leq\frac{2M}{r!}
}.
$$


::: pf-proof

The rank bound is step [](#s1-2){.pf-ref}. Combining steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} gives the entrywise error bound.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required matrix and both requested estimates.

:::

:::

:::
