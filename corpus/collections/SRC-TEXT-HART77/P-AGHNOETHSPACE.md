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

::: {.problem}
(a) Show that the following are equivalent for a topological space $X$:

- $X$ is Noetherian;

- every nonempty family of closed subsets has a minimal element;

- $X$ satisfies the ascending chain condition on open subsets;

- every nonempty family of open subsets has a maximal element.

(b) A Noetherian topological space is quasicompact.

(c) Any subset of a Noetherian topological space is Noetherian in its induced topology.

(d) A Noetherian space which is also Hausdorff is a finite set with the discrete topology.
:::

::: {.solution}
**(a)** Call the conditions (i)-(iv) in the order listed.
(i) $\implies$ (ii): given a nonempty family of closed sets, choose $Y_1$ in it; if it is not minimal there is $Y_2 \subsetneq Y_1$ in the family, and so on.
The resulting descending chain stabilises, and where it stabilises is a minimal element.
(ii) $\implies$ (i): the members of a descending chain of closed sets form a nonempty family, and the chain stabilises at a minimal member.
(i) $\iff$ (iii) and (ii) $\iff$ (iv) follow by taking complements.

**(b)** Let $\theset{U_i}$ be an open cover of $X$.
By (iv), the family of finite unions of the $U_i$ has a maximal element $V$.
If $V \neq X$, some $U_i \not\subseteq V$, and $V \union U_i$ is a larger finite union, a contradiction.
So $V = X$ is a finite subcover.

**(c)** Let $Y \subseteq X$ and let $U_1 \subseteq U_2 \subseteq \cdots$ be opens in $Y$, so $U_i = V_i \intersect Y$ with $V_i$ open in $X$.
Put $W_i = V_1 \union \cdots \union V_i$.
Since the $U_i$ increase, $W_i \intersect Y = U_i$.
The chain $W_1 \subseteq W_2 \subseteq \cdots$ stabilises by (iii), so the chain $U_i$ stabilises.

**(d)** By (ii), $X$ is a finite union $X = \Union_{i \leq n} C_i$ of irreducible closed subsets.
An irreducible Hausdorff space is a point: if $x \neq y$ in $C_i$ had disjoint open neighbourhoods $U \ni x$, $V \ni y$ in $C_i$, then $U$ would be a nonempty open subset that is not dense, contradicting Ex. 1.6.
So $X$ is finite, and a finite Hausdorff space is discrete, because each point is closed and so every subset is closed.
:::
