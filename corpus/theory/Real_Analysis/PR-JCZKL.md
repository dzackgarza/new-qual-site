---
schema: qual/card@1
id: PR-JCZKL
kind: proposition
title: Plancherel theorem
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - L²
  - Norms
relations: []
review: draft
---

::: {.proposition}
If $f\in L^1(\RR^d)\cap L^2(\RR^d)$, then its [[D-5LZQ4|Fourier transform]] $\widehat f$ lies in $L^2(\RR^d)$ and
$$
\norm{f}_{L^2}^2 = \int_{\RR^d} \abs{f}^2 = \int_{\RR^d} \abs{\widehat f}^2 = \norm{\widehat{f}}_{L^2}^2 .
$$
:::

::: {.remark}
The analogue for Fourier series is Parseval's identity: for $f\in L^2([0,1])$ with Fourier coefficients $c_k\coloneqq\int_0^1 f(x)e^{-2\pi i kx}\,dx$, one has $\int_0^1\abs{f}^2=\sum_{k\in\ZZ}\abs{c_k}^2$.
:::
