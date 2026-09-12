---
schema: qual/card@1
id: P-RASP08C
kind: problem
title: "Schur test inequality for integral operator"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Spring 2008 real-analysis qualifying exam. The source constant is 1/(2e); the card's epsilon was a transcription error.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Show that, for measurable functions $f, g : [1, \infty) \to [0, \infty)$, the following inequality holds:
$$
\left|\int_{[1,\infty)^2} e^{-xy} f(x) g(y)\,dx\,dy\right| \leq \frac{1}{2e} \left(\int_1^\infty |f(x)|^2\,dx\right)^{1/2} \left(\int_1^\infty |g(x)|^2\,dx\right)^{1/2},
$$
where $dx$ denotes the Lebesgue measure on $[1, \infty)$ and $dx\,dy$ denotes the Lebesgue measure on $[1, \infty)^2 = [1, \infty) \times [1, \infty)$.
:::


::: solution
<1>1. Factor the kernel by a pointwise estimate.
::: proof
For $x,y\ge1$,
\[
(x-1)(y-1)\ge0,
\]
so
\[
xy\ge x+y-1.
\]
Therefore
\[
e^{-xy}\le e^{-(x+y-1)}=e\,e^{-x}e^{-y}.
\]
Since $f,g\ge0$,
\[
\begin{aligned}
\int_{[1,\infty)^2}e^{-xy}f(x)g(y)\,dx\,dy
&\le e
\left(\int_1^\infty e^{-x}f(x)\,dx\right)
\left(\int_1^\infty e^{-y}g(y)\,dy\right).
\end{aligned}
\]
:::

<1>2. Apply Cauchy--Schwarz in each variable.
::: proof
Cauchy--Schwarz gives
\[
\int_1^\infty e^{-x}f(x)\,dx
\le
\left(\int_1^\infty e^{-2x}\,dx\right)^{1/2}\|f\|_2
=\frac{e^{-1}}{\sqrt2}\|f\|_2.
\]
Similarly,
\[
\int_1^\infty e^{-y}g(y)\,dy
\le \frac{e^{-1}}{\sqrt2}\|g\|_2.
\]
Combining these estimates yields
\[
\begin{aligned}
\left|\int_{[1,\infty)^2}e^{-xy}f(x)g(y)\,dx\,dy\right|
&\le e\left(\frac{e^{-1}}{\sqrt2}\right)^2\|f\|_2\|g\|_2\\
&=\boxed{\frac1{2e}\|f\|_2\|g\|_2}.
\end{aligned}
\]
This is the required inequality.
:::
:::
