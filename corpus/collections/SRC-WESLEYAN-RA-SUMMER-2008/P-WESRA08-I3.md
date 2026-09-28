---
schema: qual/card@1
id: P-WESRA08-I3
kind: problem
title: State the monotone convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Monotone Convergence]
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

::: {.problem}
State the Lebesgue monotone convergence theorem in an abstract measure space.
:::

::: {.solution}
Let $(X,\mathcal M,\mu)$ be a measure space, and let
\[
0\le f_1\le f_2\le\cdots
\]
be measurable functions with
\[
f_n(x)\longrightarrow f(x)
\]
for almost every $x\in X$.
Then $f$ is measurable and
\[
\boxed{
\int_X f\,d\mu
=\lim_{n\to\infty}\int_X f_n\,d\mu,}
\]
where both sides are allowed to equal $+\infty$.
:::
