---
schema: qual/card@1
id: P-WESRA16-A1
kind: problem
title: 'A $[0,1]$-valued measurable function is either essentially an indicator or has a positive-measure middle level set'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group A, problem A1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $f:\mathbb R^d\to[0,1]$ be Lebesgue measurable and set
\[
W_n=\{x:2^{-n}\le f(x)\le1-2^{-n}\}.
\]
Prove that either

1. there is a measurable $X\subset\mathbb R^d$ such that $f=\mathbf1_X$ almost everywhere, or

2. $\lambda(W_n)>0$ for some $n$.
:::
