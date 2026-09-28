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
Each member of $\mathcal B$ is a product of open sets, hence box-open. Conversely, if $x\in\prod U_\alpha$ with each $U_\alpha$ open, choose $B_\alpha\in\mathcal B_\alpha$ with $x_\alpha\in B_\alpha\subseteq U_\alpha$; then $x\in\prod B_\alpha\subseteq\prod U_\alpha$. So every box-open set is a union of members of $\mathcal B$, and $\mathcal B$ generates the box topology.

For the product topology, let $\mathcal B'$ consist of the products $\prod B_\alpha$ with $B_\alpha\in\mathcal B_\alpha$ for $\alpha$ in a finite set $F$ and $B_\alpha=X_\alpha$ for $\alpha\notin F$. It covers the product. If $x\in\prod B_\alpha\cap\prod C_\alpha$ with finite index sets $F$ and $G$, choose $D_\alpha\in\mathcal B_\alpha$ with $x_\alpha\in D_\alpha\subseteq B_\alpha\cap C_\alpha$ for $\alpha\in F\cup G$, and put $D_\alpha=X_\alpha$ otherwise; then $\prod D_\alpha\in\mathcal B'$ and $x\in\prod D_\alpha\subseteq\prod B_\alpha\cap\prod C_\alpha$. So $\mathcal B'$ is a basis. Its members are basic product-open sets. If $x\in\prod U_\alpha$ with $U_\alpha$ open and $U_\alpha=X_\alpha$ outside a finite set $F$, choose $B_\alpha\in\mathcal B_\alpha$ with $x_\alpha\in B_\alpha\subseteq U_\alpha$ for $\alpha\in F$ and $B_\alpha=X_\alpha$ otherwise; then $x\in\prod B_\alpha\subseteq\prod U_\alpha$. Hence $\mathcal B'$ generates the product topology.
:::
