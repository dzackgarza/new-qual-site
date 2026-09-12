---
schema: qual/card@1
id: P-WWNJC
kind: problem
title: Without using the Riesz Representation Theorem, compute
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Spring 2016 Problem 6 in the preserved UGA source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Without using the Riesz Representation Theorem, compute
\[
\sup \left\{\left|\int_{0}^{1} f(x) e^{x} d x\right| \suchthat f \in L^{2}([0,1], m),~~ \|f\|_{2} \leq 1\right\}
\]
:::
::: solution
<1>1. Obtain the sharp upper bound.
::: proof
For any $f\in L^2([0,1])$ with $\|f\|_2\le1$, Cauchy--Schwarz gives
\[
\left|\int_0^1 f(x)e^x\,dx\right|
\le \|f\|_2\,\|e^x\|_2
\le \|e^x\|_2.
\]
Now
\[
\|e^x\|_2^2
=\int_0^1e^{2x}\,dx
=\frac{e^2-1}{2},
\]
so the supremum is at most
\[
\sqrt{\frac{e^2-1}{2}}.
\]
:::

<1>2. Show that the bound is attained.
::: proof
Let
\[
f_0(x):=\frac{e^x}{\|e^x\|_2}.
\]
Then $\|f_0\|_2=1$ and
\[
\int_0^1 f_0(x)e^x\,dx
=\frac{\|e^x\|_2^2}{\|e^x\|_2}
=\|e^x\|_2.
\]
Therefore
\[
\boxed{
\sup_{\|f\|_2\le1}
\left|\int_0^1 f(x)e^x\,dx\right|
=\sqrt{\frac{e^2-1}{2}}.}
\]
No form of the Riesz Representation Theorem is needed.
:::
:::
