---
schema: qual/card@1
id: T-HRPNO
kind: theorem
title: "The Residue Theorem"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.theorem title="The Residue Theorem"}
Let $f$ be meromorphic on a region $\Omega$ with poles \( \ts{ \elts{z}{N} } \).
Then for any $\gamma \in \Omega\sm \ts{ \elts{z}{N} }$,
\[
{1 \over 2\pi i } \int_\gamma f(z) \dz = \sum_{j=1}^N n_\gamma(z_j) \Res_{z=z_j} f
.\]
If $\gamma$ is a toy contour with winding number 1 about each pole, then
\[
{1\over 2\pi i}\int_\gamma f\dz = \sum_{j=1}^N \Res_{z=z_j}f
.\]

:::{.remark}
Stein and Shakarchi, *Complex Analysis*, Ch. 3 Theorem 2.4.
:::

:::
