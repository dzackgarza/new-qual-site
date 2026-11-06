---
schema: qual/card@1
id: P-XYIBX
kind: problem
title: Antiderivatives by radical substitution, starting with $\int\frac{1-\sqrt{x}}{1+\sqrt{x}}\,dx$
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
  note: Corrected the first stored logarithmic antiderivative and normalized constants, absolute values, and real domains across the bundle.
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
    its answer: all twelve substitutions and primitives, each re-derived and checked by differentiating the stated answer, the domains of the real-valued integrands being those stated on the card
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Twelve substitutions, each primitive verified by differentiation.
---

::: {.problem}
Evaluate the following antiderivatives on intervals where the real-valued integrands are defined:

1. $\displaystyle \int \frac{1-\sqrt x}{1+\sqrt x}\,dx$.
2. $\displaystyle \int \frac{dx}{\sqrt x+2\sqrt[3]x}$.
3. $\displaystyle \int \frac{dx}{\sqrt x-\sqrt[3]x}$.
4. $\displaystyle \int \frac{dx}{\sqrt x+\sqrt[4]x}$.
5. $\displaystyle \int \frac{\sqrt[3]x+1}{\sqrt[3]x-1}\,dx$.
6. $\displaystyle \int \frac{dx}{(x+1)\sqrt x}$ and $\displaystyle \int \frac{dx}{2x\sqrt{x-1}}$.
7. $\displaystyle \int \frac{x}{\sqrt[3]{x+1}}\,dx$.
8. $\displaystyle \int \frac{dx}{x\sqrt{4x-1}}$.
9. $\displaystyle \int \frac{2\,dx}{x\sqrt{25x^4-1}}$.
10. $\displaystyle \int \frac{dx}{\sqrt x\sqrt{1-4x}}$.
11. $\displaystyle \int \frac{6-2x}{\sqrt{9-x^2}}\,dx$.
12. $\displaystyle \int \frac{dx}{\sqrt{x\sqrt x-x^2}}$.
:::

::: {.solution}

Each item is integrated on an interval on which its integrand is real and
continuous; the substituted variable is written $t$ and the substitution is
stated in each step. Where an answer is written with a fractional power, it is
the primitive on the interior of the domain.

::: pf

::: {.pf-step #one}

$\displaystyle\int\frac{1-\sqrt x}{1+\sqrt x}\,dx=-x+4\sqrt x-4\ln(1+\sqrt
x)+C$.

::: pf-proof

With $t=\sqrt x$, $x=t^2$, $dx=2t\,dt$ and $\frac{1-t}{1+t}=-1+\frac{2}{1+t}$,
so the integral is
$\int\left(-2t+4-\frac{4}{1+t}\right)dt=-t^2+4t-4\ln\abs{1+t}+C$. Substituting
back and noting $1+t>0$ gives the stated form; differentiating gives
$-1+\frac{2}{\sqrt x}-\frac{4}{2\sqrt x(1+\sqrt x)}=-1+\frac{2(1+\sqrt
x)-2}{\sqrt x(1+\sqrt x)}=\frac{1-\sqrt x}{1+\sqrt x}$.

:::

:::

::: {.pf-step #two}

$\displaystyle\int\frac{dx}{\sqrt x+2\sqrt[3]x}=2\sqrt
x-6\sqrt[3]x+24\sqrt[6]x-48\ln\abs{\sqrt[6]x+2}+C$.

::: pf-proof

With $t=x^{1/6}$, $x=t^6$, $dx=6t^5dt$, $\sqrt x=t^3$, $\sqrt[3]x=t^2$, so the
integrand is $\frac{6t^5}{t^3+2t^2}dt=\frac{6t^3}{t+2}dt$. Dividing,
$6t^3=(t+2)(6t^2-12t+24)-48$, so the integral is
$2t^3-6t^2+24t-48\ln\abs{t+2}+C$; substituting back gives the stated powers of
$x$.

:::

:::

::: {.pf-step #three}

$\displaystyle\int\frac{dx}{\sqrt x-\sqrt[3]x}=2\sqrt
x+3\sqrt[3]x+6\sqrt[6]x+6\ln\abs{\sqrt[6]x-1}+C$.

::: pf-proof

With the same $t=x^{1/6}$ the integrand is
$\frac{6t^5}{t^3-t^2}dt=\frac{6t^3}{t-1}dt$, and $6t^3=(t-1)(6t^2+6t+6)+6$, so
the integral is $2t^3+3t^2+6t+6\ln\abs{t-1}+C$, which is the stated form since
$t^3=\sqrt x$, $t^2=\sqrt[3]x$, $t=\sqrt[6]x$.

:::

:::

::: {.pf-step #four}

$\displaystyle\int\frac{dx}{\sqrt x+\sqrt[4]x}=2\sqrt
x-4\sqrt[4]x+4\ln\abs{\sqrt[4]x+1}+C$.

::: pf-proof

With $t=x^{1/4}$, $x=t^4$, $dx=4t^3dt$, $\sqrt x=t^2$, so the integrand is
$\frac{4t^3}{t^2+t}dt=\frac{4t^2}{t+1}dt$, and $4t^2=(t+1)(4t-4)+4$. So the
integral is $2t^2-4t+4\ln\abs{t+1}+C$, which is the stated form.

:::

:::

::: {.pf-step #five}

$\displaystyle\int\frac{\sqrt[3]x+1}{\sqrt[3]x-1}\,dx=x+3x^{2/3}+6x^{1/3}+6\ln\abs{x^{1/3}-1}+C$.

::: pf-proof

With $t=\sqrt[3]x$, $x=t^3$, $dx=3t^2dt$, the integrand is
$\frac{3t^2(t+1)}{t-1}dt$, and $3t^2(t+1)=(t-1)(3t^2+6t+6)+6$. So the integral
is $t^3+3t^2+6t+6\ln\abs{t-1}+C$, which is the stated form because $t^3=x$.

:::

:::

::: {.pf-step #six}

$\displaystyle\int\frac{dx}{(x+1)\sqrt x}=2\arctan\sqrt x+C$ and
$\displaystyle\int\frac{dx}{2x\sqrt{x-1}}=\arctan\sqrt{x-1}+C$.

::: pf-proof

For the first, $t=\sqrt x$ gives $dx=2t\,dt$ and $x+1=t^2+1$, so the integral
is $\int\frac{2dt}{t^2+1}=2\arctan t+C$. For the second, $t=\sqrt{x-1}$ gives
$x=t^2+1$, $dx=2t\,dt$, so the integral is
$\int\frac{2t\,dt}{2(t^2+1)t}=\int\frac{dt}{t^2+1}=\arctan t+C$.
Differentiating the first answer gives $\frac{2}{\sqrt
x}\cdot\frac{1}{1+x}=\frac{2}{(x+1)\sqrt x}$ and the second gives
$\frac{1}{2\sqrt{x-1}}\cdot\frac{1}{x}=\frac{1}{2x\sqrt{x-1}}$, as required.

:::

:::

::: {.pf-step #seven}

$\displaystyle\int\frac{x}{\sqrt[3]{x+1}}\,dx=\frac35(x+1)^{5/3}-\frac32(x+1)^{2/3}+C$.

::: pf-proof

With $u=x+1$, $x=u-1$, $dx=du$, so the integral is
$\int(u^{2/3}-u^{-1/3})du=\frac35u^{5/3}-\frac32u^{2/3}+C$, which gives the
stated form; differentiating gives
$(u^{2/3}-u^{-1/3})\frac{du}{dx}=(x+1)^{2/3}-(x+1)^{-1/3}=\frac{x+1-1}{(x+1)^{1/3}}=\frac{x}{\sqrt[3]{x+1}}$.

:::

:::

::: {.pf-step #eight}

$\displaystyle\int\frac{dx}{x\sqrt{4x-1}}=2\arctan\sqrt{4x-1}+C$.

::: pf-proof

With $u=\sqrt{4x-1}$, $u^2=4x-1$, $x=\frac{u^2+1}{4}$ and
$dx=\frac{u\,du}{2}$, so the integral is
$\int\frac{u\,du/2}{\frac{u^2+1}{4}u}=\int\frac{2\,du}{u^2+1}=2\arctan u+C$.
Differentiating gives
$\frac{2}{1+(4x-1)}\cdot\frac{4}{2\sqrt{4x-1}}=\frac{1}{x\sqrt{4x-1}}$.

:::

:::

::: {.pf-step #nine}

$\displaystyle\int\frac{2\,dx}{x\sqrt{25x^4-1}}=\arctan\sqrt{25x^4-1}+C$.

::: pf-proof

Let $v=\sqrt{25x^4-1}$, so that $v^2+1=25x^4$ and
$\frac{dv}{dx}=\frac{100x^3}{2v}=\frac{50x^3}{v}$. Then $\frac{d}{dx}\arctan
v=\frac{50x^3}{v(1+v^2)}=\frac{50x^3}{v\cdot25x^4}=\frac{2}{xv}$, which is the
integrand, so the stated function is a primitive; no substitution is needed
beyond this verification.

:::

:::

::: {.pf-step #ten}

$\displaystyle\int\frac{dx}{\sqrt x\sqrt{1-4x}}=\arcsin(2\sqrt x)+C$ on
$0<x<\frac14$, and there it equals $\frac12\arcsin(8x-1)+C'$ for another
constant.

::: pf-proof

With $u=2\sqrt x$, $du=\frac{dx}{\sqrt x}$ and $1-4x=1-u^2$, so the integral
is $\int\frac{du}{\sqrt{1-u^2}}=\arcsin u+C$, and $u=2\sqrt x$; on the stated
interval $0<u<1$ and the square root is real. Differentiating gives
$\frac{2}{2\sqrt x}\cdot\frac{1}{\sqrt{1-4x}}$. For the second form, put
$\theta=\arcsin(2\sqrt x)$; then $\cos2\theta=1-2\sin^2\theta=1-8x$, so
$2\theta=\arccos(1-8x)=\frac\pi2-\arcsin(1-8x)=\frac\pi2+\arcsin(8x-1)$,
giving $\theta=\frac\pi4+\frac12\arcsin(8x-1)$.

:::

:::

::: {.pf-step #eleven}

$\displaystyle\int\frac{6-2x}{\sqrt{9-x^2}}\,dx=6\arcsin\left(\frac
x3\right)+2\sqrt{9-x^2}+C$ on $\abs x<3$.

::: pf-proof

Splitting the integral, $\int\frac{6\,dx}{\sqrt{9-x^2}}=6\arcsin\frac x3$ by
the substitution $x=3\sin\theta$, and
$\int\frac{-2x\,dx}{\sqrt{9-x^2}}=2\sqrt{9-x^2}$ because
$\frac{d}{dx}2\sqrt{9-x^2}=\frac{-2x}{\sqrt{9-x^2}}$. Differentiating the sum
gives
$\frac{6}{\sqrt{9-x^2}}-\frac{2x}{\sqrt{9-x^2}}=\frac{6-2x}{\sqrt{9-x^2}}$,
which is the integrand.

:::

:::

::: {.pf-step #twelve}

$\displaystyle\int\frac{dx}{\sqrt{x\sqrt x-x^2}}=4\arcsin(x^{1/4})+C$ on
$0<x<1$.

::: pf-proof

On the stated interval $x\sqrt x-x^2=x^{3/2}(1-\sqrt x)>0$, and $\sqrt{x\sqrt
x-x^2}=x^{3/4}\sqrt{1-\sqrt x}$ because $x^{3/2}=(x^{3/4})^2$. With
$u=x^{1/4}$, $x=u^4$, $dx=4u^3du$ and $x^{3/4}=u^3$, so the integrand is
$\frac{4u^3du}{u^3\sqrt{1-u^2}}=\frac{4du}{\sqrt{1-u^2}}$, whose primitive is
$4\arcsin u+C$. Differentiating the answer gives
$\frac{4}{4x^{3/4}}\cdot\frac{1}{\sqrt{1-\sqrt
x}}=\frac{1}{x^{3/4}\sqrt{1-\sqrt x}}$, which is the integrand.

:::

:::

:::


:::
