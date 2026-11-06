---
schema: qual/card@1
id: P-UVSXF
kind: problem
title: Antiderivative of $x\sqrt{x+1}$
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
  note: Corrected the exponent in the stored substitution work.
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
    its answer: the substitution u = x + 1 and the resulting primitive, checked by differentiating the answer on the interior of the domain
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The substitution and the power rule, with the primitive verified by differentiation.
---

::: {.problem}
Evaluate
$$
\int x\sqrt{x+1}\,dx.
$$
:::

::: {.solution}

The integrand is defined and continuous on $x\ge-1$.

::: pf

::: {.pf-step #substitution}

With $u=x+1$, $x=u-1$, $dx=du$, and
$x\sqrt{x+1}=(u-1)u^{1/2}=u^{3/2}-u^{1/2}$.

::: pf-proof

Substituting $x=u-1$ in $x\sqrt{x+1}$ gives $(u-1)\sqrt u$, and distributing
$\sqrt u=u^{1/2}$ gives $u^{3/2}-u^{1/2}$; both terms are defined and
continuous for $u\ge0$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int
x\sqrt{x+1}\,dx=\frac25(x+1)^{5/2}-\frac23(x+1)^{3/2}+C}$ on $(-1,\infty)$.

::: pf-proof

By step [](#substitution){.pf-ref} the integral is
$\int(u^{3/2}-u^{1/2})\,du=\frac25u^{5/2}-\frac23u^{3/2}+C$, using the power
rule $\frac{d}{du}u^{p}=\frac{p}{u^{1-p}}$ for $p>0$, and substituting back
$u=x+1$ gives the answer. Differentiating the answer gives
$\frac25\cdot\frac52(x+1)^{3/2}-\frac23\cdot\frac32(x+1)^{1/2}=(x+1)^{3/2}-(x+1)^{1/2}=x\sqrt{x+1}$,
which is the integrand; the formula holds on the interior of the domain, where
the fractional powers are differentiable.

:::

:::

:::


:::
