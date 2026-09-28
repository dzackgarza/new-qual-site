---
schema: qual/card@1
id: P-2ALGH
kind: problem
title: $\int(\ln x)^2\,dx$ and the reduction formula for $\int x^a e^{bx}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Integration by Parts
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
3. $\displaystyle \int \ln ^2 (x) ~dx = \color{blue} {2 x - 2 x \ln (x) + x \ln ^2 (x)}​$

- **Solution:** $u = \ln ^2 (x)​$, $v = x​$, $du = \frac {2 \ln (x)}{x} ~dx​$, $dv = dx​$

- **Solution:** $x \ln ^2 (x) - \int x \cdot \frac {2 \ln (x)}{x} ~dx = x \ln ^2 (x) - 2(x \ln (x) - x)$

- **Used 2019**

4. $\displaystyle \int x^a e^{bx} ~dx = \frac {1}{b} x^a e^{bx} - \int \frac {a}{b} x^{a-1} e^{bx}$

   1. $\displaystyle \int xe^{2x} ~dx = \color {blue} {\frac {1}{4} (2x-1) e^{2x}}​$

   2. $\displaystyle \int x^3 e^{-x} ~dx = \color {blue} {- (x^3 + 3x^2 + 6x + 6) e^{-x}}$

   3. $\displaystyle \int_0^{\infty} x^3 e^{-x} ~dx = \color {blue} {6}​$

   4. $\displaystyle \int x^2e^x ~dx =\color {blue}{(x^2 - 2x + 2) e^x}​$

   - **Used 2018**

   5. $\displaystyle \int xe^{-x} ~dx = \color {blue} {- (x + 1) e^ {-x}}$

   6. $\displaystyle \int_{0}^{\infty} x^3e^{-x^2} ~dx = \color {blue} {\frac {1}{2}}​$
:::

::: {.solution}
<1>1. $\int (\ln x)^2 \, dx = x (\ln x)^2 - 2x \ln x + 2x + C$.
::: {.proof}
Integrate by parts, $\int u \, dv = uv - \int v \, du$, with $u = (\ln x)^2$ and $dv = dx$, so $du = \frac{2 \ln x}{x} \, dx$ and $v = x$:
$$\int (\ln x)^2 \, dx = x (\ln x)^2 - \int x \cdot \frac{2 \ln x}{x} \, dx = x (\ln x)^2 - 2 \int \ln x \, dx.$$
By parts again with $u = \ln x$, $dv = dx$, so $du = \frac{1}{x}\,dx$, $v = x$:
$$\int \ln x \, dx = x \ln x - \int x \cdot \frac{1}{x} \, dx = x \ln x - x + C_1.$$
Substituting,
$$\int (\ln x)^2 \, dx = x (\ln x)^2 - 2(x \ln x - x) + C = x (\ln x)^2 - 2x \ln x + 2x + C.$$
:::

<1>2. For $b \neq 0$, the reduction formula $\int x^a e^{bx} \, dx = \frac{1}{b} x^a e^{bx} - \frac{a}{b} \int x^{a-1} e^{bx} \, dx$ holds.
::: {.proof}
By parts with $u = x^a \implies du = a x^{a-1} dx$, and $dv = e^{bx} dx \implies v = \frac{1}{b} e^{bx}$.
:::

<1>3. The following cases of the reduction formula hold.
::: {.proof}
$\int x e^{2x} \, dx = \frac{1}{2} x e^{2x} - \frac{1}{4} e^{2x} + C = \frac{1}{4}(2x - 1)e^{2x} + C$.

$\int x^3 e^{-x} \, dx = -(x^3 + 3x^2 + 6x + 6)e^{-x} + C$.

$\int_0^\infty x^3 e^{-x} \, dx = \Gamma(4) = 3! = 6$.

With $t = x^2$, $dt = 2x\,dx$: $\int_0^\infty x^3 e^{-x^2} \, dx = \frac{1}{2} \int_0^\infty t e^{-t} \, dt = \frac{1}{2} \Gamma(2) = \frac{1}{2}$.
:::
:::
