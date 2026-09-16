---
schema: qual/card@1
id: P-WESRA03-I6
kind: problem
title: Lebesgue integrability does not imply Riemann integrability
classification:
  areas: [real-analysis]
  topics: [Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Is every bounded real-valued function on $[0,1]$ that is Lebesgue integrable also Riemann integrable?
:::

::: {.solution}
No. Take the Dirichlet function
\[
f=\mathbf1_{\mathbb Q\cap[0,1]}.
\]
It is bounded and Lebesgue measurable, and since $\mathbb Q\cap[0,1]$ is countable,
\[
\int_0^1 f\,dm=0.
\]
But every nonempty interval contains both rational and irrational points, so on every subinterval the infimum of $f$ is $0$ and the supremum is $1$.
Thus every lower Darboux sum is $0$ and every upper Darboux sum is $1$.
Hence $f$ is not Riemann integrable.
:::
