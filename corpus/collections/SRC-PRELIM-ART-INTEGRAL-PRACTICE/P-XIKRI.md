---
schema: qual/card@1
id: P-XIKRI
kind: problem
title: $\int\frac{4x^3+2x}{x^4+1}\,dx$
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
    its answer: the split of the integrand and both primitives, checked by differentiating the answer term by term
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The split into two substitutions, each verified by differentiation.
---

::: {.problem}
Evaluate
$$
\int\frac{4x^3+2x}{x^4+1}\,dx.
$$
:::

::: {.solution}

The integrand is defined and continuous on $\RR$, since $x^4+1\ge1$.

::: pf

::: {.pf-step #quartic}

$\displaystyle\int\frac{4x^3}{x^4+1}\,dx=\ln(x^4+1)+C$.

::: pf-proof

With $u=x^4+1$, $du=4x^3\,dx$, so the integral is $\int\frac{du}{u}=\ln u+C$,
the modulus being unnecessary because $u\ge1>0$; equivalently
$\frac{d}{dx}\ln(x^4+1)=\frac{4x^3}{x^4+1}$.

:::

:::

::: {.pf-step #arctan}

$\displaystyle\int\frac{2x}{x^4+1}\,dx=\arctan(x^2)+C$.

::: pf-proof

With $u=x^2$, $du=2x\,dx$ and $x^4+1=u^2+1$, so the integral is
$\int\frac{du}{u^2+1}=\arctan u+C=\arctan(x^2)+C$; directly
$\frac{d}{dx}\arctan(x^2)=\frac{2x}{1+x^4}$ by the chain rule.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\frac{4x^3+2x}{x^4+1}\,dx=\ln(x^4+1)+\arctan(x^2)+C}$
on $\RR$.

::: pf-proof

The integral of a sum is the sum of the integrals, so steps
[](#quartic){.pf-ref} and [](#arctan){.pf-ref} give the value, and
differentiating the answer, $\frac{4x^3}{x^4+1}+\frac{2x}{1+x^4}$, recovers
the integrand. The two primitives are on the connected interval $\RR$, so a
single constant suffices.

:::

:::

:::


:::
