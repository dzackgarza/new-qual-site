---
schema: qual/card@1
id: E-E2LGY
kind: problem
title: Pointwise limits of entire functions, uniform on segments, are entire and compactly
  convergent
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Uniform Convergence
  - Sequences of Functions
  - Morera
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of entire functions where

- $f_n \to g$ pointwise for some $g:\CC\to\CC$.
- On every line segment in $\CC$, $f_n \to g$ uniformly.

Show that 

- $g$ is entire, and
- $f_n\to g$ uniformly on every compact subset of $\CC$.
:::

::: {.solution}
Let $K\subset\CC$ be compact. Choose a closed square $Q$ whose interior contains $K$, put $\delta=\operatorname{dist}(K,\partial Q)>0$, and let $L$ be the perimeter of $Q$.

::: pf

::: {.pf-step #uniform-on-boundary}
$f_n\to g$ uniformly on $\partial Q$.

::: pf-proof
$\partial Q$ is the union of four line segments, and $f_n\to g$ uniformly on each.
:::

:::

::: {.pf-step #cauchy-estimate-on-K}
$\sup_{z\in K}\abs{f_n(z)-f_m(z)}\le{L\over2\pi\delta}\sup_{\xi\in\partial Q}\abs{f_n(\xi)-f_m(\xi)}$.

::: pf-proof
For $z\in K$, the Cauchy integral formula applied to the entire function $f_n-f_m$ gives
\[
f_n(z)-f_m(z)={1\over2\pi i}\oint_{\partial Q}{f_n(\xi)-f_m(\xi)\over\xi-z}\dxi
,\]
and $\abs{\xi-z}\ge\delta$ on $\partial Q$.
:::

:::

::: {.pf-step #uniform-on-K}
$f_n\to g$ uniformly on $K$.

::: pf-proof
By step [](#uniform-on-boundary){.pf-ref} the right side of step [](#cauchy-estimate-on-K){.pf-ref} tends to $0$ as $n,m\to\infty$, so $(f_n)$ is uniformly Cauchy on $K$. It converges uniformly on $K$, and the limit is the pointwise limit $g$.
:::

:::

::: {.pf-step #g-entire}
$g$ is entire.

::: pf-proof
By step [](#uniform-on-K){.pf-ref}, $g$ is a uniform limit of continuous functions on every compact set, hence continuous. For every closed triangle $T$, $\int_{\partial T} g=\lim_n\int_{\partial T} f_n=0$ by uniform convergence on $\partial T$ and Cauchy's theorem. By Morera's theorem, $g$ is entire.
:::

:::

::: pf-qed
Steps [](#g-entire){.pf-ref} and [](#uniform-on-K){.pf-ref} are the two claims.
:::

:::




:::
