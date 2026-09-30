---
schema: qual/card@1
id: P-W7RQ2
kind: problem
title: $(1+|\xi|^2)^{-\epsilon}$ is the Fourier transform of an $L^1$ function
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
Show that for each \( \epsilon>0 \) the following function is the Fourier transform of an $L^1(\RR^n)$ function:
\[
F(\xi) \definedas \qty{1 \over 1 + \abs{\xi}^2}^{\epsilon}
.\]

*Hint: show that*

\[
K_\delta(x) &\definedas \delta^{-n/2} e^{-\pi \abs{x}^2 \over \delta} \\
f(x) &\definedas \int_0^{\infty } K_{\delta}(x) e^{-\pi \delta} \delta^{\epsilon - 1} \,d \delta \\
\Gamma(s) &\definedas \int_0^{\infty } e^{-t} t^{s-1} \dt \\
\implies \fourier{f}(\xi) &= \int_0^{\infty } e^{- \pi \delta \abs{\xi}^2} e^{ -\pi \delta} \delta^{\epsilon - 1}
= \pi^{-s} \Gamma(\epsilon) F(\xi)
.\]
:::
::: {.solution}
*Setup note.* Normalize the Fourier transform as $\fourier{f}(\xi) = \int f(x) e^{-2\pi i x\cdot\xi}\,dx$. The Gaussian $K_\delta(x) = \delta^{-n/2}e^{-\pi|x|^2/\delta}$ has Fourier transform $e^{-\pi\delta|\xi|^2}$, and $\int K_\delta = 1$ for every $\delta > 0$.

::: pf

::: pf-step

Define $f(x) \definedas \int_0^\infty K_\delta(x)\, e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta$ for $\eps > 0$.

:::

::: {.pf-step #s2}

$f \in L^1(\RR^n)$.

::: pf-proof

by Tonelli and $\int K_\delta = 1$,
\[
\int_{\RR^n}|f(x)|\,dx \le \int_0^\infty e^{-\pi\delta}\,\delta^{\eps-1} \Big(\int_{\RR^n} K_\delta(x)\,dx\Big)\,d\delta = \int_0^\infty e^{-\pi\delta}\delta^{\eps-1}\,d\delta = \frac{\Gamma(\eps)}{\pi^\eps} < \infty .
\]

:::

:::

::: {.pf-step #s3}

Compute $\fourier{f}$.

::: pf-proof

since $f$ is an integral of $L^1$ functions, the Fourier transform passes under the integral (Fubini for the absolutely convergent double integral):
\[
\fourier{f}(\xi) = \int_0^\infty \fourier{K_\delta}(\xi)\, e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta = \int_0^\infty e^{-\pi\delta|\xi|^2}\,e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta = \int_0^\infty e^{-\pi\delta(1+|\xi|^2)}\,\delta^{\eps-1}\,d\delta .
\]

:::

:::

::: {.pf-step #s4}

Evaluate the last integral.

::: pf-proof

substitute $t = \pi\delta(1+|\xi|^2)$:
\[
\int_0^\infty e^{-\pi\delta(1+|\xi|^2)}\,\delta^{\eps-1}\,d\delta = \Big(\pi(1+|\xi|^2)\Big)^{-\eps} \int_0^\infty e^{-t} t^{\eps-1}\,dt = \pi^{-\eps}\,\Gamma(\eps)\,\Big(1+|\xi|^2\Big)^{-\eps} .
\]

:::

:::

::: pf-step

Conclude.

::: pf-proof

by steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $\fourier{f}(\xi) = \pi^{-\eps}\Gamma(\eps)\,(1+|\xi|^2)^{-\eps}$, so
\[
F(\xi) = \Big(1+|\xi|^2\Big)^{-\eps} = \frac{\pi^\eps}{\Gamma(\eps)}\,\fourier{f}(\xi) = \fourier{\Big(\frac{\pi^\eps}{\Gamma(\eps)} f\Big)}(\xi),
\]
and $\frac{\pi^\eps}{\Gamma(\eps)}f \in L^1$ by step [](#s2){.pf-ref}. Hence $F$ is the Fourier transform of an $L^1$ function.

:::

:::

:::

:::
