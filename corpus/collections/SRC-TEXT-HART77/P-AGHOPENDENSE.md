---
schema: qual/card@1
id: P-AGHOPENDENSE
kind: problem
title: Opens are dense in an irreducible space, and closures stay irreducible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Zariski Topology
relations:
- kind: uses
  target: D-9DIKB
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.6 (scan page
    23 of the retained PDF). What was checked: both printed sentences — that a
    nonempty open subset of an irreducible space is dense and irreducible, and
    that a subset which is irreducible in its induced topology has irreducible
    closure — against the card, which states them as two sentences of the same
    content. No difference; no repair needed; the exercise carries no star.
    What was not checked: the solution was read only for consistency, not re-
    derived.
---

::: {.problem}
Any nonempty open subset of an irreducible topological space is dense and irreducible.
If $Y$ is a subset of a topological space $X$ which is irreducible in its induced topology, then the closure $\bar{Y}$ is also irreducible.
:::

::: {.solution}
**Density.** Let $U \subseteq X$ be open and nonempty with $X$ irreducible, and suppose $\cl_X(U) \neq X$.
Then
$$
X = (X \sm U) \union \cl_X(U)
$$
writes $X$ as a union of two proper closed subsets, contradicting irreducibility.

**Irreducibility of opens.** Suppose $U = (A \intersect U) \union (B \intersect U)$ with $A, B$ closed in $X$.
Then $X = A \union B \union (X \sm U)$ is a union of three closed sets, so by irreducibility $X$ equals one of them.
It is not $X \sm U$, since $U \neq \emptyset$; so $X = A$ or $X = B$, and $U = A \intersect U$ or $U = B \intersect U$.

**Closures.** Suppose $Y$ is irreducible and write $\cl_X(Y) = A \union B$ with $A, B$ closed in $X$.
Intersecting with $Y$ gives $Y = (A \intersect Y) \union (B \intersect Y)$, so by irreducibility $Y \subseteq A \intersect Y \subseteq A$ after relabelling.
Then $\cl_X(Y) \subseteq \cl_X(A) = A$, so the decomposition was trivial and $\cl_X(Y)$ is irreducible.
:::

::: {.remark}
Irreducible is strictly stronger than connected: connected forbids a decomposition into two proper *disjoint* closed sets, irreducible forbids it without disjointness.
$V(xy)$ is connected and reducible.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.6, PDF p. 1: for density he writes $X=(X\sm U)\cup\bar U$ and concludes $\bar U=X$; for irreducibility of $U$ he uses that a decomposition $U\subseteq C_1\cup C_2$ gives $X=\bar C_1\cup\bar C_2$; for the closure he uses $X=\bar C_1\cup\bar C_2$ on a decomposition of $\bar Y$.
Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.6, PDF p. 3, proves the same two claims, with a lemma that a space is irreducible when every nonempty open set is dense.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.6, PDF p. 2, answers only "See [3]" and gives no proof.
The proof above runs Borcherds' density and closure arguments and replaces his closure step by the finite-union form of irreducibility, $X=A\cup B\cup(X\sm U)$.
Agree with Borcherds and Park; Troiani contains no solution to compare.
:::
