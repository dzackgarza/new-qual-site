---
schema: qual/card@1
id: P-WESRA07-I1
kind: problem
title: State the dominated convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Part I, item 1 of the Real Analysis section of the Wesleyan University Analysis Qualifier, Summer 2007, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Give a precise statement of the dominated convergence theorem.
:::

::: solution
Let $(X,\mathcal A,\mu)$ be a measure space, and let $(f_n)$ be measurable complex-valued functions such that
\[
f_n(x)\longrightarrow f(x)
\]
for almost every $x\in X$. Suppose there exists $g\in L^1(\mu)$ such that
\[
|f_n(x)|\le g(x)
\]
for almost every $x\in X$ and every $n$.

Then $f\in L^1(\mu)$ and
\[
\lim_{n\to\infty}\int_X |f_n-f|\,d\mu=0.
\]
In particular,
\[
\boxed{\lim_{n\to\infty}\int_X f_n\,d\mu=\int_X f\,d\mu.}
\]
:::
