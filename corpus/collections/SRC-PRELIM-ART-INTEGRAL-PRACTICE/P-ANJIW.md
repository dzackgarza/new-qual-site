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
---

::: problem
2. $\displaystyle \int \frac {xe^x\ln x - e^x}{x\ln^2 x} = \color {blue} {\frac {e^x}{\ln x}}$

- **Used 2018**

3. $\displaystyle \int (\tan(x) + \cot(x))^2 ~dx = \color {blue} {\tan(x)-\cot(x)}$

- **Solution:** $\sin ^2 (x) + \cos ^2 (x) = 1$

- **Used 2018**
:::

::: {.solution}
**Goal:** Evaluate the indefinite integrals: (a) $\int \frac{x e^x \ln x - e^x}{x (\ln x)^2} \, dx$ (b) $\int (\tan x + \cot x)^2 \, dx$

<1>1. $\int \frac{x e^x \ln x - e^x}{x (\ln x)^2} \, dx = \frac{e^x}{\ln x} + C$.
Proof: <2>1. Recognize the integrand as the derivative of the quotient $g(x) = \frac{e^x}{\ln x}$.
<2>2. By the quotient rule: $$\frac{d}{dx}\left(\frac{e^x}{\ln x}\right) = \frac{\left(\frac{d}{dx} e^x\right) \ln x - e^x \left(\frac{d}{dx} \ln x\right)}{(\ln x)^2} = \frac{e^x \ln x - e^x \cdot \frac{1}{x}}{(\ln x)^2} = \frac{x e^x \ln x - e^x}{x (\ln x)^2}.$$ <2>3. Since the integrand is the exact derivative of $\frac{e^x}{\ln x}$, the antiderivative is $\frac{e^x}{\ln x} + C$.

<1>2. $\int (\tan x + \cot x)^2 \, dx = \tan(x) - \cot(x) + C$.
Proof: <2>1. Expand the square: $$(\tan x + \cot x)^2 = \tan^2 x + 2\tan x \cot x + \cot^2 x = \tan^2 x + 2 + \cot^2 x.$$ <2>2. Apply the Pythagorean trigonometric identities $\tan^2 x = \sec^2 x - 1$ and $\cot^2 x = \csc^2 x - 1$: $$\tan^2 x + 2 + \cot^2 x = (\sec^2 x - 1) + 2 + (\csc^2 x - 1) = \sec^2 x + \csc^2 x.$$ <2>3. Integrate term-by-term: $$\int (\sec^2 x + \csc^2 x) \, dx = \tan x - \cot x + C.$$ Q.E.D.
:::
