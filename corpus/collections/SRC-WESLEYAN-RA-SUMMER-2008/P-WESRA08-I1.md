---
schema: qual/card@1
id: P-WESRA08-I1
kind: problem
title: Define the Borel sets on the real line
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Borel Sets]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Give a precise definition of the Borel sets on the real line.
:::

::: {.solution}
The **Borel sigma-algebra** on $\RR$ is
\[
\mathcal B(\RR):=\sigma(\mathcal O),
\]
where $\mathcal O$ is the family of open subsets of $\RR$.
Equivalently, it is the smallest sigma-algebra containing every open interval.

A subset $E\subseteq\RR$ is called a **Borel set** exactly when
\[
E\in\mathcal B(\RR).
\]
:::
