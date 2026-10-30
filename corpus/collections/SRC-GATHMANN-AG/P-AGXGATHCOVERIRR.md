---
schema: qual/card@1
id: P-AGXGATHCOVERIRR
kind: problem
title: Connectedness and irreducibility from a pairwise intersecting open cover
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Connectedness
  - Open Covers
relations: []
review: draft
---

::: {.problem}
Let $\theset{U_i}_{i\in I} \covers X$ be an open cover of a topological space with $U_i \intersect U_j \neq \emptyset$ for every $i, j$.

(a) Show that if $U_i$ is connected for every $i$ then $X$ is connected.

(b) Show that if $U_i$ is irreducible for every $i$ then $X$ is irreducible.
:::

::: {.solution}
Assume $X\neq\emptyset$, so that $I\neq\emptyset$; fix $i_0\in I$.

::: pf

::: {.pf-step}
If every $U_i$ is connected, then $X$ is connected.

::: pf-proof

::: {.pf-step #each-in-one}
Let $X=X_1\coprod X_2$ with $X_1,X_2$ disjoint and open. Then each $U_i$ lies in $X_1$ or in $X_2$.

::: pf-proof
The sets $U_i\intersect X_1$ and $U_i\intersect X_2$ are disjoint, open in $U_i$, and their union is $U_i$. Since $U_i$ is connected, one of them is empty, so $U_i$ lies in the other one.
:::

:::

::: {.pf-step #all-in-one}
All $U_i$ lie in the same piece.

::: pf-proof
By step [](#each-in-one){.pf-ref}, relabel so that $U_{i_0}\subseteq X_1$. For any $i$, the set $U_i\intersect U_{i_0}$ is nonempty by hypothesis and lies in $X_1$, so $U_i$ meets $X_1$. Since $U_i$ lies in one of $X_1$, $X_2$ and $X_1\intersect X_2=\emptyset$, we get $U_i\subseteq X_1$.
:::

:::

::: pf-qed
By step [](#all-in-one){.pf-ref}, $X=\Union_i U_i\subseteq X_1$, so $X_2=\emptyset$. Hence $X$ has no decomposition into two nonempty disjoint open subsets, and $X$ is connected.
:::

:::

:::

::: {.pf-step}
If every $U_i$ is irreducible, then $X$ is irreducible.

::: pf-proof

::: {.pf-step #irr-criterion}
A nonempty space $Z$ is irreducible if and only if any two nonempty open subsets of $Z$ meet.

::: pf-proof
If $Z=F_1\union F_2$ with $F_1,F_2$ proper closed subsets, then $Z\sm F_1$ and $Z\sm F_2$ are nonempty open sets with $(Z\sm F_1)\intersect(Z\sm F_2)=Z\sm(F_1\union F_2)=\emptyset$. Conversely, if $A,B$ are nonempty disjoint open subsets, then $Z=(Z\sm A)\union(Z\sm B)$ is a union of two proper closed subsets.
:::

:::

::: {.pf-step #meet-in-Ui}
Let $U,V\subseteq X$ be nonempty and open. Choose $i,j$ with $U\intersect U_i\neq\emptyset$ and $V\intersect U_j\neq\emptyset$. Then $U\intersect U_i\intersect U_j\neq\emptyset$.

::: pf-proof
Such $i,j$ exist because the $U_i$ cover $X$. The sets $U\intersect U_i$ and $U_i\intersect U_j$ are open in $U_i$; the first is nonempty by the choice of $i$ and the second by hypothesis. By step [](#irr-criterion){.pf-ref} applied to the irreducible space $U_i$, they meet.
:::

:::

::: {.pf-step #meet-in-Uj}
With $U,V,i,j$ as in step [](#meet-in-Ui){.pf-ref}, $U\intersect V\neq\emptyset$.

::: pf-proof
The sets $U\intersect U_i\intersect U_j$ and $V\intersect U_j$ are open in $U_j$. The first is nonempty by step [](#meet-in-Ui){.pf-ref} and the second by the choice of $j$. By step [](#irr-criterion){.pf-ref} applied to the irreducible space $U_j$, they have a common point, and that point lies in $U\intersect V$.
:::

:::

::: pf-qed
$X$ is nonempty, and by step [](#meet-in-Uj){.pf-ref} any two nonempty open subsets of $X$ meet. By step [](#irr-criterion){.pf-ref}, $X$ is irreducible.
:::

:::

:::

:::
:::
