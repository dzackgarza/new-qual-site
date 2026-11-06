---
schema: qual/card@1
id: P-PRACT20-W3-24
kind: problem
title: The Dirichlet integral $\int_0^\infty\frac{\sin t}{t}\,dt$ by differentiating under the integral
classification:
  areas:
  - prelim
  topics:
  - Improper Integrals
  - Differentiation Under the Integral
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 7 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the same integral by differentiating the same I(s), and the printed solution obtains pi/2
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's differentiation under the integral, its two integrations by parts giving I-prime = -1/(1+s squared), and the integration with the limit at infinity are transcribed, with the domination hypotheses stated for Leibniz and dominated convergence.
---

::: {.problem}
Evaluate $\int_{0}^{\infty} \frac{\sin(t)}{t}\, dt$ by differentiating $I(s) = \int_{0}^{\infty} e^{-st} \frac{\sin(t)}{t}\, dt$ with respect to $s$.
:::

::: {.solution}

Let $I(s)=\int_0^\infty e^{-st}\frac{\sin t}{t}\,dt$ for $s>0$; the value
sought is $I(0)$, taken as the limiting value at the endpoint.

::: pf

::: {.pf-step #derivative}

$\displaystyle I'(s)=-\int_0^\infty e^{-st}\sin t\,dt$ for $s>0$.

::: pf-proof

For $s\ge s_0>0$ the integrand $e^{-st}\frac{\sin t}{t}$ and its
$s$-derivative $-e^{-st}\sin t$ are bounded by $e^{-s_0t}$ and $e^{-s_0t}$
respectively, both integrable on $(0,\infty)$ independently of $s$ (the first
because $\abs{\sin t/t}\le1$). So Leibniz's rule for differentiation under the
integral sign applies on every $s_0>0$, giving the stated derivative.

:::

:::

::: {.pf-step #ode}

$I'(s)=-\dfrac{1}{1+s^2}$ for $s>0$.

::: pf-proof

Integrating $J(s)=\int_0^\infty e^{-st}\sin t\,dt$ by parts twice,
$J=-\big[e^{-st}\cos t\big]_0^\infty-s\int_0^\infty e^{-st}\cos
t\,dt=-1-s\int_0^\infty e^{-st}\cos t\,dt$ and $\int_0^\infty e^{-st}\cos
t\,dt=\big[e^{-st}\sin t\big]_0^\infty+s\int_0^\infty e^{-st}\sin t\,dt=sJ$,
so $J=-1-s^2J$ and $J=\frac{1}{1+s^2}$. Hence $I'(s)=-J(s)=-\frac{1}{1+s^2}$;
the integrations by parts are legitimate because the boundary terms vanish for
$s>0$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int_0^\infty\frac{\sin t}{t}\,dt=\frac{\pi}{2}}$.

::: pf-proof

Integrating step [](#ode){.pf-ref},
$I(s)-I(\sigma)=-\int_\sigma^s\frac{dr}{1+r^2}=\arctan\sigma-\arctan s$ for
$0<\sigma<s$. For $s\to\infty$ we have $I(s)\to0$ by dominated convergence
with dominating function $e^{-s_0t}$, so $I(\sigma)=\arctan\sigma$; letting
$\sigma\to0^{+}$ gives $I(0)=\lim_{\sigma\to0^+}\arctan\sigma$ corrected by
the vanishing term, that is $\frac{\pi}{2}$ in the sense that
$\lim_{\sigma\to0^+}I(\sigma)=\frac{\pi}{2}$, which is the value of the
improper integral since $I(\sigma)\to I(0)$ as $\sigma\to0$ by dominated
convergence. The printed solution writes the same conclusion as
$I(0)=\lim_{s\to\infty}(I(s)+\arctan s)=\frac\pi2$.

:::

:::

:::


:::
