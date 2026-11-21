---
schema: qual/card@1
id: P-B6FMH
kind: problem
title: Integrals of $1/\sqrt{x(1-x)}$, $x/(1-x^2+\sqrt{1-x^2})$, and $1/(x(x^2+1))$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Improper Integrals
  - Trigonometric Substitution
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
    The nine leaf steps of the three integrals asserted their claim with no proof body; each now
    carries one. No claim and no value is changed: $\pi$, $\pi/6$, $-\ln(\sqrt{1-x^2}+1)+C$ and
    $\frac12\ln2$ stand as they were. Cited by number only: the derivative of $\arcsin$, the
    fundamental theorem of calculus with the endpoint limits of the improper integrals, the
    implicit differentiation of $u=\sqrt{1-x^2}$, and the standard antiderivatives
    $\int dx/x=\ln\abs x$ and $\int x\,dx/(x^2+1)=\frac12\ln(x^2+1)$. Checked: that
    $\sqrt{u^2}=u$ on the range of the substitution, that the partial-fraction identity
    assembles over the common denominator, that the two logarithmic forms agree, and that the
    upper limit tends to $-\frac12\ln1=0$.
---

::: {.problem}
Evaluate:

(a) $\displaystyle\int_0^1\frac{dx}{\sqrt{x(1-x)}}$, and then $\displaystyle\int_{e^{1/2}}^{e^{3/4}}\frac{dx}{x\sqrt{\ln x\,(1-\ln x)}}$;

(b) $\displaystyle\int\frac{x}{1-x^2+\sqrt{1-x^2}}\,dx$ on $(-1,1)$;

(c) $\displaystyle\int_1^\infty\frac{dx}{x(x^2+1)}$.
:::

::: {.solution}
::: pf

::: pf-step
$\int_0^1 \frac{1}{\sqrt{x(1-x)}} \, dx = \pi$ and $\int_{e^{1/2}}^{e^{3/4}} \frac{1}{x\sqrt{\ln x(1-\ln x)}} \, dx = \frac{\pi}{6}$.

::: pf-proof

::: pf-step
Substitute $u = \sqrt{x} \implies x = u^2, dx = 2u \, du$.

::: pf-proof
$u=\sqrt x$ is continuous and increasing on $[0,1]$ with derivative $1/(2\sqrt x)$ on $(0,1]$; inverting gives $x=u^2$ and differentiating, $dx=2u\,du$. The endpoints map to $u=0$ and $u=1$.
:::

:::

::: pf-step
The integral becomes: $$\int_0^1 \frac{2u}{\sqrt{u^2(1-u^2)}} \, du = \int_0^1 \frac{2}{\sqrt{1-u^2}} \, du = [2\arcsin(u)]_0^1 = 2\arcsin(1) - 2\arcsin(0) = 2\left(\frac{\pi}{2}\right) - 0 = \pi.$$

::: pf-proof
With $x=u^2$ we have $1-x=1-u^2$, so $\sqrt{x(1-x)}=\sqrt{u^2(1-u^2)}=u\sqrt{1-u^2}$ for $u\ge0$, and the differential contributes the factor $2u$, which cancels the $u$; hence the integrand is $2/\sqrt{1-u^2}$. The derivative of $\arcsin u$ is $1/\sqrt{1-u^2}$ on $(-1,1)$, so $2\arcsin u$ is an antiderivative; the integrand has integrable singularities at both endpoints, and the fundamental theorem applies by taking the limit of the integral over $[\varepsilon,1-\varepsilon]$ and using that $\arcsin$ is continuous at $\pm1$. Finally $\arcsin1=\pi/2$ and $\arcsin0=0$.
:::

:::

::: pf-step
For $\int_{e^{1/2}}^{e^{3/4}} \frac{1}{x\sqrt{\ln x(1-\ln x)}} \, dx$, substitute $t = \ln(x) \implies dt = \frac{1}{x}dx$: $$\int_{1/2}^{3/4} \frac{1}{\sqrt{t(1-t)}} \, dt = [2\arcsin(\sqrt{t})]_{1/2}^{3/4} = 2\arcsin(\sqrt{3}/2) - 2\arcsin(1/\sqrt{2}) = 2\left(\frac{\pi}{3} - \frac{\pi}{4}\right) = \frac{\pi}{6}.$$

::: pf-proof
$\ln$ is increasing, so the endpoints $x=e^{1/2}$ and $x=e^{3/4}$ become $t=1/2$ and $t=3/4$, and $dt=dx/x$ absorbs the factor $1/x$. An antiderivative of $1/\sqrt{t(1-t)}$ on $(0,1)$ is $2\arcsin\sqrt t$, since differentiating gives $\frac{2}{\sqrt{1-t}}\cdot\frac{1}{2\sqrt t}=\frac{1}{\sqrt{t(1-t)}}$. The values are $\arcsin(\sqrt3/2)=\pi/3$ and $\arcsin(1/\sqrt2)=\pi/4$, so the difference is $2(\pi/3-\pi/4)=\pi/6$.
:::

:::

:::

:::

::: pf-step
$\int \frac{x}{1-x^2+\sqrt{1-x^2}} \, dx = -\ln(\sqrt{1-x^2}+1) + C$.

::: pf-proof

::: pf-step
Substitute $u = \sqrt{1-x^2} \implies u^2 = 1-x^2, u \, du = -x \, dx$.

::: pf-proof
Squaring $u=\sqrt{1-x^2}$ gives $u^2=1-x^2$; differentiating implicitly, $2u\,du=-2x\,dx$, that is $u\,du=-x\,dx$. On the interval where the integrand is defined, $1-x^2>0$, so $u>0$ and the branch of the square root is the positive one.
:::

:::

::: pf-step
Transforming the integrand: $$\int \frac{1}{u^2 + u} (-u \, du) = -\int \frac{u}{u(u+1)} \, du = -\int \frac{1}{u+1} \, du = -\ln\abs{u+1} + C.$$

::: pf-proof
The denominator is $1-x^2+\sqrt{1-x^2}=u^2+u$, the numerator $x\,dx$ is $-u\,du$ by step 2.1, and the $u$ cancels between numerator and denominator because $u>0$. Then $-\int du/(u+1)=-\ln\abs{u+1}+C$, since the derivative of $\ln\abs{u+1}$ is $1/(u+1)$ for $u\ne-1$.
:::

:::

::: pf-step
Substituting back $u = \sqrt{1-x^2}$: $-\ln(\sqrt{1-x^2}+1) + C$.

::: pf-proof
$u+1=\sqrt{1-x^2}+1>0$, so the absolute value may be dropped; replacing $u$ by its definition in the antiderivative of step 2.2 gives the displayed family, and two antiderivatives on an interval differ by a constant, which $C$ absorbs.
:::

:::

:::

:::

::: pf-step
$\int_1^\infty \frac{1}{x(x^2+1)} \, dx = \frac{1}{2}\ln(2)$.

::: pf-proof

::: pf-step
Partial fractions: $\frac{1}{x(x^2+1)} = \frac{1}{x} - \frac{x}{x^2+1}$.

::: pf-proof
Put the right side over the common denominator $x(x^2+1)$: $\frac{x^2+1}{x(x^2+1)}-\frac{x^2}{x(x^2+1)}=\frac{1}{x(x^2+1)}$, which is the left side.
:::

:::

::: pf-step
Antiderivative: $\ln\abs{x} - \frac{1}{2}\ln(x^2+1) = \frac{1}{2}\ln\left(\frac{x^2}{x^2+1}\right) = -\frac{1}{2}\ln\left(1 + \frac{1}{x^2}\right)$.

::: pf-proof
$\int dx/x=\ln\abs x$ and $\int x\,dx/(x^2+1)=\frac12\ln(x^2+1)$, the second by the substitution $w=x^2+1$, $dw=2x\,dx$. Combining the two logarithms with $\ln a-\frac12\ln b=\frac12\ln(a^2/b)$ for $a>0$ gives $\frac12\ln\bigl(x^2/(x^2+1)\bigr)$, and dividing numerator and denominator by $x^2$ turns it into $-\frac12\ln(1+1/x^2)$.
:::

:::

::: pf-step
Evaluating from $1$ to $\infty$: $$\lim_{b \to \infty} \left[-\frac{1}{2}\ln\left(1 + \frac{1}{b^2}\right)\right] - \left(-\frac{1}{2}\ln(1 + 1)\right) = 0 + \frac{1}{2}\ln(2) = \frac{1}{2}\ln(2).$$

::: pf-proof
The improper integral is the limit of $\int_1^b$ as $b\to\infty$, and by step 3.2 that is the difference of the antiderivative at $b$ and at $1$. As $b\to\infty$ we have $1+1/b^2\to1$, so by continuity of $\ln$ at $1$ the first term tends to $-\frac12\ln1=0$; at the lower endpoint the value is $-\frac12\ln2$, and subtracting it gives $+\frac12\ln2$.
:::

:::

:::

:::

:::
:::
