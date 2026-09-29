---
schema: qual/card@1
id: P-BERK79S-07
kind: problem
title: An exponential integral of a continuous function is entire
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Expanded e^{tz} into its power series and used boundedness of f on
    [0,1] to dominate uniformly on every disk |z|<=R by
    M sum R^n/n!. Interchanging sum and integral gives a power series for g
    with infinite radius of convergence, hence g is entire.
---

::: {.problem}
Let $f:[0,1]\to\mathbb C$ be continuous and define
\[
g(z)=\int_0^1 f(t)e^{tz}\,dt,
\qquad z\in\mathbb C.
\]
Prove that $g$ is entire.
:::

::: {.solution}
Since $f$ is continuous on the compact interval $[0,1]$, choose
$$
M\geq0
$$
such that
$$
\abs{f(t)}\leq M
$$
for every $t\in[0,1]$.

::: pf

::: {.pf-step #s1}

For every $R>0$, the series
$$
\sum_{n=0}^{\infty}
\frac{f(t)t^nz^n}{n!}
$$
converges uniformly on
$$
[0,1]\times\{z\in\CC:\abs{z}\leq R\}.
$$

::: pf-proof

If
$$
0\leq t\leq1
\qquad\text{and}\qquad
\abs{z}\leq R,
$$
then
$$
\abs{
\frac{f(t)t^nz^n}{n!}
}
\leq
\frac{MR^n}{n!}.
$$
The numerical series
$$
\sum_{n=0}^{\infty}\frac{MR^n}{n!}
=
Me^R
$$
converges. The Weierstrass M-test gives the required uniform convergence.

:::

:::

::: {.pf-step #s2}

For every $z\in\CC$,
$$
g(z)
=
\sum_{n=0}^{\infty}
\left(
\frac1{n!}
\int_0^1 f(t)t^n\,dt
\right)z^n.
$$

::: pf-proof

Fix $z\in\CC$ and choose $R>\abs{z}$. The exponential series gives
$$
e^{tz}
=
\sum_{n=0}^{\infty}\frac{t^nz^n}{n!}.
$$
By step [](#s1){.pf-ref}, after multiplication by $f(t)$ this series converges
uniformly in $t\in[0,1]$. Therefore it may be integrated term by term:
$$
\begin{aligned}
g(z)
&=
\int_0^1
f(t)
\sum_{n=0}^{\infty}
\frac{t^nz^n}{n!}
\,dt\\
&=
\sum_{n=0}^{\infty}
\frac{z^n}{n!}
\int_0^1f(t)t^n\,dt.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

The power series in step [](#s2){.pf-ref} has infinite radius of convergence.

::: pf-proof

Set
$$
c_n
=
\frac1{n!}
\int_0^1f(t)t^n\,dt.
$$
Then
$$
\begin{aligned}
\abs{c_n}
&\leq
\frac1{n!}
\int_0^1
\abs{f(t)}t^n\,dt\\
&\leq
\frac{M}{n!}
\int_0^1t^n\,dt\\
&=
\frac{M}{(n+1)n!}
\leq
\frac{M}{n!}.
\end{aligned}
$$
Hence for every $z\in\CC$,
$$
\sum_{n=0}^{\infty}\abs{c_nz^n}
\leq
M
\sum_{n=0}^{\infty}\frac{\abs{z}^n}{n!}
=
Me^{\abs{z}}
<
\infty.
$$
Thus the radius of convergence is infinite.

:::

:::

::: {.pf-step #s4}

The function $g$ is entire.

::: pf-proof

By step [](#s2){.pf-ref}, $g$ is represented on all of $\CC$ by the power series whose
radius of convergence is infinite by step [](#s3){.pf-ref}. A power series is analytic
throughout its disk of convergence, so
$$
\boxed{
g\text{ is entire}.
}
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
