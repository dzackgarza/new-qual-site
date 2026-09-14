---
schema: qual/card@1
id: P-WESRA11-1
kind: problem
title: 'Integral convergence need not imply almost-everywhere convergence'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash drops the subscript on $f_n$ inside the displayed integral; the card restores it from the sequence named in the same sentence.
---

::: problem
Prove or give a counterexample: if $f_n$ are continuous on $[0,1]$, $0\le f_n\le1$, and
\[
\lim_{n\to\infty}\int_0^1 f_n\,dm=0,
\]
then $f_n(x)\to0$ almost everywhere.
:::
