---
schema: qual/card@1
id: PR-IGMH4
kind: proposition
title: 'Riemann--Lebesgue lemma: $\widehat f$ is bounded, continuous, and vanishes at infinity'
prompts:
- State the Riemann-Lebesgue lemma.
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - L¹
  - Small Tails
relations: []
review: draft
---

::: {.proposition}
Let $f\in L^1(\RR^n)$.
Then its [[D-5LZQ4|Fourier transform]] $\widehat f$ is continuous on $\RR^n$, satisfies $\sup_{\xi\in\RR^n}\abs{\widehat f(\xi)}\leq\norm{f}_1$, and
$$
\widehat f(\xi)\to0 \quad\text{as } \abs{\xi}\to\infty .
$$
:::
