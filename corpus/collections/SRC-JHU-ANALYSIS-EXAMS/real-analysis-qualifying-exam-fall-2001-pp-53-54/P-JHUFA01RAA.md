---
schema: qual/card@1
id: P-JHUFA01RAA
kind: problem
title: Uniform continuity of continuous functions with limit at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f$ be continuous on $[0,\infty)$ and suppose the finite limit
\[
L=\lim_{x\to\infty}f(x)
\]
exists. Prove that $f$ is uniformly continuous on $[0,\infty)$.
:::

::: {.solution}
Fix $\varepsilon>0$. Since $f(x)\to L$, choose $R>0$ such that
\[
|f(x)-L|<\frac\varepsilon2
\qquad(x\ge R).
\]
Then whenever $x,y\ge R$,
\[
|f(x)-f(y)|
\le |f(x)-L|+|f(y)-L|
<\varepsilon.
\]

On the compact interval $[0,R+1]$, the function $f$ is uniformly continuous by the Heine--Cantor theorem. Hence there exists $\delta_0>0$ such that
\[
|x-y|<\delta_0,
\qquad x,y\in[0,R+1],
\]
implies
\[
|f(x)-f(y)|<\varepsilon.
\]
Set
\[
\delta=\min\{1,\delta_0\}.
\]
Suppose $x,y\ge0$ and $|x-y|<\delta$. If both $x,y\ge R$, the tail estimate above applies. Otherwise, one of the two points is $<R$; because $|x-y|<1$, both points then belong to $[0,R+1]$, so the compact-interval estimate applies. Thus in all cases
\[
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
\]
Therefore $f$ is uniformly continuous on $[0,\infty)$.
:::
