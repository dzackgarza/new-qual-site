---
schema: qual/card@1
id: E-SS1.EX-18
kind: problem
title: A power series re-expands around every point of its disc of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Let $f$ be a power series centered at the origin. Prove that $f$ has a power-series expansion around every point in its disc of convergence.
:::

::: {.solution}
<1>1. Write
\[
f(z)=\sum_{n=0}^{\infty}a_nz^n
\]
with radius of convergence $R$, and fix $z_0$ with $|z_0|<R$.
::: {.proof}
This is the hypothesis, with an arbitrary point chosen in the open disc of convergence.
:::

<1>2. If $w$ satisfies $|w|<R-|z_0|$, then
\[
\sum_{n=0}^{\infty}|a_n|(|z_0|+|w|)^n<\infty.
\]
::: {.proof}
The inequality $|z_0|+|w|<R$ places the positive real number $|z_0|+|w|$ strictly inside the radius of convergence. A power series converges absolutely at every point strictly inside its radius.
:::

<1>3. For such $w$, the double series
\[
\sum_{n=0}^{\infty}\sum_{k=0}^n
|a_n|\binom nk|z_0|^{n-k}|w|^k
\]
converges.
::: {.proof}
By the binomial theorem, the inner sum equals
\[
|a_n|(|z_0|+|w|)^n.
\]
Hence the double series is exactly the convergent series in <1>2.
:::

<1>4. Define, for $k\ge0$,
\[
c_k=\sum_{n=k}^{\infty}a_n\binom nk z_0^{\,n-k}.
\]
Then this series converges absolutely for every $k$.
::: {.proof}
Choose any real $\rho$ with $|z_0|<\rho<R$. Since $\sum |a_n|\rho^n<\infty$ and
\[
\binom nk |z_0|^{n-k}
=\rho^{-k}\binom nk\left(\frac{|z_0|}{\rho}\right)^{n-k}\rho^n,
\]
the factor $\binom nk(|z_0|/\rho)^{n-k}$ is bounded in $n$ for fixed $k$: polynomial growth in $n$ is dominated by the geometric factor $(|z_0|/\rho)^{n-k}$. Thus the defining series for $c_k$ is dominated by a constant multiple of $\sum |a_n|\rho^n$.
:::

<1>5. For every $|w|<R-|z_0|$,
\[
f(z_0+w)=\sum_{k=0}^{\infty}c_kw^k.
\]
::: {.proof}
Using the binomial theorem,
\[
\begin{aligned}
f(z_0+w)
&=\sum_{n=0}^{\infty}a_n(z_0+w)^n\\
&=\sum_{n=0}^{\infty}\sum_{k=0}^n
 a_n\binom nk z_0^{\,n-k}w^k.
\end{aligned}
\]
By <1>3 this double series is absolutely convergent, so its terms may be rearranged. Summing first over $n\ge k$ gives
\[
f(z_0+w)
=\sum_{k=0}^{\infty}\left(\sum_{n=k}^{\infty}a_n\binom nkz_0^{\,n-k}\right)w^k
=\sum_{k=0}^{\infty}c_kw^k.
\]
:::

<1>6. Therefore $f$ has a power-series expansion centered at $z_0$, valid at least on the disc $|z-z_0|<R-|z_0|$.
::: {.proof}
Set $w=z-z_0$ in <1>5. Since $z_0$ was arbitrary with $|z_0|<R$, the conclusion holds around every point of the original disc of convergence.
:::
:::
