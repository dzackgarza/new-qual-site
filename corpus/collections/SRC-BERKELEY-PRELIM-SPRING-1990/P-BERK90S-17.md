---
schema: qual/card@1
id: P-BERK90S-17
kind: problem
title: First-order error bound for left Riemann sums
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared differentiability on the closed interval, the interior derivative bound, the left-endpoint sum, and the constant M/(2n) with Problem 17 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Applied the mean value theorem on each subdivision interval and integrated the pointwise error before summing the local estimates.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked all endpoint cases, that the mean value points lie in the open unit interval, the local integral M/(2n^2), and the sum of n errors without assuming a continuous derivative.
---

::: {.problem}
Let $f$ be differentiable on $[0,1]$ and suppose
$$
M=\sup_{0<x<1}\abs{f'(x)}<\infty.
$$
For every positive integer $n$, prove that
$$
\abs{
\frac1n\sum_{j=0}^{n-1}f(j/n)
-\int_0^1f(x)\,dx
}
\le\frac{M}{2n}.
$$
:::

::: {.hint}
On the interval $[j/n,(j+1)/n]$, compare $f(x)$ with $f(j/n)$
using the mean value theorem. Integrate the bound
$M(x-j/n)$ over that interval.
:::

::: {.solution}
Fix a positive integer $n$, and put $x_j\coloneqq j/n$ for
$0\leq j\leq n$. The function $f$ is continuous on $[0,1]$,
so all integrals of $f$ over closed subintervals exist.

::: pf

::: {.pf-step #s1}

For $0\leq j<n$ and $x\in[x_j,x_{j+1}]$,
$$
\abs{f(x)-f(x_j)}\leq M(x-x_j).
$$

::: pf-proof

For $x=x_j$, both sides are zero. For $x>x_j$, apply the
[[T-RA-WORKSHOP-D5-4-2|mean value theorem]] to $f$ on
$[x_j,x]$. There is $\xi\in(x_j,x)\subset(0,1)$ such that
$$
f(x)-f(x_j)=f'(\xi)(x-x_j).
$$
The definition of $M$ gives $\abs{f'(\xi)}\leq M$, which
proves the estimate.

:::

:::

::: {.pf-step #s2}

For $0\leq j<n$,
$$
\abs{\frac{f(x_j)}n-\int_{x_j}^{x_{j+1}}f(x)\,dx}
\leq\frac{M}{2n^2}.
$$

::: pf-proof

Since $x_{j+1}-x_j=1/n$, the difference inside the absolute
value is the integral of $f(x_j)-f(x)$ over $[x_j,x_{j+1}]$.
The integral triangle inequality and step [](#s1){.pf-ref} give
$$
\begin{aligned}
\abs{\frac{f(x_j)}n-\int_{x_j}^{x_{j+1}}f(x)\,dx}
&\leq\int_{x_j}^{x_{j+1}}\abs{f(x_j)-f(x)}\,dx\\
&\leq M\int_{x_j}^{x_{j+1}}(x-x_j)\,dx\\
&=\frac M2(x_{j+1}-x_j)^2
=\frac{M}{2n^2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

The error of the left Riemann sum is at most $M/(2n)$.

::: pf-proof

Additivity of the integral over the subdivision gives
$$
\frac1n\sum_{j=0}^{n-1}f(x_j)-\int_0^1f(x)\,dx
=\sum_{j=0}^{n-1}
\left(\frac{f(x_j)}n-\int_{x_j}^{x_{j+1}}f(x)\,dx\right).
$$
By the triangle inequality and step [](#s2){.pf-ref}, the absolute value
of this sum is at most
$$
\sum_{j=0}^{n-1}\frac{M}{2n^2}=\frac{M}{2n}.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the asserted estimate, and $n$ was arbitrary.

:::

:::

:::
