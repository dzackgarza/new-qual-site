---
schema: qual/card@1
id: P-UCLARA11F-05
kind: problem
title: Weak type estimate for the Hardy-Littlewood maximal function
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
For $f\in L^1(\mathbb R)$, define
\[
Mf(x):=\sup_{h>0}\frac1{2h}\int_{x-h}^{x+h}|f(y)|\,dy.
\]
Prove that there is a constant $A$ such that for every $\alpha>0$,
\[
\lambda\{x\in\mathbb R:Mf(x)>\alpha\}\le \frac{A}{\alpha}\|f\|_{L^1}.
\]
If you use a covering lemma, prove it.
:::
