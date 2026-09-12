---
schema: qual/card@1
id: P-JHUFA07ANG
kind: problem
title: "A summably integrable sequence converges to zero almost everywhere"
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, Fall 2007, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f_n$ be a sequence of measurable real-valued functions on $[0,1]$ such that
\[
\sum_{n=1}^\infty \int_0^1 |f_n(x)|\,dx\le1.
\]
Prove that $f_n\to0$ almost everywhere.
:::

::: {.solution}
<1>1. The series $\sum_n |f_n|$ is finite almost everywhere.
::: {.proof}
For $N\ge1$, set
\[
S_N(x)=\sum_{n=1}^N |f_n(x)|.
\]
Then $S_N$ is measurable and $S_N\uparrow S:=\sum_{n=1}^\infty |f_n|$. By the monotone convergence theorem,
\[
\int_0^1 S(x)\,dx
=\lim_{N\to\infty}\int_0^1 S_N(x)\,dx
=\sum_{n=1}^\infty\int_0^1 |f_n(x)|\,dx
\le1.
\]
Hence $S(x)<\infty$ for almost every $x\in[0,1]$; otherwise its integral would be infinite.
:::

<1>2. Absolute summability implies pointwise convergence to zero.
::: {.proof}
For every $x$ for which $S(x)<\infty$, the numerical series
\[
\sum_{n=1}^\infty |f_n(x)|
\]
converges. Therefore its terms tend to zero:
\[
|f_n(x)|\longrightarrow0.
\]
Thus $f_n(x)\to0$ for almost every $x\in[0,1]$.
:::
:::
