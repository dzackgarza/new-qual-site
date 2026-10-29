---
schema: qual/card@1
id: P-W7RQ2
kind: problem
title: $(1+|\xi|^2)^{-\varepsilon}$ is the Fourier transform of an $L^1$ function
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}

Show that for each $\varepsilon>0$ the following function is the Fourier transform of an $L^1(\RR^n)$ function:
$$
F(\xi) \definedas \qty{1 \over 1 + \abs{\xi}^2}^{\varepsilon}.
$$

:::

::: {.hint}

Show that, with
$$
\begin{aligned}
K_\delta(x) &\definedas \delta^{-n/2} e^{-\pi \abs{x}^2 / \delta}, \\
f(x) &\definedas \int_0^{\infty } K_{\delta}(x) e^{-\pi \delta} \delta^{\varepsilon - 1} \,d \delta, \\
\Gamma(s) &\definedas \int_0^{\infty } e^{-t} t^{s-1} \dt,
\end{aligned}
$$
one has
$$
\fourier{f}(\xi) = \int_0^{\infty } e^{- \pi \delta \abs{\xi}^2} e^{ -\pi \delta} \delta^{\varepsilon - 1} \,d\delta
= \pi^{-\varepsilon} \Gamma(\varepsilon) F(\xi).
$$

:::

::: {.solution}

Normalize the Fourier transform as $\fourier{f}(\xi) = \int f(x) e^{-2\pi i x\cdot\xi}\dx$. The Gaussian $K_\delta(x) = \delta^{-n/2}e^{-\pi\abs{x}^2/\delta}$ has Fourier transform $e^{-\pi\delta\abs{\xi}^2}$, and $\int K_\delta = 1$ for every $\delta > 0$. For $\eps > 0$ let $f(x) \definedas \int_0^\infty K_\delta(x)\, e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta$.

::: pf

::: {.pf-step #s2}

$f \in L^1(\RR^n)$.

::: pf-proof

By Tonelli's theorem and $\int K_\delta = 1$,
$$
\int_{\RR^n}\abs{f(x)}\dx = \int_0^\infty e^{-\pi\delta}\,\delta^{\eps-1} \Big(\int_{\RR^n} K_\delta(x)\dx\Big)\,d\delta = \int_0^\infty e^{-\pi\delta}\delta^{\eps-1}\,d\delta = \frac{\Gamma(\eps)}{\pi^\eps} < \infty .
$$

:::

:::

::: {.pf-step #s3}

$\fourier{f}(\xi) = \int_0^\infty e^{-\pi\delta(1+\abs{\xi}^2)}\,\delta^{\eps-1}\,d\delta$.

::: pf-proof

The function $(x, \delta) \mapsto K_\delta(x) e^{-\pi\delta}\delta^{\eps-1}e^{-2\pi i x\cdot\xi}$ is absolutely integrable on $\RR^n \times (0,\infty)$ by step [](#s2){.pf-ref}, so Fubini's theorem gives
$$
\fourier{f}(\xi) = \int_0^\infty \fourier{K_\delta}(\xi)\, e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta = \int_0^\infty e^{-\pi\delta\abs{\xi}^2}\,e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta .
$$

:::

:::

::: {.pf-step #s4}

$\fourier{f}(\xi) = \pi^{-\eps}\,\Gamma(\eps)\,(1+\abs{\xi}^2)^{-\eps}$.

::: pf-proof

Substituting $t = \pi\delta(1+\abs{\xi}^2)$ in step [](#s3){.pf-ref} gives
$$
\int_0^\infty e^{-\pi\delta(1+\abs{\xi}^2)}\,\delta^{\eps-1}\,d\delta = \Big(\pi(1+\abs{\xi}^2)\Big)^{-\eps} \int_0^\infty e^{-t} t^{\eps-1}\dt = \pi^{-\eps}\,\Gamma(\eps)\,\Big(1+\abs{\xi}^2\Big)^{-\eps} .
$$

:::

:::

::: pf-qed

By step [](#s4){.pf-ref}, $F = \fourier{g}$ for $g = \frac{\pi^\eps}{\Gamma(\eps)} f$, and $g \in L^1$ by step [](#s2){.pf-ref}.

:::

:::

:::
