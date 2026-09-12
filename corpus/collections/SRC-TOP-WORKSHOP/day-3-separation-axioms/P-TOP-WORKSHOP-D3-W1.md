---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-W1
kind: problem
title: Metric spaces are Hausdorff (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
If $(X,d)$ is a metric space, then it is Hausdorff [see number 8].
:::

::: {.solution}
Let \(x\ne y\) in the metric space \((X,d)\), and put \(r=d(x,y)/3>0\). If a point \(z\) belonged to both \(B(x,r)\) and \(B(y,r)\), then the triangle inequality would give
\[
d(x,y)\le d(x,z)+d(z,y)<2r=\frac23d(x,y),
\]
a contradiction. Thus \(B(x,r)\) and \(B(y,r)\) are disjoint open neighborhoods of \(x\) and \(y\). Hence every metric space is Hausdorff.
:::
