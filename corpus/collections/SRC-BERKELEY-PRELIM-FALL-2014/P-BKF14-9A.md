---
schema: qual/card@1
id: P-BKF14-9A
kind: problem
title: Burnside's lemma and $4$-colorings of the vertices of a hexagon
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: double
    counting gives Burnside's lemma, and the six dihedral cycle types give
    430 vertex-coloring orbits.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked all rotation and reflection cycle types on six vertices and the
    fixed-coloring sum 5160 divided by 12.
---

::: {.problem}
(a) By counting the number of pairs $( g , x )$ with $g \in G , x \in X , g ( x ) = x$ , show that the number of orbits of a finite group G acting on a finite set X is the average number of fixed points of elements of the group.

(b) In how many ways (up to symmetries of the hexagon) can one color the vertices of a regular hexagon using 4 colors?
:::

::: {.solution}
<1>1. Let
$$
\Omega\coloneqq\{(g,x)\in G\times X:g(x)=x\}.
$$
Then
$$
|\Omega|
=
\sum_{g\in G}|\operatorname{Fix}(g)|.
$$

::: {.proof}
For a fixed $g\in G$, the pairs in $\Omega$ whose first coordinate is
$g$ are exactly
$$
\{g\}\times\operatorname{Fix}(g).
$$
Summing their cardinalities over $g$ gives the displayed identity.
:::

<1>2. If $X/G$ denotes the set of orbits, then
$$
|\Omega|=|G|\,|X/G|.
$$

::: {.proof}
Count instead by the second coordinate:
$$
|\Omega|
=
\sum_{x\in X}|G_x|,
$$
where $G_x$ is the stabilizer of $x$. For a fixed orbit
$O\subseteq X$, orbit-stabilizer gives
$$
|G_x|=\frac{|G|}{|O|}
$$
for every $x\in O$. Hence
$$
\sum_{x\in O}|G_x|
=
|O|\frac{|G|}{|O|}
=
|G|.
$$
Summing once over all orbits proves the claim.
:::

<1>3. Therefore the number of orbits is
$$
\boxed{
|X/G|
=
\frac1{|G|}
\sum_{g\in G}|\operatorname{Fix}(g)|.
}
$$

::: {.proof}
Equate the two expressions for $|\Omega|$ from steps <1>1 and <1>2
and divide by $|G|$. This proves part (a).
:::

<1>4. For the hexagon, the identity fixes
$$
4^6
$$
colorings.

::: {.proof}
The identity imposes no equality among the six vertex colors, so each
vertex may be colored independently in $4$ ways.
:::

<1>5. The two rotations through $\pm60^\circ$ each fix $4$ colorings,
the two rotations through $\pm120^\circ$ each fix $4^2$ colorings, and
the rotation through $180^\circ$ fixes $4^3$ colorings.

::: {.proof}
A coloring fixed by a permutation of the vertices must be constant on
each cycle of that permutation.

A rotation through $\pm60^\circ$ is one $6$-cycle, so it has $4$
fixed colorings. A rotation through $\pm120^\circ$ has two
$3$-cycles, so it has $4^2$ fixed colorings. The rotation through
$180^\circ$ has three $2$-cycles, so it has $4^3$ fixed colorings.
:::

<1>6. Each of the three reflections through midpoints of opposite
sides fixes $4^3$ colorings, while each of the three reflections
through opposite vertices fixes $4^4$ colorings.

::: {.proof}
A reflection through midpoints of opposite sides pairs the six
vertices into three transposed pairs, giving three cycles and hence
$4^3$ fixed colorings.

A reflection through opposite vertices fixes those two vertices and
interchanges the remaining four vertices in two pairs. It therefore
has four cycles and fixes $4^4$ colorings.
:::

<1>7. The number of colorings up to symmetry is
$$
\boxed{430}.
$$

::: {.proof}
The symmetry group of the regular hexagon is the dihedral group of
order $12$. Applying step <1>3 and the fixed-point counts from steps
<1>4--<1>6 gives
$$
\begin{aligned}
\frac1{12}
\left(
4^6
+2\cdot4
+2\cdot4^2
+4^3
+3\cdot4^3
+3\cdot4^4
\right)
&=
\frac{
4096+8+32+64+192+768
}{12}\\
&=
\frac{5160}{12}\\
&=
430.
\end{aligned}
$$
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>7 proves part (b).
:::
:::
