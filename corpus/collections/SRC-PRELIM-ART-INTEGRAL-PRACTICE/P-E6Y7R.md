---
schema: qual/card@1
id: P-E6Y7R
kind: problem
title: Antiderivatives of $x\arcsin(1/x)$, $x\arctan x$, and $x\sin(2x)$
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
  note: Corrected the sign of the x cos(2x) term.
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
    its answer: all four by-parts computations and the definite integral, each antiderivative checked by differentiating it
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Three integrations by parts and the evaluation of the definite integral from its primitive.
---

::: {.problem}
Evaluate
$$
\int x\arcsin\!\left(\frac1x\right)\,dx
\quad (x>1),
$$
$$
\int x\arctan x\,dx,
\qquad
\int_0^1x\arctan x\,dx,
$$
and
$$
\int x\sin(2x)\,dx.
$$
:::

::: {.solution}

All four integrands are continuous on the intervals stated; for the first,
$x>1$ ensures $\arcsin(1/x)$ is defined and the principal branch is used.

::: pf

::: {.pf-step #arcsin}

$\displaystyle\int
x\arcsin\left(\frac1x\right)dx=\frac12\left(x^2\arcsin\left(\frac1x\right)+\sqrt{x^2-1}\right)+C$
on $x>1$.

::: pf-proof

Integrate by parts with $u=\arcsin\frac1x$ and $dv=x\,dx$. For $x>1$,
$\frac{d}{dx}\arcsin\frac1x=\frac{1}{\sqrt{1-1/x^2}}\cdot\left(-\frac{1}{x^2}\right)=-\frac{1}{x\sqrt{x^2-1}}$,
since $\sqrt{1-1/x^2}=\frac{\sqrt{x^2-1}}{x}$ for $x>0$. So the integral is
$\frac{x^2}{2}\arcsin\frac1x+\frac12\int\frac{x\,dx}{\sqrt{x^2-1}}=\frac{x^2}{2}\arcsin\frac1x+\frac12\sqrt{x^2-1}+C$,
using $\frac{d}{dx}\sqrt{x^2-1}=\frac{x}{\sqrt{x^2-1}}$. Differentiating the
answer gives
$x\arcsin\frac1x+\frac{x^2}{2}\left(-\frac{1}{x\sqrt{x^2-1}}\right)+\frac{x}{2\sqrt{x^2-1}}=x\arcsin\frac1x$.

:::

:::

::: {.pf-step #arctan}

$\displaystyle\int x\arctan x\,dx=\frac12\left((x^2+1)\arctan x-x\right)+C$
and $\displaystyle\int_0^1x\arctan x\,dx=\frac\pi4-\frac12$.

::: pf-proof

Integrate by parts with $u=\arctan x$, $dv=x\,dx$: $\int x\arctan
x\,dx=\frac{x^2}{2}\arctan
x-\frac12\int\frac{x^2}{1+x^2}dx=\frac{x^2}{2}\arctan
x-\frac12\int\left(1-\frac{1}{1+x^2}\right)dx=\frac{x^2}{2}\arctan x-\frac
x2+\frac12\arctan x+C$, which is the stated form; differentiating it gives
$x\arctan x+\frac{x^2+1}{2}\cdot\frac{1}{1+x^2}-\frac12=x\arctan x$.
Evaluating at $1$ and at $0$: the primitive at $1$ is
$\frac12(2\cdot\frac\pi4-1)=\frac\pi4-\frac12$ and at $0$ it is $0$, so the
definite integral is $\frac\pi4-\frac12$.

:::

:::

::: {.pf-step #sine}

$\displaystyle\int x\sin(2x)\,dx=-\frac12x\cos(2x)+\frac14\sin(2x)+C$.

::: pf-proof

Integrate by parts with $u=x$, $dv=\sin(2x)dx$, so $v=-\frac12\cos(2x)$: the
integral is $-\frac x2\cos(2x)+\frac12\int\cos(2x)dx=-\frac
x2\cos(2x)+\frac14\sin(2x)+C$. Differentiating gives
$-\frac12\cos2x+x\sin2x+\frac12\cos2x=x\sin2x$, which checks it.

:::

:::

:::


:::
