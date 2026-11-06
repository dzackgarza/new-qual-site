---
schema: qual/card@1
id: P-EAYXF
kind: problem
title: $\int\frac{e^x}{e^x+1}\,dx$
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
    its answer: the substitution u = e^x + 1 and the resulting primitive, checked by differentiating the answer
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
\int \frac{e^x}{e^x+1}\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #substitution}

With $u=e^x+1$, $du=e^x\,dx$ and $\frac{e^x}{e^x+1}dx=\frac{du}{u}$.

::: pf-proof

The derivative of $e^x+1$ is $e^x$, so the substitution carries the numerator
times $dx$ to $du$ and the denominator to $u$; $u=e^x+1>1>0$, so
$\frac{du}{u}$ is defined everywhere.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\frac{e^x}{e^x+1}\,dx=\ln(e^x+1)+C}$ on $\RR$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is $\int\frac{du}{u}=\ln
u+C=\ln(e^x+1)+C$. Directly, $\frac{d}{dx}\ln(e^x+1)=\frac{e^x}{e^x+1}$ by the
chain rule, and the integrand is continuous on $\RR$ with positive
denominator, so these are all its primitives; the modulus in $\ln\abs{u}$ is
unnecessary because $u>0$.

:::

:::

:::


:::
