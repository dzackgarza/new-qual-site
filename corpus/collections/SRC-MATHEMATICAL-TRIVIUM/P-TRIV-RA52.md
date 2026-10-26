---
schema: qual/card@1
id: P-TRIV-RA52
kind: problem
title: Divergence of the $p$-series $\sum n^{-\alpha}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 52, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in N to infinity against Real Analysis Problem 52 on page 12 of the source PDF.
---

::: {.problem}
For what values of $\alpha$ the series $\displaystyle\sum_{n=1}^{N} \frac{1}{n^\alpha}$ diverges as $N \to \infty$?
:::

::: pf

::: pf-step

If
$$
\alpha\leq0,
$$
then the terms
$$
n^{-\alpha}
$$
do not tend to $0$.


::: pf-proof

If $\alpha=0$, then $n^{-\alpha}=1$. If $\alpha<0$, then
$$
n^{-\alpha}=n^{|\alpha|}\to\infty.
$$

:::

:::

::: pf-step

Therefore the series diverges for
$$
\alpha\leq0.
$$


::: pf-proof

A necessary condition for convergence of a series is that its terms tend to
$0$. Step <1>1 shows this condition fails.

:::

:::

::: pf-step

Suppose
$$
0<\alpha\leq1.
$$
Then the function
$$
x\longmapsto x^{-\alpha}
$$
is positive and decreasing on $[1,\infty)$.


::: pf-proof

Its derivative is
$$
-\alpha x^{-\alpha-1}<0.
$$

:::

:::

::: pf-step

For every integer $N\geq1$,
$$
\sum_{n=1}^{N}n^{-\alpha}
\geq
\int_1^{N+1}x^{-\alpha}\,dx.
$$


::: pf-proof

Because $x^{-\alpha}$ is decreasing, for
$$
x\in[n,n+1]
$$
one has
$$
x^{-\alpha}\leq n^{-\alpha}.
$$
Integrating over each interval and summing from $n=1$ to $N$ gives the
inequality.

:::

:::

::: pf-step

If
$$
0<\alpha<1,
$$
then
$$
\int_1^{N+1}x^{-\alpha}\,dx
=
\frac{(N+1)^{1-\alpha}-1}{1-\alpha}
\longrightarrow\infty.
$$


::: pf-proof

Since $1-\alpha>0$, the power $(N+1)^{1-\alpha}$ tends to infinity.

:::

:::

::: pf-step

If
$$
\alpha=1,
$$
then
$$
\int_1^{N+1}\frac{dx}{x}
=
\log(N+1)
\longrightarrow\infty.
$$


::: pf-proof

Evaluate the logarithmic antiderivative.

:::

:::

::: pf-step

Hence the series diverges for every
$$
\alpha\leq1.
$$


::: pf-proof

Step <1>2 handles $\alpha\leq0$. For $0<\alpha\leq1$, steps <1>4--<1>6
show that the partial sums dominate a quantity tending to infinity.

:::

:::

::: pf-step

If
$$
\alpha>1,
$$
the series converges.


::: pf-proof

The integral test gives
$$
\int_1^\infty x^{-\alpha}\,dx
=
\frac1{\alpha-1}<\infty.
$$
Therefore the corresponding positive decreasing series converges.

:::

:::

::: pf-step

Therefore the divergence region is exactly
$$
\boxed{\alpha\leq1}.
$$


::: pf-proof

Step <1>7 proves divergence there, while step <1>8 excludes every
$\alpha>1$.

:::

:::

::: pf-qed

Step <1>9 is the required classification.

:::

:::
