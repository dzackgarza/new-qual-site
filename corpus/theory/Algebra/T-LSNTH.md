---
schema: qual/card@1
id: T-LSNTH
kind: theorem
title: Existence of a primary decomposition in a Noetherian ring
slogan: 'Every proper ideal of a Noetherian ring is a finite intersection of primary ideals.'
classification:
  areas:
  - algebra
  topics:
  - Primary Ideals
  - Noetherian Rings
relations: []
review: draft
---

::: {.theorem}
Let $R$ be a [[D-TZXBO|Noetherian]] ring and $I\subsetneq R$ a proper ideal.
Then $I$ is a finite intersection of [[D-JGYK4|primary ideals]].
:::

::: {.proof}
Call a proper ideal $J$ *irreducible* if $J=J_1\intersect J_2$ for ideals $J_1,J_2$ forces $J=J_1$ or $J=J_2$.

First, every proper ideal is a finite intersection of irreducible ideals.
Otherwise the set of proper ideals that are not is nonempty, and since $R$ is Noetherian it has a maximal element $J$; being reducible, $J=J_1\intersect J_2$ with both $J_i$ strictly containing $J$, and by maximality each $J_i$ is a finite intersection of irreducible ideals, so $J$ is one too, a contradiction.

Second, an irreducible ideal is primary.
Let $J$ be irreducible, let $xy\in J$ with $x\notin J$, and consider the ascending chain
$$
(J:y)\ \subseteq\ (J:y^2)\ \subseteq\ \cdots,
$$
which stabilizes because $R$ is Noetherian: choose $n\geq 1$ with $(J:y^n)=(J:y^{n+1})$.
Then $J = (J+\generators x)\intersect(J+\generators{y^n})$: one inclusion is clear, and if $z=i_1+a x=i_2+b y^n$ lies in the right-hand side, then $zy=i_1y+axy\in J$ and $zy=i_2y+by^{n+1}$, so $by^{n+1}\in J$, hence $b\in(J:y^{n+1})=(J:y^n)$ and $z=i_2+by^n\in J$.
The ideal $J+\generators x$ strictly contains $J$, so irreducibility forces $J=J+\generators{y^n}$, that is $y^n\in J$.
Hence some power of $y$ lies in $J$ whenever $xy\in J$ and $x\notin J$, which is primarity.

Composing the two steps writes $I$ as a finite intersection of primary ideals.
:::
