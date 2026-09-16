---
schema: qual/card@1
id: PR-IGMH4
kind: proposition
title: 'Riemann--Lebesgue lemma: $\widehat f$ is bounded, continuous, and vanishes at infinity'
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

::: {.proof}
The bound follows from $\abs{f(x)e^{-2\pi i x\cdot\xi}}=\abs{f(x)}$.
If $\xi_k\to\xi$, the integrands $f(x)e^{-2\pi i x\cdot\xi_k}$ converge pointwise and are dominated by $\abs{f}$, so $\widehat f(\xi_k)\to\widehat f(\xi)$ by dominated convergence.

For the decay, since $e^{\pi i}=-1$, substituting $x\mapsto x+\xi/(2\abs{\xi}^2)$ gives $\widehat f(\xi)=-\int_{\RR^n}f\big(x+\tfrac{\xi}{2\abs{\xi}^2}\big)e^{-2\pi i x\cdot\xi}\,dx$ for $\xi\neq0$, so
$$
\abs{\widehat f(\xi)}\leq\frac12\norm{f-f\big(\cdot+\tfrac{\xi}{2\abs{\xi}^2}\big)}_1\to0 \quad\text{as }\abs{\xi}\to\infty,
$$
by continuity of translation in $L^1(\RR^n)$.
:::
