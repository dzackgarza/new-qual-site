---
schema: qual/card@1
id: P-WESRA03-I8
kind: problem
title: Continuity from above requires finite measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Short Answer Question 8 of the Wesleyan Preliminary Exam in Analysis, August 4, 2003, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $\mu$ be a measure and let $F_1\supseteq F_2\supseteq\cdots$ be measurable. Is it always true that
\[
\mu\!\left(\bigcap_{n=1}^\infty F_n\right)=\lim_{n\to\infty}\mu(F_n)?
\]
:::

::: solution
No, not without a finiteness hypothesis. For Lebesgue measure on $\mathbb R$, let
\[
F_n=[n,\infty).
\]
Then $(F_n)$ is decreasing and
\[
\bigcap_{n=1}^\infty F_n=\varnothing,
\]
so the measure of the intersection is $0$, while
\[
\mu(F_n)=\infty
\]
for every $n$.

If $\mu(F_1)<\infty$, then continuity from above does hold:
\[
\mu\!\left(\bigcap_nF_n\right)=\lim_n\mu(F_n).
\]
:::
