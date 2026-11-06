---
schema: qual/card@1
id: P-Y6XVP
kind: problem
title: Antiderivative of $e^{x+e^x}$
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
    its answer: the substitution u = e^x and the resulting primitive, checked by differentiating the answer
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
\int e^{x+e^x}\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #substitution}

With $u=e^x$, $du=e^x\,dx$ and $e^{x+e^x}\,dx=e^x e^{e^x}\,dx=e^{u}\,du$.

::: pf-proof

$e^{x+e^x}=e^x\cdot e^{e^x}$ by the addition formula for the exponential, and
$u=e^x$ has $\frac{du}{dx}=e^x$, so the integrand is $e^u\,du$ with $u=e^x$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int e^{x+e^x}\,dx=e^{e^x}+C}$ on $\RR$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is $\int
e^u\,du=e^u+C=e^{e^x}+C$; directly, $\frac{d}{dx}e^{e^x}=e^{e^x}\cdot
e^x=e^{x+e^x}$ by the chain rule, and the integrand is continuous on $\RR$.

:::

:::

:::


:::
