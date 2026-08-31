---
schema: qual/card@1
id: P-KVFWY
kind: problem
title: Continuous on $\CC$ and holomorphic off $\RR$ implies entire
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Schwarz Reflection
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Suppose that $f: \CC\to\CC$ is continuous everywhere and analytic on $\CC\setminus \RR$ and prove that $f$ is entire.
:::

::: {.solution}
Just reproducing the proof of holomorphicity in the Schwarz reflection theorem.

- Note $f$ is continuous on $\CC$ since analytic implies continuous ($f$ equals its power series, where the partials sums uniformly converge to it, and uniform limit of continuous is continuous).

- Strategy: take $D$ a disc centered at a point $x\in \RR$, show $f$ is holomorphic in $D$ by Morera's theorem.

- Let $\Delta \subset D$ be a triangle in $D$.

- Case 1: If $\Delta \intersect \RR = 0$, then $f$ is holomorphic on $\Delta$ and $\int_\Delta f = 0$.

- Case 2: one side or vertex of $\Delta$ intersects $\RR$, and wlog the rest of $\Delta$ is in $\HH^+$.

  - Then let $\Delta_\eps$ be the perturbation $\Delta + i\eps = \theset{z+ i\eps \suchthat z\in \Delta}$; then $\Delta_\eps \intersect \RR = 0$ and $\int_{\Delta_\eps} f = 0$.

  - Now let $\eps\to 0$ and conclude by continuity of $f$.

    - Parametrize $\Delta$ by a piecewise-smooth closed curve $\gamma: [a,b] \to \CC$, and write $\gamma_\eps(t) \da \gamma(t) + i\eps$ for the corresponding parametrization of $\Delta_\eps$.
      Then $\gamma_\eps'(t) = \gamma'(t)$, so
      $$
      \int_{\Delta_\eps} f = \int_a^b f(\gamma_\eps(t)) \gamma_\eps'(t)\,dt = \int_a^b f(\gamma(t) + i\eps) \gamma'(t)\,dt.
      $$

    - We claim this converges to $\int_\Delta f = \int_a^b f(\gamma(t))\gamma'(t)\,dt$ as $\eps \to 0$.
      The image $\gamma([a,b])$ is compact, so $f$ is uniformly continuous on a compact neighborhood of it: for every $\eta > 0$ there is $\eps_0 > 0$ such that $|f(\gamma(t) + i\eps) - f(\gamma(t))| < \eta$ for all $t \in [a,b]$ and all $0 < \eps < \eps_0$.
      Since $\gamma'$ is bounded on $[a,b]$ (it is continuous on a compact interval), say $|\gamma'(t)| \le M$, we get
      $$
      \left| \int_a^b f(\gamma(t)+i\eps)\gamma'(t)\,dt - \int_a^b f(\gamma(t))\gamma'(t)\,dt \right|
      \le \int_a^b |f(\gamma(t)+i\eps) - f(\gamma(t))|\,|\gamma'(t)|\,dt
      \le \eta M (b-a),
      $$
      which tends to $0$ as $\eta \to 0$.
      Hence $\int_{\Delta_\eps} f \to \int_\Delta f$, and since each $\int_{\Delta_\eps} f = 0$, we get $\int_\Delta f = 0$.

- Case 3: $\Delta$ intersects both $\HH^+$ and $\HH^-$.

  - Break into smaller triangles, each of which falls into one of the previous two cases.
:::
