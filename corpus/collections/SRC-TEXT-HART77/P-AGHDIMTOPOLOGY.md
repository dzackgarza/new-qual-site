---
schema: qual/card@1
id: P-AGHDIMTOPOLOGY
kind: problem
title: Dimension under subspaces, open covers, and closed subsets
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Noetherian Spaces
  - Irreducibility
relations:
- kind: uses
  target: D-5LJUX
review: draft
---

::: {.problem}
(a) If $Y$ is any subset of a topological space $X$, then $\dim Y \leq \dim X$.

(b) If $X$ is covered by open subsets $\theset{U_i}$, then $\dim X = \sup_i \dim U_i$.

(c) Give an example of a topological space $X$ with a dense open subset $U$ such that $\dim U < \dim X$.

(d) If $Y$ is a closed subset of an irreducible finite-dimensional space $X$ with $\dim Y = \dim X$, then $Y = X$.

(e) Give an example of a Noetherian topological space of infinite dimension.
:::

::: {.solution}
**(a)** Let $Z_0 \subsetneq \cdots \subsetneq Z_n$ be a chain of irreducible closed subsets of $Y$.
Their closures $\bar Z_i$ in $X$ are irreducible by Ex. 1.6 and closed.
Since $Z_i$ is closed in $Y$, one has $\bar Z_i \intersect Y = Z_i$, so the chain $\bar Z_0 \subsetneq \cdots \subsetneq \bar Z_n$ is strict.
Hence $\dim X \geq n$, and so $\dim X \geq \dim Y$.

**(b)** By (a), $\sup_i \dim U_i \leq \dim X$.
Conversely, let $C_0 \subsetneq \cdots \subsetneq C_n$ be a chain of irreducible closed subsets of $X$, and choose $i$ with $U_i \intersect C_0 \neq \emptyset$.
Each $C_j \intersect U_i$ is a nonempty open subset of the irreducible space $C_j$, hence irreducible and dense in $C_j$ by Ex. 1.6, and it is closed in $U_i$.
Its closure in $X$ is $C_j$, so the chain $C_0 \intersect U_i \subsetneq \cdots \subsetneq C_n \intersect U_i$ is strict, and $\dim U_i \geq n$.

**(c)** Let $X = \theset{a, b}$ with open sets $\emptyset$, $\theset{a}$ and $X$.
The closed sets are $\emptyset$, $\theset{b}$ and $X$; both $\theset{b}$ and $X$ are irreducible, so $\theset{b} \subsetneq X$ gives $\dim X = 1$.
The open set $U = \theset{a}$ is dense, since the only closed set containing it is $X$, and $\dim U = 0$.

**(d)** Let $Z_0 \subsetneq \cdots \subsetneq Z_n$ be a chain of irreducible closed subsets of $Y$ with $n = \dim Y$.
These are closed in $X$ because $Y$ is.
If $Z_n \neq X$, then appending the irreducible closed set $X$ gives a chain of length $n + 1$ in $X$, contradicting $\dim X = n$.
So $Z_n = X$, and $X = Z_n \subseteq Y$.

**(e)** Take $X = \ZZ_{\geq 0}$ with closed sets $\emptyset$, $X$, and $\theset{1,\ldots,i}$ for each $i \geq 1$.
These sets are closed under finite unions and arbitrary intersections, so they define a topology.
Every closed set other than $\emptyset$ is irreducible, because the closed sets are totally ordered.
The chain $\theset{1} \subsetneq \theset{1,2} \subsetneq \cdots$ gives chains of every length, so $\dim X = \infty$.
A strictly descending chain of closed sets has at most one member equal to $X$, and below that its members are $\theset{1,\ldots,i}$ with decreasing $i$, so it is finite and $X$ is Noetherian.
:::
