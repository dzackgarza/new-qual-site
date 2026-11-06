---
schema: qual/card@1
id: P-XRZVW
kind: problem
title: Antiderivatives of $\frac{1}{\sqrt{x^2+25}}$ and $\frac{1}{(1+x^2)^{3/2}}$
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
    its answer: both primitives by differentiating them, and the positivity of the logarithm's argument for all real x
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Two primitives, each verified by differentiation.
---

::: {.problem}
Evaluate
$$
\int\frac{dx}{\sqrt{x^2+25}}
\qquad\text{and}\qquad
\int\frac{dx}{(1+x^2)^{3/2}}.
$$
:::

::: {.solution}

Both integrands are continuous on $\RR$.

::: pf

::: {.pf-step #logarithm}

$\displaystyle\int\frac{dx}{\sqrt{x^2+25}}=\ln\left(x+\sqrt{x^2+25}\right)+C$.

::: pf-proof

Differentiate $\ln(x+\sqrt{x^2+25})$ by the chain rule:
$\frac{1}{x+\sqrt{x^2+25}}\left(1+\frac{x}{\sqrt{x^2+25}}\right)=\frac{1}{x+\sqrt{x^2+25}}\cdot\frac{\sqrt{x^2+25}+x}{\sqrt{x^2+25}}=\frac{1}{\sqrt{x^2+25}}$,
so the stated function is a primitive. No absolute value is needed:
$\sqrt{x^2+25}>\abs x$, so $x+\sqrt{x^2+25}>0$ for every real $x$, and the
integrand is continuous on the connected interval $\RR$.

:::

:::

::: {.pf-step #cube}

$\displaystyle\int\frac{dx}{(1+x^2)^{3/2}}=\frac{x}{\sqrt{1+x^2}}+C$.

::: pf-proof

By the quotient rule,
$\frac{d}{dx}\frac{x}{\sqrt{1+x^2}}=\frac{\sqrt{1+x^2}-x\cdot\frac{x}{\sqrt{1+x^2}}}{1+x^2}=\frac{\frac{(1+x^2)-x^2}{\sqrt{1+x^2}}}{1+x^2}=\frac{1}{(1+x^2)^{3/2}}$,
which is the integrand; the denominator is positive everywhere and the
interval is connected, so these are all the primitives.

:::

:::

:::


:::
