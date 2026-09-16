---
schema: qual/card@1
id: P-AZOFF-H09
kind: problem
title: Monic polynomials have modulus at least $1$ somewhere on the unit circle
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the OCR LaTeX and the broken accent in Rouché against Rouché’s theorem, Problem 9, of Azoff Problems by Topic.pdf; the source itself omits the first part it mentions.
---

::: {.problem}
Prove that
$$
\max_{\abs{z}=1} \abs{a_0 + a_1 z + \cdots + a_{n-1}z^{n-1} + z^n} \ge 1.
$$

Hint: The first part of the problem asks for a statement of Rouché’s Theorem.
:::
