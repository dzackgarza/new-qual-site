---
schema: qual/card@1
id: P-TRIV-RA53
kind: problem
title: Sum of the alternating harmonic series
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 53, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the series $\sum _ { n = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { n } } { n } }$
:::

::: pf

::: pf-step

For $|x|<1$,
$$
\frac1{1+x}
=
\sum_{m=0}^{\infty}(-1)^m x^m.
$$


::: pf-proof

This is the geometric-series identity with ratio $-x$.

:::

:::

::: pf-step

Integrating term by term from $0$ to $x$, for $0\leq x<1$,
$$
\log(1+x)
=
\sum_{n=1}^{\infty}
\frac{(-1)^{n-1}}n x^n.
$$


::: pf-proof

On every interval $[0,r]$ with $r<1$, the geometric series in step <1>1
converges uniformly, so termwise integration is valid:
$$
\int_0^x\frac{dt}{1+t}
=
\sum_{m=0}^{\infty}
(-1)^m
\int_0^x t^m\,dt.
$$
The left side is $\log(1+x)$, and relabeling $n=m+1$ gives the series.

:::

:::

::: pf-step

The series
$$
\sum_{n=1}^{\infty}
\frac{(-1)^{n-1}}n
$$
converges.


::: pf-proof

The terms $1/n$ decrease monotonically to $0$, so the alternating-series test
applies.

:::

:::

::: pf-step

Letting $x\to1^-$ in step <1>2 gives
$$
\sum_{n=1}^{\infty}
\frac{(-1)^{n-1}}n
=
\log2.
$$


::: pf-proof

By Abel's theorem, if a power series converges at the boundary point $x=1$,
then its values for $0\leq x<1$ tend to that boundary sum as $x\to1^-$. Step
<1>3 supplies the boundary convergence. The left side of step <1>2 tends to
$\log2$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
\sum_{n=1}^{\infty}
\frac{(-1)^n}{n}
=
-\log2.
}
$$


::: pf-proof

Multiply the identity in step <1>4 by $-1$.

:::

:::

::: pf-qed

Step <1>5 is the required sum.

:::

:::
