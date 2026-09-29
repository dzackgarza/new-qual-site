---
schema: qual/card@1
id: P-BERK85SU-17
kind: problem
title: Nonnegative coefficients force a singularity at the positive boundary point
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Assuming continuation near 1, choose t<1 whose Taylor disk in the glued
    analytic domain reaches a positive real point t+h>1. The Taylor
    coefficients at t are nonnegative sums of the original nonnegative
    coefficients. Rearranging the nonnegative double series at h gives
    sum_n a_n(t+h)^n<infinity, contradicting radius 1.
---

::: {.problem}
Let
\[
f(z)=\sum_{n=0}^\infty a_nz^n,
\]
where every $a_n$ is a nonnegative real number and the series has radius of convergence $1$.
Prove that $f$ cannot be analytically continued to a function analytic in a neighborhood of $z=1$.
:::

::: {.solution}
Suppose, for contradiction, that $f$ admits an analytic continuation
to a neighborhood of $1$.
Write
$$
D(c,r)=\{z\in\CC:\abs{z-c}<r\}.
$$

::: pf

::: pf-step

There is a number $\rho>0$ and a function $F$ analytic on
$$
D(0,1)\cup D(1,\rho)
$$
such that $F=f$ on $D(0,1)$.

::: pf-proof

By assumption, there is a function analytic on some disk
$D(1,\rho)$ that agrees with $f$ on the nonempty overlap with the
unit disk. The two analytic functions therefore glue to an analytic
function $F$ on the displayed union.

:::

:::

::: {.pf-step #s2}

Choose
$$
0<\delta<\min\left\{\frac12,\frac\rho4\right\},
\qquad
t=1-\delta.
$$
Then
$$
D(t,2\delta)
\subset
D(0,1)\cup D(1,\rho).
$$

::: pf-proof

Let $z\in D(t,2\delta)$. If $\abs{z}<1$, then
$z\in D(0,1)$. If $\abs{z}\ge1$, then
$$
\abs{z-1}
\le
\abs{z-t}+\abs{t-1}
<
2\delta+\delta
<
\rho.
$$
Thus $z\in D(1,\rho)$. This proves the inclusion.

:::

:::

::: {.pf-step #s3}

For every integer $k\ge0$,
$$
\frac{F^{(k)}(t)}{k!}
=
\sum_{n=k}^\infty
a_n\binom{n}{k}t^{n-k},
$$
and this number is nonnegative.

::: pf-proof

Since $0<t<1$, the original power series converges in a neighborhood
of $t$ and may be differentiated term by term. Hence
$$
F^{(k)}(t)
=
\sum_{n=k}^\infty
a_n\frac{n!}{(n-k)!}t^{n-k}.
$$
Dividing by $k!$ gives the displayed formula. Every term is
nonnegative because $a_n\ge0$ and $t>0$.

:::

:::

::: {.pf-step #s4}

Set
$$
h=\frac{3\delta}{2}.
$$
Then
$$
t+h=1+\frac\delta2>1,
$$
and the Taylor series of $F$ about $t$ converges at $t+h$.

::: pf-proof

By step [](#s2){.pf-ref}, $F$ is analytic on the disk $D(t,2\delta)$, so its
Taylor series about $t$ converges for $\abs{z-t}<2\delta$. Since
$h=3\delta/2<2\delta$, it converges at $z=t+h$.

:::

:::

::: {.pf-step #s5}

One has
$$
\sum_{n=0}^\infty a_n(t+h)^n<\infty.
$$

::: pf-proof

By step [](#s4){.pf-ref},
$$
F(t+h)
=
\sum_{k=0}^\infty
\frac{F^{(k)}(t)}{k!}h^k.
$$
Substituting step [](#s3){.pf-ref} gives
$$
F(t+h)
=
\sum_{k=0}^\infty
\sum_{n=k}^\infty
a_n\binom{n}{k}t^{n-k}h^k.
$$
Every term in this double series is nonnegative. Hence its order of
summation may be interchanged, giving
$$
\begin{aligned}
F(t+h)
&=
\sum_{n=0}^\infty
a_n
\sum_{k=0}^n
\binom{n}{k}t^{n-k}h^k\\
&=
\sum_{n=0}^\infty
a_n(t+h)^n.
\end{aligned}
$$
The left-hand side is finite, so the displayed series converges.

:::

:::

::: {.pf-step #s6}

The convergence in step [](#s5){.pf-ref} contradicts the assumption that
the radius of convergence of
$$
\sum_{n=0}^\infty a_nz^n
$$
is $1$.

::: pf-proof

Step [](#s4){.pf-ref} gives $t+h>1$. A power series that converges at the point
$z=t+h$ has radius of convergence at least $t+h>1$, contradicting
the stated radius $1$.

:::

:::

::: {.pf-step #s7}

Therefore $f$ cannot be analytically continued to a function
analytic in a neighborhood of $1$.

::: pf-proof

The assumption of such a continuation led to the contradiction in
step [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::
