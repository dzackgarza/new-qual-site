---
schema: qual/card@1
id: P-WESRA08-I5
kind: problem
title: State the Radon-Nikodym theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Radon-Nikodym Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
State the Radon-Nikodym theorem.
:::

::: solution
Let $(X,\mathcal M)$ be a measurable space, and let $\mu$ and $\nu$ be sigma-finite positive measures on $\mathcal M$.
If
\[
\nu\ll\mu,
\]
then there exists a measurable function $f:X\to[0,\infty)$ such that
\[
\boxed{\nu(E)=\int_E f\,d\mu}
\qquad(E\in\mathcal M).
\]
The function $f$ is unique up to $\mu$-almost-everywhere equality and is denoted
\[
f=\frac{d\nu}{d\mu}.
\]
:::
