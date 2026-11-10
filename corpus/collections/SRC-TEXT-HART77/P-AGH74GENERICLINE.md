---
schema: qual/card@1
id: P-AGH74GENERICLINE
kind: problem
title: Almost every line meets a plane curve of degree $d$ in exactly $d$ points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Intersection Theory
  - Degree
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.4 and its hint together with Exercises I.5.4 and I.7.3 in the Hartshorne source. The proof constructs the closed exceptional locus from the dual curve and the pencils through singular points, then uses total line-curve intersection multiplicity d to count distinct points.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Given a curve $Y$ of degree $d$ in $\PP^2$, show that there is a nonempty open subset $U$ of $\dualof{(\PP^2)}$ in its Zariski topology such that each $L \in U$ meets $Y$ in exactly $d$ points.

*Hint:* Show that the set of lines in $\dualof{(\PP^2)}$ which are either tangent to $Y$ or pass through a singular point of $Y$ is contained in a proper closed subset.

This result shows that one could have defined the degree of $Y$ to be the number $d$ such that almost all lines in $\PP^2$ meet $Y$ in $d$ points, where "almost all" refers to a nonempty open subset of the dual projective space.
:::

::: {.solution}
For a point $P\in\PP^2$, write
$$
\dualof{P}=\{L\dualof{\in(\PP^2)}:P\in L\}.
$$
This is a projective line in the dual plane.

If $d=1$, then $Y$ is a line.
Removing from $\dualof{(\PP^2)}$ the single point representing $Y$ leaves a nonempty open set, and every remaining line meets $Y$ in exactly one point.
Thus assume below that $d>1$.

::: pf

::: {.pf-step #singular-locus-finite}
The singular locus $\Sing Y$ is finite.

::: pf-proof
The singular locus is a proper closed subset of the irreducible curve $Y$.
Every proper closed subset of a noetherian irreducible curve has dimension zero and therefore consists of finitely many closed points.
Hence
$$
\Sing Y=\{P_1,\ldots,P_m\}
$$
for some $m\ge0$.
:::

:::

::: {.pf-step #singular-lines-proper-closed}
The set of lines passing through a singular point of $Y$ is a proper closed subset of $\dualof{(\PP^2)}$.

::: pf-proof
By step [](#singular-locus-finite){.pf-ref} it is
$$
B_{\mathrm{sing}}=\dualof{P_1}\cup\cdots\cup \dualof{P_m}.
$$
Each $\dualof{P_i}$ is a projective line in the dual projective plane, hence closed and proper.
Their finite union is closed and has dimension at most one, so it is proper.
:::

:::

::: {.pf-step #tangent-lines-proper-closed}
The set of tangent lines to nonsingular points of $Y$ is contained in a proper closed subset of $\dualof{(\PP^2)}$.

::: pf-proof
By [[P-AGH73DUALCURVE|Exercise I.7.3]], the tangent-line assignment
$$
\gamma:\Reg Y\dualof{\longrightarrow(\PP^2)}
$$
is a morphism, and the closure of its image is the dual algebraic set $\dualof{Y}$.
Since $\Reg Y$ is a curve, the dimension of the closure of its image is at most one.
Thus
$$
\dualof{Y}\dualof{\subsetneq(\PP^2)},
$$
which has dimension two.
Every tangent line at a nonsingular point lies in $\dualof{Y}$ by construction.
:::

:::

::: {.pf-step #generic-open-set}
There is a nonempty open subset of the dual plane consisting of lines which meet no singular point and are tangent nowhere along $\Reg Y$.

::: pf-proof
Put
$$
B=\dualof{Y}\cup B_{\mathrm{sing}}.
$$
By steps [](#singular-lines-proper-closed){.pf-ref} and [](#tangent-lines-proper-closed){.pf-ref}, $B$ is a finite union of closed subsets of dimension at most one.
Hence it is a proper closed subset of the irreducible two-dimensional projective plane $\dualof{(\PP^2)}$.
Therefore
$$
U=\dualof{(\PP^2)}\setminus B
$$
is nonempty and Zariski open.
By its definition, a line $L\in U$ passes through no singular point of $Y$ and is not tangent to $Y$ at any nonsingular point.
:::

:::

::: {.pf-step #generic-line-meets-d-points}
Every line $L\in U$ meets $Y$ in exactly $d$ distinct points.

::: pf-proof
Let $L\in U$.
Every point $P\in L\cap Y$ is nonsingular by step [](#generic-open-set){.pf-ref}. Moreover $L$ is not the tangent line at $P$, so Exercise I.5.4 together with the tangent characterization of I.7.3 gives
$$
(L.Y)_P=1.
$$

The line $L$ is not a component of $Y$: if $Y$ itself is a line, then the corresponding point of the dual plane belongs to $\dualof{Y}$ and is excluded from $U$; otherwise irreducibility already prevents a line component.
Exercise I.5.4(c) therefore gives the total intersection number
$$
\sum_{P\in L\cap Y}(L.Y)_P=d.
$$
Every summand equals one, so the number of distinct intersection points is exactly $d$.
Thus
$$
\boxed{\#(L\cap Y)=d\qquad(L\in U)}.
$$
:::

:::

::: pf-qed
Step [](#generic-open-set){.pf-ref} constructs the required nonempty open subset $U$, and step [](#generic-line-meets-d-points){.pf-ref} proves the asserted cardinality for every line represented by a point of $U$.
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 7.4, PDF p. 9: "by Ex.\ 5.4, any line not tangent to $Y$ and not passing through a singular point meets $Y$ in exactly $d$ distinct points. As $Y$ has only a finite number of singular points, the lines intersection at least one of these form a proper closed subset of $\PP^{2*}$ (in fact a union of lines). By 7.3 the lines tangent to $Y$ are also contained in a proper closed subset of $\PP^{2*}$, so there is a nonempty open subset $U$ of lines in $\PP^{2*}$ intersecting $Y$ in exactly $d$ points."
William Troiani, *Hartshorne Exercise Solutions* (October 2020), stops at §I.5 and gives no solution to 7.4.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.7.4, PDF p. 57: "using bezout, lines which meet $Y$ transversely at smooth points meet in degree $Y=d$ points; by noetherianness, the singular locus is a finite set of points on $Y$; the lines meeting one of these are a proper closed subset of $\PP^{2*}$; by 7.3, the tangent lines are contained in a proper closed subset of $\PP^{2*}$".
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.7.4, PDF p. 26: "by Bezout's Theorem, any line not tangent to $Y$ and not passing through a singular point meets $Y$ in exactly $d$ distinct points. Since $\operatorname{Sing}Y$ is closed and proper, the lines intersecting with $\operatorname{Sing}Y$ are closed in $(\PP^2)^*$. By ex 3, the tangent lines to $Y$ are contained in proper closed subsets of $(\PP^2)^*$, so there exists $U\ne\emptyset$ open in $(\PP^2)^*$ intersecting $Y$ in $d$ points."
All three are the printed hint. Step [](#singular-lines-proper-closed){.pf-ref} supplies what they assert without argument, that the union of the dual lines is proper because it has dimension at most one in the dual plane; step [](#generic-line-meets-d-points){.pf-ref} supplies the inequality $(L.Y)_P\ge1$ with equality off the tangent, which turns the total multiplicity $d$ of I.5.4(c) into a count of distinct points; and the case $d=1$, where $Y$ itself is the one line to be excluded, is treated before the proof. Matches.
:::
