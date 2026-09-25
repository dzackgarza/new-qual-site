---
schema: qual/card@1
id: P-BKF95-9
kind: problem
title: A nonlinear recurrence stays bounded away from zero
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/Fall95_extracted.md; Flash garbles the placement of $\liminf$ and $n\to\infty$, restored from the deterministic sentence.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Rewrote the recurrence as a product and bounded its factors below by
    1-x_1^k. The comparison infinite product is positive because the
    geometric series sum x_1^k converges.
---

::: {.problem}
Let $0<x_1<1$ and define
\[
x_{n+1}=x_n-x_n^{n+1}.
\]
Show that
\[
\liminf_{n\to\infty}x_n>0.
\]
:::

::: {.solution}
Set
$$
q\coloneqq x_1,
$$
so
$$
0<q<1.
$$

<1>1. For every $n\geq1$,
$$
0<x_{n+1}<x_n\leq q<1.
$$

::: {.proof}
Suppose $0<x_n<1$. Then
$$
0<x_n^n<1,
$$
so
$$
0<1-x_n^n<1.
$$
The recurrence can be written
$$
x_{n+1}
=
x_n(1-x_n^n),
$$
which therefore satisfies
$$
0<x_{n+1}<x_n.
$$
Starting from $0<x_1=q<1$, induction proves the assertion.
:::

<1>2. For every $n\geq2$,
$$
x_n
=
q\prod_{k=1}^{n-1}(1-x_k^k).
$$

::: {.proof}
The recurrence gives
$$
\frac{x_{k+1}}{x_k}
=
1-x_k^k
$$
because step <1>1 ensures $x_k\neq0$. Multiplying these identities for
$k=1,\ldots,n-1$ telescopes to the displayed product.
:::

<1>3. For every $n\geq2$,
$$
x_n
\geq
q\prod_{k=1}^{n-1}(1-q^k).
$$

::: {.proof}
By step <1>1,
$$
0<x_k\leq q<1.
$$
Hence
$$
x_k^k\leq q^k,
$$
so
$$
1-x_k^k
\geq
1-q^k.
$$
Apply this factor by factor in the product of step <1>2.
:::

<1>4. The infinite product
$$
P\coloneqq
\prod_{k=1}^{\infty}(1-q^k)
$$
converges to a strictly positive number.

::: {.proof}
Choose $K$ so large that
$$
q^k\leq\frac12
$$
for every $k\geq K$. For $0\leq t\leq1/2$,
$$
\log(1-t)\geq-2t.
$$
Therefore
$$
\sum_{k=K}^{\infty}\log(1-q^k)
\geq
-2\sum_{k=K}^{\infty}q^k
>
-\infty.
$$
The logarithmic series also consists of nonpositive terms, so its partial
sums decrease to a finite real limit. Exponentiating shows that
$$
\prod_{k=K}^{\infty}(1-q^k)>0.
$$
The finitely many factors with $k<K$ are all positive, hence the complete
product $P$ is positive.
:::

<1>5. For every $n$,
$$
x_n\geq qP>0.
$$

::: {.proof}
Each factor $1-q^k$ lies in $(0,1)$. Thus the finite products
$$
\prod_{k=1}^{n-1}(1-q^k)
$$
decrease to the infinite product $P$ and are therefore at least $P$. Step
<1>3 gives
$$
x_n
\geq
q\prod_{k=1}^{n-1}(1-q^k)
\geq
qP.
$$
The case $n=1$ also satisfies $x_1=q\geq qP$ because $P\leq1$.
:::

<1>6. One has
$$
\boxed{
\liminf_{n\to\infty}x_n
\geq
qP
>0
}.
$$

::: {.proof}
Step <1>5 gives the same positive lower bound for every term of the
sequence. Taking the lower limit preserves that inequality.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
