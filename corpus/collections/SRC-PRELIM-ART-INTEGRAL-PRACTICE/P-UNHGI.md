---
schema: qual/card@1
id: P-UNHGI
kind: problem
title: Antiderivative of $\frac{x+1}{x^2+2x+3}$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - u-Substitution
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
    its answer: that the quadratic is positive definite, the substitution and the resulting primitive, checked by differentiating the answer
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The substitution and the primitive, verified by differentiation.
---

::: {.problem}
Evaluate
$$
\int\frac{x+1}{x^2+2x+3}\,dx.
$$
:::

::: {.solution}

The quadratic $x^2+2x+3=(x+1)^2+2$ is positive for every real $x$, so the
integrand is defined and continuous on $\RR$.

::: pf

::: {.pf-step #substitution}

With $u=x^2+2x+3$, $du=2(x+1)\,dx$.

::: pf-proof

Differentiating gives $\frac{du}{dx}=2x+2=2(x+1)$, so $(x+1)\,dx=\frac12du$;
and $u=(x+1)^2+2\ge2>0$ for all $x$, so no division by zero occurs.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\frac{x+1}{x^2+2x+3}\,dx=\frac12\ln(x^2+2x+3)+C}$ on
$\RR$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is
$\frac12\int\frac{du}{u}=\frac12\ln\abs u+C=\frac12\ln(x^2+2x+3)+C$, the
modulus being unnecessary since $u>0$. Directly,
$\frac{d}{dx}\frac12\ln(x^2+2x+3)=\frac12\cdot\frac{2x+2}{x^2+2x+3}=\frac{x+1}{x^2+2x+3}$
by the chain rule, and the integrand is continuous on the interval $\RR$, so
these are all its primitives.

:::

:::

:::


:::
