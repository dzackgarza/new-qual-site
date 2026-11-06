---
schema: qual/card@1
id: P-UOENS
kind: problem
title: $\int\sin x\cos x\cot x\tan x\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
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
    its answer: the simplification cot x tan x = 1 where the integrand is defined, and the primitive, checked by differentiation; the domain restriction is stated on the card
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The reduction of the integrand and the verification of the primitive by differentiation.
---

::: {.problem}
Evaluate
$$
\int \sin x\cos x\cot x\tan x\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #product}

$\cot x\tan x=1$ at every point where both are defined.

::: pf-proof

$\cot x=\frac{\cos x}{\sin x}$ and $\tan x=\frac{\sin x}{\cos x}$, so the
product is $\frac{\cos x\sin x}{\sin x\cos x}=1$ whenever $\sin x\ne0\ne\cos
x$, which is exactly where both factors are defined.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\sin x\cos x\cot x\tan x\,dx=\frac12\sin^2x+C}$ on
each interval of $\{x:\sin x\cos x\ne0\}$.

::: pf-proof

On such an interval the integrand equals $\sin x\cos x$ by step
[](#product){.pf-ref}, and $\frac{d}{dx}\frac12\sin^2x=\sin x\cos x$ by the
chain rule, so $\frac12\sin^2x$ is a primitive there. The domain is a union of
open intervals and the integrand is continuous on each, so the primitives on
each are this function plus a constant; no single constant serves on all of
them, which is why the answer is stated per interval.

:::

:::

:::


:::
