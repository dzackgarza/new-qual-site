---
schema: qual/card@1
id: P-WESRA03-II2
kind: problem
title: Tail measure decay for an integrable function
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 2 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf; Flash drops the arrow in the displayed limit, while the surrounding text and indexed limit expression determine the statement.
---

::: {.problem}
Let $f$ be Lebesgue integrable on $\mathbb R$.
For each $n\in\mathbb N$, define
\[
E_n=\{x\in\mathbb R:|f(x)|\ge n\}.
\]
Show that
\[
\lim_{n\to\infty} n\,m(E_n)=0.
\]
:::
