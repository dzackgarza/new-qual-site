---
schema: qual/card@1
id: T-3UXK7
kind: theorem
title: Convolutions of bounded integrable functions vanish at infinity
slogan: 'If $f,g\in L^1\cap L^\infty$, then $(f*g)(x)\to0$ as $\abs{x}\to\infty$.'
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
  - Limits
relations: []
review: draft
---

::: {.theorem}
Let $f,g\in L^1(\RR^n)$ be essentially bounded.
Then the [[D-TS42Y|convolution]] $f*g$ is defined at every $x\in\RR^n$ and
$$
\lim_{\abs{x}\to\infty}(f*g)(x)=0 .
$$
:::
