---
schema: qual/card@1
id: E-5QAVX
kind: problem
title: $\abs{f''(0)}\le2$ for a self-map of $\DD$ with $f(0)=f'(0)=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Cauchy Estimates
  - Zeros
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Let f:D -> D with f(0) = f'(0) = 0" and does not say that f is holomorphic; the statement adds that hypothesis, without which the bound fails.
---

::: {.exercise}
Let $f:\DD\to \DD$ be holomorphic with $f(0) = f'(0) = 0$.
Show that $\abs{f''(0)} \leq 2$ and describe all $f$ for which this is an equality.
:::

::: {.solution}
Write $f(z) = \sum_{k\ge0} c_kz^k$ on $\DD$, so $c_2=f''(0)/2$.

::: pf

::: {.pf-step #g}
The function $g(z)\coloneqq f(z)/z^2$, extended by $g(0)=c_2$, is holomorphic on $\DD$ with $\abs{g}\le1$.

::: pf-proof
Since $c_0=f(0)=0$ and $c_1=f'(0)=0$, $f(z)=z^2\sum_{k\ge2}c_kz^{k-2}$, so $g$ is holomorphic.
For $0<r<1$ and $\abs z\le r$, the maximum modulus principle gives $\abs{g(z)}\le\max_{\abs w=r}\abs{f(w)}/r^2<1/r^2$.
Letting $r\to1$ gives $\abs{g(z)}\le1$.
:::

:::

::: {.pf-step #bound}
$\abs{f''(0)}\le2$.

::: pf-proof
By step [](#g){.pf-ref}, $\abs{f''(0)}=2\abs{c_2}=2\abs{g(0)}\le2$.
:::

:::

::: pf-step
Equality holds exactly for $\boxed{f(z)=\lambda z^2}$ with $\abs\lambda=1$.

::: pf-proof
If $\abs{f''(0)}=2$, then $\abs{g(0)}=1$, so the function $g$ of step [](#g){.pf-ref} attains its maximum modulus at the interior point $0$ and is a constant $\lambda$ with $\abs\lambda=1$.
Hence $f(z)=\lambda z^2$.
Conversely, $f(z)=\lambda z^2$ with $\abs\lambda=1$ maps $\DD$ into $\DD$, satisfies $f(0)=f'(0)=0$, and has $\abs{f''(0)}=2$.
:::

:::

:::

:::
