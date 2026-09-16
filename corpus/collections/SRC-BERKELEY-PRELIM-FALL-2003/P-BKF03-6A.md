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
\n\n::: {.solution}\nLet\n\[\nk:=\min\{m,n,p\}.\n\]\nWe prove that the rank is exactly $k$.\n\n<1>1. The upper-left $k\times k$ minor of $A(m,n)$ is a Vandermonde matrix with nonzero determinant in $\mathbb F_p$.\n::: {.proof}\nIts rows are indexed by $i=0,\dots,k-1$ and columns by $j=0,\dots,k-1$, so it is\n\[\nV=(j^i)_{0\le i,j\le k-1}.\n\]\nIts determinant is the Vandermonde product\n\[\n\det V=\prod_{0\le r<s\le k-1}(s-r).\n\]\nBecause $k\le p$, every difference $s-r$ satisfies\n\[\n1\le s-r\le k-1<p.\n\]\nHence no factor is $0$ in $\mathbb F_p$, so $\det V\ne0$ in $\mathbb F_p$. Therefore\n\[\n\operatorname{rank}_{\mathbb F_p}A(m,n)\ge k.\n\]\n:::\n\n<1>2. One has\n\[\n\operatorname{rank}_{\mathbb F_p}A(m,n)\le m\n\qquad\text{and}\qquad\n\operatorname{rank}_{\mathbb F_p}A(m,n)\le n.\n\]\n::: {.proof}\nThese are the standard row and column bounds for the rank of an $m\times n$ matrix.\n:::\n\n<1>3. One also has\n\[\n\operatorname{rank}_{\mathbb F_p}A(m,n)\le p.\n\]\n::: {.proof}\nAfter reducing modulo $p$, the column indexed by $j$ depends only on the residue class of $j$ modulo $p$, because its entries are\n\[\n1,j,j^2,\dots,j^{m-1}\n\]\nin $\mathbb F_p$. Thus there are at most $p$ distinct columns. The column space is therefore spanned by at most $p$ columns, so its dimension is at most $p$.\n:::\n\n<1>4. Combining the bounds gives the rank.\n::: {.proof}\nBy <1>2 and <1>3,\n\[\n\operatorname{rank}_{\mathbb F_p}A(m,n)\le\min\{m,n,p\}=k.\n\]\nBy <1>1, the reverse inequality holds. Hence\n\[\n\boxed{\operatorname{rank}_{\mathbb F_p}A(m,n)=\min\{m,n,p\}}.\n\]\n:::\n:::\n