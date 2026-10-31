---
schema: qual/card@1
id: P-BKS83-4
kind: problem
title: Symmetry group of a triangular network through the vertices of the unit square
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained PDF itself does not contain the required diagram. In place of the figure it prints "../Fig/Pr/Sp83-4.ps not found". The statement is therefore preserved without reconstructing the missing network.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: Confirmed that no Sp83-4 asset, duplicate statement containing the diagram, or embedded image occurs in the retained repository source packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked that two explicit triangular networks through the four surviving points have different Euclidean symmetry groups, so the retained data do not determine the requested group.
---

::: {.problem}
In the triangular network in $\RR^2$ referred to by the source, the points $P_0,P_1,P_2,P_3$ are respectively
$$
(0,0),\qquad(1,0),\qquad(0,1),\qquad(1,1).
$$
The network contains every vertical line $x=m$ and every horizontal
line $y=n$, for $m,n\in\ZZ$. In each horizontal strip, its diagonals
join
$$
(2k,n)\ \text{to}\ (2k+1,n+1)
\quad\text{and}\quad
(2k+2,n)\ \text{to}\ (2k+1,n+1)
$$
for all $k,n\in\ZZ$. Describe the group of Euclidean transformations
of $\RR^2$ that leave this network invariant.

This is the diagram in [de Souza and Silva, *Berkeley Problems in
Mathematics*, Problem 6.1.5 (Sp83), p. 88](https://hoclieuxanh.com/download-file/61e72d2e-93b4-4bce-ba30-e7a6c03ac0eb/Barkaley%20Problems%20%28chap%201%20_%207%29.pdf#page=93).
The retained exam PDF lacks it.
:::

::: {.solution}
::: pf

::: {.pf-step #network-symmetries}
The symmetry group is
$$
\boxed{
G=
\left\{
(x,y)\longmapsto
\bigl(\epsilon x+m,\,(-1)^m y+n\bigr)
:\epsilon\in\{1,-1\},\ m,n\in\ZZ
\right\}.
}
$$
Its translation subgroup is
$$
T=\{(x,y)\mapsto(x+2k,y+n):k,n\in\ZZ\}
\cong\ZZ^2,
$$
and $G/T\cong C_2\times C_2$.

::: pf-proof
The only complete straight lines in the network are the lines of the
integer square grid. An isometry preserving the network therefore
preserves that grid. It maps its integer vertices to integer vertices,
so it has an integer translation part and a linear part that is a
signed permutation of the coordinate axes.

At a vertex in an even column, the two diagonal edges point upward;
at a vertex in an odd column, they point downward. No vertex has two
diagonal edges pointing to the same horizontal side. Thus a symmetry
cannot interchange the horizontal and vertical axes. It has the form
$$
(x,y)\longmapsto(\epsilon x+m,\delta y+n),
\qquad
\epsilon,\delta\in\{1,-1\},\quad m,n\in\ZZ.
$$
The diagonals point upward at an even image column precisely when
$m$ is even. Matching their direction gives
$\delta=(-1)^m$. Conversely, each map with this relation preserves
all grid lines and takes each diagonal segment to another diagonal
segment. This proves the formula for $G$.

The maps with identity linear part have $\epsilon=1$ and $m$ even,
giving $T$. The two signs $\epsilon$ and $(-1)^m$ determine the four
cosets of $T$, so $G/T\cong C_2\times C_2$.
:::

:::

::: pf-qed
The displayed group $G$ is the full Euclidean symmetry group of the
depicted network.
:::

:::
:::
