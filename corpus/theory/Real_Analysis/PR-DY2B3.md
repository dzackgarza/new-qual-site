---
schema: qual/card@1
id: PR-DY2B3
kind: proposition
title: Fourier transforms of convolutions, translates, modulations, linear substitutions and derivatives
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Convolution
relations: []
review: draft
---

::: {.proposition}
Use the [[D-5LZQ4|Fourier transform]] $\widehat f(\xi)=\int_{\RR^n} f(x)e^{-2\pi i x\cdot\xi}\,dx$ on $L^1(\RR^n)$.
For $h\in\RR^n$ and a function $g$ on $\RR^n$, let $\tau_h g$ be the translate $(\tau_h g)(x)\coloneqq g(x+h)$.
Let $f,g\in L^1(\RR^n)$, $h\in\RR^n$, and $T\in\GL_n(\RR)$.
Then for every $\xi\in\RR^n$ [@Fol13, Theorem 8.22]:

(a) $\widehat{f * g}(\xi) = \widehat f(\xi)\,\widehat g(\xi)$, where $f*g$ is the [[D-TS42Y|convolution]];

(b) $\widehat{\tau_h f}(\xi) = e^{2\pi i \xi\cdot h}\,\widehat f(\xi)$;

(c) for $m_h(x)\coloneqq e^{2\pi i x\cdot h}f(x)$, $\widehat{m_h}(\xi) = \widehat f(\xi-h) = (\tau_{-h}\widehat f)(\xi)$;

(d) $\widehat{f\circ T}(\xi) = \abs{\det T}^{-1}\,\widehat f\big((T^{-1})^{t}\xi\big)$;

(e) if $x_jf\in L^1(\RR^n)$ for some $j$, then $\partial_{\xi_j}\widehat f$ exists and $\partial_{\xi_j}\widehat f(\xi) = \widehat{(-2\pi i x_j f)}(\xi)$;

(f) if $f\in C^1(\RR^n)$, $\partial_{x_j} f\in L^1(\RR^n)$, and $f$ vanishes at infinity, then $\widehat{\partial_{x_j} f}(\xi) = 2\pi i \xi_j\,\widehat f(\xi)$.
:::

::: {.remark}
With the other common convention $(\tau_h g)(x)\coloneqq g(x-h)$, formula (b) reads $\widehat{\tau_h f}(\xi)=e^{-2\pi i\xi\cdot h}\widehat f(\xi)$ and (c) reads $\widehat{m_h}=\tau_h\widehat f$.
:::
