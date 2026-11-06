---
schema: qual/card@1
id: P-UUACQ
kind: problem
title: Antiderivative of $\frac{x}{\sqrt{4-x^4}}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
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
    its answer: the substitution u = x^2/2 and the resulting primitive, checked by differentiating it, together with the domain where the square root is real
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The substitution and the primitive, verified by differentiation.
---

::: {.problem}
Evaluate, on an interval where the integrand is real,
$$
\int\frac{x}{\sqrt{4-x^4}}\,dx.
$$
:::

::: {.solution}

The integrand is real where $4-x^4\ge0$, that is $\abs x\le\sqrt2$, and it is
continuous there.

::: pf

::: {.pf-step #substitution}

With $u=\frac{x^2}{2}$, $du=x\,dx$ and $\sqrt{4-x^4}=2\sqrt{1-u^2}$.

::: pf-proof

$x^4=4u^2$, so $4-x^4=4(1-u^2)$ and the square root is $2\sqrt{1-u^2}$ for
$\abs u\le1$, which is the domain $\abs x\le\sqrt2$; and $\frac{du}{dx}=x$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\frac{x}{\sqrt{4-x^4}}\,dx=\frac12\arcsin\left(\frac{x^2}{2}\right)+C}$
on $(-1,1)$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is
$\int\frac{du}{2\sqrt{1-u^2}}=\frac12\arcsin
u+C=\frac12\arcsin\frac{x^2}{2}+C$. Differentiating gives
$\frac12\cdot\frac{1}{\sqrt{1-x^4/4}}\cdot x=\frac{x}{\sqrt{4-x^4}}$, which is
the integrand, and the interval $(-1,1)$ is where $\abs u<1$, that is $\abs
x<\sqrt2$ minus the endpoints where the integrand blows up; on the open
interval the formula holds.

:::

:::

:::


:::
