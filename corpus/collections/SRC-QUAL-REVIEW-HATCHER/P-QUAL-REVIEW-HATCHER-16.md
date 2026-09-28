---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-16
kind: problem
title: Degree of a normalized polynomial counts roots in the unit disk
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 16 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The deterministic extraction writes the initial inclusion as “S^1 ∈ C”; it is normalized here to the evident inclusion arrow.
---

::: {.problem}
Let $f\in\mathbb C[z]$ and assume that $f$ has no roots on the unit circle.
Consider
\[
S^1\hookrightarrow\mathbb C\xrightarrow{f}\mathbb C\setminus\{0\}\xrightarrow{\pi}S^1,
\]
where $\pi$ is the norm map.
Prove that the degree of this composition equals the number of roots of $f$ inside the unit circle.
:::
