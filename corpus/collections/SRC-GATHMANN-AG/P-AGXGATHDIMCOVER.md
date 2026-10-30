---
schema: qual/card@1
id: P-AGXGATHDIMCOVER
kind: problem
title: Dimension from an open cover, and dimension of subsets of an irreducible variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Krull Dimension
  - Open Covers
  - Irreducibility
relations: []
review: draft
---

::: {.problem}
Let $X$ be a topological space, and show

(a) If $\theset{U_i}_{i\in I}$ is an open cover of $X$, then $\dim X = \sup_{i\in I} \dim U_i$.

(b) If $X$ is an irreducible affine variety and $U\subset X$ is a nonempty open subset, then $\dim X = \dim U$.
Does this hold for any irreducible topological space?
:::

::: {.solution}
The dimension of a topological space is the supremum of the lengths $n$ of chains $Z_0 \subsetneq Z_1 \subsetneq \cdots \subsetneq Z_n$ of nonempty closed irreducible subsets.
Two standard facts are used throughout: the closure of an irreducible subset is irreducible, and a nonempty open subset of an irreducible space is irreducible and dense.

::: pf

::: {.pf-step #monotone}
If $U \subseteq V$ carries the subspace topology, then $\dim U \leq \dim V$.

::: pf-proof
Let $Z_0 \subsetneq \cdots \subsetneq Z_n$ be a chain of nonempty closed irreducible subsets of $U$, and let $\overline{Z_j}$ be the closure of $Z_j$ in $V$.
Each $\overline{Z_j}$ is nonempty, closed and irreducible, and $\overline{Z_j} \subseteq \overline{Z_{j+1}}$.
Since $Z_j$ is closed in $U$, $Z_j = \overline{Z_j} \intersect U$, so $\overline{Z_j} = \overline{Z_{j+1}}$ would give $Z_j = Z_{j+1}$.
So the closures form a chain of length $n$ in $V$, and $\dim V \geq n$.
:::

:::

::: {.pf-step}
Part (a): $\dim X = \sup_{i\in I} \dim U_i$.

::: pf-proof
By step [](#monotone){.pf-ref}, $\dim U_i \leq \dim X$ for each $i$, so $\sup_i \dim U_i \leq \dim X$.

For the reverse inequality, let $Z_0 \subsetneq \cdots \subsetneq Z_n$ be a chain of nonempty closed irreducible subsets of $X$.
Choose $p \in Z_0$ and an index $i$ with $p \in U_i$, and put $A_j \coloneqq Z_j \intersect U_i$.
Each $A_j$ contains $p$, so it is a nonempty open subset of the irreducible space $Z_j$; hence $A_j$ is irreducible and dense in $Z_j$.
Each $A_j$ is closed in $U_i$, and $A_0 \subseteq \cdots \subseteq A_n$.
If $A_j = A_{j+1}$, then by density $Z_{j+1} = \overline{A_{j+1}} = \overline{A_j} = Z_j$, which is false.
So $A_0 \subsetneq \cdots \subsetneq A_n$ is a chain of length $n$ in $U_i$, and $\sup_i \dim U_i \geq n$.
Since the chain in $X$ was arbitrary, $\sup_i \dim U_i \geq \dim X$.
:::

:::

::: {.pf-step}
Part (b): if $X$ is an irreducible affine variety and $U \subseteq X$ is nonempty and open, then $\dim U = \dim X$.

::: pf-proof
The complement $X \sm U$ is $V(f_1,\ldots,f_r)$ for some $f_1,\ldots,f_r \in A(X)$.
Since $U$ is nonempty, $X \sm U \neq X$, so some $f \coloneqq f_l$ is not the zero function.
Then the principal open set $D(f)$ is nonempty and contained in $U$.
$D(f)$ is an irreducible affine variety with coordinate ring $A(X)_f$, whose field of fractions equals that of $A(X)$, namely the function field $K(X)$.
The dimension of an irreducible affine variety is the transcendence degree of its function field over $k$, so $\dim D(f) = \operatorname{trdeg}_k K(X) = \dim X$.
By step [](#monotone){.pf-ref}, $\dim X = \dim D(f) \leq \dim U \leq \dim X$.
:::

:::

::: {.pf-step}
Part (b): the equality $\dim U = \dim X$ fails for a general irreducible topological space.

::: pf-proof
Let $X \coloneqq \theset{a,b}$ with open sets $\emptyset$, $\theset{a}$, $X$.
Its closed sets are $\emptyset$, $\theset{b}$, $X$.
$X$ is irreducible, because its only nonempty proper closed subset is $\theset{b}$ and $\theset{b} \union \theset{b} \neq X$.
The chain $\theset{b} \subsetneq X$ has length $1$ and no chain is longer, so $\dim X = 1$.
The nonempty open subset $U \coloneqq \theset{a}$ is a single point, so $\dim U = 0 \neq \dim X$.
:::

:::

:::
:::
