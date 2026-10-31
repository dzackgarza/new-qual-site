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
(a) Evaluate $\displaystyle\int(\ln x)^2\,dx$ for $x>0$.

(b) Let $b\ne0$. Show that
$$
\int x^a e^{bx}\,dx=\frac1b x^a e^{bx}-\frac ab\int x^{a-1}e^{bx}\,dx,
$$
and use it to evaluate $\displaystyle\int xe^{2x}\,dx$, $\displaystyle\int x^3e^{-x}\,dx$, $\displaystyle\int_0^\infty x^3e^{-x}\,dx$, $\displaystyle\int x^2e^x\,dx$, $\displaystyle\int xe^{-x}\,dx$ and $\displaystyle\int_0^\infty x^3e^{-x^2}\,dx$.
:::

::: {.solution}

::: pf

::: pf-step

$\int (\ln x)^2 \, dx = x (\ln x)^2 - 2x \ln x + 2x + C$.

::: pf-proof

Integrate by parts, $\int u \, dv = uv - \int v \, du$, with $u = (\ln x)^2$ and $dv = dx$, so $du = \frac{2 \ln x}{x} \, dx$ and $v = x$:
$$\int (\ln x)^2 \, dx = x (\ln x)^2 - \int x \cdot \frac{2 \ln x}{x} \, dx = x (\ln x)^2 - 2 \int \ln x \, dx.$$
By parts again with $u = \ln x$, $dv = dx$, so $du = \frac{1}{x}\,dx$, $v = x$:
$$\int \ln x \, dx = x \ln x - \int x \cdot \frac{1}{x} \, dx = x \ln x - x + C_1.$$
Substituting,
$$\int (\ln x)^2 \, dx = x (\ln x)^2 - 2(x \ln x - x) + C = x (\ln x)^2 - 2x \ln x + 2x + C.$$

:::

:::

::: pf-step

For $b \neq 0$, the reduction formula $\int x^a e^{bx} \, dx = \frac{1}{b} x^a e^{bx} - \frac{a}{b} \int x^{a-1} e^{bx} \, dx$ holds.

::: pf-proof

By parts with $u = x^a \implies du = a x^{a-1} dx$, and $dv = e^{bx} dx \implies v = \frac{1}{b} e^{bx}$.

:::

:::

::: pf-step

The following cases of the reduction formula hold.

::: pf-proof

$\int x e^{2x} \, dx = \frac{1}{2} x e^{2x} - \frac{1}{4} e^{2x} + C = \frac{1}{4}(2x - 1)e^{2x} + C$.

$\int x^3 e^{-x} \, dx = -(x^3 + 3x^2 + 6x + 6)e^{-x} + C$.

$\int_0^\infty x^3 e^{-x} \, dx = \Gamma(4) = 3! = 6$.

With $t = x^2$, $dt = 2x\,dx$: $\int_0^\infty x^3 e^{-x^2} \, dx = \frac{1}{2} \int_0^\infty t e^{-t} \, dt = \frac{1}{2} \Gamma(2) = \frac{1}{2}$.

:::

:::

:::

:::
