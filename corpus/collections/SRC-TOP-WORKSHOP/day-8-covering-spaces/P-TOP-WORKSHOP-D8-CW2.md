---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-CW2
kind: problem
title: A wedge of two spheres as a covering space (warm-up)
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Counterexamples
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
Prove or disprove: $S^2\vee S^2$ is a covering space of $S^2$.
:::

::: {.solution}
The statement is false. The space \(S^2\vee S^2\) is connected. If it covered \(S^2\), then because \(S^2\) is simply connected, every connected covering of \(S^2\) would be one-sheeted and therefore a homeomorphism onto \(S^2\).

But \(S^2\vee S^2\) is not homeomorphic to \(S^2\); for example,
\[
H_2(S^2\vee S^2)\cong\mathbb Z\oplus\mathbb Z,
\qquad
H_2(S^2)\cong\mathbb Z.
\]
Therefore \(S^2\vee S^2\) cannot be a covering space of \(S^2\).
:::
