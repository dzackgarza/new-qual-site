---
schema: qual/card@1
id: E-G5BOG
kind: problem
title: Subspaces of Hausdorff spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that a subspace of a Hausdorff space is Hausdorff.
:::

::: {.solution}
Let $Y\subseteq X$, where $X$ is Hausdorff, and let $y_1\ne y_2$ be points of $Y$. Choose disjoint open sets $U_1,U_2\subseteq X$ with $y_i\in U_i$. Then
\[
U_1\cap Y,\qquad U_2\cap Y
\]
are disjoint open neighborhoods of $y_1,y_2$ in the subspace $Y$. Hence $Y$ is Hausdorff.
:::
