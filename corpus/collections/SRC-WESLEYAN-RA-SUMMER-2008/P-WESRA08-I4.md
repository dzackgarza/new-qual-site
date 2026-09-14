---
schema: qual/card@1
id: P-WESRA08-I4
kind: problem
title: State Holder's inequality
classification:
  areas: [real-analysis]
  topics: [Lp Spaces, Holder Inequality]
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
State Holder's inequality for functions in $L^p$ spaces.
:::

::: solution
Let $(X,\mathcal M,\mu)$ be a measure space, let $1\le p,q\le\infty$ satisfy
\[
\frac1p+\frac1q=1,
\]
and let $f\in L^p(\mu)$ and $g\in L^q(\mu)$.
Then $fg\in L^1(\mu)$ and
\[
\boxed{
\int_X|fg|\,d\mu
\le \|f\|_p\,\|g\|_q.}
\]
Equivalently,
\[
\|fg\|_1\le\|f\|_p\|g\|_q.
\]
:::
