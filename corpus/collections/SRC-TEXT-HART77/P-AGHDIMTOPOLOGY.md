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
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.10 (scan page
    23 of the retained PDF). What was checked: parts (a) through (e) against
    the card — dim Y <= dim X for a subset; dim X = sup dim U_i for an open
    cover; a dense open subset of smaller dimension; a closed subset of an
    irreducible finite-dimensional space with dim Y = dim X being the space;
    and a Noetherian space of infinite dimension. All five agree; the card
    renders (c) with the same content in a different order of clauses. No
    repair needed; no star. What was not checked: the solution was read only
    for consistency, not re-derived.
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

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.10, PDF p. 1: (a) takes closures of a chain in $Y$; (b) selects a cover member meeting the bottom of a chain in $X$, intersects the chain with it and uses Exercise 1.6; (c) is the two-point space with one open point; (d) appends $X$ to a chain of maximal length in $Y$; (e) is the positive integers with the initial segments as proper closed sets.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.10, PDF p. 3: (a) and (b) are "solved in [3]"; (c) is the Sierpiński space; (d) is one sentence; (e) is $\NN$ with initial segments.
Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.10, PDF pp. 4--5: (a), (b), (c), (d) as above, and for (e) the localization of a polynomial ring in infinitely many variables at the complement of the union of the ideals $(x_{m_i+1},\ldots,x_{m_{i+1}})$, whose quotients have unbounded height.
The proof above is Borcherds' argument part for part, with the strictness of the chains in (a) and (b) checked through $\bar Z_i\cap Y=Z_i$ and through densities in the irreducible $C_j$, and with the topology in (e) verified to be closed under finite unions and arbitrary intersections as well as Noetherian.
Agree; the only difference is that Borcherds' (e) and Park's (e) are different examples, and the card keeps Borcherds'.
:::
