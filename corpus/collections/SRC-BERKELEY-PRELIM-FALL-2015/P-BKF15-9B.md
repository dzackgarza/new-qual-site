---
schema: qual/card@1
id: P-BKF15-9B
kind: problem
title: Nonattacking rook placements on a chessboard up to symmetry
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
    Independently checked the retained Fall 2015 solution packet. The
    printed diagonal-reflection total 774 is an arithmetic typo: its own
    involution formula evaluates to 764, and 764 is the value required by
    the packet's final correct total 5282.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked all eight symmetry fixed-point counts via permutations:
    involutions for diagonal reflections, square roots of the reversal for
    quarter-turns, and the centralizer of the reversal for the half-turn.
---

::: {.problem}
How many ways are there to arrange 8 rooks on an 8 by 8 chessboard so that no two attack each other (in other words, each row and column contains exactly one rook), where two ways are counted as the same if they are equivalent under one of the 8 symmetries of the chessboard?
You may assume the Polya–Burnside theorem that the number of orbits of a finite group on a finite set is the average number of fixed points of elements of the group.
:::

::: {.solution}
Label the rows and columns by
$$
1,\ldots,8.
$$
A nonattacking rook placement is the graph of a unique permutation
$$
\sigma\in S_8,
$$
with a rook in the square
$$
(i,\sigma(i)).
$$
Put
$$
w(i)\coloneqq9-i,
$$
so
$$
w=(1\,8)(2\,7)(3\,6)(4\,5).
$$

<1>1. The identity symmetry fixes
$$
8!=40320
$$
placements.

::: {.proof}
Every one of the $8!$ permutations of the columns determines a
nonattacking rook placement, and the identity fixes all of them.
:::

<1>2. Neither the horizontal nor the vertical reflection fixes any
placement.

::: {.proof}
Under vertical reflection, a rook in
$$
(i,j)
$$
is sent to
$$
(i,w(j)).
$$
No column is fixed by $w$, since $j=9-j$ has no integral solution.
Thus a fixed placement would have to contain two distinct rooks in the
same row, impossible.

Under horizontal reflection,
$$
(i,j)\longmapsto(w(i),j).
$$
Again no row is fixed, so a fixed placement would contain two distinct
rooks in the same column. Hence both fixed-point counts are $0$.
:::

<1>3. A placement is fixed by reflection in the main diagonal if and
only if
$$
\sigma^2=1.
$$

::: {.proof}
Reflection in the main diagonal sends the graph of $\sigma$ to
$$
\{(\sigma(i),i):1\le i\le8\},
$$
which is the graph of $\sigma^{-1}$. Thus the graph is fixed exactly
when
$$
\sigma=\sigma^{-1},
$$
equivalently $\sigma^2=1$.
:::

<1>4. Each diagonal reflection fixes exactly
$$
764
$$
placements.

::: {.proof}
By step <1>3, the fixed placements for one diagonal are the
involutions in $S_8$. An involution with exactly $k$ transpositions,
where $0\le k\le4$, is obtained by choosing and pairing $2k$ of the
$8$ symbols. Its number is
$$
\frac{8!}{2^k k!(8-2k)!}.
$$
Therefore the total is
$$
\begin{aligned}
\sum_{k=0}^4
\frac{8!}{2^k k!(8-2k)!}
&=
1+28+210+420+105\\
&=
764.
\end{aligned}
$$
The two diagonal reflections are conjugate in the symmetry group of
the square, so they have the same number of fixed placements.
:::

<1>5. A placement fixed by a rotation through $90^\circ$ corresponds
to a permutation satisfying
$$
\sigma^2=w.
$$

::: {.proof}
Choose the quarter-turn
$$
(i,j)\longmapsto(j,w(i)).
$$
If $(i,\sigma(i))$ is a rook, its image is
$$
(\sigma(i),w(i)).
$$
For the placement to be fixed, the rook in row $\sigma(i)$ must
therefore lie in column $w(i)$:
$$
\sigma(\sigma(i))=w(i).
$$
This is exactly $\sigma^2=w$.
:::

<1>6. Each of the two quarter-turns fixes exactly
$$
12
$$
placements.

::: {.proof}
The permutation $w$ is a product of four disjoint transpositions. A
cycle whose square is a product of two transpositions must be a
$4$-cycle, and the square of a $4$-cycle is precisely a pair of
disjoint transpositions. Hence a square root $\sigma$ of $w$ consists
of two $4$-cycles, each joining a pair of the four transpositions of
$w$.

There are
$$
3
$$
ways to partition four transpositions into two unordered pairs. For a
fixed pair
$$
(a\,b)(c\,d),
$$
there are exactly two $4$-cycles whose square is this product, for
example
$$
(a\,c\,b\,d)
\qquad\text{and}\qquad
(a\,d\,b\,c).
$$
Thus
$$
3\cdot2^2=12
$$
square roots occur. The two quarter-turns are conjugate as board
symmetries and therefore have the same fixed-point count.
:::

<1>7. A placement is fixed by the $180^\circ$ rotation if and only if
$$
\sigma w=w\sigma.
$$

::: {.proof}
The half-turn sends
$$
(i,\sigma(i))
$$
to
$$
(w(i),w(\sigma(i))).
$$
The rotated placement is the original one exactly when the rook in row
$w(i)$ has column $w(\sigma(i))$ for every $i$, namely
$$
\sigma(w(i))=w(\sigma(i)).
$$
:::

<1>8. The half-turn fixes exactly
$$
384
$$
placements.

::: {.proof}
The four orbits of $w$ are the pairs
$$
\{1,8\},\{2,7\},\{3,6\},\{4,5\}.
$$
A permutation commuting with $w$ may permute these four pairs
arbitrarily, giving $4!$ choices. After choosing the image pair for
each source pair, there are independently two choices for which member
maps to which member, giving $2^4$ choices. Conversely every such
choice commutes with $w$. Hence the centralizer has size
$$
2^4\cdot4!
=
16\cdot24
=
384.
$$
By step <1>7 this is the fixed-point count.
:::

<1>9. The number of rook placements up to the eight symmetries of the
board is
$$
\boxed{5282}.
$$

::: {.proof}
By the Polya--Burnside theorem and steps <1>1--<1>8, the number of
orbits is
$$
\begin{aligned}
\frac18
\left(
40320
+2\cdot0
+2\cdot764
+2\cdot12
+384
\right)
&=
\frac{42256}{8}\\
&=
5282.
\end{aligned}
$$
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required number of equivalence classes.
:::
:::
