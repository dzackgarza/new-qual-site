---
schema: qual/card@1
id: E-WTCTP
kind: problem
title: "A zero of $f'$ of order $n-1$ makes $f$ locally $n$-to-one"
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Rouché
  - Argument Principle
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source omits that f is holomorphic and that n >= 1; the statement adds both.
---

::: {.exercise}
Let $f$ be holomorphic near $z_0$ and $n\ge1$.
Show that if $z_0$ is a zero of $f'$ of order $n-1$, then $f$ is $n$-to-one in a neighborhood of $z_0$.

:::

::: {.solution}
"$n$-to-one" means: there are neighborhoods $U$ of $z_0$ and $W$ of $f(z_0)$ such that every $w\in W\setminus\theset{f(z_0)}$ has exactly $n$ preimages in $U$.
Let $w_0 = f(z_0)$.

::: pf

::: {.pf-step #order}
$f - w_0$ has a zero of order exactly $n$ at $z_0$.

::: pf-proof
$(f-w_0)(z_0) = 0$ and $(f-w_0)' = f'$ has a zero of order $n-1$ at $z_0$.
:::

:::

::: {.pf-step #disk}
There is $\rho>0$ such that on $0<\abs{z-z_0}\le\rho$ both $f(z)\neq w_0$ and $f'(z)\neq0$.

::: pf-proof
Zeros of the nonzero holomorphic functions $f-w_0$ and $f'$ are isolated.
:::

:::

::: {.pf-step #count}
Let $\delta = \min_{\abs{z-z_0}=\rho}\abs{f(z)-w_0} > 0$. For every $w$ with $\abs{w-w_0}<\delta$, $f-w$ has exactly $n$ zeros, counted with multiplicity, in $\abs{z-z_0}<\rho$.

::: pf-proof
On $\abs{z-z_0}=\rho$, $\abs{(f(z)-w)-(f(z)-w_0)} = \abs{w-w_0} < \delta \le \abs{f(z)-w_0}$.
By Rouché's theorem, $f-w$ and $f-w_0$ have the same number of zeros in the disk, which is $n$ by steps [](#order){.pf-ref} and [](#disk){.pf-ref}.
:::

:::

::: pf-step
For $0<\abs{w-w_0}<\delta$, the equation $f(z) = w$ has exactly $n$ distinct solutions in $\abs{z-z_0}<\rho$.

::: pf-proof
A solution $z$ is not $z_0$, since $w\neq w_0$, so $f'(z)\neq0$ by step [](#disk){.pf-ref} and $z$ is a simple zero of $f-w$.
Step [](#count){.pf-ref} then counts $n$ distinct solutions.
:::

:::

:::

:::
