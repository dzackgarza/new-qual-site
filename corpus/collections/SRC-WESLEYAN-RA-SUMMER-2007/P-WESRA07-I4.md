---
schema: qual/card@1
id: P-WESRA07-I4
kind: problem
title: State Egorov's theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Give a precise statement of Egorov's theorem.
:::

::: {.solution}
Let $(X,\mathcal A,\mu)$ be a finite measure space, and let $f_n,f:X\to\mathbb C$ be measurable functions such that
\[
f_n(x)\longrightarrow f(x)
\]
for almost every $x\in X$.

Then $f_n\to f$ almost uniformly: for every $\varepsilon>0$ there exists $E\in\mathcal A$ with
\[
\mu(E)<\varepsilon
\]
such that $f_n\to f$ uniformly on $X\setminus E$.
:::
