---
schema: qual/card@1
id: E-SKD7P
kind: problem
title: Power series converge uniformly on compact subdiscs of the disc of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Uniform Convergence
  - Convergence Tests
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Show that any power series converges uniformly within its radius of convergence." This is false on the open disc of convergence: $\sum_k z^k$ does not converge uniformly on $\abs{z}<1$. The statement now asks for uniform convergence on every closed disc of radius $r$ strictly less than the radius of convergence.'
---

::: {.exercise}
Show that a power series $\sum_{k\geq 0} c_k(z-z_0)^k$ with radius of convergence $R>0$ converges uniformly on every closed disc $\abs{z-z_0}\leq r$ with $0<r<R$.
:::

::: {.solution}
By the Cauchy--Hadamard formula, $R = 1/L$ where $L \coloneqq \limsup_k \abs{c_k}^{1/k}$, with $R=\infty$ when $L=0$. Fix $0<r<R$ and put $f_k(z) \coloneqq c_k(z-z_0)^k$.

::: pf

::: {.pf-step #bound}
$\sup_{\abs{z-z_0}\leq r}\abs{f_k(z)} \leq M_k \coloneqq \abs{c_k}r^k$.

::: pf-proof
On the closed disc, $\abs{z-z_0}^k\leq r^k$.
:::

:::

::: {.pf-step #summable}
$\sum_{k\geq 0} M_k < \infty$.

::: pf-proof
$\limsup_k M_k^{1/k} = rL < 1$, because $r<R=1/L$ (and $rL=0$ when $L=0$). The root test gives convergence.
:::

:::

::: pf-step
$\sum_k f_k$ converges uniformly on $\abs{z-z_0}\leq r$.

::: pf-proof
This is the Weierstrass $M$-test, with steps [](#bound){.pf-ref} and [](#summable){.pf-ref}.
:::

:::

:::

:::
