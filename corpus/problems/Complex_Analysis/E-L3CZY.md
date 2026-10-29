---
schema: qual/card@1
id: E-L3CZY
kind: problem
title: Compactly convergent series of holomorphic functions are holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if each $f_n$ is holomorphic on an open set $\Omega \subseteq \CC$ and $F \coloneqq \sum_{n=1}^\infty f_n$ converges uniformly on every compact subset of $\Omega$, then $F$ is holomorphic on $\Omega$.
:::

::: {.solution}
Write $S_N\coloneqq\sum_{n=1}^Nf_n$; each $S_N$ is holomorphic on $\Omega$.

::: pf

::: {.pf-step #continuous}
$F$ is continuous on $\Omega$.

::: pf-proof
For $z_0\in\Omega$ choose $r>0$ with $\overline{D_r(z_0)}\subset\Omega$. On this compact disk $S_N\to F$ uniformly, so $F$ is a uniform limit of continuous functions there.
:::

:::

::: {.pf-step #triangles}
$\int_{\partial T}F(z)\,dz=0$ for every closed triangle $T\subset\Omega$.

::: pf-proof
By Cauchy's theorem for triangles, $\int_{\partial T}S_N(z)\,dz=0$. Since $\partial T$ is compact, $S_N\to F$ uniformly on it, so $\int_{\partial T}F(z)\,dz=\lim_{N\to\infty}\int_{\partial T}S_N(z)\,dz=0$.
:::

:::

::: pf-step
$F$ is holomorphic on $\Omega$.

::: pf-proof
Apply Morera's theorem on each disk in $\Omega$, using steps [](#continuous){.pf-ref} and [](#triangles){.pf-ref}.
:::

:::

:::

:::

::: {.remark}
Cauchy's integral formula on nested compact disks then shows that $F^{(k)}=\sum_{n=1}^\infty f_n^{(k)}$ for every $k\ge1$, with uniform convergence on compact subsets of $\Omega$.
:::
