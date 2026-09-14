---
schema: qual/card@1
id: P-WESRA03-I5
kind: problem
title: Uniformly bounded pointwise convergence on a finite-measure set
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $E\subset\mathbb R$ be Lebesgue measurable with $m(E)<\infty$.
Suppose $(f_n)$ is a uniformly bounded sequence of real-valued measurable functions on $E$ and $f_n(x)\to f(x)$ for every $x\in E$.
What relationship holds between $\int_Ef_n\,dm$ and $\int_Ef\,dm$?
:::

::: solution
Choose $M<\infty$ such that
\[
|f_n(x)|\le M
\qquad(n\ge1,\ x\in E).
\]
Then also $|f(x)|\le M$, and
\[
M\mathbf1_E\in L^1(\mathbb R)
\]
because $m(E)<\infty$.
The Dominated Convergence Theorem therefore gives
\[
\boxed{\lim_{n\to\infty}\int_E f_n\,dm=\int_E f\,dm.}
\]
:::
