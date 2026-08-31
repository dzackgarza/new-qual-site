---
schema: qual/card@1
id: P-RASP04B
kind: problem
title: "Computation of series-integral and double integral"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Compute the values of the following two expressions.
You must justify your answers.

(a) $\displaystyle\sum_{n=0}^{\infty} \int_0^\infty e^{-2x} \frac{(-1)^n}{(2n+1)!} x^{2n+1}\,dx.$

(b) $\displaystyle\int_0^\infty \left(\int_0^\infty x^2 e^{-x^2} \sin(x^2) e^{-yx}\,dx\right)dy.$

You may find the following integration formula useful:
$$
\int e^{-ax}\sin x\,dx = -\frac{1}{a^2+1} e^{-ax}[\cos x + a\sin x] + C.
$$
:::

::: {.solution}
**(a).**

<1>1. $\int_0^\infty e^{-2x} x^{2n+1}\,dx = \frac{(2n+1)!}{2^{2n+2}}$.
::: {.proof}
$\int_0^\infty e^{-ax} x^m\,dx = \frac{m!}{a^{m+1}}$ with $a = 2$, $m = 2n+1$.
:::

<1>2. Hence the summand is $\frac{(-1)^n}{(2n+1)!} \cdot \frac{(2n+1)!}{2^{2n+2}} = \frac{(-1)^n}{2^{2n+2}}$.
::: {.proof}
<1>1.
:::

<1>3. Therefore the sum is $\sum_{n=0}^{\infty} \frac{(-1)^n}{2^{2n+2}} = \frac{1}{4}\sum_{n=0}^{\infty} \left(-\frac{1}{4}\right)^n = \frac{1}{4} \cdot \frac{1}{1 + 1/4} = \frac{1}{4} \cdot \frac{4}{5} = \frac{1}{5}$.
::: {.proof}
geometric series.
:::

<1>4. Hence the value of (a) is $\frac{1}{5}$.
::: {.proof}
<1>3.
:::

**(b).**

<1>1. By Fubini (the integrand is nonnegative... actually it is not, but it is absolutely integrable), swap the order of integration:
$$\int_0^\infty \int_0^\infty x^2 e^{-x^2}\sin(x^2) e^{-yx}\,dx\,dy = \int_0^\infty x^2 e^{-x^2}\sin(x^2)\left(\int_0^\infty e^{-yx}\,dy\right)dx.$$
::: {.proof}
Fubini's theorem.
:::

<1>2. $\int_0^\infty e^{-yx}\,dy = \frac{1}{x}$.
::: {.proof}
elementary integral.
:::

<1>3. Hence the integral is $\int_0^\infty x e^{-x^2}\sin(x^2)\,dx$.
::: {.proof}
<1>1 and <1>2.
:::

<1>4. Substitute $u = x^2$, $du = 2x\,dx$: $\int_0^\infty x e^{-x^2}\sin(x^2)\,dx = \frac{1}{2}\int_0^\infty e^{-u}\sin u\,du$.
::: {.proof}
change of variables.
:::

<1>5. $\int_0^\infty e^{-u}\sin u\,du = \frac{1}{2}$.
::: {.proof}
using the given formula (or $\int_0^\infty e^{-u}\sin u\,du = \frac{1}{1^2 + 1} = \frac{1}{2}$).
:::

<1>6. Hence the value of (b) is $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>4 (a) and <1>6 (b).
:::
:::
