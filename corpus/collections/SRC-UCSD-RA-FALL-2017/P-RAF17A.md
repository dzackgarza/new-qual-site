---
schema: qual/card@1
id: P-RAF17A
kind: problem
title: "Limits and integrals involving exponentials, series, and iterated integrals"
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
  note: Checked against Problem 1 of the official UCSD Fall 2017 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Added the missing Fatou, monotone-convergence, and Tonelli justifications and normalized legacy solution/proof blocks.
---

::: {.problem}
In each case below find $L$ (allowing for values of $\pm\infty$) and justify the calculations:

(a) $L = \lim_{n \to \infty} \int_0^{\sqrt{\pi}} e^{-n\cos(x^2)}\,dx.$

(b) $L = \lim_{N \to \infty} \sum_{k=0}^{N} \int_0^N \frac{x^k}{k!}\,e^{-2x}\,dx.$

(c) $L = \int_0^\infty \left[\int_0^\infty e^{-y/x}\,e^{-x^2/2}\,dx\right]dy.$
:::

::: {.solution}
**(a).**

::: pf

::: {.pf-step #p1-s1}
On $[0, \sqrt{\pi}]$, $\cos(x^2) \ge 0$ for $x^2 \le \pi/2$ and $\cos(x^2) < 0$ for $x^2 > \pi/2$.

::: pf-proof
$\cos$ is positive on $[0, \pi/2)$ and negative on $(\pi/2, \pi]$.
:::

:::

::: {.pf-step #p1-s2}
Hence $e^{-n\cos(x^2)} \to 0$ pointwise on $\{x : \cos(x^2) > 0\}$ and $\to \infty$ on $\{x : \cos(x^2) < 0\}$.

::: pf-proof
step [](#p1-s1){.pf-ref}.
:::

:::

::: {.pf-step #p1-s3}
The integrand is dominated by $1$ on $\{x : \cos(x^2) \ge 0\}$ (where $e^{-n\cos} \le 1$), and on $\{x : \cos(x^2) < 0\}$ it grows.

::: pf-proof
step [](#p1-s2){.pf-ref}.
:::

:::

::: {.pf-step #p1-s4}
The contribution from the region where $\cos(x^2)\ge0$ tends to $0$, while the contribution from the region where $\cos(x^2)<0$ tends to $+\infty$.

::: pf-proof
On the first region, dominated convergence applies with dominating function $1$. On the second region, which has positive measure, Fatou's lemma gives
\[
\liminf_{n\to\infty}\int_{\{\cos(x^2)<0\}}e^{-n\cos(x^2)}\,dx
\ge
\int_{\{\cos(x^2)<0\}}\liminf_{n\to\infty}e^{-n\cos(x^2)}\,dx
=\infty.
\]
:::

:::

::: {.pf-step #p1-s5}
Hence $L = +\infty$.

::: pf-proof
step [](#p1-s4){.pf-ref}.
:::

:::

:::

**(b).**

::: pf

::: {.pf-step #p2-s1}
$\sum_{k=0}^{N} \frac{x^k}{k!} \to e^x$ as $N \to \infty$.

::: pf-proof
power series of the exponential.
:::

:::

::: pf-step
Hence $\sum_{k=0}^{N} \int_0^N \frac{x^k}{k!} e^{-2x}\,dx = \int_0^N \left(\sum_{k=0}^{N} \frac{x^k}{k!}\right) e^{-2x}\,dx$.

::: pf-proof
step [](#p2-s1){.pf-ref} and linearity.
:::

:::

::: {.pf-step #p2-s3}
As $N \to \infty$, this tends to $\int_0^\infty e^x e^{-2x}\,dx = \int_0^\infty e^{-x}\,dx = 1$.

::: pf-proof
Define
\[
h_N(x)=\mathbf1_{[0,N]}(x)e^{-2x}\sum_{k=0}^N\frac{x^k}{k!}.
\]
Then $h_N\uparrow e^{-x}$ pointwise on $[0,\infty)$, so the Monotone Convergence Theorem gives the claimed limit.
:::

:::

::: {.pf-step #p2-s4}
Hence $L = 1$.

::: pf-proof
step [](#p2-s3){.pf-ref}.
:::

:::

:::

**(c).**

::: pf

::: {.pf-step #p3-s1}
Tonelli's theorem permits reversing the order of integration, and $\int_0^\infty e^{-y/x}\,dy=x$ for fixed $x>0$.

::: pf-proof
The integrand is nonnegative, so Tonelli applies without any prior integrability assumption. The inner integral equals $x$ by the change of variables $u=y/x$.
:::

:::

::: {.pf-step #p3-s2}
Hence $L = \int_0^\infty x e^{-x^2/2}\,dx$.

::: pf-proof
step [](#p3-s1){.pf-ref}.
:::

:::

::: {.pf-step #p3-s3}
$\int_0^\infty x e^{-x^2/2}\,dx = 1$ (substituting $u = x^2/2$, $du = x\,dx$).

::: pf-proof
$\int_0^\infty x e^{-x^2/2}\,dx = \int_0^\infty e^{-u}\,du = 1$.
:::

:::

::: {.pf-step #p3-s4}
Hence $L = 1$.

::: pf-proof
step [](#p3-s2){.pf-ref} and step [](#p3-s3){.pf-ref}.
:::

:::

::: pf-qed
step [](#p1-s5){.pf-ref} (a), step [](#p2-s4){.pf-ref} (b), step [](#p3-s4){.pf-ref} (c).
:::

:::
:::
