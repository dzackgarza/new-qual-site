---
schema: qual/card@1
id: T-S3C3S
kind: theorem
title: Lebesgue differentiation theorem
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Differentiation
  - Integrals
relations: []
review: draft
---

::: {.theorem title="Lebesgue differentiation theorem"}
Let $d\geq1$ and let $f\colon\RR^d\to\CC$ be Lebesgue [[D-R5DL3|integrable]].
Then for almost every $x\in\RR^d$,
$$
\lim_{\substack{m(B)\to0\\ x\in B}}\frac{1}{m(B)}\int_B f(y)\,dy=f(x),
$$
where the limit is taken over open balls $B\subseteq\RR^d$ containing $x$ as their Lebesgue measure $m(B)$ tends to $0$ [@SS05].
:::

::: {.corollary}
Let $f\colon\RR\to\CC$ be Lebesgue integrable, and for $h>0$ define $A_h f\colon\RR\to\CC$ by
$$
A_h f(x)\coloneqq\frac{1}{2h}\int_{x-h}^{x+h}f(y)\,dy.
$$
Then $A_h f(x)\to f(x)$ as $h\to0^+$ for almost every $x\in\RR$, and $\norm{A_h f-f}_{L^1(\RR)}\to0$ as $h\to0^+$ [@SS05].
:::
