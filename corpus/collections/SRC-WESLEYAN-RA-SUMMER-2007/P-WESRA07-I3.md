---
schema: qual/card@1
id: P-WESRA07-I3
kind: problem
title: Define almost uniform convergence
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Give the definition of almost uniform convergence for a sequence of functions.
:::

::: solution
Let $(X,\mathcal A,\mu)$ be a measure space and let $f_n,f$ be measurable functions on $X$.
We say that $f_n$ converges to $f$ almost uniformly if for every $\varepsilon>0$ there exists a measurable set $E\in\mathcal A$ such that
\[
\mu(E)<\varepsilon
\]
and $f_n\to f$ uniformly on $X\setminus E$.
Equivalently, for every $\varepsilon>0$ there is $E\in\mathcal A$ with $\mu(E)<\varepsilon$ such that
\[
\boxed{\sup_{x\in X\setminus E}|f_n(x)-f(x)|\longrightarrow0.}
\]
:::
