---
schema: qual/card@1
id: E-SS6.EX-5
kind: problem
title: $\abs{\Gamma(1/2+it)}^2=\frac{2\pi}{e^{\pi t}+e^{-\pi t}}$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: 1 - s = conj(s) for
    s = 1/2 + it, so Gamma(s)Gamma(1-s) = |Gamma(s)|^2; Gamma(conj s) = conj(Gamma(s)) holds on
    Re s > 0 because the defining integral is holomorphic there and real on the real axis, and the
    proof now says so rather than quoting a general Schwarz reflection principle without
    hypothesis; sin(pi(1/2 + it)) = cos(i pi t) = cosh(pi t) is computed from the addition formula
    and cos(iz) = cosh z; pi/cosh(pi t) = 2 pi/(e^{pi t} + e^{-pi t}). The square root step notes
    that the right side is positive, so there is no sign ambiguity. Statement unchanged; no
    retained solution set covers the exercises of Stein-Shakarchi.
---

::: {.exercise}
Use the fact that $\Gamma(s)\Gamma(1-s)=\pi/\sin\pi s$ to prove that

$$
\abs{ \Gamma (1 / 2 + i t) } = \sqrt {\frac {2 \pi}{e ^ {\pi t} + e ^ {- \pi t}}}, \quad \text{whenever } t \in \RR.
$$
:::

::: {.solution}
With $s=\tfrac12+it$ the two factors of the reflection formula are complex conjugates, so their product is $\abs{\Gamma(s)}^2$, and $\sin\pi s=\cosh\pi t$ turns the right side into the displayed expression. The argument is this card's own; no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #conjugate}
For $s=\tfrac12+it$ one has $1-s=\overline s$, and $\Gamma(\overline s)=\overline{\Gamma(s)}$.

::: pf-proof
$1-(\tfrac12+it)=\tfrac12-it=\overline s$. The identity $\Gamma(\overline s)=\overline{\Gamma(s)}$ for $\Re s>0$ follows because the integral $\Gamma(s)=\int_0^\infty e^{-x}x^{s-1}\dd x$ defining $\Gamma$ on the half-plane $\Re s>0$ may be differentiated under the integral sign, so it is holomorphic there and real for real $s$; a holomorphic function on a domain symmetric about the real axis that is real on the real axis satisfies $f(\overline s)=\overline{f(s)}$, by the Schwarz reflection principle or by expanding in a power series about a real point.
:::

:::


::: {.pf-step #reflection}
$\displaystyle\abs{\Gamma(\tfrac12+it)}^2=\frac{\pi}{\sin\pi(\tfrac12+it)}$.

::: pf-proof
Take $s=\tfrac12+it$, so that $1-s=\overline s$. The reflection formula $\Gamma(s)\Gamma(1-s)=\pi/\sin\pi s$ then reads $\Gamma(s)\overline{\Gamma(s)}=\pi/\sin\pi s$ by step [](#conjugate){.pf-ref}, and $\Gamma(s)\overline{\Gamma(s)}=\abs{\Gamma(s)}^2$. Note $\Re s=\tfrac12>0$, so $s$ is in the half-plane on which $\Gamma$ is defined by the integral and the reflection formula applies.
:::

:::


::: {.pf-step #sine}
$\sin\pi(\tfrac12+it)=\cosh\pi t$.

::: pf-proof
$\sin(\tfrac\pi2+w)=\cos w$ for all complex $w$, by the addition formula; taking $w=i\pi t$ gives $\sin\pi(\tfrac12+it)=\cos(i\pi t)=\cosh\pi t$, since $\cos(iz)=\cosh z$.
:::

:::


::: {.pf-step #value}
$\displaystyle\abs{\Gamma(\tfrac12+it)}^2=\frac{2\pi}{e^{\pi t}+e^{-\pi t}}$.

::: pf-proof
By steps [](#reflection){.pf-ref} and [](#sine){.pf-ref}, $\abs{\Gamma(\tfrac12+it)}^2=\pi/\cosh\pi t$, and $\cosh\pi t=(e^{\pi t}+e^{-\pi t})/2$, so $\pi/\cosh\pi t=2\pi/(e^{\pi t}+e^{-\pi t})$.
:::

:::


::: {.pf-step #conclusion}
For every real $t$, $\displaystyle\abs{\Gamma(\tfrac12+it)}=\sqrt{\frac{2\pi}{e^{\pi t}+e^{-\pi t}}}$.

::: pf-proof
The right-hand side of step [](#value){.pf-ref} is a positive real number for every real $t$, since $e^{\pi t}+e^{-\pi t}>0$; so its positive square root is $\abs{\Gamma(\tfrac12+it)}$, and no sign ambiguity remains.
:::

:::

:::
:::
