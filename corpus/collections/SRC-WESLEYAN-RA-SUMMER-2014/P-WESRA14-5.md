---
schema: qual/card@1
id: P-WESRA14-5
kind: problem
title: 'Subsequence and finite-measure converse for the source’s convergence-in-measure definition'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. The source uses the name “convergence in measure” for the displayed exceptional-set-uniform definition (usually called almost uniform convergence). The card preserves the source definition rather than silently replacing it with the standard one.
---

::: {.problem}
The source defines that measurable $f_n$ converge *in measure* to $f$ if for every $\varepsilon>0$ there are $N$ and a measurable $B$ with $\mu(B)<\varepsilon$ such that
\[
|f_n(x)-f(x)|<\varepsilon
\]
for every $n\ge N$ and every $x\notin B$.

(a) Under this definition, prove that some subsequence converges to $f$ almost everywhere.

(b) If $\mu(X)<\infty$ and $f_n\to f$ almost everywhere, prove convergence in the displayed source sense.
:::
