---
schema: qual/card@1
id: P-AZOFF-E01
kind: problem
title: Boundary behavior of power series with radius of convergence $1$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For (a), used coefficients 1/(n+1)^2, whose series has radius one and
    converges absolutely on the unit circle. For (b), used 1/(1+z), whose
    geometric Taylor series has radius one but diverges at z=1. For (c),
    compactness of the closed unit disk turns analyticity at every boundary
    point into analyticity on a strictly larger centered disk, contradicting
    the stated radius of convergence.
---

::: {.problem}
Suppose $f$ is analytic on a region $\Omega$ in $\CC$ containing the open unit disk $\DD$ and we have $f(z) = \sum a_n z^n$ with this power series having radius of convergence $1$.

a) Give an example of such an $f$ so that the series converges at every point on the unit circle $\mathbb{T}$.

b) Give an example of such an $f$ which is analytic at $1$, but $\sum a_n$ diverges.

c) Prove that $f$ cannot be analytic at each point of $\mathbb{T}$.
:::

::: {.solution}
<1>1. For part (a), one example is
$$
\boxed{
f_a(z)=\sum_{n=0}^{\infty}\frac{z^n}{(n+1)^2}.
}
$$

::: {.proof}
If $\abs{z}<1$, the series converges absolutely by comparison with the
geometric series $\sum \abs{z}^n$. If $\abs{z}>1$, then
$$
\frac{\abs{z}^{n+1}/(n+2)^2}
{\abs{z}^n/(n+1)^2}
=
\abs{z}\left(\frac{n+1}{n+2}\right)^2
\longrightarrow
\abs{z}>1,
$$
so the terms $\abs{z}^n/(n+1)^2$ do not tend to zero.
Thus its radius of convergence is exactly $1$, and the sum defines an
analytic function on the open unit disk.

If $\abs{z}=1$, then
$$
\sum_{n=0}^{\infty}
\abs{\frac{z^n}{(n+1)^2}}
=
\sum_{n=0}^{\infty}\frac1{(n+1)^2}
<\infty.
$$
Hence the power series converges at every point of the unit circle.
:::

<1>2. For part (b), one example is
$$
\boxed{
f_b(z)=\frac1{1+z}.
}
$$

::: {.proof}
The function $f_b$ is analytic on
$$
\CC\sm\{-1\},
$$
a region containing the open unit disk, and in particular it is analytic at
$z=1$. At the origin,
$$
f_b(z)
=
\sum_{n=0}^{\infty}(-1)^n z^n
$$
for $\abs{z}<1$. The nearest singularity to the origin is $-1$, so this
Taylor series has radius of convergence $1$. Its coefficient sum is
$$
\sum_{n=0}^{\infty}a_n
=
\sum_{n=0}^{\infty}(-1)^n,
$$
whose partial sums alternate between $1$ and $0$. Thus the coefficient sum
diverges even though $f_b$ is analytic at $1$.
:::

<1>3. For part (c), $f$ cannot be analytic at every point of the unit circle.

::: {.proof}
Suppose instead that $f$ were analytic at every point of the unit circle.
Together with the given analyticity on a region containing the open unit
disk, this gives an open set $U$ on which $f$ is analytic and which contains
the closed unit disk
$$
K=\{z\in\CC:\abs{z}\leq1\}.
$$
Since $K$ is compact and $U$ is open, there is an $\varepsilon>0$ such that
every point at distance less than $\varepsilon$ from $K$ lies in $U$.
Consequently,
$$
\{z\in\CC:\abs{z}<1+\varepsilon\}
\subseteq U.
$$

The Taylor series of a function analytic on the disk
$\abs{z}<1+\varepsilon$ converges there to the function. Hence the Taylor
series of $f$ at the origin has radius of convergence at least
$1+\varepsilon$, contradicting the hypothesis that its radius is exactly
$1$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the requested examples, and step <1>3 proves the
impossibility in part (c).
:::
:::
