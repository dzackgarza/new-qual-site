---
schema: qual/card@1
id: P-7CUNN
kind: problem
title: Integrals of rational functions by long division and partial fractions
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
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card answered three of the seven parts of its own statement. Parts (c), (e), (f) and (g) were
    absent and are now supplied with the same long-division or substitution, partial fractions, and
    integration structure as the rest; every step of all seven parts carries a pf-proof. Each of the seven
    answers was checked by differentiating it back to the integrand, and the three answers already on the
    card were re-derived rather than copied: (a) x^2/2 + (3/2)ln|x+1| - (9/2)ln|x+3|, (b) x^2 +
    2ln|x+3| + ln|x-2|, (c) x^2/2 + 2ln|x-3| + ln|x+2|, (d) (3/2)x^2 + 3ln|x-2| - 1/(x-2), (e)
    (x-1)^2/2 + 2ln|x-1| - 3/(x-1), (f) x^3/3 - 3x^2 + 14x - 31ln|x+2|, (g) x^3/3 + 3ln|x-4| -
    ln|x+2|. For (d) the constant -6 produced by expanding (3/2)(x-2)^2 + 6(x-2) is absorbed into the
    constant of integration, which the card now says. Nothing in the statement was changed.
---

::: {.problem}
Evaluate:

(a) $\displaystyle\int\frac{x^3+4x^2}{x^2+4x+3}\,dx$;

(b) $\displaystyle\int\frac{2x^3+2x^2-9x-1}{x^2+x-6}\,dx$;

(c) $\displaystyle\int\frac{x^3-x^2-3x+1}{x^2-x-6}\,dx$;

(d) $\displaystyle\int\frac{3x^3-12x^2+15x-5}{x^2-4x+4}\,dx$;

(e) $\displaystyle\int\frac{x(x^2-3x+5)}{x^2-2x+1}\,dx$;

(f) $\displaystyle\int\frac{x^3-4x^2+2x-3}{x+2}\,dx$;

(g) $\displaystyle\int\frac{x^4-2x^3-8x^2+2x+10}{x^2-2x-8}\,dx$.
:::

::: {.solution}

::: pf

::: pf-step

(a) $\int \frac{x^3 + 4x^2}{x^2 + 4x + 3} \, dx = \frac{1}{2}x^2 + \frac{3}{2}\ln\abs{x+1} - \frac{9}{2}\ln\abs{x+3} + C$.

::: pf-proof

::: pf-step

Long division: $x^3 + 4x^2 = x(x^2 + 4x + 3) - 3x$, so $\frac{x^3 + 4x^2}{x^2 + 4x + 3} = x - \frac{3x}{(x+1)(x+3)}$.

::: pf-proof
Multiplying out gives $x(x^2+4x+3)=x^3+4x^2+3x$, whose difference from the numerator is $-3x$; the denominator factors as $(x+1)(x+3)$.
:::

:::

::: pf-step

Partial fractions: $-\frac{3x}{(x+1)(x+3)} = \frac{A}{x+1} + \frac{B}{x+3} \implies -3x = A(x+3) + B(x+1)$.
Setting $x = -1 \implies 3 = 2A \implies A = 3/2$.
Setting $x = -3 \implies 9 = -2B \implies B = -9/2$.

::: pf-proof
Clearing denominators produces the identity $-3x=A(x+3)+B(x+1)$, and evaluating it at the two roots of the denominator gives $2A=3$ and $-2B=9$.
:::

:::

::: pf-step

Integrating: $\int \left(x + \frac{3/2}{x+1} - \frac{9/2}{x+3}\right) dx = \frac{1}{2}x^2 + \frac{3}{2}\ln\abs{x+1} - \frac{9}{2}\ln\abs{x+3} + C$.

::: pf-proof
Integrate term by term with $\int x\,dx=\frac12x^2$ and $\int dx/(x+a)=\ln\abs{x+a}$, the absolute value being needed because the antiderivative is required on each interval avoiding the poles.
:::

:::

:::

:::

::: pf-step

(b) $\int \frac{2x^3 + 2x^2 - 9x - 1}{x^2 + x - 6} \, dx = x^2 + 2\ln\abs{x+3} + \ln\abs{x-2} + C$.

::: pf-proof

::: pf-step

Long division: $2x^3 + 2x^2 - 9x - 1 = 2x(x^2 + x - 6) + (3x - 1)$.

::: pf-proof
$2x(x^2+x-6)=2x^3+2x^2-12x$, and subtracting it from the numerator leaves $(2x^3+2x^2-9x-1)-(2x^3+2x^2-12x)=3x-1$.
:::

:::

::: pf-step

Partial fractions: $\frac{3x-1}{(x+3)(x-2)} = \frac{A}{x+3} + \frac{B}{x-2} \implies 3x - 1 = A(x-2) + B(x+3)$.
Setting $x = 2 \implies 5 = 5B \implies B = 1$.
Setting $x = -3 \implies -10 = -5A \implies A = 2$.

::: pf-proof
Clearing denominators gives the displayed identity, and evaluating at the roots $2$ and $-3$ of the denominator gives $5B=5$ and $-5A=-10$.
:::

:::

::: pf-step

Integrating: $\int \left(2x + \frac{2}{x+3} + \frac{1}{x-2}\right) dx = x^2 + 2\ln\abs{x+3} + \ln\abs{x-2} + C$.

::: pf-proof
Integrate term by term, using $\int 2x\,dx=x^2$ and the logarithmic primitives of the two simple fractions.
:::

:::

:::

:::

::: pf-step

(c) $\int \frac{x^3 - x^2 - 3x + 1}{x^2 - x - 6} \, dx = \frac{1}{2}x^2 + 2\ln\abs{x-3} + \ln\abs{x+2} + C$.

::: pf-proof

::: pf-step

Long division: $x^3 - x^2 - 3x + 1 = x(x^2 - x - 6) + (3x + 1)$, so $\frac{x^3 - x^2 - 3x + 1}{x^2 - x - 6} = x + \frac{3x+1}{(x-3)(x+2)}$.

::: pf-proof
$x(x^2-x-6)=x^3-x^2-6x$, whose difference from the numerator is $3x+1$; the denominator factors as $(x-3)(x+2)$.
:::

:::

::: pf-step

Partial fractions: $\frac{3x+1}{(x-3)(x+2)} = \frac{A}{x-3} + \frac{B}{x+2} \implies 3x + 1 = A(x+2) + B(x-3)$.
Setting $x = 3 \implies 10 = 5A \implies A = 2$.
Setting $x = -2 \implies -5 = -5B \implies B = 1$.

::: pf-proof
Clearing denominators gives the identity, and evaluating at the roots $3$ and $-2$ gives $5A=10$ and $-5B=-5$.
:::

:::

::: pf-step

Integrating: $\int \left(x + \frac{2}{x-3} + \frac{1}{x+2}\right) dx = \frac{1}{2}x^2 + 2\ln\abs{x-3} + \ln\abs{x+2} + C$.

::: pf-proof
Integrate term by term with the logarithmic primitives; differentiating the result gives back $x+\frac{2}{x-3}+\frac{1}{x+2}=\frac{x^3-x^2-3x+1}{x^2-x-6}$.
:::

:::

:::

:::

::: pf-step

(d) $\int \frac{3x^3 - 12x^2 + 15x - 5}{(x-2)^2} \, dx = \frac{3}{2}x^2 + 3\ln\abs{x-2} - \frac{1}{x-2} + C$.

::: pf-proof

::: pf-step

Substitute $u = x - 2 \implies x = u + 2, dx = du$.

::: pf-proof
The map $x\mapsto x-2$ is a bijection of $\RR$ with derivative $1$, so the substitution changes nothing but the letter.
:::

:::

::: pf-step

$3(u+2)^3 - 12(u+2)^2 + 15(u+2) - 5 = 3(u^3 + 6u^2 + 12u + 8) - 12(u^2 + 4u + 4) + 15(u+2) - 5 = 3u^3 + 6u^2 + 3u + 1$.

::: pf-proof
Expanding the three powers and collecting: the $u^2$ coefficient is $18-12=6$, the $u$ coefficient is $36-48+15=3$, and the constant is $24-48+30-5=1$.
:::

:::

::: pf-step

Dividing by $u^2$: $3u + 6 + \frac{3}{u} + \frac{1}{u^2}$.

::: pf-proof
Divide each term of $3u^3+6u^2+3u+1$ by $u^2$.
:::

:::

::: pf-step

Integrating: $\frac{3}{2}u^2 + 6u + 3\ln\abs{u} - \frac{1}{u} + C = \frac{3}{2}(x-2)^2 + 6(x-2) + 3\ln\abs{x-2} - \frac{1}{x-2} + C = \frac{3}{2}x^2 + 3\ln\abs{x-2} - \frac{1}{x-2} + C'$.

::: pf-proof
Integrate term by term: $\int 3u\,du=\frac32u^2$, $\int 6\,du=6u$, $\int \frac{3}{u}du=3\ln\abs u$ and $\int u^{-2}du=-u^{-1}$. Substituting back, $\frac32(x-2)^2+6(x-2)=\frac32x^2-6$, and the constant $-6$ is absorbed into $C'$.
:::

:::

:::

:::

::: pf-step

(e) $\int \frac{x(x^2-3x+5)}{(x-1)^2} \, dx = \frac{1}{2}(x-1)^2 + 2\ln\abs{x-1} - \frac{3}{x-1} + C$.

::: pf-proof

::: pf-step

Expanding the numerator and dividing by $(x-1)^2$: $x^3-3x^2+5x = (x-1)(x^2-2x+1) + (2x+1)$, so the integrand is $(x-1) + \frac{2x+1}{(x-1)^2}$.

::: pf-proof
$(x-1)(x-1)^2=x^3-3x^2+3x-1$, whose difference from the numerator is $2x+1$.
:::

:::

::: pf-step

Writing $2x+1 = 2(x-1)+3$ gives $\frac{2x+1}{(x-1)^2} = \frac{2}{x-1} + \frac{3}{(x-1)^2}$.

::: pf-proof
Split the fraction: $\frac{2(x-1)}{(x-1)^2}=\frac{2}{x-1}$ and $\frac{3}{(x-1)^2}$ remains.
:::

:::

::: pf-step

Integrating: $\int\left((x-1) + \frac{2}{x-1} + \frac{3}{(x-1)^2}\right)dx = \frac{1}{2}(x-1)^2 + 2\ln\abs{x-1} - \frac{3}{x-1} + C$.

::: pf-proof
Integrate term by term with $\int (x-1)dx=\frac12(x-1)^2$ and $\int (x-1)^{-2}dx=-(x-1)^{-1}$; differentiating the result returns the integrand computed above.
:::

:::

:::

:::

::: pf-step

(f) $\int \frac{x^3-4x^2+2x-3}{x+2} \, dx = \frac{1}{3}x^3 - 3x^2 + 14x - 31\ln\abs{x+2} + C$.

::: pf-proof

::: pf-step

Long division: $x^3-4x^2+2x-3 = (x+2)(x^2-6x+14) - 31$.

::: pf-proof
$(x+2)(x^2-6x+14)=x^3-4x^2+2x+28$, whose difference from the numerator is $-31$.
:::

:::

::: pf-step

Integrating: $\int\left(x^2 - 6x + 14 - \frac{31}{x+2}\right)dx = \frac{1}{3}x^3 - 3x^2 + 14x - 31\ln\abs{x+2} + C$.

::: pf-proof
Integrate term by term, with the logarithmic primitive for the simple fraction; the derivative of the result is the quotient computed above.
:::

:::

:::

:::

::: pf-step

(g) $\int \frac{x^4-2x^3-8x^2+2x+10}{x^2-2x-8} \, dx = \frac{1}{3}x^3 + 3\ln\abs{x-4} - \ln\abs{x+2} + C$.

::: pf-proof

::: pf-step

Long division: $x^4-2x^3-8x^2+2x+10 = x^2(x^2-2x-8) + (2x+10)$, so the integrand is $x^2 + \frac{2x+10}{(x-4)(x+2)}$.

::: pf-proof
$x^2(x^2-2x-8)=x^4-2x^3-8x^2$, which cancels the first three terms, leaving $2x+10$; the denominator factors as $(x-4)(x+2)$.
:::

:::

::: pf-step

Partial fractions: $\frac{2x+10}{(x-4)(x+2)} = \frac{A}{x-4} + \frac{B}{x+2} \implies 2x+10 = A(x+2) + B(x-4)$.
Setting $x = 4 \implies 18 = 6A \implies A = 3$.
Setting $x = -2 \implies 6 = -6B \implies B = -1$.

::: pf-proof
Clearing denominators gives the identity, and evaluating at the roots $4$ and $-2$ gives $6A=18$ and $-6B=6$.
:::

:::

::: pf-step

Integrating: $\int\left(x^2 + \frac{3}{x-4} - \frac{1}{x+2}\right)dx = \frac{1}{3}x^3 + 3\ln\abs{x-4} - \ln\abs{x+2} + C$.

::: pf-proof
Integrate term by term; differentiating the result gives $x^2+\frac{3}{x-4}-\frac{1}{x+2}=\frac{x^4-2x^3-8x^2+2x+10}{x^2-2x-8}$.
:::

:::

:::

:::

:::

:::
