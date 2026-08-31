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
---

::: problem
13. $\displaystyle \int_{0}^{1} \frac {1}{\sqrt {x(1-x)}} ~dx = 2 \sin ^{-1} (\sqrt {x}) |_{0}^{1} = \color {blue} {\pi}$

- **Solution:** $u = \sqrt {x}$, $du = \frac {1}{2 \sqrt {x}} ~dx$

- **Solution:** $\frac {1}{\sqrt {x(1-x)}} ~dx = \frac {2}{\sqrt {1 - u^2}} ~du$

  1. $\displaystyle \int_{e^{\frac {1}{2}}}^{e^{\frac {3}{4}}} \frac {1}{x\sqrt {\ln(x)(1-\ln(x))}} ~dx = \color {blue} {\frac {\pi}{6}}$

  - **Solution:** $u = \ln (x)$, $du = \frac {1}{x} ~dx$

  - **Solution:** $\int_{e^{\frac {1}{2}}}^{e^{\frac {3}{4}}} \frac {1}{x\sqrt {\ln(x)(1-\ln(x))}} ~dx = \int_{\frac {1}{2}}^{\frac {3}{4}} \frac {1}{\sqrt {x(1-x)}} ~dx = 2 \sin ^{-1} (\sqrt {x}) |_{\frac {1}{2}}^{\frac {3}{4}} = 2(\frac {\pi}{3} - \frac {\pi}{4})$

  - **Used 2019**, *Unsolved*

14. $\displaystyle \int \frac {x}{1-x^2 + \sqrt {1- x^2}} ~dx = \color {blue} {- \ln (\sqrt {1-x^2}+1)}$

- **Solution:** $u^2 = 1 - x^2$, $u ~du = - x ~dx$

- **Solution:** $\frac {x}{1-x^2 + \sqrt {1- x^2}} ~dx = \frac {1}{1-x^2 + \sqrt {1- x^2}} \cdot x ~dx = \frac {1}{u^2 + u} \cdot (-u) ~du = - \frac {1}{u + 1} ~du$

15. $\displaystyle \int_{1}^{\infty} \frac {1}{x(x^2+1)} ~dx = \frac {1}{2} \ln (\frac {1}{x^2} + 1) |_{1}^{\infty} = \color {blue} {\frac {1}{2} \ln (2)}$

- **Solution:** $u = \frac {1}{x^2} + 1​$, $du = -2 \frac {1}{x^3} ~dx​$

- **Solution:** $\frac {1}{x(x^2+1)} ~dx = \frac {1}{(\frac {1}{x^2} + 1)} \cdot \frac {1}{x^3} ~dx = - \frac {1}{2u} du$

- **Used 2019**
:::

::: {.solution}
**Goal:** Evaluate the following integrals: (a) $\int_0^1 \frac{1}{\sqrt{x(1-x)}} \, dx$ and $\int_{e^{1/2}}^{e^{3/4}} \frac{1}{x\sqrt{\ln x(1-\ln x)}} \, dx$.
(b) $\int \frac{x}{1-x^2+\sqrt{1-x^2}} \, dx$.
(c) $\int_1^\infty \frac{1}{x(x^2+1)} \, dx$.

<1>1. $\int_0^1 \frac{1}{\sqrt{x(1-x)}} \, dx = \pi$.
::: {.proof}
<2>1. Substitute $u = \sqrt{x} \implies x = u^2, dx = 2u \, du$.
:::
<2>2. The integral becomes: $$\int_0^1 \frac{2u}{\sqrt{u^2(1-u^2)}} \, du = \int_0^1 \frac{2}{\sqrt{1-u^2}} \, du = [2\arcsin(u)]_0^1 = 2\arcsin(1) - 2\arcsin(0) = 2\left(\frac{\pi}{2}\right) - 0 = \pi.$$ <2>3. For $\int_{e^{1/2}}^{e^{3/4}} \frac{1}{x\sqrt{\ln x(1-\ln x)}} \, dx$, substitute $t = \ln(x) \implies dt = \frac{1}{x}dx$: $$\int_{1/2}^{3/4} \frac{1}{\sqrt{t(1-t)}} \, dt = [2\arcsin(\sqrt{t})]_{1/2}^{3/4} = 2\arcsin(\sqrt{3}/2) - 2\arcsin(1/\sqrt{2}) = 2\left(\frac{\pi}{3} - \frac{\pi}{4}\right) = \frac{\pi}{6}.$$

<1>2. $\int \frac{x}{1-x^2+\sqrt{1-x^2}} \, dx = -\ln(\sqrt{1-x^2}+1) + C$.
::: {.proof}
<2>1. Substitute $u = \sqrt{1-x^2} \implies u^2 = 1-x^2, u \, du = -x \, dx$.
:::
<2>2. Transforming the integrand: $$\int \frac{1}{u^2 + u} (-u \, du) = -\int \frac{u}{u(u+1)} \, du = -\int \frac{1}{u+1} \, du = -\ln|u+1| + C.$$ <2>3. Substituting back $u = \sqrt{1-x^2}$: $-\ln(\sqrt{1-x^2}+1) + C$.

<1>3. $\int_1^\infty \frac{1}{x(x^2+1)} \, dx = \frac{1}{2}\ln(2)$.
::: {.proof}
<2>1. Partial fractions: $\frac{1}{x(x^2+1)} = \frac{1}{x} - \frac{x}{x^2+1}$.
:::
<2>2. Antiderivative: $\ln|x| - \frac{1}{2}\ln(x^2+1) = \frac{1}{2}\ln\left(\frac{x^2}{x^2+1}\right) = -\frac{1}{2}\ln\left(1 + \frac{1}{x^2}\right)$.
<2>3. Evaluating from $1$ to $\infty$: $$\lim_{b \to \infty} \left[-\frac{1}{2}\ln\left(1 + \frac{1}{b^2}\right)\right] - \left(-\frac{1}{2}\ln(1 + 1)\right) = 0 + \frac{1}{2}\ln(2) = \frac{1}{2}\ln(2).$$ Q.E.D.
:::
