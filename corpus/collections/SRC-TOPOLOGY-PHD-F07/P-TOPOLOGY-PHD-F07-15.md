---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-15
kind: problem
title: The surface with polygonal symbol $xyzx^{-1}zy^{-1}$, and classification of
  closed surfaces by even-sided polygons
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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part Two, question 3 of the Topology Ph.D. Qualifying Exam
    in assets/attachments/F07phdtop.pdf. A finite polygon presentation classifies
    compact connected surfaces without boundary; without compactness the literal
    statement in part (ii) is too broad.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Computed one vertex class, three edge classes, and one face, hence chi=-1.
    The two z occurrences have the same boundary orientation, so the surface is
    nonorientable and therefore is the connected sum of three projective planes.
    Then stated the orientable and nonorientable normal polygon forms and their
    Euler characteristics.
---

::: {.problem}
(i) The polygonal symbol of a certain surface without boundary is $xyzx^{-1}zy^{-1}$.
Identify the surface.
What is its Euler characteristic?

(ii) Explain how polygons with an even number of sides may be used to classify surfaces without boundary.
You do not need to give detailed proofs.
:::

::: {.solution}
For part (i), let the six vertices of the polygon, in boundary order, be
\[
v_0,v_1,\ldots,v_5,
\]
so that its directed boundary word is
\[
x\,y\,z\,x^{-1}\,z\,y^{-1}.
\]

<1>1. All six polygon vertices are identified to one vertex in the quotient.
::: {.proof}
Matching equally labelled edges in the directions indicated by their labels gives the endpoint identifications
\[
\begin{array}{c|c}
\text{edge pair}&\text{vertex identifications}\\
\hline
x,\ x^{-1}&v_0\sim v_4,\quad v_1\sim v_3,\\
y,\ y^{-1}&v_1\sim v_0,\quad v_2\sim v_5,\\
z,\ z&v_2\sim v_4,\quad v_3\sim v_5.
\end{array}
\]
The first two rows already give
\[
v_4\sim v_0\sim v_1\sim v_3
\qquad\text{and}\qquad
v_2\sim v_5.
\]
The $z$-identifications join these two classes, since
\[
v_2\sim v_4.
\]
Hence every $v_i$ belongs to the same equivalence class.
:::

<1>2. The quotient surface has Euler characteristic
\[
\chi=-1.
\]
::: {.proof}
The polygon quotient gives a CW structure with one $2$-cell, one $1$-cell for each paired label $x,y,z$, and by <1>1 one $0$-cell.
Thus
\[
F=1,
\qquad
E=3,
\qquad
V=1,
\]
and therefore
\[
\chi=V-E+F=1-3+1=-1.
\]
:::

<1>3. The quotient surface is nonorientable.
::: {.proof}
In the boundary word the two occurrences of $z$ have the same exponent:
\[
\cdots z\cdots z\cdots.
\]
Thus the two $z$-edges are glued with the same boundary direction rather than with opposite boundary directions.
For an orientation on the polygon interior to descend across a paired boundary edge, the induced boundary orientations on the two copies must be opposite.
The $z$-pair violates this condition, so no orientation descends to the quotient surface.
Hence the surface is nonorientable.
:::

<1>4. The surface in part (i) is
\[
\boxed{\mathbb{RP}^2\#\mathbb{RP}^2\#\mathbb{RP}^2},
\]
the nonorientable surface of genus $3$, and its Euler characteristic is
\[
\boxed{-1}.
\]
::: {.proof}
By the classification theorem for compact connected surfaces, a closed nonorientable surface is uniquely a connected sum
\[
N_k=\#^k\mathbb{RP}^2
\]
for some $k\ge1$, and
\[
\chi(N_k)=2-k.
\]
By <1>2--<1>3 the present surface is nonorientable and has Euler characteristic $-1$.
Therefore
\[
-1=2-k,
\]
so $k=3$.
:::

For part (ii), a finite polygon can only produce a compact quotient, so the polygon classification applies to compact connected surfaces without boundary.

<1>5. Every compact connected surface without boundary can be represented by a polygon with an even number of sides whose sides are identified in pairs.
::: {.proof}
Such a surface admits a finite triangulation.
By joining adjacent triangles across suitably chosen edges, one may cut the triangulation open to a single polygonal disk.
Every edge along the boundary of this disk comes from cutting an edge of the surface and therefore occurs exactly twice.
Recovering the original surface consists of identifying each such pair.
Consequently the boundary has an even number of sides and can be encoded by a word in which each edge label occurs exactly twice, with an exponent recording its direction along the boundary.
:::

<1>6. In the orientable case, elementary cut-and-paste changes of the polygon reduce the edge word to
\[
a_1b_1a_1^{-1}b_1^{-1}
\cdots
a_gb_ga_g^{-1}b_g^{-1}.
\]
Its quotient is the orientable surface
\[
\Sigma_g=\#^g(S^1\times S^1)
\]
of genus $g$, with
\[
\chi(\Sigma_g)=2-2g.
\]
::: {.proof}
For an orientable quotient, every paired label can be arranged to occur once in each direction.
The standard polygon-reduction moves gather the pairs into commutator blocks
\[
[a_i,b_i]=a_ib_ia_i^{-1}b_i^{-1}.
\]
Each block is the usual fundamental polygon for one torus handle, so the quotient is a connected sum of $g$ tori.
The standard one-vertex CW structure has
\[
V=1,
\qquad
E=2g,
\qquad
F=1,
\]
giving
\[
\chi=1-2g+1=2-2g.
\]
The sphere is the genus-$0$ case; it may also be represented by a $2$-gon with word $aa^{-1}$.
:::

<1>7. In the nonorientable case, elementary cut-and-paste changes reduce the edge word to
\[
a_1a_1a_2a_2\cdots a_ka_k.
\]
Its quotient is the nonorientable surface
\[
N_k=\#^k\mathbb{RP}^2
\]
of genus $k$, with
\[
\chi(N_k)=2-k.
\]
::: {.proof}
The presence of a paired edge occurring twice with the same direction produces a crosscap.
The polygon-reduction moves collect all orientation-reversing pairs into square blocks
\[
a_i a_i.
\]
A single square block is the standard polygonal presentation of $\mathbb{RP}^2$, and concatenating $k$ such blocks gives the connected sum of $k$ projective planes.
Its standard one-vertex CW structure has
\[
V=1,
\qquad
E=k,
\qquad
F=1,
\]
so
\[
\chi=1-k+1=2-k.
\]
:::

<1>8. These normal forms classify compact connected surfaces without boundary.
::: {.proof}
Every such surface has a paired polygon presentation by <1>5.
The reduction in <1>6--<1>7 places it in exactly one of two families: orientable or nonorientable.
Orientability distinguishes the two families.
Within the orientable family, the Euler characteristic determines
\[
g=1-\frac{\chi}{2};
\]
within the nonorientable family it determines
\[
k=2-\chi.
\]
Thus the polygonal normal form records exactly the orientability and genus, which are the invariants in the classification theorem.
:::
:::
