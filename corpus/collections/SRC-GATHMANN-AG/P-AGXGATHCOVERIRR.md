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
Let $\ts{U_i}_{i\in I} \covers X$ be an open cover of a topological space with $U_i \intersect U_j \neq \emptyset$ for every $i, j$.

a. Show that if $U_i$ is connected for every $i$ then $X$ is connected.

b. Show that if $U_i$ is irreducible for every $i$ then $X$ is irreducible.
:::

::: {.solution}
**Part a**:
Suppose toward a contradiction that $X = X_1 {\textstyle\coprod} X_2$ with $X_i$ proper, disjoint, and open.
Since $\ts{U_i} \covers X$, for each $j\in I$ this forces $U_j \subseteq X_1$ or $U_j \subseteq X_2$, since otherwise $U_j \intersect X_1 \intersect X_2$ would be nonempty.
So without loss of generality (relabeling if necessary), assume $U_j \subseteq X_1$ for some fixed $j$.
Then for every $i\neq j$ we have $U_i \intersect U_j$ nonempty by assumption, so in fact $U_i \subseteq X_1$ for every $i\in I$.
But then $\Union_{i\in I}U_i \subseteq X_1$, and since $\ts{U_i}$ was a cover, this forces $X\subseteq X_1$ and thus $X_2 = \emptyset$.

**Part b**:

**Claim**: $X$ is irreducible $\iff$ any two nonempty open subsets intersect.

Otherwise, if $U, V \subset X$ are open, nonempty and disjoint, then $X\sm U$ and $X\sm V$ are proper and closed.
But then $X = \qty{X\sm U} \union \qty{X\sm V}$ is a union of proper closed subsets, forcing $X$ to be reducible.

So it suffices to show that if $U, V\subset X$ are nonempty and open, then $U\intersect V$ is nonempty.
Since $\ts{U_i} \covers X$, we can find a pair $i, j$ such that there is at least one point in $U\intersect U_i$ and one point in $V \intersect U_j$.

By assumption $U_i\intersect U_j$ is nonempty, so both $U\intersect U_i$ and $U_j \intersect U_i$ are nonempty open subsets of $U_i$.
Since $U_i$ was assumed irreducible, they must intersect, so there exists a point
\[
x_0 \in \qty{U\intersect U_i} \intersect \qty{U_j \intersect U_i} = U\intersect \qty{U_i \intersect U_j} \da \tilde U
.\]

Similarly $\tilde U \intersect V$ and $U_j \intersect V$ are nonempty open subsets of $V$, and thus intersect.
So there is a point
\[
\tilde x_0 \in \qty{\tilde U \intersect V} \intersect \qty{U_j \intersect V} = \tilde U\intersect V = U\intersect V \intersect \qty{U_i \intersect U_j}
,\]
and in particular $\tilde x_0 \in U\intersect V$ as desired.
:::

::: {.remark}
Erratum: several steps above are false or circular.

- In part a, $X_1\intersect X_2$ is empty by assumption, so "otherwise $U_j\intersect X_1\intersect X_2$ would be nonempty" gives no reason. The reason $U_j$ lies in one of $X_1$, $X_2$ is that $U_j=(U_j\intersect X_1)\coprod(U_j\intersect X_2)$ is a decomposition of the connected space $U_j$ into disjoint open subsets; likewise $U_i\subseteq X_1$ because $U_i$ lies in one of $X_1$, $X_2$ and meets $U_j\subseteq X_1$.
- In the source the complements $X\sm U$ and $X\sm V$ are written as a disjoint union; they need not be disjoint, and only their union is used.
- In part b the second intersection step works in $V$, which is not assumed irreducible, and uses the nonemptiness of $\tilde U\intersect V$, which is what is being proved. The irreducible space to use is $U_j$: the sets $\tilde U\intersect U_j=U\intersect U_i\intersect U_j$ (which contains $x_0$) and $V\intersect U_j$ are nonempty open subsets of $U_j$, so they meet, and any common point lies in $U\intersect V$.
:::
