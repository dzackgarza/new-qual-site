---
schema: qual/card@1
id: E-Y22HZ
kind: problem
title: Locally uniform limits of holomorphic functions converge with all derivatives
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Cauchy Estimates
  - Sequences of Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source printed "if f_k -> f uniformly with f holomorphic then every nth derivative satisfies f_k^(n) -> f^(n) uniformly", which is false on the whole domain (z^k/k -> 0 uniformly on the unit disc while its derivatives z^(k-1) do not) and does not assume the f_k holomorphic; the statement now takes f_k holomorphic on an open set and concludes uniform convergence on compact subsets.'
---

::: {.exercise}
Let $f_k$ be holomorphic on an open set $\Omega$.
Show that if $f_k \to f$ uniformly on compact subsets of $\Omega$, then $f$ is holomorphic and every $n$th derivative satisfies $f_k^{(n)}\to f^{(n)}$ uniformly on compact subsets of $\Omega$.
:::

::: {.solution}
Fix $n\ge0$ and a compact set $K\subset\Omega$.

::: pf

::: {.pf-step #holo}
$f$ is holomorphic on $\Omega$.

::: pf-proof
This is the uniform limit theorem for holomorphic functions, proved by Goursat's and Morera's theorems on discs.
:::

:::

::: {.pf-step #thicken}
There is $r>0$ such that $K_r\coloneqq\{z : \operatorname{dist}(z,K)\le r\}$ is a compact subset of $\Omega$.

::: pf-proof
If $\Omega=\CC$ take $r=1$; otherwise $\operatorname{dist}(K,\CC\setminus\Omega)>0$ because $K$ is compact and $\CC\setminus\Omega$ is closed, and take $r$ less than half of it.
$K_r$ is closed and bounded.
:::

:::

::: pf-step
$\sup_K\abs{f_k^{(n)} - f^{(n)}}\to0$.

::: pf-proof
By step [](#holo){.pf-ref}, $g_k\coloneqq f_k - f$ is holomorphic on $\Omega$.
For $z\in K$, the closed disc of radius $r$ about $z$ lies in $K_r$ by step [](#thicken){.pf-ref}, so the Cauchy estimates give
$$
\abs{g_k^{(n)}(z)} \le \frac{n!}{r^n}\sup_{K_r}\abs{g_k}.
$$
The right-hand side is independent of $z\in K$ and tends to $0$ because $K_r$ is compact.
:::

:::

:::

:::
