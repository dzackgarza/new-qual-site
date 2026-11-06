---
schema: qual/card@1
id: P-JHXZS
kind: problem
title: $\int 2018^x\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
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
    its answer: evaluating the antiderivative by differentiating it, which turns on the single derivative in step 1 and requires no hypothesis on x
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The single derivative used is that of an exponential, and the primitive is verified by differentiating it.
---

::: {.problem}
Evaluate
$$
\int 2018^x\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #derivative}

$\dfrac{d}{dx}2018^x=(\ln 2018)\,2018^x$ on $\RR$.

::: pf-proof

$2018^x=e^{x\ln 2018}$, and by the chain rule $\frac{d}{dx}e^{ux}=ue^{ux}$
with $u=\ln 2018$, which is the stated derivative.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int2018^x\,dx=\frac{2018^x}{\ln 2018}+C}$ on $\RR$.

::: pf-proof

$\ln 2018>0$, so $\frac{1}{\ln2018}$ is defined, and differentiating the
displayed primitive gives $\frac{1}{\ln 2018}(\ln 2018)2018^x=2018^x$ by step
[](#derivative){.pf-ref}. The integrand is continuous on the interval $\RR$,
so its antiderivatives are exactly this function plus a constant.

:::

:::

:::


:::
