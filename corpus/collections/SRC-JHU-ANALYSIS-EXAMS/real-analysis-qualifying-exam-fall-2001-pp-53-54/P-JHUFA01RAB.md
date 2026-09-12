---
schema: qual/card@1
id: P-JHUFA01RAB
kind: problem
title: Convolution of functions vanishing at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f,g:\mathbb R\to\mathbb R$ be continuous, suppose
\[
\lim_{|x|\to\infty}f(x)=0,
\qquad
\int_{-\infty}^\infty |g(y)|\,dy<\infty,
\]
and define
\[
h(x)=\int_{-\infty}^\infty f(x-y)g(y)\,dy.
\]
Prove that
\[
\lim_{|x|\to\infty}h(x)=0.
\]
:::

::: {.solution}
Because $f$ is continuous and tends to $0$ at both ends, it is bounded; write
\[
M=\|f\|_\infty<\infty.
\]
Fix $\varepsilon>0$. Choose $R>0$ so large that
\[
\int_{|y|>R}|g(y)|\,dy<\frac{\varepsilon}{2M}
\]
when $M>0$; if $M=0$, then $f\equiv0$ and there is nothing to prove.

Since $f(x)\to0$ as $|x|\to\infty$, there exists $A>0$ such that
\[
|f(z)|<\frac{\varepsilon}{2\|g\|_1}
\qquad(|z|>A)
\]
when $\|g\|_1>0$; if $g=0$ a.e., the conclusion is immediate.

Now take $|x|>A+R$. For every $|y|\le R$ one has
\[
|x-y|\ge |x|-|y|>A,
\]
so
\[
\begin{aligned}
|h(x)|
&\le \int_{|y|\le R}|f(x-y)|\,|g(y)|\,dy
 +\int_{|y|>R}|f(x-y)|\,|g(y)|\,dy\\
&\le \frac{\varepsilon}{2\|g\|_1}\int_{|y|\le R}|g(y)|\,dy
 +M\int_{|y|>R}|g(y)|\,dy\\
&<\frac\varepsilon2+\frac\varepsilon2
=\varepsilon.
\end{aligned}
\]
Hence $h(x)\to0$ as $|x|\to\infty$.
:::
