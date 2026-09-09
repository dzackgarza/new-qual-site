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

::: problem
In each case below find $L$ (allowing for values of $\pm\infty$) and justify the calculations:

(a) $L = \lim_{n \to \infty} \int_0^{\sqrt{\pi}} e^{-n\cos(x^2)}\,dx.$

(b) $L = \lim_{N \to \infty} \sum_{k=0}^{N} \int_0^N \frac{x^k}{k!}\,e^{-2x}\,dx.$

(c) $L = \int_0^\infty \left[\int_0^\infty e^{-y/x}\,e^{-x^2/2}\,dx\right]dy.$
:::

::: solution
**(a).**

<1>1. On $[0, \sqrt{\pi}]$, $\cos(x^2) \ge 0$ for $x^2 \le \pi/2$ and $\cos(x^2) < 0$ for $x^2 > \pi/2$.
::: proof
$\cos$ is positive on $[0, \pi/2)$ and negative on $(\pi/2, \pi]$.
:::

<1>2. Hence $e^{-n\cos(x^2)} \to 0$ pointwise on $\{x : \cos(x^2) > 0\}$ and $\to \infty$ on $\{x : \cos(x^2) < 0\}$.
::: proof
<1>1.
:::

<1>3. The integrand is dominated by $1$ on $\{x : \cos(x^2) \ge 0\}$ (where $e^{-n\cos} \le 1$), and on $\{x : \cos(x^2) < 0\}$ it grows.
::: proof
<1>2.
:::

<1>4. The contribution from the region where $\cos(x^2)\ge0$ tends to $0$, while the contribution from the region where $\cos(x^2)<0$ tends to $+\infty$.
::: proof
On the first region, dominated convergence applies with dominating function $1$. On the second region, which has positive measure, Fatou's lemma gives
\[
\liminf_{n\to\infty}\int_{\{\cos(x^2)<0\}}e^{-n\cos(x^2)}\,dx
\ge
\int_{\{\cos(x^2)<0\}}\liminf_{n\to\infty}e^{-n\cos(x^2)}\,dx
=\infty.
\]
:::

<1>5. Hence $L = +\infty$.
::: proof
<1>4.
:::

**(b).**

<1>1. $\sum_{k=0}^{N} \frac{x^k}{k!} \to e^x$ as $N \to \infty$.
::: proof
power series of the exponential.
:::

<1>2. Hence $\sum_{k=0}^{N} \int_0^N \frac{x^k}{k!} e^{-2x}\,dx = \int_0^N \left(\sum_{k=0}^{N} \frac{x^k}{k!}\right) e^{-2x}\,dx$.
::: proof
<1>1 and linearity.
:::

<1>3. As $N \to \infty$, this tends to $\int_0^\infty e^x e^{-2x}\,dx = \int_0^\infty e^{-x}\,dx = 1$.
::: proof
Define
\[
h_N(x)=\mathbf1_{[0,N]}(x)e^{-2x}\sum_{k=0}^N\frac{x^k}{k!}.
\]
Then $h_N\uparrow e^{-x}$ pointwise on $[0,\infty)$, so the Monotone Convergence Theorem gives the claimed limit.
:::

<1>4. Hence $L = 1$.
::: proof
<1>3.
:::

**(c).**

<1>1. Tonelli's theorem permits reversing the order of integration, and $\int_0^\infty e^{-y/x}\,dy=x$ for fixed $x>0$.
::: proof
The integrand is nonnegative, so Tonelli applies without any prior integrability assumption. The inner integral equals $x$ by the change of variables $u=y/x$.
:::

<1>2. Hence $L = \int_0^\infty x e^{-x^2/2}\,dx$.
::: proof
<1>1.
:::

<1>3. $\int_0^\infty x e^{-x^2/2}\,dx = 1$ (substituting $u = x^2/2$, $du = x\,dx$).
::: proof
$\int_0^\infty x e^{-x^2/2}\,dx = \int_0^\infty e^{-u}\,du = 1$.
:::

<1>4. Hence $L = 1$.
::: proof
<1>2 and <1>3.
:::

<1>5. Q.E.D.
::: proof
<1>5 (a), <1>4 (b), <1>4 (c).
:::
:::
