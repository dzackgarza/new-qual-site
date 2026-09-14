---
schema: qual/card@1
id: P-WESRA10-II4
kind: problem
title: 'Continuity of translations in $L^1$'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash drops the absolute-value delimiters in the displayed integral; the card records the only norm-continuity statement compatible with the surrounding translation question.
---

::: problem
Let $f\in L^1(\mathbb R)$ and define $f_t(x)=f(x-t)$.
Prove
\[
\lim_{t\to0}\int_{\mathbb R}|f-f_t|\,dm=0.
\]
If $A\subset\mathbb R$ has finite Lebesgue measure, explain what this says about the translates $A+t$.
:::
