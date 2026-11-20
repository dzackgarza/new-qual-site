---
schema: qual/card@1
id: P-ANJIW
kind: problem
title: Antiderivatives of $\frac{xe^x\ln x-e^x}{x(\ln x)^2}$ and $(\tan x+\cot x)^2$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    All six leaf steps of the two antiderivatives asserted their claim with no proof body; each
    now carries a `pf-proof`, naming the quotient rule, the fundamental theorem of calculus, the
    two Pythagorean identities and the derivatives of $\tan$ and $\cot$. No claim was changed:
    both answers and both integrands stand as they were. Checked: the quotient-rule computation
    of part (a) term by term, including the multiplication of numerator and denominator by $x$,
    and the reduction $\tan^2+2+\cot^2=\sec^2+\csc^2$ of part (b) with $\int\csc^2=-\cot$. Not
    checked: the source sheet this practice set comes from is not in the checkout; the work is
    the card's own.
---

::: {.problem}
Evaluate, on intervals where the integrands are defined,

(a) $\displaystyle\int\frac{xe^x\ln x-e^x}{x(\ln x)^2}\,dx$;

(b) $\displaystyle\int(\tan x+\cot x)^2\,dx$.
:::

::: {.solution}

::: pf

::: pf-step

$\int \frac{x e^x \ln x - e^x}{x (\ln x)^2} \, dx = \frac{e^x}{\ln x} + C$.

::: pf-proof

Steps 1.1--1.3 identify the integrand as the derivative of $e^x/\ln x$ and read the antiderivative off.

::: pf-step

The integrand is the derivative of the quotient $g(x) = \frac{e^x}{\ln x}$.

::: pf-proof

On an interval where $\ln x$ is defined and nonzero, $e^x$ and $\ln x$ are differentiable and the denominator does not vanish, so the quotient $g=e^x/\ln x$ is differentiable there; step 1.2 computes $g'$ and finds the integrand.

:::

:::

::: pf-step

By the quotient rule: $$\frac{d}{dx}\left(\frac{e^x}{\ln x}\right) = \frac{\left(\frac{d}{dx} e^x\right) \ln x - e^x \left(\frac{d}{dx} \ln x\right)}{(\ln x)^2} = \frac{e^x \ln x - e^x \cdot \frac{1}{x}}{(\ln x)^2} = \frac{x e^x \ln x - e^x}{x (\ln x)^2}.$$

::: pf-proof

The quotient rule $(u/v)'=(u'v-uv')/v^2$ with $u=e^x$ and $v=\ln x$ gives $\bigl(e^x\ln x-e^x\cdot\frac1x\bigr)/(\ln x)^2$, using $(e^x)'=e^x$ and $(\ln x)'=1/x$. Multiplying numerator and denominator by $x\ne0$ turns it into $\frac{xe^x\ln x-e^x}{x(\ln x)^2}$, which is the integrand.

:::

:::

::: pf-step

Since the integrand is the exact derivative of $\frac{e^x}{\ln x}$, the antiderivative is $\frac{e^x}{\ln x} + C$.

::: pf-proof

Steps 1.1 and 1.2 show that $g=e^x/\ln x$ has derivative equal to the integrand on each interval of its domain. By the fundamental theorem of calculus, $\int g'=g+C$ on such an interval, and any two antiderivatives of the integrand on an interval differ by a constant.

:::

:::

:::

:::

::: pf-step

$\int (\tan x + \cot x)^2 \, dx = \tan(x) - \cot(x) + C$.

::: pf-proof

Steps 2.1--2.3 reduce the square to $\sec^2+\csc^2$ and integrate the two terms.

::: pf-step

Expand the square: $$(\tan x + \cot x)^2 = \tan^2 x + 2\tan x \cot x + \cot^2 x = \tan^2 x + 2 + \cot^2 x.$$

::: pf-proof

$(\tan x+\cot x)^2=\tan^2x+2\tan x\cot x+\cot^2x$ by the binomial expansion. Where both functions are defined, $\tan x\cot x=\frac{\sin x}{\cos x}\cdot\frac{\cos x}{\sin x}=1$, so the middle term is $2$.

:::

:::

::: pf-step

Apply the Pythagorean trigonometric identities $\tan^2 x = \sec^2 x - 1$ and $\cot^2 x = \csc^2 x - 1$: $$\tan^2 x + 2 + \cot^2 x = (\sec^2 x - 1) + 2 + (\csc^2 x - 1) = \sec^2 x + \csc^2 x.$$

::: pf-proof

Dividing $\sin^2x+\cos^2x=1$ by $\cos^2x$ gives $\tan^2x+1=\sec^2x$, that is $\tan^2x=\sec^2x-1$; dividing by $\sin^2x$ gives $1+\cot^2x=\csc^2x$, that is $\cot^2x=\csc^2x-1$. Substituting in step 2.1 gives $(\sec^2x-1)+2+(\csc^2x-1)=\sec^2x+\csc^2x$.

:::

:::

::: pf-step

Integrate term-by-term: $$\int (\sec^2 x + \csc^2 x) \, dx = \tan x - \cot x + C.$$

::: pf-proof

$\frac{d}{dx}\tan x=\sec^2x$ and $\frac{d}{dx}\cot x=-\csc^2x$, so $\tan x$ is an antiderivative of $\sec^2x$ and $-\cot x$ one of $\csc^2x$. The antiderivative is linear on an interval, so $\int(\sec^2x+\csc^2x)\,dx=\tan x-\cot x+C$ on any interval on which both $\tan$ and $\cot$ are defined.

:::

:::

:::

:::

:::
:::