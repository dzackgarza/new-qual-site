---
schema: qual/card@1
id: P-JHUMAY10ANI
kind: problem
title: "Differentiation under the integral sign with a dominated partial derivative"
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 2010, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f:[0,1]\times[0,1]\to\mathbb R$ be continuous. Assume that for each $x$, the map $t\mapsto f(x,t)$ is differentiable and that
\[
\left|\frac{\partial f}{\partial t}(x,t)\right|\le g(x)
\]
for some measurable $g\in L^1([0,1])$. Define
\[
F(t)=\int_0^1 f(x,t)\,dx.
\]
Prove that
\[
F'(t)=\int_0^1\frac{\partial f}{\partial t}(x,t)\,dx.
\]
:::

::: {.solution}
Fix $t\in(0,1)$. For $h\ne0$ small enough that $t+h\in[0,1]$, define
\[
q_h(x)=\frac{f(x,t+h)-f(x,t)}{h}.
\]
For each fixed $x$, differentiability in $t$ gives
\[
q_h(x)\longrightarrow \frac{\partial f}{\partial t}(x,t)
\qquad(h\to0).
\]
By the one-variable mean value theorem, for each $x$ and such $h$, there exists $\theta$ between $t$ and $t+h$ such that
\[
q_h(x)=\frac{\partial f}{\partial t}(x,\theta).
\]
Hence
\[
|q_h(x)|\le g(x).
\]
Since $g\in L^1$, dominated convergence yields
\[
\begin{aligned}
F'(t)
&=\lim_{h\to0}\frac{F(t+h)-F(t)}h\\
&=\lim_{h\to0}\int_0^1q_h(x)\,dx\\
&=\int_0^1\frac{\partial f}{\partial t}(x,t)\,dx.
\end{aligned}
\]
The same argument with one-sided difference quotients proves the corresponding one-sided derivative statements at $t=0$ and $t=1$.
:::
