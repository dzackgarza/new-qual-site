---
schema: qual/card@1
id: P-WESRA08-II1
kind: problem
title: The nonzero set of an integrable function is sigma-finite
classification:
  areas: [real-analysis]
  topics: [Measure Theory, L1 Spaces]
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
Let $(X,\mathcal B,\mu)$ be a measure space and let $f:X\to\mathbb R$ be integrable.
Prove that
\[
\{x\in X:f(x)\ne0\}
\]
is a countable union of sets of finite measure.
:::

::: solution
For $n\ge1$, set
\[
E_n:=\{x\in X:|f(x)|\ge 1/n\}.
\]
Then each $E_n$ is measurable and
\[
\frac1n\mu(E_n)
\le \int_{E_n}|f|\,d\mu
\le \|f\|_1<\infty.
\]
Hence
\[
\mu(E_n)\le n\|f\|_1<\infty.
\]

If $f(x)\ne0$, then $|f(x)|>1/n$ for some sufficiently large $n$, so $x\in E_n$.
Conversely every $E_n$ is contained in the nonzero set.
Therefore
\[
\boxed{\{f\ne0\}=\bigcup_{n=1}^\infty E_n,}
\]
a countable union of finite-measure sets.
:::
