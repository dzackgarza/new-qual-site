---
schema: qual/card@1
id: P-PV5GI
kind: problem
title: Integrals of $\frac{\sqrt{1+\ln x}}{x\ln x}$, $\frac{7-\ln x}{x(3+\ln x)}$,
  $\frac{\sec^2 x}{1+\tan x}$, $\frac{\sin x}{\sqrt{4-\cos^2 x}}$, and $\frac{\sec^2
  x}{\sqrt{9-\tan^2 x}}$
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
  note: Corrected the sign of the final arcsine antiderivative and restored absolute values/constants where required.
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
    its answer: all five substitutions and primitives, each checked by differentiating the answer, with the partial fraction decompositions verified by multiplying out
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Five substitutions, with each primitive verified by differentiation.
---

::: {.problem}
Evaluate the five antiderivatives
$$
\int\frac{\sqrt{1+\ln x}}{x\ln x}\,dx,
\quad
\int\frac{7-\ln x}{x(3+\ln x)}\,dx,
$$
$$
\int\frac{\sec^2x}{1+\tan x}\,dx,
\quad
\int\frac{\sin x}{\sqrt{4-\cos^2x}}\,dx,
\quad
\int\frac{\sec^2x}{\sqrt{9-\tan^2x}}\,dx,
$$
on intervals where the displayed expressions are real and defined.
:::

::: {.solution}

Each part is integrated on an interval on which its integrand is continuous;
in particular the denominators in the first two parts are nonzero there.

::: pf

::: {.pf-step #first}

$\displaystyle\int\frac{\sqrt{1+\ln x}}{x\ln x}\,dx=2\sqrt{1+\ln
x}+\ln\abs{\frac{\sqrt{1+\ln x}-1}{\sqrt{1+\ln x}+1}}+C$.

::: pf-proof

Put $u=\sqrt{1+\ln x}$, so $u^2=1+\ln x$, $\ln x=u^2-1$ and
$2u\,du=\frac{dx}{x}$. Then $\frac{\sqrt{1+\ln x}}{x\ln
x}dx=\frac{u\cdot2u\,du}{u^2-1}=\frac{2u^2}{u^2-1}du$, and
$\frac{2u^2}{u^2-1}=2+\frac{2}{u^2-1}=2+\frac{1}{u-1}-\frac{1}{u+1}$.
Integrating term by term gives $2u+\ln\abs{u-1}-\ln\abs{u+1}+C$, which is the
stated form since $u>0$; it is required that $u\ne1$, that is $\ln x\ne0$.

:::

:::

::: {.pf-step #second}

$\displaystyle\int\frac{7-\ln x}{x(3+\ln x)}\,dx=-\ln x+10\ln\abs{3+\ln x}+C$.

::: pf-proof

With $u=3+\ln x$, $du=\frac{dx}{x}$ and $\ln x=u-3$, so $\frac{7-\ln x}{3+\ln
x}du=\frac{7-(u-3)}{u}du=\frac{10-u}{u}du=\left(\frac{10}{u}-1\right)du$.
Integrating gives $10\ln\abs u-u+C=10\ln\abs{3+\ln x}-3-\ln x+C$, and
absorbing the constant $-3$ gives the stated form.

:::

:::

::: {.pf-step #third}

$\displaystyle\int\frac{\sec^2x}{1+\tan x}\,dx=\ln\abs{1+\tan x}+C$.

::: pf-proof

With $u=1+\tan x$, $du=\sec^2x\,dx$, so the integral is
$\int\frac{du}{u}=\ln\abs u+C$; directly $\frac{d}{dx}\ln\abs{1+\tan
x}=\frac{\sec^2x}{1+\tan x}$.

:::

:::

::: {.pf-step #fourth}

$\displaystyle\int\frac{\sin x}{\sqrt{4-\cos^2x}}\,dx=-\arcsin\left(\frac{\cos
x}{2}\right)+C$.

::: pf-proof

With $u=\frac{\cos x}{2}$, $du=-\frac12\sin x\,dx$, so $\sin x\,dx=-2du$, and
$\sqrt{4-\cos^2x}=2\sqrt{1-u^2}$; hence the integrand is
$\frac{-2du}{2\sqrt{1-u^2}}=-\frac{du}{\sqrt{1-u^2}}$, whose primitive is
$-\arcsin u+C$. Directly, $\frac{d}{dx}\left(-\arcsin\frac{\cos
x}{2}\right)=-\frac{1}{\sqrt{1-\cos^2x/4}}\cdot\left(-\frac{\sin
x}{2}\right)=\frac{\sin x}{\sqrt{4-\cos^2x}}$.

:::

:::

::: {.pf-step #fifth}

$\displaystyle\int\frac{\sec^2x}{\sqrt{9-\tan^2x}}\,dx=\arcsin\left(\frac{\tan
x}{3}\right)+C$.

::: pf-proof

With $u=\frac{\tan x}{3}$, $du=\frac13\sec^2x\,dx$, so $\sec^2x\,dx=3du$, and
$\sqrt{9-\tan^2x}=3\sqrt{1-u^2}$; the integrand becomes
$\frac{3du}{3\sqrt{1-u^2}}=\frac{du}{\sqrt{1-u^2}}$, whose primitive is
$\arcsin u+C$. Directly, $\frac{d}{dx}\arcsin\frac{\tan
x}{3}=\frac{1}{\sqrt{1-\tan^2x/9}}\cdot\frac{\sec^2x}{3}=\frac{\sec^2x}{\sqrt{9-\tan^2x}}$.

:::

:::

:::


:::
