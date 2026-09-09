---
schema: qual/card@1
id: P-JHUMAY12RA7
kind: problem
title: Integral transform is absolutely continuous and vanishes at infinity
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
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, May 9, 2012, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^1(\mathbb R)$ and define
\[
h(x)=\int_x^{x+1}f(t)\,dt.
\]

(a) Prove that $h$ is absolutely continuous.

(b) Prove that $h(x)\to0$ as $x\to\infty$.
:::

::: {.solution}
Define
\[
F(x)=\int_0^x f(t)\,dt,
\]
with the usual signed interpretation when $x<0$. Since $f\in L^1(\mathbb R)$, the indefinite integral $F$ is absolutely continuous, and
\[
F'(x)=f(x)
\]
for almost every $x$. Since
\[
h(x)=F(x+1)-F(x),
\]
the function $h$ is a difference of absolutely continuous functions and is therefore absolutely continuous. In fact,
\[
h'(x)=f(x+1)-f(x)
\]
for almost every $x$.

For part (b),
\[
|h(x)|\le\int_x^{x+1}|f(t)|\,dt\le\int_x^\infty|f(t)|\,dt.
\]
Because $f\in L^1(\mathbb R)$, the tail integral tends to zero as $x\to\infty$. Hence
\[
h(x)\longrightarrow0.
\]
:::
