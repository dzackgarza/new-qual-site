---
schema: qual/card@1
id: P-WESRA03-II4
kind: problem
title: Epsilon-delta absolute continuity for finite measures
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Absolute Continuity]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 4 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf.
---

::: {.problem}
Let $(X,\mathcal A)$ be a measurable space, and let $\mu$ and $\nu$ be finite measures on it.
Assume that for every $A\in\mathcal A$,
\[
\mu(A)=0\implies \nu(A)=0.
\]
Prove that for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
\mu(A)<\delta\implies \nu(A)<\varepsilon.
\]
:::
