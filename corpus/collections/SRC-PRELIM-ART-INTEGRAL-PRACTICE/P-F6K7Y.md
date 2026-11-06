---
schema: qual/card@1
id: P-F6K7Y
kind: problem
title: Antiderivatives of powers of $\sec x$ and $\tan x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Integration by Parts
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Corrected the final logarithmic form in item 8 and removed the unresolved question marks.
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
    its answer: all eight primitives, each re-derived by the reduction or substitution stated and checked by differentiating the answer, including the identity relating the two forms of the last one
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Integration by parts for the secant cube, the substitution u = tan x or u = sec x for the others, and the Pythagorean identities.
---

::: {.problem}
Evaluate
$$
\int\sec^3x\,dx,\quad \int\sec^4x\,dx,\quad
\int\tan^2x\,dx,\quad \int\tan^3x\,dx,
$$
$$
\int\tan^4x\,dx,\quad
\int\sec^3x\tan^3x\,dx,
\quad
\int(\tan^4x+\tan^2x)\,dx,
$$
and
$$
\int\frac{2\sin^2x}{\cos^3x}\,dx.
$$
:::

::: {.solution}

All integrands are continuous where their denominators do not vanish: on the
intervals where $\cos x\ne0$ for the secant and tangent powers, and where
$\cos x>0$ for the logarithm-free forms, the identities $\tan'x=\sec^2x$ and
$\sec'x=\sec x\tan x$ being used throughout.

::: pf

::: {.pf-step #secant-cube}

$\displaystyle\int\sec^3x\,dx=\frac12\left(\sec x\tan x+\ln\abs{\sec x+\tan
x}\right)+C$.

::: pf-proof

Integrate by parts with $u=\sec x$, $dv=\sec^2x\,dx$, so $du=\sec x\tan x\,dx$
and $v=\tan x$: then $I=\sec x\tan x-\int\sec x\tan^2x\,dx=\sec x\tan
x-\int\sec x(\sec^2x-1)dx=\sec x\tan x-I+\int\sec x\,dx$. So $2I=\sec x\tan
x+\ln\abs{\sec x+\tan x}$, since $\frac{d}{dx}\ln\abs{\sec x+\tan x}=\sec x$;
this gives the stated primitive, and differentiating it returns $\sec^3x$.

:::

:::

::: {.pf-step #secant-fourth}

$\displaystyle\int\sec^4x\,dx=\tan x+\frac13\tan^3x+C$.

::: pf-proof

$\sec^4x=(1+\tan^2x)\sec^2x$, so with $u=\tan x$, $du=\sec^2x\,dx$ the
integral is $\int(1+u^2)du=u+\frac13u^3$, which gives the stated form;
differentiating it gives $(1+\tan^2x)\sec^2x=\sec^4x$.

:::

:::

::: {.pf-step #tangent-powers}

$\displaystyle\int\tan^2x\,dx=\tan x-x+C$,
$\displaystyle\int\tan^3x\,dx=\frac12\tan^2x+\ln\abs{\cos x}+C$ and
$\displaystyle\int\tan^4x\,dx=\frac13\tan^3x-\tan x+x+C$.

::: pf-proof

$\tan^2x=\sec^2x-1$ has primitive $\tan x-x$. Next $\tan^3x=\tan
x(\sec^2x-1)$, so with $u=\tan x$ the first part is $\int
u\,du=\frac12\tan^2x$ and the second is $-\int\tan x\,dx=\ln\abs{\cos x}$,
since $\frac{d}{dx}\ln\abs{\cos x}=-\tan x$. For the fourth power,
$\tan^4x=\tan^2x(\sec^2x-1)=\tan^2x\sec^2x-\tan^2x$, whose primitive is
$\frac13\tan^3x-(\tan x-x)$ by the first two computations. Each displayed
primitive differentiates back to its integrand.

:::

:::

::: {.pf-step #mixed}

$\displaystyle\int\sec^3x\tan^3x\,dx=\frac15\sec^5x-\frac13\sec^3x+C$ and
$\displaystyle\int(\tan^4x+\tan^2x)\,dx=\frac13\tan^3x+C$.

::: pf-proof

With $u=\sec x$, $du=\sec x\tan x\,dx$ and $\tan^2x=\sec^2x-1=u^2-1$, so
$\sec^3x\tan^3x\,dx=\sec^2x\tan^2x\cdot\sec x\tan x\,dx=u^2(u^2-1)du$, whose
primitive is $\frac15u^5-\frac13u^3$. For the second,
$\tan^4x+\tan^2x=\tan^2x(1+\tan^2x)=\tan^2x\sec^2x$, whose primitive is
$\frac13\tan^3x$ because $\frac{d}{dx}\tan^3x=3\tan^2x\sec^2x$.

:::

:::

::: {.pf-step #sine-over-cosine}

$\displaystyle\int\frac{2\sin^2x}{\cos^3x}\,dx=\sec x\tan x-\ln\abs{\sec
x+\tan x}+C=\sec x\tan x+\ln\abs{\sec x-\tan x}+C$.

::: pf-proof

$\frac{2\sin^2x}{\cos^3x}=2\frac{1-\cos^2x}{\cos^3x}=2(\sec^3x-\sec x)$, so
the integral is $2\int\sec^3x\,dx-2\int\sec x\,dx=\left(\sec x\tan
x+\ln\abs{\sec x+\tan x}\right)-2\ln\abs{\sec x+\tan x}$ by step
[](#secant-cube){.pf-ref}, which is $\sec x\tan x-\ln\abs{\sec x+\tan x}$. The
second form uses $(\sec x-\tan x)(\sec x+\tan x)=\sec^2x-\tan^2x=1$, which
turns the logarithm into its negative.

:::

:::

:::


:::
