---
schema: qual/card@1
id: E-NBS6F
kind: problem
title: Products of Hausdorff spaces in the box and product topologies
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Hausdorff Spaces
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

Prove Theorem 19.4: if each space $X_\alpha$ is a Hausdorff space, then $\prod X_\alpha$ is a Hausdorff space in both the box and product topologies.
:::

::: {.solution}
Let $x=(x_\alpha)$ and $y=(y_\alpha)$ be distinct points of $\prod X_\alpha$. Then for some index $\beta$,
\[
x_\beta\ne y_\beta.
\]
Since $X_\beta$ is Hausdorff, choose disjoint open neighborhoods $U_\beta,V_\beta$ of $x_\beta,y_\beta$.

In the product topology, set
\[
U=\pi_\beta^{-1}(U_\beta),\qquad V=\pi_\beta^{-1}(V_\beta).
\]
These are disjoint open neighborhoods of $x,y$. Hence the product topology is Hausdorff.

The box topology is finer than the product topology, so the same two sets are box-open. Thus the box product is Hausdorff as well.
:::
