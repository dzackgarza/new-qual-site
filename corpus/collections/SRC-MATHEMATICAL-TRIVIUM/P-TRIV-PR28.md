---
schema: qual/card@1
id: P-TRIV-PR28
kind: problem
title: Chi-squared test of a Poisson fit to a cosmic-ray spectrum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 28, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the garbled spectrum table, including the 80-90 MeV bin, against Probability Problem 28 on page 31 of the source PDF.
---

::: {.problem}
In an experiment on the detection of cosmic rays a detector counts particles with different energies coming from different directions.
The observed spectrum of the particles is shown in table below.

| Energy, MeV | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 |
|---|---|---|---|---|---|---|---|---|---|
| # of p. | 15 | 71 | 75 | 68 | 39 | 17 | 10 | 4 | 1 |

At the significance level 0.05, test the hypothesis that the particle spectrum is distributed according to the Poisson distribution with parameter $\lambda$.
Find the effective estimate for $\lambda$.
:::
