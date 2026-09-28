---
schema: qual/card@1
id: P-BKF03-6A
kind: problem
title: Rank over $\mathbb F_p$ of the power matrix $(j^i)$
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
  note: Checked against Problem 6A of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the nonzero Vandermonde minor and the upper bound from repeated residue-class columns.
---

::: {.problem}
Let $A ( m , n )$ be the $m \times n$ matrix with entries

$$
a _ { i j } = j ^ { i } \quad ( 0 \leq i \leq m - 1 , 0 \leq j \leq n - 1 ) ,
$$

where $0 ^ { 0 } = 1$ by definition.
Regarding the entries of $A ( m , n )$ as representing congruence classes (mod p), determine the rank of $A ( m , n )$ over the finite field $\mathbb { F } _ { p } ~ = ~ \mathbb { Z } / p \mathbb { Z }$ for all $m , n \geq 1$ and all primes p.
:::


::: {.solution}
Let
\[
k:=\min\{m,n,p\}.
\]
We prove that the rank is exactly $k$.

<1>1. The upper-left $k\times k$ minor of $A(m,n)$ is a Vandermonde matrix with nonzero determinant in $\mathbb F_p$.
::: {.proof}
Its rows are indexed by $i=0,\dots,k-1$ and columns by $j=0,\dots,k-1$, so it is
\[
V=(j^i)_{0\le i,j\le k-1}.
\]
Its determinant is the Vandermonde product
\[
\det V=\prod_{0\le r<s\le k-1}(s-r).
\]
Because $k\le p$, every difference $s-r$ satisfies
\[
1\le s-r\le k-1<p.
\]
Hence no factor is $0$ in $\mathbb F_p$, so $\det V\ne0$ in $\mathbb F_p$. Therefore
\[
\operatorname{rank}_{\mathbb F_p}A(m,n)\ge k.
\]
:::

<1>2. One has
\[
\operatorname{rank}_{\mathbb F_p}A(m,n)\le m
\qquad\text{and}\qquad
\operatorname{rank}_{\mathbb F_p}A(m,n)\le n.
\]
::: {.proof}
These are the standard row and column bounds for the rank of an $m\times n$ matrix.
:::

<1>3. One also has
\[
\operatorname{rank}_{\mathbb F_p}A(m,n)\le p.
\]
::: {.proof}
After reducing modulo $p$, the column indexed by $j$ depends only on the residue class of $j$ modulo $p$, because its entries are
\[
1,j,j^2,\dots,j^{m-1}
\]
in $\mathbb F_p$. Thus there are at most $p$ distinct columns. The column space is therefore spanned by at most $p$ columns, so its dimension is at most $p$.
:::

<1>4. Combining the bounds gives the rank.
::: {.proof}
By <1>2 and <1>3,
\[
\operatorname{rank}_{\mathbb F_p}A(m,n)\le\min\{m,n,p\}=k.
\]
By <1>1, the reverse inequality holds. Hence
\[
\boxed{\operatorname{rank}_{\mathbb F_p}A(m,n)=\min\{m,n,p\}}.
\]
:::
:::
