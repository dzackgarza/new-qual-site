---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-17
kind: problem
title: The surface with polygonal symbol $xy^{-1}x^{-1}zwz^{-1}\nu yw^{-1}\nu^{-1}$, and
  classification of closed surfaces by even-sided polygons
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Classification
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part Two, question 5 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. A finite polygon
    presentation classifies compact connected surfaces without boundary; the
    literal phrase "surfaces without boundary" is broader if noncompact surfaces
    are allowed.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Verified two vertex classes, five edge classes, and one face, giving chi=-2.
    Every edge label occurs once with each orientation, so the surface is
    orientable and has genus 2. Rewrote the polygon-classification portion with
    distinct Lamport labels and the compactness qualification.
---

::: {.problem}
(i) The polygonal symbol of a certain surface without boundary is $xy^{-1}x^{-1}zwz^{-1}\nu yw^{-1}\nu^{-1}$.
Identify the surface.
What is its Euler characteristic?

(ii) Explain how polygons with an even number of sides may be used to classify surfaces without boundary.
You do not need to give detailed proofs.
:::

::: {.solution}
<1>1. The symbol has $10$ sides, and each of the five letters $x, y, z, w, \nu$ appears once with a positive and once with a negative exponent.
::: {.proof}
The boundary word is
\[
xy^{-1}x^{-1}zwz^{-1}\nu yw^{-1}\nu^{-1}.
\]
The five labels are $x,y,z,w,\nu$, and inspection shows that each occurs exactly twice, once with exponent $+1$ and once with exponent $-1$.
:::

<1>2. Hence the surface is orientable.
::: {.proof}
For a paired polygon presentation of a surface, an orientation of the polygon interior descends across a paired edge precisely when the two boundary occurrences have opposite directions.
By <1>1, every pair occurs once positively and once negatively, so all edge gluings preserve a global orientation on the quotient.
:::

<1>3. After the edge identifications there are exactly two vertex classes:
\[
\{v_0,v_3,v_6\}
\qquad\text{and}\qquad
\{v_1,v_2,v_4,v_5,v_7,v_8,v_9\},
\]
where $v_0,\ldots,v_9$ are the polygon vertices in boundary order.
::: {.proof}
Matching the directed edge pairs gives
\[
\begin{array}{c|c}
\text{label}&\text{vertex identifications}\\
\hline
x&v_0\sim v_3,\quad v_1\sim v_2,\\
y&v_2\sim v_7,\quad v_1\sim v_8,\\
z&v_3\sim v_6,\quad v_4\sim v_5,\\
w&v_4\sim v_9,\quad v_5\sim v_8,\\
\nu&v_6\sim v_0,\quad v_7\sim v_9.
\end{array}
\]
The first coordinates in the $x,z,\nu$ relations produce
\[
v_0\sim v_3\sim v_6.
\]
The remaining relations produce
\[
v_1\sim v_2\sim v_7\sim v_9\sim v_4\sim v_5\sim v_8.
\]
No displayed relation joins these two classes, so there are exactly two quotient vertices.
:::

<1>4. The quotient has
\[
V=2,
\qquad
E=5,
\qquad
F=1,
\]
and hence
\[
\chi=V-E+F=-2.
\]
::: {.proof}
The vertex count is <1>3.
There is one edge in the quotient for each of the five paired labels, so $E=5$, and the polygon interior gives one $2$-cell, so $F=1$.
Therefore
\[
\chi=2-5+1=-2.
\]
:::

<1>5. The surface is the orientable surface of genus $2$, namely
\[
\boxed{(S^1\times S^1)\#(S^1\times S^1)},
\]
and its Euler characteristic is
\[
\boxed{-2}.
\]
::: {.proof}
By <1>2 the surface is orientable.
The classification theorem for compact connected orientable surfaces gives
\[
\chi=2-2g.
\]
Using <1>4,
\[
-2=2-2g,
\]
so $g=2$.
:::

<1>6. Every compact connected surface without boundary can be represented by a polygon with an even number of sides, with the sides identified in pairs.
::: {.proof}
Take a finite triangulation of the surface and cut along a suitable collection of edges so that the remaining union of triangles is a single polygonal disk.
Every cut edge appears twice on the boundary of this disk, so the boundary sides occur in pairs and their total number is even.
Regluing each pair reconstructs the surface.
:::

<1>7. Cut-and-paste moves reduce every such paired polygon to one of the two normal forms
\[
a_1b_1a_1^{-1}b_1^{-1}\cdots a_gb_ga_g^{-1}b_g^{-1}
\]
or
\[
a_1a_1a_2a_2\cdots a_ka_k.
\]
::: {.proof}
These are the polygonal normal forms in the classification theorem for compact connected surfaces.
The first has every paired edge appearing with opposite orientations and represents the connected sum of $g$ tori.
The second contains orientation-reversing pairs and represents the connected sum of $k$ projective planes.
:::

<1>8. The normal form determines the surface: the orientable form has
\[
\chi=2-2g,
\]
and the nonorientable form has
\[
\chi=2-k.
\]
::: {.proof}
For the orientable normal form, the standard one-vertex CW structure has one face and $2g$ edges, giving
\[
\chi=1-2g+1=2-2g.
\]
For the nonorientable normal form it has one face and $k$ edges, giving
\[
\chi=1-k+1=2-k.
\]
Orientability distinguishes the two families, and within each family the Euler characteristic determines the genus.
Thus the paired polygon determines the homeomorphism type after reduction to normal form.
:::
:::
