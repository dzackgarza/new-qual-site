---
schema: qual/card@1
id: P-WESCA05-II5
kind: problem
title: "A Schwarz–Pick bound in terms of $f(0)$"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 2, problem 5 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Suppose $f$ is analytic in the open unit disk $D$ and $|f(z)|<1$ for all $z\in D$.
Let $a=f(0)$ and define
\[
g(z)=\frac{f(z)-a}{1-\overline a\,f(z)}.
\]
Using $g$ and the fact that $g$ maps $D$ to $D$, prove that
\[
|f(z)|\le\frac{|f(0)|+|z|}{1-|f(0)||z|}
\qquad(z\in D).
\]
:::
