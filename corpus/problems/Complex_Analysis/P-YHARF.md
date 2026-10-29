---
schema: qual/card@1
id: P-YHARF
kind: problem
title: Taylor coefficients of a function with a pole on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
  - Convergence Tests
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source printed the series as starting at n = 1, which would force f(0) = 0, a hypothesis it does not state; the series now starts at n = 0. Also removed a commented-out duplicate formula and the doubled word "the the".'
---

::: {.problem}
Suppose that $f$ is holomorphic in an open set containing the closed
unit disc, except for a pole at $z_0$ on the unit circle. Let
$f(z) = \sum_{n = 0}^\infty c_n z^n$ denote the power series in
the open disc. Show that (1) $c_n \neq 0$ for all large enough
$n$'s, and (2)
$\displaystyle \lim_{n \rightarrow \infty} \frac{c_n}{c_{n+1}}= z_0$.
:::

::: {.solution}
Let the pole of $f$ at $z_0$ have order $m$, with principal part $\sum_{j=1}^m A_j(z-z_0)^{-j}$, $A_m\ne0$.
The remainder $h(z)=f(z)-\sum_{j=1}^m A_j(z-z_0)^{-j}$ is holomorphic on $\abs{z}<R$ for some $R>1$; write $h(z)=\sum d_nz^n$.

::: pf

::: {.pf-step #coeff}
$c_n=z_0^{-n}\sum_{j=1}^m(-1)^jA_jz_0^{-j}\binom{n+j-1}{j-1}+d_n$, with $d_n=O(r^{-n})$ for some $r>1$.

::: pf-proof
For $\abs{z}<1=\abs{z_0}$,
$$
\frac1{(z-z_0)^j}
=(-1)^j z_0^{-j}
\sum_{n=0}^\infty
\binom{n+j-1}{j-1}\frac{z^n}{z_0^n}.
$$
Cauchy's estimates for $h$ on a circle of radius $r$ with $1<r<R$ bound $d_n$.
:::

:::

::: {.pf-step #asym}
$c_n=Cz_0^{-n}n^{m-1}\qty(1+O(1/n))$ for a constant $C\ne0$.

::: pf-proof
In step [](#coeff){.pf-ref}, the $j=m$ term is a polynomial in $n$ of degree $m-1$ with leading coefficient $(-1)^mA_mz_0^{-m}/(m-1)!\ne0$, the terms with $j<m$ have smaller degree, and $\abs{z_0^{-n}}=1$ while $d_n$ decays exponentially.
:::

:::

::: pf-step
(1) $c_n\ne0$ for all large $n$, and (2) $c_n/c_{n+1}\to z_0$.

::: pf-proof
Part (1) follows from step [](#asym){.pf-ref}, and
$$
\frac{c_n}{c_{n+1}}
=z_0\qty(\frac{n}{n+1})^{m-1}
\frac{1+O(1/n)}{1+O(1/n)}
\longrightarrow z_0.
$$
:::

:::

:::

:::
