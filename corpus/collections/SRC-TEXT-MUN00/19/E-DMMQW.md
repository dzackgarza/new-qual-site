---
schema: qual/card@1
id: E-DMMQW
kind: problem
title: Basis theorem for the box and product topologies
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Bases
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

Prove Theorem 19.2: suppose the topology on each space $X_\alpha$ is given by a basis $\mathcal{B}_\alpha$.
The collection of all sets of the form $\prod_{\alpha \in J} B_\alpha$, where $B_\alpha \in \mathcal{B}_\alpha$ for each $\alpha$, serves as a basis for the box topology on $\prod_{\alpha \in J} X_\alpha$; and the collection of all sets of the same form, where $B_\alpha \in \mathcal{B}_\alpha$ for finitely many indices $\alpha$ and $B_\alpha = X_\alpha$ for all the remaining indices, serves as a basis for the product topology.
:::

::: {.solution}
For the box topology, let
\[
\mathcal B=\left\{\prod_{\alpha\in J}B_\alpha:B_\alpha\in\mathcal B_\alpha\right\}.
\]
It covers the product because each $\mathcal B_\alpha$ covers $X_\alpha$. If
\[
x\in\prod B_\alpha\cap\prod C_\alpha,
\]
then for every $\alpha$, because $\mathcal B_\alpha$ is a basis, there is $D_\alpha\in\mathcal B_\alpha$ such that
\[
x_\alpha\in D_\alpha\subseteq B_\alpha\cap C_\alpha.
\]
Hence
\[
x\in\prod D_\alpha\subseteq\left(\prod B_\alpha\right)\cap\left(\prod C_\alpha\right),
\]
so $\mathcal B$ is a basis.

For the product topology, take only those products for which $B_\alpha=X_\alpha$ except at finitely many indices. The same argument works, and the intersection of two such basic products again has only finitely many nontrivial coordinates. Therefore these products form a basis for the product topology.
:::
