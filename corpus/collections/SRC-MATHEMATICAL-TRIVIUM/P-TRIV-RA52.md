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

::: {.solution}
<1>1. If
$$
\alpha\leq0,
$$
then the terms
$$
n^{-\alpha}
$$
do not tend to $0$.

::: {.proof}
If $\alpha=0$, then $n^{-\alpha}=1$. If $\alpha<0$, then
$$
n^{-\alpha}=n^{|\alpha|}\to\infty.
$$
:::

<1>2. Therefore the series diverges for
$$
\alpha\leq0.
$$

::: {.proof}
A necessary condition for convergence of a series is that its terms tend to
$0$. Step <1>1 shows this condition fails.
:::

<1>3. Suppose
$$
0<\alpha\leq1.
$$
Then the function
$$
x\longmapsto x^{-\alpha}
$$
is positive and decreasing on $[1,\infty)$.

::: {.proof}
Its derivative is
$$
-\alpha x^{-\alpha-1}<0.
$$
:::

<1>4. For every integer $N\geq1$,
$$
\sum_{n=1}^{N}n^{-\alpha}
\geq
\int_1^{N+1}x^{-\alpha}\,dx.
$$

::: {.proof}
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

<1>5. If
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

::: {.proof}
Since $1-\alpha>0$, the power $(N+1)^{1-\alpha}$ tends to infinity.
:::

<1>6. If
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

::: {.proof}
Evaluate the logarithmic antiderivative.
:::

<1>7. Hence the series diverges for every
$$
\alpha\leq1.
$$

::: {.proof}
Step <1>2 handles $\alpha\leq0$. For $0<\alpha\leq1$, steps <1>4--<1>6
show that the partial sums dominate a quantity tending to infinity.
:::

<1>8. If
$$
\alpha>1,
$$
the series converges.

::: {.proof}
The integral test gives
$$
\int_1^\infty x^{-\alpha}\,dx
=
\frac1{\alpha-1}<\infty.
$$
Therefore the corresponding positive decreasing series converges.
:::

<1>9. Therefore the divergence region is exactly
$$
\boxed{\alpha\leq1}.
$$

::: {.proof}
Step <1>7 proves divergence there, while step <1>8 excludes every
$\alpha>1$.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required classification.
:::
:::
