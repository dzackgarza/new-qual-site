---
schema: qual/card@1
id: P-TO7UO
kind: problem
title: Antiderivative of $\frac{1+e^x}{1-e^x}$
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
  note: Corrected the missing factor of 2 in the stored antiderivative.
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
    its answer: the partial fraction split in u = e^x and the resulting primitive, checked by differentiating it on each side of x = 0
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. The substitution and partial fractions, with the primitive verified by differentiation on each side of the singularity.
---

::: {.problem}
Evaluate
$$
\int \frac{1+e^x}{1-e^x}\,dx.
$$
:::

::: {.solution}

The integrand is defined where $e^x\ne1$, that is on $\RR\setminus\{0\}$.

::: pf

::: {.pf-step #split}

With $u=e^x$, so that $dx=\frac{du}{u}$, one has
$\dfrac{1+u}{u(1-u)}=\dfrac1u+\dfrac2{1-u}$.

::: pf-proof

The identity is a partial fraction decomposition:
$\frac1u+\frac2{1-u}=\frac{(1-u)+2u}{u(1-u)}=\frac{1+u}{u(1-u)}$, which is an
identity of rational functions on $u\ne0,1$.

:::

:::

::: {.pf-step #value}

$\boxed{\displaystyle\int\frac{1+e^x}{1-e^x}\,dx=x-2\ln\abs{1-e^x}+C}$ on each
of $x<0$ and $x>0$.

::: pf-proof

By step [](#split){.pf-ref}, with $u=e^x$ and $du=e^x\,dx$, the integral is
$\int\left(\frac1u+\frac2{1-u}\right)du=\ln\abs u-2\ln\abs{1-u}+C$, and
$\ln\abs u=\ln e^x=x$. Directly,
$\frac{d}{dx}\left(x-2\ln\abs{1-e^x}\right)=1-2\cdot\frac{-e^x}{1-e^x}=1+\frac{2e^x}{1-e^x}=\frac{1-e^x+2e^x}{1-e^x}=\frac{1+e^x}{1-e^x}$,
which is the integrand; the absolute value is needed because $1-e^x$ changes
sign at $x=0$.

:::

:::

:::


:::
