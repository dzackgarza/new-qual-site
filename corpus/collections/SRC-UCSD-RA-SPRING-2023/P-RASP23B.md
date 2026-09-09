---
schema: qual/card@1
id: P-RASP23B
kind: problem
title: "Uniform convergence and integration on finite measure spaces"
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
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Assume that $\mu(X) < \infty$.
Let $\{f_n\}$ be a bounded sequence of complex functions.
Assume that $f_n \to f$ uniformly as $n \to \infty$.
Prove that $\int_X f_n\,d\mu \to \int_X f\,d\mu$.
Show by an example that the assumption $\mu(X) < \infty$ cannot be dropped.
:::

::: solution
<1>1. Prove convergence when $\mu(X)<\infty$.
::: proof
Uniform convergence gives
\[
\|f_n-f\|_\infty\longrightarrow0.
\]
Since $\mu(X)<\infty$,
\[
\begin{aligned}
\left|\int_X f_n\,d\mu-\int_X f\,d\mu\right|
&\le\int_X|f_n-f|\,d\mu\\
&\le \mu(X)\|f_n-f\|_\infty
\longrightarrow0.
\end{aligned}
\]
Thus
\[
\boxed{\int_Xf_n\,d\mu\longrightarrow\int_Xf\,d\mu.}
\]
:::

<1>2. Show that finite total measure is necessary in general.
::: proof
Take $X=[0,\infty)$ with Lebesgue measure and define
\[
f_n(x)=\frac1n\mathbf1_{[0,n]}(x).
\]
Then
\[
\|f_n\|_\infty=\frac1n\longrightarrow0,
\]
so $f_n\to0$ uniformly. However,
\[
\int_0^\infty f_n(x)\,dx
=\frac1n\,m([0,n])=1
\]
for every $n$. Therefore the integrals do not converge to the integral of the uniform limit.
:::
:::
