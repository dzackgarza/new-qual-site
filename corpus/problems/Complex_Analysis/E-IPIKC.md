---
schema: qual/card@1
id: E-IPIKC
kind: problem
title: Entire functions with $\abs{f(z)/z^{n}}$ bounded at infinity are polynomials of degree at most $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source does not say that f is entire and asks what happens if the bound holds "on all of C", where z^n vanishes at 0; the statement adds that f is entire and asks about the bound on C minus 0.
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Merged E-DDKSS (CARD-04), which states that n is a nonnegative integer; the statement now says so.
---

::: {.exercise}
Let $f$ be entire and let $n\geq 0$ be an integer.
Show that if $\abs{f(z)/z^n}$ is bounded for $\abs{z}\geq R$, then $f$ is a polynomial of degree at most $n$.
What happens if this bound holds on all of $\CC\setminus\theset{0}$?
:::

::: {.solution}
Suppose $\abs{f(z)}\le M\abs z^n$ for $\abs z\ge R$, and write $f(z) = \sum_{j\geq 0}c_j z^j$ on $\CC$.

::: pf

::: pf-step
$f$ is a polynomial of degree at most $n$.

::: pf-proof
For $k\ge1$ and $\rho\ge R$, the Cauchy estimate on the circle $\abs\xi=\rho$ gives
$$
\abs{c_{n+k}}={\abs{f^{(n+k)}(0)}\over(n+k)!} \le {1\over 2\pi} \int_{\abs{\xi} = \rho} {M\abs{\xi}^n \over \abs{\xi}^{n+k+1}}\abs{\dxi} = M\rho^{-k}
,$$
which tends to $0$ as $\rho\to\infty$. So $c_j=0$ for $j>n$.
:::

:::

::: pf-step
If the bound holds on $\CC\setminus\theset0$, then $\boxed{f(z)=cz^n}$ for a constant $c$.

::: pf-proof
The function $h(z) \coloneqq f(z)/z^n$ is holomorphic and bounded on $\CC\setminus\theset0$, so its singularity at $0$ is removable and $h$ extends to a bounded entire function.
By Liouville's theorem $h$ is a constant $c$, so $f(z)=cz^n$.
:::

:::

:::

:::
