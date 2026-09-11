---
schema: qual/card@1
id: P-AGHNOETHSPACE
kind: problem
title: Four characterisations of a Noetherian space, and what they force
classification:
  areas:
  - algebraic-geometry
  topics:
  - Noetherian Spaces
  - Quasicompactness
  - Irreducibility
relations:
- kind: uses
  target: D-9DIKB
review: draft
---

::: problem
(a) Show that the following are equivalent for a topological space $X$:

- $X$ is Noetherian;
- every nonempty family of closed subsets has a minimal element;
- $X$ satisfies the ascending chain condition on open subsets;
- every nonempty family of open subsets has a maximal element.

(b) A Noetherian topological space is quasicompact.

(c) Any subset of a Noetherian topological space is Noetherian in its induced topology.

(d) A Noetherian space which is also Hausdorff is a finite set with the discrete topology.
:::

::: solution
**(a)** $1 \implies 2$: given a family $\ts{Y_j}$ of closed sets, choose $Y_1$; if it is not minimal there is $Y_2 \subsetneq Y_1$, and so on.
The resulting descending chain stabilises, and where it stabilises is a minimal element.
$1 \iff 3$ and $2 \iff 4$ are complementation.
$4 \implies 3$: a chain of opens is a family, so it has a maximal element, which is where it stabilises.

**(b)** Let $\mcu$ be an open cover and set $V_n = \Union_{i \leq n} U_i$.
Then $V_1 \subseteq V_2 \subseteq \cdots$ is an ascending chain of opens, so it stabilises at some $V_n$, and $V_n = \Union_i U_i = X$ is a finite subcover.

**(c)** Let $U_1 \subseteq U_2 \subseteq \cdots$ be opens in $Y$, so $U_i = V_i \intersect Y$ with $V_i$ open in $X$.
The family $\ts{V_i}$ has a maximal element $V_n$, and then $U_n = V_n \intersect Y$ is maximal in the chain.

**(d)** Decompose $X = \Union_{i \leq n} C_i$ into irreducible components.
Each $C_i$ is Hausdorff, and an irreducible Hausdorff space is a point: if $x \neq y$ in $C_i$ had disjoint neighbourhoods $U \ni x$, $V \ni y$, then $U$ would be a nonempty open that is not dense, contradicting irreducibility.
So $X$ is a finite union of closed points, hence finite and discrete.
:::
