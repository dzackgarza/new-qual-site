---
schema: qual/card@1
id: P-PHHXJ
kind: problem
title: Integrals of $\sqrt{1-x^2}$, $\sqrt{16-x^2}$ on $[-4,4]$, and $(1+x)\sqrt{1-x^2}$
  on $[-1,1]$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometric Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-ART-INTEGRAL-PRACTICE has an empty provenance list, its own
    remark records that the drill sheet's original paper was not found, and
    searching assets/attachments/ and the migration records finds no copy of the
    sheet, so there is no page to read and the printed statement could not be
    compared with a source document. What was checked here is the statement and
    its answer: the trigonometric antiderivative by differentiating it, and both definite integrals re-derived, the second and third from the areas of semicircles and the oddness of x sqrt(1 - x^2)
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. A trigonometric substitution for the antiderivative, and area and parity arguments for the two definite integrals.
---

::: {.problem}
Evaluate
$$
\int\sqrt{1-x^2}\,dx,
\qquad
\int_{-4}^{4}\sqrt{16-x^2}\,dx,
$$
and
$$
\int_{-1}^{1}(1+x)\sqrt{1-x^2}\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #antiderivative}

$\displaystyle\int\sqrt{1-x^2}\,dx=\frac12\left(\arcsin
x+x\sqrt{1-x^2}\right)+C$ on $(-1,1)$.

::: pf-proof

Put $x=\sin u$ with $u\in(-\frac\pi2,\frac\pi2)$, so $dx=\cos u\,du$ and
$\sqrt{1-x^2}=\cos u>0$; the integral is
$\int\cos^2u\,du=\frac12\int(1+\cos2u)du=\frac12u+\frac14\sin2u+C=\frac12(u+\sin
u\cos u)+C$ using $\sin2u=2\sin u\cos u$. Substituting back $\sin u=x$, $\cos
u=\sqrt{1-x^2}$ gives the stated primitive. Differentiating it returns the integrand:
$\frac12\left(\frac{1}{\sqrt{1-x^2}}+\sqrt{1-x^2}-\frac{x^2}{\sqrt{1-x^2}}\right)=\frac12\cdot\frac{1+(1-x^2)-x^2}{\sqrt{1-x^2}}=\frac{1-x^2}{\sqrt{1-x^2}}=\sqrt{1-x^2}$.

:::

:::

::: {.pf-step #semicircle}

$\displaystyle\int_{-4}^{4}\sqrt{16-x^2}\,dx=8\pi$.

::: pf-proof

For $-4\le x\le4$ the graph of $y=\sqrt{16-x^2}$ is the upper half of the
circle $x^2+y^2=16$, a region of area $\frac12\pi\cdot4^2=8\pi$; the integral
of a nonnegative continuous function over an interval is the area under its
graph, so the value is $8\pi$. Equivalently, step [](#antiderivative){.pf-ref}
scaled by $4$ gives $\left[\frac12\left(16\arcsin\frac
x4+x\sqrt{16-x^2}\right)\right]_{-4}^{4}=\frac12(16\cdot\frac\pi2+16\cdot\frac\pi2)=8\pi$.

:::

:::

::: {.pf-step #linear}

$\displaystyle\int_{-1}^{1}(1+x)\sqrt{1-x^2}\,dx=\frac\pi2$.

::: pf-proof

Split the integral: $\int_{-1}^1\sqrt{1-x^2}\,dx$ is the area of the upper
unit semicircle, $\frac\pi2$, and $\int_{-1}^1x\sqrt{1-x^2}\,dx=0$ because the
integrand $x\sqrt{1-x^2}$ is odd and the interval is symmetric, the integrand
being continuous on $[-1,1]$. So the total is $\frac\pi2+0=\frac\pi2$.

:::

:::

:::


:::
