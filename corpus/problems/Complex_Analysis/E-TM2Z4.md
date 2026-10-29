---
schema: qual/card@1
id: E-TM2Z4
kind: problem
title: Images of sequences of poles converge to anything
classification:
  areas:
  - complex-analysis
  topics:
  - Casorati-Weierstrass
  - Poles
  - Singularities
  - Identity Theorem
relations: []
review: draft
---

::: {.exercise}
Let $f$ be holomorphic in $0 < \abs{z-z_0} < r$, minus a sequence of poles $\theset{z_k} \to z_0$.
Show that for any $w\in \CC$, there is a sequence $\theset{w_k}\to z_0$ with $f(w_k)\to w$.
:::

::: {.solution}
Fix $w\in\CC$.

::: pf

::: {.pf-step #bounded-away}
If no sequence $w_k\to z_0$ of points that are not poles has $f(w_k)\to w$, then there are $\varepsilon>0$ and $\delta\in(0,r)$ with $\abs{f(z)-w}\geq\varepsilon$ whenever $0<\abs{z-z_0}<\delta$ and $z$ is not a pole.

::: pf-proof
Otherwise, for each $n$ there is a point $w_n$, not a pole, with $0<\abs{w_n-z_0}<1/n$ and $\abs{f(w_n)-w}<1/n$, and this sequence has $w_n\to z_0$ and $f(w_n)\to w$.
:::

:::

::: {.pf-step #g-extends}
Under the conclusion of step [](#bounded-away){.pf-ref}, $g\coloneqq 1/(f-w)$ extends holomorphically to $\abs{z-z_0}<\delta$ with $g(z_k) = 0$ for the poles $z_k$ in that disc and $g(z_0) = 0$.

::: pf-proof
Off the poles, $g$ is holomorphic with $\abs{g}\leq 1/\varepsilon$. At each pole $z_k$, $g(z)\to 0$ as $z\to z_k$, so $z_k$ is a removable singularity with $g(z_k) = 0$. The extension is bounded and holomorphic on $0<\abs{z-z_0}<\delta$, so $z_0$ is removable by Riemann's theorem, and $g(z_0) = \lim_k g(z_k) = 0$ by continuity.
:::

:::

::: {.pf-step #contradiction}
The conclusion of step [](#bounded-away){.pf-ref} is false.

::: pf-proof
By step [](#g-extends){.pf-ref}, the zeros $z_k$ of $g$ accumulate at $z_0$, an interior point of the disc, so $g\equiv 0$ by the identity theorem. But $g = 1/(f-w)\neq 0$ at every point that is not a pole.
:::

:::

::: pf-step
There is a sequence $w_k\to z_0$ with $f(w_k)\to w$.

::: pf-proof
This follows from steps [](#bounded-away){.pf-ref} and [](#contradiction){.pf-ref}.
:::

:::

:::

:::
