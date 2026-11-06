---
schema: qual/card@1
id: P-VYOWN
kind: problem
title: Antiderivatives of $\frac{x+\sin x}{1+\cos x}$ and $\frac{xe^x}{(e^x+1)^2}$
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
    its answer: the half-angle identities, the derivative of x tan(x/2), and the integration by parts, each checked by differentiating the stated primitive
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Half-angle identities for the first integrand and one integration by parts with a rational substitution for the second.
---

::: {.problem}
Evaluate
$$
\int\frac{x+\sin x}{1+\cos x}\,dx
$$
and
$$
\int\frac{x e^x}{(e^x+1)^2}\,dx.
$$
:::

::: {.solution}

Both integrands are continuous where the denominators do not vanish: $1+\cos
x=0$ only at $x\equiv\pi\pmod{2\pi}$, and $e^x+1>0$ for all $x$.

::: pf

::: {.pf-step #half-angle}

$\dfrac{\sin x}{1+\cos x}=\tan\dfrac x2$ and $\dfrac{1}{1+\cos
x}=\dfrac12\sec^2\dfrac x2$.

::: pf-proof

Using $\sin x=2\sin\frac x2\cos\frac x2$ and $1+\cos x=2\cos^2\frac x2$, the
first quotient is $\frac{2\sin\frac x2\cos\frac x2}{2\cos^2\frac x2}=\tan\frac
x2$, and the second is $\frac{1}{2\cos^2\frac x2}=\frac12\sec^2\frac x2$; both
hold where $\cos\frac x2\ne0$, that is where $1+\cos x\ne0$.

:::

:::

::: {.pf-step #first}

$\boxed{\displaystyle\int\frac{x+\sin x}{1+\cos x}\,dx=x\tan\frac x2+C}$ on
each interval where $\cos\frac x2\ne0$.

::: pf-proof

By step [](#half-angle){.pf-ref} the integrand is $\frac{x}{1+\cos
x}+\tan\frac x2=\frac x2\sec^2\frac x2+\tan\frac x2$. Differentiating
$x\tan\frac x2$ gives $\tan\frac x2+x\cdot\frac12\sec^2\frac x2$, which is
exactly that, so $x\tan\frac x2$ is a primitive; the integrand is continuous
on each component of $\{\cos\frac x2\ne0\}$, so adding a constant gives all of
them there.

:::

:::

::: {.pf-step #second}

$\boxed{\displaystyle\int\frac{xe^x}{(e^x+1)^2}\,dx=\frac{xe^x}{e^x+1}-\ln(e^x+1)+C}$
on $\RR$.

::: pf-proof

Integrate by parts with $u=x$ and $dv=\frac{e^x}{(e^x+1)^2}dx$: since
$\frac{d}{dx}\left(-\frac{1}{e^x+1}\right)=\frac{e^x}{(e^x+1)^2}$, one may
take $v=-\frac1{e^x+1}$, giving
$\int\frac{xe^x}{(e^x+1)^2}dx=-\frac{x}{e^x+1}+\int\frac{dx}{e^x+1}$. The last
integral is $x-\ln(e^x+1)$, as differentiating shows:
$\frac{d}{dx}\left(x-\ln(e^x+1)\right)=1-\frac{e^x}{e^x+1}=\frac{1}{e^x+1}$.
Hence the integral is $-\frac{x}{e^x+1}+x-\ln(e^x+1)+C$, and
$x-\frac{x}{e^x+1}=x\cdot\frac{e^x+1-1}{e^x+1}=\frac{xe^x}{e^x+1}$, which is
the stated form; differentiating it gives $\frac{xe^x}{(e^x+1)^2}$.

:::

:::

:::


:::
