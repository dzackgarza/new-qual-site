---
schema: qual/card@1
id: P-B4WQK
kind: problem
title: "Suppose that $f: \\CC\\to\\CC$ is continuous everywhere and analytic on $\\CC\\setminus \\RR$ and\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - morera
  - schwarz-reflection
  - holomorphic-functions
relations: []
review: draft
---

Suppose that $f: \CC\to\CC$ is continuous everywhere and analytic on $\CC\setminus \RR$ and prove that $f$ is entire.

::: {.remark}
Something missing?
:::
::: {.solution}
::: {.concept}
:::

- Note $f$ is continuous on $\CC$ since analytic implies continuous ($f$ equals its power series, where the partials sums uniformly converge to it, and uniform limit of continuous is continuous).

- Strategy: take $D$ a disc centered at a point $x\in \RR$, show $f$ is holomorphic in $D$ by Morera's theorem.

- Let $\Delta \subset D$ be a triangle in $D$.

- Case 1: If $\Delta \intersect \RR = 0$, then $f$ is holomorphic on $\Delta$ and $\int_\Delta f = 0$.

- Case 2: one side or vertex of $\Delta$ intersects $\RR$, and wlog the rest of $\Delta$ is in $\HH^+$.

  - Then let $\Delta_\eps$ be the perturbation $\Delta + i\eps = \theset{z+ i\eps \suchthat z\in \Delta}$; then $\Delta_\eps \intersect \RR = 0$ and $\int_{\Delta_\eps} f = 0$.

  - Now let $\eps\to 0$ and conclude by continuity of $f$ (???)

    - We want
    \begin{align*}
    \int_{\Delta_\eps} f = \int_a^b f(\gamma_\eps(t)) \gamma_\eps'(t)\,dt \converges{\eps\to 0}\to \int_a^b f(\gamma(t)) \gamma_\eps'(t)\,dt =\int_{\Delta}  f
    \end{align*}
    where $\gamma_\eps, \gamma$ are curves parametrizing $\Delta_\eps, \Delta$ respectively.

    - Since $\gamma, \gamma_\eps$ are closed and bounded in $\CC$, they are compact subsets.
      Thus it suffices to show that $f(\gamma_\eps(t)) \gamma_\eps'(t)$ converges uniformly to $f(\gamma(t))\gamma'(t)$.

    - ??

- Case 3: $\Delta$ intersects both $\HH^+$ and $\HH^-$.

  - Break into smaller triangles, each of which falls into one of the previous two cases.
:::
