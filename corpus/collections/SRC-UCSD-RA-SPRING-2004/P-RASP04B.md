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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2004 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced an unsupported Fubini aside by an explicit absolute-integrability estimate and normalized legacy solution/proof blocks.
---

::: {.problem}
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

::: pf

::: {.pf-step #p1-s1}
$\int_0^\infty e^{-2x} x^{2n+1}\,dx = \frac{(2n+1)!}{2^{2n+2}}$.

::: pf-proof
$\int_0^\infty e^{-ax} x^m\,dx = \frac{m!}{a^{m+1}}$ with $a = 2$, $m = 2n+1$.
:::

:::

::: pf-step
Hence the summand is $\frac{(-1)^n}{(2n+1)!} \cdot \frac{(2n+1)!}{2^{2n+2}} = \frac{(-1)^n}{2^{2n+2}}$.

::: pf-proof
step [](#p1-s1){.pf-ref}.
:::

:::

::: {.pf-step #p1-s3}
Therefore the sum is $\sum_{n=0}^{\infty} \frac{(-1)^n}{2^{2n+2}} = \frac{1}{4}\sum_{n=0}^{\infty} \left(-\frac{1}{4}\right)^n = \frac{1}{4} \cdot \frac{1}{1 + 1/4} = \frac{1}{4} \cdot \frac{4}{5} = \frac{1}{5}$.

::: pf-proof
geometric series.
:::

:::

::: {.pf-step #p1-s4}
Hence the value of (a) is $\frac{1}{5}$.

::: pf-proof
step [](#p1-s3){.pf-ref}.
:::

:::

:::

**(b).**

::: pf

::: {.pf-step #p2-s1}
The integrand is absolutely integrable, so Fubini's theorem permits swapping the order of integration.

::: pf-proof
Indeed, by Tonelli's theorem,
\[
\begin{aligned}
&\int_0^\infty\int_0^\infty
\left|x^2e^{-x^2}\sin(x^2)e^{-yx}\right|\,dx\,dy\\
&=\int_0^\infty x^2e^{-x^2}|\sin(x^2)|
\left(\int_0^\infty e^{-yx}\,dy\right)dx\\
&=\int_0^\infty xe^{-x^2}|\sin(x^2)|\,dx
\le \int_0^\infty xe^{-x^2}\,dx
=\frac12<\infty.
\end{aligned}
\]
Hence Fubini applies, giving
$$\int_0^\infty \int_0^\infty x^2 e^{-x^2}\sin(x^2) e^{-yx}\,dx\,dy = \int_0^\infty x^2 e^{-x^2}\sin(x^2)\left(\int_0^\infty e^{-yx}\,dy\right)dx.$$
:::

:::

::: {.pf-step #p2-s2}
$\int_0^\infty e^{-yx}\,dy = \frac{1}{x}$.

::: pf-proof
elementary integral.
:::

:::

::: pf-step
Hence the integral is $\int_0^\infty x e^{-x^2}\sin(x^2)\,dx$.

::: pf-proof
step [](#p2-s1){.pf-ref} and step [](#p2-s2){.pf-ref}.
:::

:::

::: {.pf-step #p2-s4}
Substitute $u = x^2$, $du = 2x\,dx$: $\int_0^\infty x e^{-x^2}\sin(x^2)\,dx = \frac{1}{2}\int_0^\infty e^{-u}\sin u\,du$.

::: pf-proof
change of variables.
:::

:::

::: {.pf-step #p2-s5}
$\int_0^\infty e^{-u}\sin u\,du = \frac{1}{2}$.

::: pf-proof
using the given formula (or $\int_0^\infty e^{-u}\sin u\,du = \frac{1}{1^2 + 1} = \frac{1}{2}$).
:::

:::

::: {.pf-step #p2-s6}
Hence the value of (b) is $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.

::: pf-proof
step [](#p2-s4){.pf-ref} and step [](#p2-s5){.pf-ref}.
:::

:::

::: pf-qed
step [](#p1-s4){.pf-ref} (a) and step [](#p2-s6){.pf-ref} (b).
:::

:::
:::
