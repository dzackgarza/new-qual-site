---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS3B-P4
kind: problem
title: Lift maps between simply connected covering spaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
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
(May 2019) Let $p:\widetilde X\to X$ and $q:\widetilde Y\to Y$ be covering maps such that both $\widetilde X$ and $\widetilde Y$ are connected and simply connected.
Show that for every map $f:X\to Y$ there is a map $\widetilde f:\widetilde X\to\widetilde Y$ such that $f\circ p=q\circ\widetilde f$.
:::

::: {.solution}
Choose \(\widetilde x_0\in\widetilde X\), let \(x_0=p(\widetilde x_0)\), and choose \(\widetilde y_0\in q^{-1}(f(x_0))\). Consider
\[
f\circ p:\widetilde X\to Y.
\]
Since \(\widetilde X\) is simply connected,
\[
(f\circ p)_*\pi_1(\widetilde X,\widetilde x_0)=1.
\]
Also \(q_*\pi_1(\widetilde Y,\widetilde y_0)=1\) because \(\widetilde Y\) is simply connected. Hence the covering-space lifting criterion is satisfied, so there is a lift
\[
\widetilde f:\widetilde X\to\widetilde Y
\]
with \(\widetilde f(\widetilde x_0)=\widetilde y_0\) and
\[
q\circ\widetilde f=f\circ p.
\]
Thus every map \(f:X\to Y\) lifts after precomposition with the simply connected cover of \(X\).
:::
