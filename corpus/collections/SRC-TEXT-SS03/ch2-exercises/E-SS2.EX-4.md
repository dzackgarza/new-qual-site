---
schema: qual/card@1
id: E-SS2.EX-4
kind: problem
title: The Gaussian $e^{-\pi x^2}$ is its own Fourier transform
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Fourier Transform
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The four ingredients
    are separated and each is named: holomorphy of the integral with the
    differentiating formula (dominated convergence with the Gaussian weight), the
    integration by parts with the boundary term and its vanishing, the constant
    argument through the product rule on a connected domain, and the value at
    zero. Not checked: the book's own text of the exercise and its value of the
    Gaussian integral, neither of which is retained in this checkout; the
    statement is as transcribed on the card. No retained solution set covers the
    exercise (the collection's provenance is a Google Books record), so the
    argument is the card's own. No statement repair.
---

::: {.exercise}
Prove that for all $\xi \in \CC$ we have $e^{-\pi\xi^2} = \int_{-\infty}^{\infty} e^{-\pi x^2} e^{2\pi i x\xi}\, dx$.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Put
$$
F(\xi)=\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi ix\xi}\,dx,\qquad \xi\in\CC .
$$

::: pf

::: {.pf-step #entire}
$F$ is entire, and for every $\xi\in\CC$
$$
F'(\xi)=2\pi i\int_{-\infty}^{\infty}x\,e^{-\pi x^2}e^{2\pi ix\xi}\,dx .
$$

::: pf-proof
Write $\xi=s+it$ with $s,t\in\RR$, so that $\abs{e^{2\pi ix\xi}}=e^{-2\pi xt}$. On a compact $K\subset\CC$ the quantities $\abs{s},\abs{t}$ are bounded by some $C$. For $N\ge0$,
$$
\abs{x^N e^{-\pi x^2}e^{2\pi ix\xi}}\le \abs{x}^N e^{-\pi x^2+2\pi C\abs{x}},
$$
and the right side is integrable on $\RR$ and independent of $\xi\in K$, since $e^{-\pi x^2+2\pi C\abs{x}}$ decays exponentially. So the integrand and each of its $\xi$-derivatives $\bigl(2\pi ix\bigr)^N e^{-\pi x^2}e^{2\pi ix\xi}$ are dominated on $K$ by an integrable function of $x$ alone. The dominated convergence theorem then gives that $F$ is complex differentiable on the interior of $K$ with the derivative obtained by differentiating under the integral sign, and $K$ was arbitrary; the displayed formula is that statement for $N=1$.
:::

:::

::: {.pf-step #parts}
$F'(\xi)=-2\pi\xi F(\xi)$ for every $\xi\in\CC$.

::: pf-proof
Since $\frac{d}{dx}e^{-\pi x^2}=-2\pi x e^{-\pi x^2}$, step [](#entire){.pf-ref} gives
$$
F'(\xi)=-i\int_{-\infty}^{\infty}\Bigl(\frac{d}{dx}e^{-\pi x^2}\Bigr)e^{2\pi ix\xi}\,dx .
$$
Integrate by parts on $[-R,R]$: both factors are continuously differentiable, so
$$
\int_{-R}^{R}\Bigl(\frac{d}{dx}e^{-\pi x^2}\Bigr)e^{2\pi ix\xi}\,dx
=\Bigl[e^{-\pi x^2}e^{2\pi ix\xi}\Bigr]_{-R}^{R}-\int_{-R}^{R}e^{-\pi x^2}\bigl(2\pi i\xi\bigr)e^{2\pi ix\xi}\,dx .
$$
The boundary term tends to $0$ as $R\to\infty$, because $\abs{e^{-\pi x^2}e^{2\pi ix\xi}}=e^{-\pi x^2-2\pi x\operatorname{Im}\xi}\to0$ at both ends for fixed $\xi$, and dominated convergence lets the integral on the right pass to the limit. Hence
$$
F'(\xi)=-i\Bigl(0-2\pi i\xi\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi ix\xi}\,dx\Bigr)=-i\bigl(-2\pi i\xi\bigr)F(\xi)=-2\pi\xi F(\xi),
$$
using $(-i)(-2\pi i\xi)=2\pi i^2\xi=-2\pi\xi$.
:::

:::

::: {.pf-step #constant}
$e^{\pi\xi^2}F(\xi)$ is constant on $\CC$.

::: pf-proof
$e^{\pi\xi^2}$ and $F$ are entire, so their product is entire, and the product rule with step [](#parts){.pf-ref} gives
$$
\frac{d}{d\xi}\Bigl(e^{\pi\xi^2}F(\xi)\Bigr)=2\pi\xi e^{\pi\xi^2}F(\xi)+e^{\pi\xi^2}\bigl(-2\pi\xi F(\xi)\bigr)=0
$$
at every $\xi$. An entire function with vanishing derivative on the connected set $\CC$ is constant.
:::

:::

::: {.pf-step #value}
$F(0)=1$.

::: pf-proof
At $\xi=0$ the integrand is the real Gaussian $e^{-\pi x^2}$, and $\int_{-\infty}^{\infty}e^{-\pi x^2}\,dx=1$.
:::

:::

::: {.pf-step}
$F(\xi)=e^{-\pi\xi^2}$ for every $\xi\in\CC$, that is
$$
e^{-\pi\xi^2}=\int_{-\infty}^{\infty}e^{-\pi x^2}e^{2\pi ix\xi}\,dx .
$$

::: pf-proof
By steps [](#constant){.pf-ref} and [](#value){.pf-ref} the constant value of $e^{\pi\xi^2}F(\xi)$ is $e^{0}F(0)=1$, so $F(\xi)=e^{-\pi\xi^2}$ for every $\xi\in\CC$, and $F$ is the integral displayed on the card.
:::

:::

:::

:::

::: {.remark title="Variations"}
A common form of this exercise lets the reader assume the identity for real $\xi$ and asks only for the extension to all $\xi\in\CC$, with every step justified: both sides are entire functions of $\xi$ (the integral by differentiation under the integral sign, or Morera with Fubini), and they agree on $\RR$, so they agree on $\CC$ by the identity theorem.
:::
