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
Then for every $\xi\in\RR^n$:

(a) $\widehat{f * g}(\xi) = \widehat f(\xi)\,\widehat g(\xi)$, where $f*g$ is the [[D-TS42Y|convolution]];

(b) $\widehat{\tau_h f}(\xi) = e^{2\pi i \xi\cdot h}\,\widehat f(\xi)$;

(c) for $m_h(x)\coloneqq e^{2\pi i x\cdot h}f(x)$, $\widehat{m_h}(\xi) = \widehat f(\xi-h) = (\tau_{-h}\widehat f)(\xi)$;

(d) $\widehat{f\circ T}(\xi) = \abs{\det T}^{-1}\,\widehat f\big((T^{-1})^{t}\xi\big)$;

(e) if $x_jf\in L^1(\RR^n)$ for some $j$, then $\partial_{\xi_j}\widehat f$ exists and $\partial_{\xi_j}\widehat f(\xi) = \widehat{(-2\pi i x_j f)}(\xi)$;

(f) if $f\in C^1(\RR^n)$, $\partial_{x_j} f\in L^1(\RR^n)$, and $f$ vanishes at infinity, then $\widehat{\partial_{x_j} f}(\xi) = 2\pi i \xi_j\,\widehat f(\xi)$.
:::

::: {.proof}
(a) By Fubini's theorem, justified since $\int\int\abs{f(x-y)g(y)}\,dy\,dx=\norm{f}_1\norm{g}_1$,
$$
\widehat{f*g}(\xi)=\int\int f(x-y)g(y)e^{-2\pi i (x-y)\cdot\xi}e^{-2\pi i y\cdot\xi}\,dx\,dy=\widehat f(\xi)\widehat g(\xi).
$$

(b) Substituting $y=x+h$ gives $\int f(x+h)e^{-2\pi i x\cdot\xi}\,dx=e^{2\pi i h\cdot\xi}\int f(y)e^{-2\pi i y\cdot\xi}\,dy$.

(c) $\int f(x)e^{-2\pi i x\cdot(\xi-h)}\,dx=\widehat f(\xi-h)$.

(d) Substituting $y=Tx$, so $dx=\abs{\det T}^{-1}dy$ and $x\cdot\xi=T^{-1}y\cdot\xi=y\cdot (T^{-1})^t\xi$, gives the formula.

(e) The difference quotients of $\xi_j\mapsto e^{-2\pi i x\cdot\xi}$ are bounded by $2\pi\abs{x_j}$, so dominated convergence with dominating function $2\pi\abs{x_jf}$ allows differentiation under the integral sign.

(f) Integrating by parts in $x_j$ on $[-R,R]$ and letting $R\to\infty$, the boundary terms vanish because $f$ vanishes at infinity, so $\int \partial_{x_j}f(x)e^{-2\pi i x\cdot\xi}\,dx=2\pi i\xi_j\int f(x)e^{-2\pi i x\cdot\xi}\,dx$.
:::

::: {.remark}
With the other common convention $(\tau_h g)(x)\coloneqq g(x-h)$, formula (b) reads $\widehat{\tau_h f}(\xi)=e^{-2\pi i\xi\cdot h}\widehat f(\xi)$ and (c) reads $\widehat{m_h}=\tau_h\widehat f$.
:::
