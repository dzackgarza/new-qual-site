---
schema: qual/card@1
id: P-WESRA13A-II2
kind: problem
title: 'A positive-measure set of points lying in many measurable sets — as extracted'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. The deterministic extraction reads $\mu(B_i)>3/2$, which is inconsistent with $\mu(X)=1$. The numerical threshold is therefore recorded as an unresolved extractor/source defect rather than silently changed.
---

::: problem
Let $(X,\mathcal B,\mu)$ be a measure space with $\mu(X)=1$, and let $B_1,\dots,B_N\in\mathcal B$ satisfy
\[
\mu(B_i)>\frac32\qquad(1\le i\le N).
\]
Show that there is $C\in\mathcal B$ of positive measure such that for every $x\in C$,
\[
\frac1N\sum_{i=1}^N\chi_{B_i}(x)>\frac12.
\]
:::
