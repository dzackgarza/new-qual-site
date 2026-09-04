---
schema: qual/card@1
id: P-3WQES
kind: problem
title: Closed surfaces with one $0$-cell and two $1$-cells
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Surfaces
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 7 of the official UGA Fall 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified the Euler-characteristic restriction and explicit one-vertex/two-edge decompositions for all four resulting closed surfaces.
---

::: problem
Identify (with proof, but of course you can appeal to the classification of surfaces) all of the compact surfaces without boundary that have a cell decomposition having exactly one 0-cell and exactly two 1-cells (with no restriction on the number of cells of dimension larger than 1).
:::

::: {.solution}
<1>1. Any such cell decomposition is connected and has a finite number, say $r$, of $2$-cells.
::: {.proof}
The unique $0$-cell lies in the $0$-skeleton.
Each $1$-cell is attached to that vertex at both endpoints, so the $1$-skeleton is connected.
Every $2$-cell is attached to the $1$-skeleton, hence the whole surface is connected.

Since the surface is compact and the given cell decomposition is a CW decomposition, the surface is contained in a finite subcomplex; because the whole space is the surface, only finitely many cells occur.
As the ambient space is a surface, the cells have dimensions at most $2$.
Let $r$ denote the number of $2$-cells.
:::

<1>2. One necessarily has
\[
r\ge1.
\]
::: {.proof}
If $r=0$, the surface would equal its $1$-skeleton, a graph with one vertex and two edges.
Its second homology with $\mathbb Z/2$ coefficients would therefore vanish.

On the other hand, every connected compact surface without boundary has a mod-$2$ fundamental class, so
\[
H_2(S;\mathbb Z/2)\cong\mathbb Z/2.
\]
This contradiction shows that at least one $2$-cell is present.
:::

<1>3. The Euler characteristic satisfies
\[
\chi(S)=1-2+r=r-1\ge0.
\]
::: {.proof}
For a finite CW decomposition,
\[
\chi(S)=c_0-c_1+c_2.
\]
Here
\[
c_0=1,
\qquad
c_1=2,
\qquad
c_2=r.
\]
Thus
\[
\chi(S)=1-2+r=r-1.
\]
By <1>2, $r\ge1$, so $\chi(S)\ge0$.
:::

<1>4. By the classification of compact connected surfaces, the only possible surfaces are
\[
S^2,
\qquad
\mathbb{RP}^2,
\qquad
T^2,
\qquad
K,
\]
where $K$ is the Klein bottle.
::: {.proof}
For the closed orientable surface $\Sigma_g$ of genus $g$,
\[
\chi(\Sigma_g)=2-2g.
\]
The condition $\chi\ge0$ gives
\[
g=0\quad\text{or}\quad g=1,
\]
namely $S^2$ and $T^2$.

For the closed nonorientable surface $N_k$ of nonorientable genus $k\ge1$,
\[
\chi(N_k)=2-k.
\]
The condition $\chi\ge0$ gives
\[
k=1\quad\text{or}\quad k=2,
\]
namely $\mathbb{RP}^2$ and the Klein bottle.
No other closed connected surface has nonnegative Euler characteristic.
:::

<1>5. The sphere $S^2$ admits a decomposition with one $0$-cell and two $1$-cells.
::: {.proof}
Embed a figure-eight graph
\[
S^1\vee S^1
\]
in $S^2$ so that the two circles meet at a single point.
Use the common point as the unique $0$-cell and the two circle interiors as the two $1$-cells.
The complement of this figure-eight in $S^2$ has three connected components, each an open disk.
Taking these three components as $2$-cells gives a CW decomposition with cell counts
\[
(c_0,c_1,c_2)=(1,2,3).
\]
Indeed, its Euler characteristic is
\[
1-2+3=2=\chi(S^2).
\]
:::

<1>6. The projective plane $\mathbb{RP}^2$ admits such a decomposition with two $2$-cells.
::: {.proof}
Start with the standard polygon model of $\mathbb{RP}^2$ as a $2$-gon whose boundary word is
\[
aa.
\]
Its two polygon vertices are identified to one vertex, and the two boundary sides are identified to one $1$-cell $a$.

Inside the polygon add an arc $b$ joining the two vertices.
After the vertex identification, the interior of this arc is a second $1$-cell whose two endpoints are the unique vertex.
The arc divides the polygon into two disks, which become two $2$-cells after the quotient.
This is merely a subdivision of the standard polygon model, so the quotient is still $\mathbb{RP}^2$.
Thus
\[
(c_0,c_1,c_2)=(1,2,2).
\]
:::

<1>7. The torus $T^2$ admits such a decomposition with one $2$-cell.
::: {.proof}
Use the standard square model with boundary word
\[
aba^{-1}b^{-1}.
\]
All four vertices are identified to one $0$-cell, the edge classes $a$ and $b$ give exactly two $1$-cells, and the square interior is one $2$-cell.
Hence
\[
(c_0,c_1,c_2)=(1,2,1).
\]
:::

<1>8. The Klein bottle $K$ also admits such a decomposition with one $2$-cell.
::: {.proof}
Use the standard square model of the Klein bottle with boundary word
\[
aba^{-1}b.
\]
Again all four vertices become one $0$-cell, the two edge classes $a,b$ give exactly two $1$-cells, and the square interior gives one $2$-cell.
Thus
\[
(c_0,c_1,c_2)=(1,2,1).
\]
:::

<1>9. Therefore the complete list is
\[
\boxed{S^2,\ \mathbb{RP}^2,\ T^2,\ \text{and the Klein bottle}.}
\]
::: {.proof}
Necessity follows from <1>3--<1>4, and <1>5--<1>8 explicitly realize every surface on the list.
:::
:::
