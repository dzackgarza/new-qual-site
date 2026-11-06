---
schema: qual/card@1
id: P-IOAQB
kind: problem
title: Integrals of $\frac{1}{x(\ln x)^2}$ and $\frac{1}{x^2}\cos\frac{1}{x}$
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
  note: Corrected the sign of the first stored antiderivative.
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
    its answer: the two substitutions, the improper integral evaluated as a limit, and both primitives checked by differentiation
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Two substitutions, the improper integral as a limit of primitives, and the third primitive verified by differentiation.
---

::: {.problem}
Evaluate
$$
\int\frac{dx}{x(\ln x)^2},
\qquad
\int_2^\infty\frac{dx}{x(\ln x)^2},
$$
and
$$
\int \frac1{x^2}\cos\!\left(\frac1x\right)\,dx.
$$
:::

::: {.solution}

Write $\ln$ for the natural logarithm; the three integrands are defined on
$x>0$, on $x\ge2$, and on $x\ne0$ respectively.

::: pf

::: {.pf-step #log}

$\displaystyle\int\frac{dx}{x(\ln x)^2}=-\frac{1}{\ln x}+C$ on each interval
where $\ln x\ne0$.

::: pf-proof

With $u=\ln x$, $du=\frac{dx}{x}$, so the integral is $\int
u^{-2}\,du=-u^{-1}+C=-\frac{1}{\ln x}+C$. Directly,
$\frac{d}{dx}\left(-\frac{1}{\ln x}\right)=\frac{1}{(\ln x)^2}\cdot\frac1x$ by
the chain rule, which is the integrand.

:::

:::

::: {.pf-step #improper}

$\displaystyle\int_2^\infty\frac{dx}{x(\ln x)^2}=\frac{1}{\ln 2}$.

::: pf-proof

The integrand is positive and continuous on $[2,\infty)$, so the improper
integral is $\lim_{R\to\infty}\int_2^R\frac{dx}{x(\ln
x)^2}=\lim_{R\to\infty}\left[-\frac1{\ln
x}\right]_2^R=\lim_{R\to\infty}\left(-\frac{1}{\ln
R}+\frac{1}{\ln2}\right)=\frac{1}{\ln 2}$, using step [](#log){.pf-ref} and
$\ln R\to\infty$.

:::

:::

::: {.pf-step #reciprocal}

$\displaystyle\int\frac{1}{x^2}\cos\left(\frac1x\right)dx=-\sin\left(\frac1x\right)+C$
on each of $x>0$ and $x<0$.

::: pf-proof

With $u=\frac1x$, $du=-\frac{dx}{x^2}$, so the integral is $-\int\cos
u\,du=-\sin u+C=-\sin\left(\frac1x\right)+C$. Directly,
$\frac{d}{dx}\left(-\sin\frac1x\right)=-\cos\left(\frac1x\right)\cdot\left(-\frac{1}{x^2}\right)=\frac{1}{x^2}\cos\left(\frac1x\right)$
by the chain rule.

:::

:::

:::


:::
