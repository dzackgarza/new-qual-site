---
schema: qual/card@1
id: P-AZOFF-E10
kind: problem
title: Uniform convergence of $\sum\sin(nz)/2^n$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Liouville, FTA, and power series, Problem 10, of Azoff Problems by Topic.pdf, which reads Im z < ln 2; added an erratum remark with a counterexample and the corrected region.
---

::: {.problem}
Prove that the series $\sum_{n=1}^\infty \frac{\sin(nz)}{2^n}$ converges uniformly on $\{z : \operatorname{Im} z < \ln 2\}$.
:::

::: {.remark}
Erratum: the statement is false as written in the source.
For $z = iy$ we have $\abs{\sin(nz)} = \sinh(n\abs{y})$, so at $z = -2i$ the terms have modulus $\sinh(2n)/2^n \to \infty$ and the series diverges, although $\operatorname{Im}(-2i) < \ln 2$.
Even on the strip $\{\abs{\operatorname{Im} z} < \ln 2\}$, where the series converges, the convergence is not uniform: at $z = iy$ with $0 < y < \ln 2$ the terms are $i\sinh(ny)/2^n$, with $\sinh(ny)/2^n \ge (e^{y}/2)^n/4$ for $ny \ge 1$, and $e^y/2 \to 1$ as $y \to \ln 2$, so no tail is uniformly small.
The correct statement is that the series converges uniformly on $\{z : \abs{\operatorname{Im} z} \le c\}$ for each $c < \ln 2$, hence locally uniformly on $\{z : \abs{\operatorname{Im} z} < \ln 2\}$.
:::
