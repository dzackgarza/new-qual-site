---
schema: qual/card@1
id: P-PAVWJ
kind: problem
title: Integrals of rational functions with $x^2+1$ in the denominator
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
    its answer: all nine decompositions, each multiplied out to fix its coefficients, and all nine primitives checked by differentiating, including the polynomial divisions in items eight and nine
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Nine partial fraction or polynomial division decompositions, each verified by clearing denominators and by differentiating the primitive.
---

::: {.problem}
Evaluate the nine rational antiderivatives listed below:
$$
\frac{x^2}{x^2+1},\quad
\frac{4x^2+x+7}{x^2+1},\quad
\frac{3x^2+x+3}{x(x^2+1)},\quad
\frac{2x-3}{x^3+x},
$$
$$
\frac{4x^2-11x-19}{(x-5)(x^2+1)},\quad
\frac{3x^2+2x-7}{(x-5)(x^2+1)},
$$
$$
\frac{-2x+4}{(x^2+1)(x-1)^2},\quad
\frac{x^4+2x^3+5x^2+4x+6}{x^3+x^2+x+1},
$$
and
$$
\frac{2x^5+4x^3+4x}{x^4+1}.
$$
:::

::: {.solution}

Each integrand is a rational function, integrated on each interval where its
denominator is nonzero. In each step the decomposition is obtained by clearing
denominators and comparing coefficients or evaluating at the poles, and the
primitive is checked by differentiating it.

::: pf

::: {.pf-step #one-two}

$\displaystyle\int\frac{x^2}{x^2+1}dx=x-\arctan x+C$ and
$\displaystyle\int\frac{4x^2+x+7}{x^2+1}dx=4x+\frac12\ln(x^2+1)+3\arctan x+C$.

::: pf-proof

$\frac{x^2}{x^2+1}=1-\frac{1}{x^2+1}$, whose primitive is $x-\arctan x$. For
the second, divide: $4x^2+x+7=4(x^2+1)+(x+3)$, so the integrand is
$4+\frac{x}{x^2+1}+\frac{3}{x^2+1}$, whose primitive is
$4x+\frac12\ln(x^2+1)+3\arctan x$, since
$\frac{d}{dx}\frac12\ln(x^2+1)=\frac{x}{x^2+1}$.

:::

:::

::: {.pf-step #three-four}

$\displaystyle\int\frac{3x^2+x+3}{x(x^2+1)}dx=3\ln\abs x+\arctan x+C$ and
$\displaystyle\int\frac{2x-3}{x^3+x}dx=-3\ln\abs x+\frac32\ln(x^2+1)+2\arctan
x+C$.

::: pf-proof

Write $\frac{3x^2+x+3}{x(x^2+1)}=\frac{A}{x}+\frac{Bx+C}{x^2+1}$; clearing
denominators gives $3x^2+x+3=A(x^2+1)+(Bx+C)x$, so $A=3$ from the constant
terms, $C=1$ from the coefficient of $x$, and $A+B=3$ gives $B=0$. So the
integrand is $\frac3x+\frac{1}{x^2+1}$. Similarly
$\frac{2x-3}{x(x^2+1)}=\frac{A}{x}+\frac{Bx+C}{x^2+1}$ gives $A=-3$, $C=2$,
$A+B=0$, so $B=3$, and the integrand is
$-\frac3x+\frac{3x}{x^2+1}+\frac{2}{x^2+1}$, whose primitive is the stated
one; in both cases differentiating returns the integrand, since
$\frac{d}{dx}\frac12\ln(x^2+1)=\frac{x}{x^2+1}$.

:::

:::

::: {.pf-step #five-six}

$\displaystyle\int\frac{4x^2-11x-19}{(x-5)(x^2+1)}dx=\ln\abs{x-5}+\frac32\ln(x^2+1)+4\arctan
x+C$ and
$\displaystyle\int\frac{3x^2+2x-7}{(x-5)(x^2+1)}dx=3\ln\abs{x-5}+2\arctan
x+C$.

::: pf-proof

For the first,
$\frac{4x^2-11x-19}{(x-5)(x^2+1)}=\frac{A}{x-5}+\frac{Bx+C}{x^2+1}$ with
$A=\frac{4\cdot25-55-19}{26}=1$; then $4x^2-11x-19=(x^2+1)+(Bx+C)(x-5)$ gives
$B=3$ from the $x^2$ coefficient, $C=4$ from the constant term, and the $x$
coefficient agrees: $C-5B=4-15=-11$. For the second,
$A=\frac{3\cdot25+10-7}{26}=3$ and $3x^2+2x-7=3(x^2+1)+(Bx+C)(x-5)$ gives
$B=0$, $C=2$, again consistent with $C-5B=2$. Integrating $\frac{Bx+C}{x^2+1}$
as $B\frac{x}{x^2+1}+C\frac{1}{x^2+1}$ gives the stated logarithms and
arctangents.

:::

:::

::: {.pf-step #seven}

$\displaystyle\int\frac{-2x+4}{(x^2+1)(x-1)^2}dx=-2\ln\abs{x-1}-\frac{1}{x-1}+\ln(x^2+1)+\arctan
x+C$.

::: pf-proof

Write
$\frac{-2x+4}{(x^2+1)(x-1)^2}=\frac{A}{x-1}+\frac{B}{(x-1)^2}+\frac{Cx+D}{x^2+1}$.
Multiplying out, $-2x+4=A(x-1)(x^2+1)+B(x^2+1)+(Cx+D)(x-1)^2$; at $x=1$ this
gives $B=1$, comparing $x^3$ coefficients gives $C=-A$, comparing constants
gives $4=-A+B+D$, and comparing $x^2$ coefficients gives $0=1-A-2C+D$.
Solving, $A=-2$, $C=2$, $D=1$. Integrating gives
$-2\ln\abs{x-1}-\frac{1}{x-1}+\ln(x^2+1)+\arctan x$, since
$\int\frac{2x+1}{x^2+1}dx=\ln(x^2+1)+\arctan x$. Differentiating the answer
gives $\frac{-2}{x-1}+\frac{1}{(x-1)^2}+\frac{2x+1}{x^2+1}$, which over the
common denominator $(x-1)^2(x^2+1)$ has numerator
$-2(x-1)(x^2+1)+(x^2+1)+(2x+1)(x-1)^2=-2x+4$, which checks it.

:::

:::

::: {.pf-step #eight}

$\displaystyle\int\frac{x^4+2x^3+5x^2+4x+6}{x^3+x^2+x+1}dx=\frac12x^2+x+3\ln\abs{x+1}+2\arctan
x+C$.

::: pf-proof

Division of polynomials gives
$x^4+2x^3+5x^2+4x+6=x(x^3+x^2+x+1)+(x^3+4x^2+3x+6)$ and then
$x^3+4x^2+3x+6=(x^3+x^2+x+1)+(3x^2+2x+5)$, so the integrand is
$x+1+\frac{3x^2+2x+5}{(x+1)(x^2+1)}$, using $x^3+x^2+x+1=(x+1)(x^2+1)$. For
the last part,
$\frac{3x^2+2x+5}{(x+1)(x^2+1)}=\frac{A}{x+1}+\frac{Bx+C}{x^2+1}$ with
$A=\frac{3-2+5}{2}=3$, and $3x^2+2x+5=3(x^2+1)+(Bx+C)(x+1)$ gives $B=0$,
$C=2$. Integrating gives $\frac12x^2+x+3\ln\abs{x+1}+2\arctan x$, whose
derivative is $x+1+\frac{3}{x+1}+\frac{2}{x^2+1}$, which is the integrand.

:::

:::

::: {.pf-step #nine}

$\displaystyle\int\frac{2x^5+4x^3+4x}{x^4+1}dx=x^2+\ln(x^4+1)+\arctan(x^2)+C$.

::: pf-proof

Division gives $2x^5+4x^3+4x=2x(x^4+1)+(4x^3+2x)$, so the integrand is
$2x+\frac{4x^3}{x^4+1}+\frac{2x}{x^4+1}$. The primitives are $x^2$ for $2x$,
$\ln(x^4+1)$ for $\frac{4x^3}{x^4+1}$ because
$\frac{d}{dx}\ln(x^4+1)=\frac{4x^3}{x^4+1}$, and $\arctan(x^2)$ for
$\frac{2x}{x^4+1}$ because $\frac{d}{dx}\arctan(x^2)=\frac{2x}{1+x^4}$;
summing and differentiating checks the answer.

:::

:::

:::


:::
