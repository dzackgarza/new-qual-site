---
schema: qual/card@1
id: PR-DPRY7
kind: proposition
title: The Gaussian is an eigenfunction of the Fourier transform
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
---

::: {.proposition}
Let $g\colon\RR^d\to\RR$ be the Gaussian $g(x) \coloneqq e^{-\pi \abs{x}^2}$.
Then its [[D-5LZQ4|Fourier transform]] is $\widehat g = g$.
Moreover, for $t>0$ the [[D-EWXAT|dilation]] $g_t(x)=t^{-d}g(t^{-1}x)$ satisfies
$$
\widehat{g_t}(\xi) = g(t\xi) = e^{-\pi t^2 \abs{\xi}^2}, \qquad \xi\in\RR^d .
$$
:::
