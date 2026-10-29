---
schema: qual/card@1
id: T-DTXIA
kind: theorem
title: Fourier inversion
slogan: 'If both $f$ and $\widehat f$ are integrable, inverse Fourier transform recovers $f$ at every Lebesgue point.'
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
---

::: {.theorem}
Let $f\in L^1(\RR^n)$, and suppose its [[D-5LZQ4|Fourier transform]] $\widehat f(\xi)=\int_{\RR^n}f(x)e^{-2\pi i x\cdot\xi}\,dx$ also lies in $L^1(\RR^n)$.
Then
$$
F(x)\coloneqq\int_{\RR^n}\widehat f(\xi)e^{2\pi i x\cdot\xi}\,d\xi
$$
defines a bounded continuous function $F\colon\RR^n\to\CC$, and $F(x)=f(x)$ for almost every $x\in\RR^n$.
More precisely, $F(x)=f(x)$ at every Lebesgue point $x$ of $f$, that is, every $x$ with
$$
\lim_{r\to0^+}\frac{1}{m(B_r(x))}\int_{B_r(x)}\abs{f(y)-f(x)}\,dy=0 ;
$$
in particular, $F(x)=f(x)$ at every point $x$ at which $f$ is continuous.
:::
