---
schema: qual/card@1
id: P-TRIV-RA52
kind: problem
title: Divergence of the $p$-series $\sum n^{-\alpha}$
classification:
  areas: [real-analysis]
  topics:
  - Series Convergence
  - p-Series
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

::: pf

::: {.pf-step #s1-1}

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
n^{-\alpha}=n^{\abs{\alpha}}\to\infty.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore the series diverges for
$$
\alpha\leq0.
$$


::: pf-proof

A necessary condition for convergence of a series is that its terms tend to
$0$. Step [](#s1-1){.pf-ref} shows this condition fails.

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

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-5}

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

::: {.pf-step #s1-6}

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

::: {.pf-step #s1-7}

Hence the series diverges for every
$$
\alpha\leq1.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} handles $\alpha\leq0$. For $0<\alpha\leq1$, steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}
show that the partial sums dominate a quantity tending to infinity.

:::

:::

::: {.pf-step #s1-8}

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

::: {.pf-step #s1-9}

Therefore the divergence region is exactly
$$
\boxed{\alpha\leq1}.
$$


::: pf-proof

Step [](#s1-7){.pf-ref} proves divergence there, while step [](#s1-8){.pf-ref} excludes every
$\alpha>1$.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required classification.

:::

:::

:::
