---
schema: qual/card@1
id: P-AZOFF-H01
kind: problem
title: Partial sums of the exponential series have no zeros in the unit disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash mangles the summand in the exponential partial sum. The same deterministic packet prints $1+z+z^2/2!+\cdots+z^n/n!$ explicitly in H8, which resolves this local extraction defect.
---

::: problem
For each nonnegative integer $n$, define
\[
f_n(z)=\sum_{k=0}^n\frac{z^k}{k!}.
\]
Prove that $f_n$ has no roots in the open unit disk.
(Hint: check $n=1$ and $n=2$ directly.)
:::
