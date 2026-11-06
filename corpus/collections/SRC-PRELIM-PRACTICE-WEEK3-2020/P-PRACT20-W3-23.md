---
schema: qual/card@1
id: P-PRACT20-W3-23
kind: problem
title: The Gaussian integral via polar coordinates
classification:
  areas:
  - prelim
  topics:
  - Multiple Integrals
  - Polar Coordinates
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 6-7 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the same quadrant integral and the same deduction of the Gaussian integral, and the printed solution gives pi/4 and sqrt pi
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's polar computation and its Fubini factorisation are transcribed, with the positivity of G and the evenness step stated.
---

::: {.problem}
Let $D = \{ (x, y) \in \RR^{2} : x \geq 0, y \geq 0 \}$.

(a) Calculate $\displaystyle\iint_{D} e^{-(x^{2} + y^{2})}\, dx\, dy$.

(b) Use (a) to evaluate the Gaussian integral $\displaystyle\int_{-\infty}^{\infty} e^{-x^{2}}\, dx$.
:::

::: {.solution}

Let $D$ be the first quadrant and $G=\int_0^\infty e^{-x^2}dx$; the double
integral over $D$ is computed in polar coordinates, and Fubini then identifies
it with $G^2$.

::: pf

::: {.pf-step #polar}

$\displaystyle\iint_D e^{-(x^2+y^2)}\,dx\,dy=\frac{\pi}{4}$.

::: pf-proof

In polar coordinates $x=r\cos\theta$, $y=r\sin\theta$ with
$dx\,dy=r\,dr\,d\theta$, the quadrant is $0\le\theta\le\frac\pi2$, $0\le
r<\infty$, and $x^2+y^2=r^2$. So the integral is $\int_0^{\pi/2}\int_0^\infty
e^{-r^2}r\,dr\,d\theta=\frac\pi2\Big[-\frac12e^{-r^2}\Big]_0^\infty=\frac\pi2\cdot\frac12=\frac\pi4$,
the inner integral being computed by the substitution $u=r^2$.

:::

:::

::: {.pf-step #fubini}

$\displaystyle\iint_D e^{-(x^2+y^2)}\,dx\,dy=\Big(\int_0^\infty
e^{-x^2}dx\Big)^2=G^2$.

::: pf-proof

The integrand is a product $e^{-x^2}e^{-y^2}$ of a function of $x$ and a
function of $y$, nonnegative and measurable on the quadrant; Tonelli's theorem
permits the double integral to be written as the iterated integral
$\int_0^\infty e^{-x^2}\big(\int_0^\infty e^{-y^2}dy\big)dx$, and the inner
integral is the constant $G$, so the result is $G\cdot G=G^2$. Since both
factors are positive and finite-or-infinite, the equality holds in
$[0,\infty]$.

:::

:::

::: {.pf-step #gaussian}

$G=\frac{\sqrt\pi}{2}$ and
$\boxed{\displaystyle\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi}$.

::: pf-proof

Steps [](#polar){.pf-ref} and [](#fubini){.pf-ref} give $G^2=\frac\pi4$, and
$G>0$ since the integrand is positive on a set of positive measure, so
$G=\frac{\sqrt\pi}{2}$. The integrand $e^{-x^2}$ is even, so the integral over
$\RR$ is twice the integral over $[0,\infty)$, giving
$2\cdot\frac{\sqrt\pi}{2}=\sqrt\pi$, which is the printed conclusion.

:::

:::

:::


:::
