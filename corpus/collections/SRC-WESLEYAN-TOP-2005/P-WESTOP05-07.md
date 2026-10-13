---
schema: qual/card@1
id: P-WESTOP05-07
kind: problem
title: Fundamental group, first homology, and classification of an octagon quotient
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Take an octagon and identify its edges according to the cyclic word
\[
ab^{-1}cdc^{-1}bd^{-1}a.
\]
Find the fundamental group and first homology group of the resulting surface, and identify the surface in the standard classification.
:::

::: {.solution}
Label the octagon vertices cyclically by
\[
v_0,v_1,\dots,v_7,
\]
so the boundary edges are
\[
[v_0,v_1],\ [v_1,v_2],\dots,[v_7,v_0].
\]

The boundary word is
\[
a\,b^{-1}\,c\,d\,c^{-1}\,b\,d^{-1}\,a.
\]

## Vertex identifications

<1>1. The two \(a\)-edges identify
\[
v_0\sim v_7
\qquad\text{and}\qquad
v_1\sim v_0.
\]

::: {.proof}
The first \(a\)-edge is oriented
\[
v_0\to v_1,
\]
and the final \(a\)-edge is oriented
\[
v_7\to v_0.
\]
Matching the arrows identifies starts with starts and ends with ends.
:::

<1>2. The two \(b\)-edges identify
\[
v_2\sim v_5
\qquad\text{and}\qquad
v_1\sim v_6.
\]

::: {.proof}
The boundary edge \([v_1,v_2]\) is labeled \(b^{-1}\), so its \(b\)-arrow
runs
\[
v_2\to v_1.
\]
The other \(b\)-edge runs
\[
v_5\to v_6.
\]
Match starts and ends.
:::

<1>3. The two \(c\)-edges identify
\[
v_2\sim v_5
\qquad\text{and}\qquad
v_3\sim v_4.
\]

::: {.proof}
The \(c\)-edge \([v_2,v_3]\) is oriented
\[
v_2\to v_3,
\]
while the edge \([v_4,v_5]\) labeled \(c^{-1}\) has \(c\)-orientation
\[
v_5\to v_4.
\]
:::

<1>4. The two \(d\)-edges identify
\[
v_3\sim v_7
\qquad\text{and}\qquad
v_4\sim v_6.
\]

::: {.proof}
The \(d\)-edge \([v_3,v_4]\) is oriented
\[
v_3\to v_4,
\]
while the edge \([v_6,v_7]\) labeled \(d^{-1}\) has \(d\)-orientation
\[
v_7\to v_6.
\]
:::

<1>5. Hence there are exactly two vertex classes:
\[
\boxed{
A=\{v_0,v_1,v_3,v_4,v_6,v_7\}}
\]
and
\[
\boxed{
B=\{v_2,v_5\}}.
\]

::: {.proof}
Steps <1>1--<1>4 generate the displayed equivalence classes, and no listed
identification connects a vertex in \(B\) to one in \(A\).
:::

## Euler characteristic and surface type

<1>6. The quotient has
\[
\boxed{
V=2,\qquad E=4,\qquad F=1}.
\]

::: {.proof}
There are two vertex classes by step <1>5, four paired edge classes
\(a,b,c,d\), and one octagon interior.
:::

<1>7. Therefore
\[
\boxed{
\chi=V-E+F=2-4+1=-1}.
\]

::: {.proof}
Apply the cellular formula for Euler characteristic.
:::

<1>8. The quotient surface is nonorientable.

::: {.proof}
The two occurrences of \(a\) in the boundary word have the same orientation.
Thus the corresponding edge pair is glued with the boundary directions
matched rather than reversed. In the polygon classification of surfaces,
such a same-direction pair produces a crosscap, hence nonorientability.
:::

<1>9. A closed connected nonorientable surface of genus \(k\) has
\[
\chi=2-k.
\]

::: {.proof}
Its standard polygon has one vertex, \(k\) edge classes, and one face, so
\[
\chi=1-k+1=2-k.
\]
:::

<1>10. Since
\[
-1=2-k,
\]
one has
\[
\boxed{k=3}.
\]

::: {.proof}
Solve for \(k\).
:::

<1>11. Hence the quotient is
\[
\boxed{
N_3
=
\mathbb{RP}^2\#\mathbb{RP}^2\#\mathbb{RP}^2}.
\]

::: {.proof}
The quotient is closed and connected, is nonorientable by step <1>8, and
has nonorientable genus \(3\) by step <1>10. Apply the classification of
closed surfaces.
:::

## Fundamental group

<1>12. In the quotient \(1\)-skeleton, the \(a\)- and \(d\)-edges are loops
at \(A\), while the \(b\)- and \(c\)-edges join \(B\) to \(A\).

::: {.proof}
From the vertex classes in step <1>5:
the \(a\)-edge has endpoints in \(A\), the \(d\)-edge has endpoints in \(A\),
and representatives for \(b,c\) have one endpoint in \(B\) and the other in
\(A\).
:::

<1>13. Choose the \(c\)-edge as a maximal tree in the \(1\)-skeleton.

::: {.proof}
There are two vertices \(A,B\), and the \(c\)-edge joins them. A single edge
joining the two vertices is a maximal tree.
:::

<1>14. Collapsing this tree identifies \(A\) and \(B\) and does not change
the fundamental group.

::: {.proof}
Collapsing a maximal tree in a connected graph is a homotopy equivalence and
is the standard step in obtaining a presentation from a CW complex.
:::

<1>15. After setting \(c=1\), the \(2\)-cell attaching word becomes
\[
\boxed{
a\,b^{-1}\,d\,b\,d^{-1}\,a}.
\]

::: {.proof}
Start with
\[
a\,b^{-1}\,c\,d\,c^{-1}\,b\,d^{-1}\,a
\]
and replace \(c,c^{-1}\) by the identity after the tree collapse.
:::

<1>16. Thus
\[
\boxed{
\pi_1
\cong
\left\langle
a,b,d
\ \middle|\
a\,b^{-1}dbd^{-1}a=1
\right\rangle}.
\]

::: {.proof}
The collapsed \(1\)-skeleton is a wedge of three circles \(a,b,d\), and the
single \(2\)-cell imposes the relation from step <1>15.
:::

<1>17. Cyclically conjugating the relator gives the equivalent presentation
\[
\boxed{
\pi_1
\cong
\left\langle
a,b,d
\ \middle|\
a^2[b^{-1},d]=1
\right\rangle}.
\]

::: {.proof}
The relator
\[
a\,b^{-1}dbd^{-1}a
\]
is cyclically conjugate to
\[
a^2b^{-1}dbd^{-1}
=
a^2[b^{-1},d].
\]
Replacing a relator by a conjugate does not change its normal closure.
:::

<1>18. By the surface classification, this group is also isomorphic to the
standard nonorientable genus-\(3\) surface group
\[
\boxed{
\left\langle
x,y,z
\ \middle|\
x^2y^2z^2=1
\right\rangle}.
\]

::: {.proof}
Step <1>11 identifies the underlying surface with
\[
N_3=\#^3\mathbb{RP}^2,
\]
whose standard polygon presentation has the displayed fundamental group.
:::

## First homology

<1>19. Abelianizing the presentation in step <1>17 kills the commutator
\[
[b^{-1},d].
\]

::: {.proof}
Every commutator is trivial in an abelian group.
:::

<1>20. Hence the only remaining relation in the abelianization is
\[
\boxed{2a=0}.
\]

::: {.proof}
The relator
\[
a^2[b^{-1},d]
\]
becomes
\[
a^2
\]
after abelianization.
:::

<1>21. Therefore
\[
\boxed{
H_1
\cong
\pi_1^{\mathrm{ab}}
\cong
\mathbb Z\langle b\rangle
\oplus
\mathbb Z\langle d\rangle
\oplus
\mathbb Z/2\langle a\rangle}.
\]

::: {.proof}
The generators \(b,d\) remain free, while \(a\) is subject only to
\(2a=0\).
:::

<1>22. Thus
\[
\boxed{
H_1
\cong
\mathbb Z^2\oplus\mathbb Z/2}.
\]

::: {.proof}
This is the group in step <1>21 written in standard form.
:::

<1>23. Q.E.D.

::: {.proof}
Step <1>17 gives a presentation of the fundamental group, step <1>22 gives
the first homology group, and step <1>11 identifies the surface as
\(\#^3\mathbb{RP}^2\).
:::
:::
