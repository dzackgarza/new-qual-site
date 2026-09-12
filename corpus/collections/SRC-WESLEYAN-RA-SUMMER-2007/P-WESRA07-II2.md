---
schema: qual/card@1
id: P-WESRA07-II2
kind: problem
title: L1 convergence implies convergence in measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Part II, item 2 of the Real Analysis section of the Wesleyan University Analysis Qualifier, Summer 2007, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $(X,\mathcal A,\mu)$ be a measure space. Suppose $f_n,f\in L^1(X,\mu)$ and
\[
\int_X|f_n-f|\,d\mu\longrightarrow0.
\]
Prove that for every $a>0$,
\[
\mu\{x:|f_n(x)-f(x)|>a\}\longrightarrow0.
\]
:::

::: solution
Fix $a>0$ and set
\[
E_n=\{x:|f_n(x)-f(x)|>a\}.
\]
On $E_n$ one has $|f_n-f|>a$, hence
\[
a\,\mu(E_n)
\le \int_{E_n}|f_n-f|\,d\mu
\le \int_X|f_n-f|\,d\mu.
\]
Therefore
\[
\mu(E_n)
\le \frac1a\|f_n-f\|_{L^1}
\longrightarrow0.
\]
Thus $f_n\to f$ in measure.
:::
