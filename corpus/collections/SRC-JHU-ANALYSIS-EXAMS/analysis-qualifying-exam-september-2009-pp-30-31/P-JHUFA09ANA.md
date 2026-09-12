---
schema: qual/card@1
id: P-JHUFA09ANA
kind: problem
title: Pointwise versus uniform convergence of continuous functions
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Analysis Qualifying Exam, September 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $(f_n)$ is a sequence of continuous functions on $[0,1]$ converging pointwise to a continuous function $f$. Must $f_n\to f$ uniformly? Prove your answer.
:::

::: {.solution}
No. Define
\[
f_n(x)=\max\{1-n|x-1/n|,0\}.
\]
Each $f_n$ is continuous on $[0,1]$, and
\[
\|f_n\|_\infty=f_n(1/n)=1.
\]
Hence $(f_n)$ cannot converge uniformly to $0$.

On the other hand, $f_n\to0$ pointwise. Indeed, $f_n(0)=0$ for every $n$. If $x>0$ is fixed, then for all sufficiently large $n$ one has $2/n<x$, while $f_n$ is supported in $[0,2/n]$. Thus $f_n(x)=0$ eventually. Therefore
\[
f_n(x)\longrightarrow0
\qquad(x\in[0,1]),
\]
and the pointwise limit $f\equiv0$ is continuous.

So pointwise convergence of continuous functions to a continuous limit does not imply uniform convergence.
:::
