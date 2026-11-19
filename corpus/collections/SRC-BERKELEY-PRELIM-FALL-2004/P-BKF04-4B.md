---
schema: qual/card@1
id: P-BKF04-4B
kind: problem
title: The Fresnel-type integral $\int_0^\infty e^{iwt}t^{-1/2}\,dt$
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Transcribed from the retained solution sheet — Berkeley preliminary examination, Fall 2004,
    solutions, assets/attachments/f04solution.pdf, Problem 4B on PDF p. 6 — and restructured
    into steps; the card's prose was that sheet's argument. Two slips in the sheet are not
    reproduced: it prints the concavity inequality with the sign reversed ('sin x ≤ 2x/π'),
    where the argument needs sin x ≥ 2x/π on [0, π/2], and it bounds the arc integral by
    π/(4wR²), where the correct bound from its own computation is π/(4wR)(1 - e^{-wR²}). The
    card's π/(4wR) is right and is kept. Added: the orientation check that the contour is
    closed, the explicit real part of iwu², the Gaussian rescaling, and the absolute-convergence
    reason that I(-w) is the conjugate of I(w). Not claimed: any source besides the sheet; the
    collection's provenance lists it.
---

::: {.problem}
Evaluate $I(w)\coloneqq\int_0^\infty\frac{e^{iwt}}{\sqrt t}\,dt$ for every nonzero real number $w$. You may use the formula $\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi$.
:::

::: {.solution}
The argument is the retained solution sheet's: **Berkeley preliminary examination, Fall 2004, solutions** (`assets/attachments/f04solution.pdf`), Problem 4B, PDF p. 6. Throughout $w \ne 0$ is real, $f(u) \coloneqq e^{iwu^{2}}$ is entire, and for $R > 0$ the contour consists of $\gamma_{1}$ from $0$ to $R$ on the real axis, $\gamma_{2}$ the arc $Re^{it}$, $0 \le t \le \pi/4$, and $\gamma_{3}$ from $Re^{i\pi/4}$ back to $0$.

::: pf

::: {.pf-step #substitution}
$I(w) = 2\int_{0}^{\infty}f(u)\,du$.

::: pf-proof
With $t = u^{2}$ on $(0,\infty)$ one has $dt = 2u\\,du$ and $\sqrt t = u$, so $e^{iwt}/\sqrt t\\,dt = e^{iwu^{2}}\cdot\frac{2u\\,du}{u} = 2f(u)\\,du$; the substitution is a homeomorphism of $(0,\infty)$ onto itself.

:::

:::

::: {.pf-step #cauchy}
$\int_{\gamma_{1}}f + \int_{\gamma_{2}}f + \int_{\gamma_{3}}f = 0$ for every $R > 0$.

::: pf-proof
The contour is closed: $\gamma_{3}$ ends where $\gamma_{1}$ begins. $f$ is entire, being the exponential of a polynomial, so Cauchy's theorem applies on the closed triangular sector bounding the region between the three paths.

:::

:::

::: {.pf-step #arc}
For $w > 0$, $\abs{\int_{\gamma_{2}}f(u)\\,du} \le \frac{\pi}{4wR}$, which tends to $0$.

::: pf-proof
For $u = Re^{it}$ with $0 \le t \le \pi/4$ one has $u^{2} = R^{2}e^{2it}$, so $iwu^{2} = iwR^{2}(\cos 2t + i\sin 2t)$ has real part $-wR^{2}\sin 2t$ and $\abs{f(u)} = e^{-wR^{2}\sin 2t}$. On $[0,\pi/2]$ the sine is concave with $\sin 0 = 0$ and $\sin(\pi/2) = 1$, so $\sin x \ge \frac{2x}{\pi}$ there; applying this at $x = 2t$ gives $\abs{f(u)} \le e^{-4wR^{2}t/\pi}$. Since $\abs{du} = R\\,dt$ on the arc, the integral is at most $R\int_{0}^{\pi/4}e^{-4wR^{2}t/\pi}dt = \frac{\pi}{4wR}\bigl(1 - e^{-wR^{2}}\bigr) \le \frac{\pi}{4wR}$.

:::

:::

::: {.pf-step #third}
$\int_{\gamma_{3}}f(u)\\,du = -e^{i\pi/4}\int_{0}^{R}e^{-ws^{2}}ds$.

::: pf-proof
Write $u = se^{i\pi/4}$ with $s$ decreasing from $R$ to $0$; then $u^{2} = s^{2}e^{i\pi/2} = is^{2}$, so $iwu^{2} = -ws^{2}$ and $f(u) = e^{-ws^{2}}$, while $du = e^{i\pi/4}ds$. Hence the integral is $\int_{R}^{0}e^{-ws^{2}}e^{i\pi/4}ds = -e^{i\pi/4}\int_{0}^{R}e^{-ws^{2}}ds$.

:::

:::

::: {.pf-step #positive}
For $w > 0$, $\int_{0}^{\infty}f(u)\\,du = e^{i\pi/4}\cdot\frac{1}{2}\sqrt{\frac{\pi}{w}}$, so $I(w) = (1+i)\sqrt{\frac{\pi}{2w}}$.

::: pf-proof
By steps [](#cauchy){.pf-ref}, [](#arc){.pf-ref} and [](#third){.pf-ref}, $\int_{0}^{R}f = e^{i\pi/4}\int_{0}^{R}e^{-ws^{2}}ds - \int_{\gamma_{2}}f$; letting $R \to \infty$ the arc term vanishes and $\int_{0}^{\infty}e^{-ws^{2}}ds = \frac{1}{\sqrt w}\int_{0}^{\infty}e^{-x^{2}}dx = \frac{1}{2}\sqrt{\frac{\pi}{w}}$, using $x = \sqrt w\\,s$ and the given Gaussian integral with the integrand even. Then $I(w) = 2e^{i\pi/4}\cdot\frac12\sqrt{\frac{\pi}{w}} = e^{i\pi/4}\sqrt{\frac{\pi}{w}}$, and $e^{i\pi/4} = \frac{1+i}{\sqrt2}$ turns this into $(1+i)\sqrt{\frac{\pi}{2w}}$.

:::

:::

::: {.pf-step #negative}
For $w < 0$, $I(w) = \overline{I(\abs w)}$.

::: pf-proof
The integrand of $I(w)$ at $w = -\abs w$ is $e^{-i\abs w t}/\sqrt t$, the complex conjugate of $e^{i\abs w t}/\sqrt t$ because $t > 0$ makes $1/\sqrt t$ real; integrating preserves conjugation and the improper integral converges absolutely, since $\abs{e^{\pm i\abs w t}/\sqrt t} = t^{-1/2}$ is integrable near $0$ and at $\infty$.

:::

:::

::: pf-step
For every $w \ne 0$, $I(w) = \boxed{(1 + i\operatorname{sgn}(w))\sqrt{\frac{\pi}{2\abs w}}}$.

::: pf-proof
For $w > 0$ this is step [](#positive){.pf-ref}, whose right side equals $(1+i)\sqrt{\pi/(2w)}$ with $\operatorname{sgn}(w) = 1$. For $w < 0$ step [](#negative){.pf-ref} gives $\overline{(1+i)}\sqrt{\frac{\pi}{2\abs w}} = (1-i)\sqrt{\frac{\pi}{2\abs w}}$, and $1 + i\operatorname{sgn}(w) = 1-i$.

:::

:::

:::
:::
