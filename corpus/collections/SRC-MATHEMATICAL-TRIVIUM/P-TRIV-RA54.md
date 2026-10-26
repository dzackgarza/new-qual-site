---
schema: qual/card@1
id: P-TRIV-RA54
kind: problem
title: $\sum_{n\ge1}\frac{x^{n-1}}{n(n+1)}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 54, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the sum $\sum _ { n = 1 } ^ { \infty } { \frac { x ^ { n - 1 } } { n ( n + 1 ) } }$ for all possible values of x.
:::

Define
$$
S(x)
=
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n(n+1)}.
$$

::: pf

::: pf-step

The series converges absolutely for
$$
|x|\leq1.
$$


::: pf-proof

If $|x|\leq1$, then
$$
\left|
\frac{x^{n-1}}{n(n+1)}
\right|
\leq
\frac1{n(n+1)}.
$$
The comparison series converges, since
$$
\frac1{n(n+1)}
=
\frac1n-\frac1{n+1}
$$
telescopes.

:::

:::

::: pf-step

If
$$
|x|>1,
$$
the series diverges.


::: pf-proof

The term magnitudes are
$$
\frac{|x|^{n-1}}{n(n+1)}.
$$
Exponential growth dominates the quadratic denominator, so these terms do not tend to $0$.

:::

:::

::: pf-step

Therefore the complete convergence set is
$$
\boxed{|x|\leq1}.
$$


::: pf-proof

Combine steps <1>1--<1>2.

:::

:::

::: pf-step

For every $n\geq1$,
$$
\frac1{n(n+1)}
=
\frac1n-\frac1{n+1}.
$$


::: pf-proof

Combine the two fractions on the right over the common denominator $n(n+1)$.

:::

:::

::: pf-step

For $|x|<1$ and $x\neq0$,
$$
S(x)
=
\sum_{n=1}^{\infty}
\frac{x^{n-1}}n
-
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n+1}.
$$


::: pf-proof

Use step <1>4 term by term.
Absolute convergence permits splitting the series.

:::

:::

::: pf-step

The first sum in step <1>5 is
$$
\sum_{n=1}^{\infty}
\frac{x^{n-1}}n
=
-\frac{\log(1-x)}x.
$$


::: pf-proof

For $|x|<1$,
$$
-\log(1-x)
=
\sum_{n=1}^{\infty}\frac{x^n}{n}.
$$
Divide by $x$.

:::

:::

::: pf-step

The second sum in step <1>5 is
$$
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n+1}
=
\frac{-\log(1-x)-x}{x^2}.
$$


::: pf-proof

Set $m=n+1$:
$$
\sum_{n=1}^{\infty}
\frac{x^{n-1}}{n+1}
=
\frac1{x^2}
\sum_{m=2}^{\infty}
\frac{x^m}{m}.
$$
Now
$$
\sum_{m=2}^{\infty}\frac{x^m}{m}
=
-\log(1-x)-x.
$$

:::

:::

::: pf-step

Therefore, for $|x|<1$ and $x\neq0$,
$$
\boxed{
S(x)
=
\frac{x+(1-x)\log(1-x)}{x^2}.
}
$$


::: pf-proof

Substitute steps <1>6--<1>7 into step <1>5 and combine over the denominator $x^2$.

:::

:::

::: pf-step

At $x=0$,
$$
\boxed{S(0)=\frac12}.
$$


::: pf-proof

In the original series, every term with $n\geq2$ contains a positive power of $x$ and vanishes at $x=0$.
The $n=1$ term is
$$
\frac1{1\cdot2}.
$$
The formula in step <1>8 has the same removable limit.

:::

:::

::: pf-step

At $x=1$,
$$
\boxed{S(1)=1}.
$$


::: pf-proof

The series becomes
$$
\sum_{n=1}^{\infty}
\frac1{n(n+1)}
=
\sum_{n=1}^{\infty}
\left(
\frac1n-\frac1{n+1}
\right),
$$
which telescopes to $1$.

:::

:::

::: pf-step

At $x=-1$,
$$
\boxed{S(-1)=2\log2-1}.
$$


::: pf-proof

Because the series converges absolutely at $x=-1$, its value equals the continuous boundary limit of the power-series expression in step <1>8. Thus
$$
S(-1)
=
-1+2\log2.
$$

:::

:::

::: pf-qed

Step <1>3 gives the full convergence set, and steps <1>8--<1>11 give the sum at every point of that set.

:::

:::
