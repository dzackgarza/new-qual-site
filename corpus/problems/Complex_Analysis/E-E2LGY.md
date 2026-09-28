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
Let $K\subset\CC$ be compact. Choose a closed square $Q$ and $\delta>0$ such that every point of $K$ has distance at least $\delta$ from $\partial Q$, and let $L$ be the perimeter of $Q$.

<1>1. $f_n\to g$ uniformly on $\partial Q$.

::: {.proof}
$\partial Q$ is the union of four line segments, and $f_n\to g$ uniformly on each.
:::

<1>2. $\sup_{z\in K}\abs{f_n(z)-f_m(z)}\le{L\over2\pi\delta}\sup_{\xi\in\partial Q}\abs{f_n(\xi)-f_m(\xi)}$.

::: {.proof}
For $z\in K$, the Cauchy integral formula applied to the entire function $f_n-f_m$ gives
\[
f_n(z)-f_m(z)={1\over2\pi i}\oint_{\partial Q}{f_n(\xi)-f_m(\xi)\over\xi-z}\dxi
,\]
and $\abs{\xi-z}\ge\delta$ on $\partial Q$.
:::

<1>3. $f_n\to g$ uniformly on $K$.

::: {.proof}
By step <1>1 the right side of step <1>2 tends to $0$ as $n,m\to\infty$, so $(f_n)$ is uniformly Cauchy on $K$. It converges uniformly on $K$, and the limit is the pointwise limit $g$.
:::

<1>4. $g$ is entire.

::: {.proof}
By step <1>3, $g$ is a uniform limit of continuous functions on every compact set, hence continuous. For every closed triangle $T$, $\int_{\partial T} g=\lim_n\int_{\partial T} f_n=0$ by uniform convergence on $\partial T$ and Cauchy's theorem. By Morera's theorem, $g$ is entire.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>4 and <1>3 are the two claims.
:::
:::



