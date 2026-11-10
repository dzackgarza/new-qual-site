---
schema: qual/card@1
id: P-AGHCOORDCHAR
kind: problem
title: Which $k$-algebras are affine coordinate rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coordinate Rings
  - Reduced Rings
  - Varieties
relations:
- kind: uses
  target: PR-7OT2Z
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.5 (scan page
    23 of the retained PDF). What was checked: the printed biconditional — B
    is isomorphic to the affine coordinate ring of some algebraic set in A^n
    for some n if and only if B is a finitely generated k-algebra with no
    nilpotent elements — against the card's statement, word for word. No
    difference; no repair needed; the exercise carries no star. What was not
    checked: the solution was read only for consistency with the statement,
    not re-derived.
---

::: {.problem}
Show that a $k$-algebra $B$ is isomorphic to the affine coordinate ring of some algebraic set in $\AA^n$, for some $n$, if and only if $B$ is a finitely generated $k$-algebra with no nilpotent elements.
:::

::: {.solution}
Two facts carry it: an ideal $I$ is radical exactly when $R/I$ is reduced, and $B$ is a finitely generated $k$-algebra exactly when $B \cong k[x_1,\ldots,x_n]/I$ for some $n$ and some ideal $I$.

**($\impliedby$)** Let $B$ be finitely generated and reduced, and present it as $B \cong k[x_1,\ldots,x_n]/I_B$.
Take $Y = V(I_B) \subseteq \AA^n$.
Since $B$ is reduced, $I_B$ is radical, so the Nullstellensatz gives $I(Y) = I(V(I_B)) = \sqrt{I_B} = I_B$ and therefore $A(Y) = k[x_1,\ldots,x_n]/I(Y) \cong B$.

**($\implies$)** If $B = A(Y) = k[x_1,\ldots,x_n]/I(Y)$, the presentation exhibits $B$ as a finitely generated $k$-algebra, and $I(Y)$ is radical for any $Y$, so $B$ is reduced.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.5, PDF p. 1: he proves that a finitely generated algebra with no nilpotents is the coordinate ring of $V(I)$, using that the presentation ideal $I$ equals its own radical because the quotient is reduced and that $I(V(I))=\sqrt{I}$ by the Nullstellensatz; the converse, that a coordinate ring is finitely generated and reduced, he leaves unstated.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.5, PDF p. 2, and Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.5, PDF p. 2, prove both directions, Park by showing that the kernel of a surjection $k[x_1,\ldots,x_n]\to B$ is radical exactly when $B$ is reduced.
The proof above isolates the same two facts — radical exactly when reduced, and finite generation exactly as a presentation $k[x_1,\ldots,x_n]/I$ — and runs Park's argument for both directions.
Agree.
:::
