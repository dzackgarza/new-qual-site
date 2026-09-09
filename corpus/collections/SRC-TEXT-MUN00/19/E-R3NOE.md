---
schema: qual/card@1
id: E-R3NOE
kind: problem
title: Products of subspaces are subspaces
classification:
  areas:
  - topology
  topics:
  - Product Topology
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

Prove Theorem 19.3: let $A_\alpha$ be a subspace of $X_\alpha$, for each $\alpha \in J$.
Then $\prod A_\alpha$ is a subspace of $\prod X_\alpha$ if both products are given the box topology, or if both products are given the product topology.
:::

::: {.solution}
Let $A=\prod A_\alpha\subseteq X=\prod X_\alpha$.

For the box topology, a basic open set of the subspace $A$ has the form
\[
A\cap\prod U_\alpha=\prod(A_\alpha\cap U_\alpha),
\]
which is a basic box-open set in the product of the subspaces $A_\alpha$. Conversely every basic box-open set in $\prod A_\alpha$ has this form. Thus the topologies agree.

For the product topology the same computation applies, with $U_\alpha=X_\alpha$ for all but finitely many $\alpha$. Then
\[
A_\alpha\cap U_\alpha=A_\alpha
\]
for all but finitely many $\alpha$, exactly the basis condition for the product topology on $\prod A_\alpha$. Hence the two subspace descriptions agree in the product topology as well.
:::
