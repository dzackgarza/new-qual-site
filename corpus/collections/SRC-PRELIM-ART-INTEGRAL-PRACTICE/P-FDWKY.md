---
schema: qual/card@1
id: P-FDWKY
kind: problem
title: Partial-fraction antiderivatives of six rational functions
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Partial Fractions
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
    its answer: all six partial fraction decompositions, each multiplied out to check the coefficients, and all six primitives checked by differentiating
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Six partial fraction decompositions, each verified by clearing denominators, and the primitives by differentiation.
---

::: {.problem}
Evaluate the six rational antiderivatives
$$
\int\frac{x}{x-1}\,dx,
\quad
\int\frac{7x+5}{x^2+x-2}\,dx,
\quad
\int\frac{x}{x^2-x-6}\,dx,
$$
$$
\int\frac{1+x^2}{1-x^2}\,dx,
\quad
\int\frac{dx}{x(x-1)^2},
\quad
\int\frac{x}{(x+5)^2}\,dx.
$$
:::

::: {.solution}

Each integrand is a rational function, integrated on each interval on which
its denominator does not vanish; a partial fraction decomposition is exhibited
in each step and checked by putting the pieces over the common denominator.

::: pf

::: {.pf-step #one-two}

$\displaystyle\int\frac{x}{x-1}dx=x+\ln\abs{x-1}+C$ and
$\displaystyle\int\frac{7x+5}{x^2+x-2}dx=3\ln\abs{x+2}+4\ln\abs{x-1}+C$.

::: pf-proof

$\frac{x}{x-1}=\frac{(x-1)+1}{x-1}=1+\frac{1}{x-1}$, whose primitive is
$x+\ln\abs{x-1}$. Since $x^2+x-2=(x+2)(x-1)$, write
$\frac{7x+5}{(x+2)(x-1)}=\frac{A}{x+2}+\frac{B}{x-1}$; multiplying out gives
$7x+5=A(x-1)+B(x+2)$, and setting $x=-2$ gives $A=3$, setting $x=1$ gives
$B=4$. So the primitive is $3\ln\abs{x+2}+4\ln\abs{x-1}$, and differentiating
gives $\frac{3}{x+2}+\frac{4}{x-1}=\frac{7x+5}{x^2+x-2}$.

:::

:::

::: {.pf-step #three-four}

$\displaystyle\int\frac{x}{x^2-x-6}dx=\frac35\ln\abs{x-3}+\frac25\ln\abs{x+2}+C$
and $\displaystyle\int\frac{1+x^2}{1-x^2}dx=-x+\ln\abs{x+1}-\ln\abs{x-1}+C$.

::: pf-proof

$x^2-x-6=(x-3)(x+2)$ and $\frac{x}{(x-3)(x+2)}=\frac{A}{x-3}+\frac{B}{x+2}$
with $x=A(x+2)+B(x-3)$, so $A=\frac35$ at $x=3$ and $B=\frac25$ at $x=-2$, and
$\frac35(x+2)+\frac25(x-3)=x$ confirms it. For the second, dividing gives
$\frac{1+x^2}{1-x^2}=-1+\frac{2}{1-x^2}$, and
$\frac{2}{1-x^2}=\frac{1}{1+x}+\frac{1}{1-x}=\frac{1}{x+1}-\frac{1}{x-1}$;
integrating termwise and using $\int\frac{dx}{1-x}=-\ln\abs{1-x}$ gives the
stated primitive, which differentiates to
$-1+\frac{1}{x+1}-\frac{1}{x-1}=\frac{-(x^2-1)+(x-1)-(x+1)}{x^2-1}=\frac{1+x^2}{1-x^2}$.

:::

:::

::: {.pf-step #five}

$\displaystyle\int\frac{dx}{x(x-1)^2}=\ln\abs x-\ln\abs{x-1}-\frac{1}{x-1}+C$.

::: pf-proof

Put $\frac{1}{x(x-1)^2}=\frac{A}{x}+\frac{B}{x-1}+\frac{C}{(x-1)^2}$ and
multiply by $x(x-1)^2$: $1=A(x-1)^2+Bx(x-1)+Cx$. At $x=0$, $A=1$; at $x=1$,
$C=1$; comparing coefficients of $x^2$, $0=A+B$, so $B=-1$. Integrating gives
$\ln\abs x-\ln\abs{x-1}-\frac{1}{x-1}$, since
$\int\frac{dx}{(x-1)^2}=-\frac{1}{x-1}$; differentiating returns
$\frac1x-\frac{1}{x-1}+\frac{1}{(x-1)^2}$, which is the original by the
identity $1=(x-1)^2-x(x-1)+x$.

:::

:::

::: {.pf-step #six}

$\displaystyle\int\frac{x}{(x+5)^2}dx=\ln\abs{x+5}+\frac{5}{x+5}+C$.

::: pf-proof

Write
$\frac{x}{(x+5)^2}=\frac{(x+5)-5}{(x+5)^2}=\frac{1}{x+5}-\frac{5}{(x+5)^2}$;
integrating gives $\ln\abs{x+5}+\frac{5}{x+5}$, since
$\frac{d}{dx}\frac{5}{x+5}=-\frac{5}{(x+5)^2}$, and differentiating the sum
returns $\frac{1}{x+5}-\frac{5}{(x+5)^2}=\frac{x}{(x+5)^2}$.

:::

:::

:::


:::
