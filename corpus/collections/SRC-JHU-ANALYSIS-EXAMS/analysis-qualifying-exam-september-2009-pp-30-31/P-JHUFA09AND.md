---
schema: qual/card@1
id: P-JHUFA09AND
kind: problem
title: "Integral of the derivative of a monotone function is bounded by its total increase"
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the JHU Analysis Qualifying Exam, September 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$ be nondecreasing. Assume that $f$ is differentiable almost everywhere. Prove that
\[
\int_0^1 f'(x)\,dx\le f(1)-f(0).
\]
:::

::: {.solution}
For $0<h<1$, define
\[
q_h(x)=\begin{cases}
\dfrac{f(x+h)-f(x)}h,&0\le x\le1-h,\\
0,&1-h<x\le1.
\end{cases}
\]
Since $f$ is nondecreasing, $q_h\ge0$. At every point $x\in[0,1)$ where $f'(x)$ exists,
\[
q_h(x)\longrightarrow f'(x)
\qquad(h\downarrow0).
\]
Choose any sequence $h_n\downarrow0$. By Fatou's lemma,
\[
\int_0^1 f'(x)\,dx
\le \liminf_{n\to\infty}\int_0^1 q_{h_n}(x)\,dx.
\]
Now
\[
\begin{aligned}
\int_0^1q_h(x)\,dx
&=\frac1h\int_0^{1-h}(f(x+h)-f(x))\,dx\\
&=\frac1h\left(\int_{1-h}^1 f(u)\,du-\int_0^h f(u)\,du\right).
\end{aligned}
\]
Monotonicity gives
\[
\int_{1-h}^1 f(u)\,du\le hf(1),
\qquad
\int_0^h f(u)\,du\ge hf(0).
\]
Hence
\[
\int_0^1q_h(x)\,dx\le f(1)-f(0).
\]
Combining this with Fatou yields
\[
\boxed{\int_0^1 f'(x)\,dx\le f(1)-f(0)}.
\]
:::
