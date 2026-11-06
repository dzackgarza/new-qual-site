---
schema: qual/card@1
id: P-R67LO
kind: problem
title: Antiderivatives of trigonometric products of $\sin x$ and $\cos x$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
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
    its answer: all six expansions and substitutions, each primitive checked by differentiating it, and the parity identity for the first integrand verified
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Expansions of the squared sum and of the products, and substitutions u = cos x in the odd-power cases.
---

::: {.problem}
Evaluate
$$
\int(\sin x+\cos x)^2dx,
$$
$$
\int\frac32\sin(2x)(\sin x+\cos x)dx,
\quad
\int\cos^2x(1+\sin x)dx,
$$
$$
\int\sin^3x\cos^5x\,dx,
\quad
\int\cos^3x\sin x\,dx,
\quad
\int\sin^3x\sqrt{\cos x}\,dx.
$$
:::

::: {.solution}

All integrands are continuous on $\RR$ except the last, which is continuous on
the intervals where $\cos x>0$.

::: pf

::: {.pf-step #sum-square}

$\displaystyle\int(\sin x+\cos x)^2dx=x-\frac12\cos2x+C$.

::: pf-proof

$(\sin x+\cos x)^2=\sin^2x+2\sin x\cos x+\cos^2x=1+\sin2x$ using
$\sin^2+\cos^2=1$ and $2\sin x\cos x=\sin2x$. The primitive is therefore
$x-\frac12\cos2x$, since $\frac{d}{dx}\left(-\frac12\cos2x\right)=\sin2x$;
equivalently $x+\sin^2x+C$, the two differing by the constant $\frac12$.

:::

:::

::: {.pf-step #weighted}

$\displaystyle\int\frac32\sin(2x)(\sin x+\cos x)\,dx=\sin^3x-\cos^3x+C$.

::: pf-proof

$\sin2x(\sin x+\cos x)=2\sin x\cos x\sin x+2\sin x\cos x\cos x=2\sin^2x\cos
x+2\sin x\cos^2x$, so the integrand is $3\sin^2x\cos x+3\sin x\cos^2x$. The
first term has primitive $\sin^3x$, since $\frac{d}{dx}\sin^3x=3\sin^2x\cos
x$, and the second has primitive $-\cos^3x$, since
$\frac{d}{dx}(-\cos^3x)=3\cos^2x\sin x$; summing gives the stated primitive.

:::

:::

::: {.pf-step #product}

$\displaystyle\int\cos^2x(1+\sin x)\,dx=-\frac13\cos^3x+\frac12(x+\sin x\cos
x)+C$.

::: pf-proof

Expanding, $\cos^2x(1+\sin x)=\cos^2x+\cos^2x\sin x$. The first term has
primitive $\frac12(x+\sin x\cos x)$ by the power-reduction formula
$\cos^2x=\frac12(1+\cos2x)$, and the second has primitive $-\frac13\cos^3x$
because $\frac{d}{dx}\left(-\frac13\cos^3x\right)=\cos^2x\sin x$. Summing
gives the answer, and differentiating it returns $\cos^2x+\cos^2x\sin x$.

:::

:::

::: {.pf-step #odd-powers}

$\displaystyle\int\sin^3x\cos^5x\,dx=-\frac16\cos^6x+\frac18\cos^8x+C$ and
$\displaystyle\int\cos^3x\sin x\,dx=-\frac14\cos^4x+C$.

::: pf-proof

With $u=\cos x$, $du=-\sin x\,dx$ and $\sin^3x=(1-u^2)\sin x$, so the first
integrand becomes $-(1-u^2)u^5du=(u^7-u^5)du$, whose primitive is
$\frac18u^8-\frac16u^6$; substituting back gives the stated form. For the
second, with the same $u$, $\cos^3x\sin x\,dx=-u^3du$, whose primitive is
$-\frac14u^4$.

:::

:::

::: {.pf-step #root}

On intervals where $\cos x>0$, $\displaystyle\int\sin^3x\sqrt{\cos
x}\,dx=-\frac23\cos^{3/2}x+\frac27\cos^{7/2}x+C$.

::: pf-proof

With $u=\cos x>0$, $du=-\sin x\,dx$ and $\sin^3x=(1-u^2)\sin x$, so the
integrand becomes $-(1-u^2)u^{1/2}du=(u^{5/2}-u^{1/2})du$, whose primitive is
$\frac27u^{7/2}-\frac23u^{3/2}$; substituting $u=\cos x$ gives the answer.
Differentiating it gives $\frac27\cdot\frac72\cos^{5/2}x(-\sin
x)-\frac23\cdot\frac32\cos^{1/2}x(-\sin x)=\sin
x\cos^{1/2}x(1-\cos^2x)=\sin^3x\sqrt{\cos x}$, which checks it on the
intervals where $\cos x>0$.

:::

:::

:::


:::
