---
schema: qual/card@1
id: P-WESCA05-I6
kind: problem
title: "Winding number of a circle about a distant point"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 6 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Find the winding number of
$$
\gamma(t)=4e^{it}+2i,\qquad 0\le t\le2\pi,
$$
about the point $10+10i$.
:::

::: {.solution}

::: pf

::: pf-step

The curve $\gamma$ is the positively oriented circle of radius $4$ centered at $2i$.


::: pf-proof

The parametrization
$$
\gamma(t)=2i+4e^{it},
\qquad 0\le t\le2\pi,
$$
is the standard counterclockwise parametrization of that circle.

:::

:::

::: {.pf-step #s1-2}

The point $w=10+10i$ lies outside this circle.


::: pf-proof

Its distance from the center $2i$ is
$$
|w-2i|
=|10+8i|
=\sqrt{10^2+8^2}
=\sqrt{164}
>4.
$$

:::

:::

::: {.pf-step #s1-3}

The winding number is
$$
\boxed{\operatorname{Ind}(\gamma,10+10i)=0}.
$$


::: pf-proof

The function
$$
z\longmapsto\frac1{z-w}
$$
is holomorphic on and inside the circle because $w$ lies outside it by step [](#s1-2){.pf-ref}. By Cauchy's theorem,
$$
\int_\gamma\frac{dz}{z-w}=0.
$$
Hence
$$
\operatorname{Ind}(\gamma,w)
=\frac1{2\pi i}\int_\gamma\frac{dz}{z-w}
=0.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required winding number.

:::

:::

:::
