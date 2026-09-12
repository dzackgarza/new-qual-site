---
schema: qual/card@1
id: P-TOP-WORKSHOP-D4-W2
kind: problem
title: A continuous bijective open (or closed) map is a homeomorphism (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Continuity
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
Let $f:X\to Y$ be a continuous, bijective, open map.
Show that $f$ is a homeomorphism.
[Open map can be replaced with closed map and the same result holds.]
:::

::: {.solution}
Since \(f\) is bijective, it has an inverse \(f^{-1}:Y\to X\). To prove that \(f\) is a homeomorphism it remains only to show that \(f^{-1}\) is continuous.

If \(U\subseteq X\) is open, then
\[
(f^{-1})^{-1}(U)=f(U),
\]
which is open in \(Y\) because \(f\) is an open map. Hence \(f^{-1}\) is continuous.

If instead \(f\) is assumed closed, then for every closed \(F\subseteq X\),
\[
(f^{-1})^{-1}(F)=f(F)
\]
is closed in \(Y\). Thus \(f^{-1}\) is continuous by the closed-set criterion. In either case \(f\) is a homeomorphism.
:::
