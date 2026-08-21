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
solved: true
---

::: problem
Show that for each \( \epsilon>0 \) the following function is the Fourier transform of an $L^1(\RR^n)$ function:
\[
F(\xi) \da \qty{1 \over 1 + \abs{\xi}^2}^{\epsilon}
.\]


*Hint: show that*

\[
K_\delta(x) &\da \delta^{-n/2} e^{-\pi \abs{x}^2 \over \delta} \\
f(x) &\da \int_0^{\infty } K_{\delta}(x) e^{-\pi \delta} \delta^{\epsilon - 1} \,d \delta \\
\Gamma(s) &\da \int_0^{\infty } e^{-t} t^{s-1} \dt \\
\implies \fourier{f}(\xi) &= \int_0^{\infty } e^{- \pi \delta \abs{\xi}^2} e^{ -\pi \delta} \delta^{\epsilon - 1}
= \pi^{-s} \Gamma(\epsilon) F(\xi)
.\]
:::
::: {.solution}
> **AI-Generated Solution**

*Setup note.* Normalize the Fourier transform as $\fourier{f}(\xi) = \int f(x) e^{-2\pi i x\cdot\xi}\,dx$. The Gaussian $K_\delta(x) = \delta^{-n/2}e^{-\pi|x|^2/\delta}$ has Fourier transform $e^{-\pi\delta|\xi|^2}$, and $\int K_\delta = 1$ for every $\delta > 0$.

<1>1. Define $f(x) \da \int_0^\infty K_\delta(x)\, e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta$ for $\eps > 0$.
<1>2. $f \in L^1(\RR^n)$.
    Proof: by Tonelli and $\int K_\delta = 1$,
    \[
    \int_{\RR^n}|f(x)|\,dx \le \int_0^\infty e^{-\pi\delta}\,\delta^{\eps-1} \Big(\int_{\RR^n} K_\delta(x)\,dx\Big)\,d\delta = \int_0^\infty e^{-\pi\delta}\delta^{\eps-1}\,d\delta = \frac{\Gamma(\eps)}{\pi^\eps} < \infty .
    \]
<1>3. Compute $\fourier{f}$.
    Proof: since $f$ is an integral of $L^1$ functions, the Fourier transform passes under the integral (Fubini for the absolutely convergent double integral):
    \[
    \fourier{f}(\xi) = \int_0^\infty \fourier{K_\delta}(\xi)\, e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta = \int_0^\infty e^{-\pi\delta|\xi|^2}\,e^{-\pi\delta}\,\delta^{\eps-1}\,d\delta = \int_0^\infty e^{-\pi\delta(1+|\xi|^2)}\,\delta^{\eps-1}\,d\delta .
    \]
<1>4. Evaluate the last integral.
    Proof: substitute $t = \pi\delta(1+|\xi|^2)$:
    \[
    \int_0^\infty e^{-\pi\delta(1+|\xi|^2)}\,\delta^{\eps-1}\,d\delta = \Big(\pi(1+|\xi|^2)\Big)^{-\eps} \int_0^\infty e^{-t} t^{\eps-1}\,dt = \pi^{-\eps}\,\Gamma(\eps)\,\Big(1+|\xi|^2\Big)^{-\eps} .
    \]
<1>5. Conclude.
    Proof: by <1>3 and <1>4, $\fourier{f}(\xi) = \pi^{-\eps}\Gamma(\eps)\,(1+|\xi|^2)^{-\eps}$, so
    \[
    F(\xi) = \Big(1+|\xi|^2\Big)^{-\eps} = \frac{\pi^\eps}{\Gamma(\eps)}\,\fourier{f}(\xi) = \fourier{\Big(\frac{\pi^\eps}{\Gamma(\eps)} f\Big)}(\xi),
    \]
    and $\frac{\pi^\eps}{\Gamma(\eps)}f \in L^1$ by <1>2. Hence $F$ is the Fourier transform of an $L^1$ function.
<1>6. Q.E.D.
:::
