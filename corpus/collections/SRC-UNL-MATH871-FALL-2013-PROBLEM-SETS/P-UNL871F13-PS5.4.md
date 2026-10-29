---
schema: qual/card@1
id: P-UNL871F13-PS5.4
kind: problem
title: The standard genus-two surface from an octagon
classification:
  areas: [topology]
  topics: [Quotient Spaces, Surfaces]
relations: []
review: draft
---

::: {.problem}
Let $X$ be an octagon.
Label its boundary edges, in counterclockwise order, by
$$
a,\ b,\ a^{-1},\ b^{-1},\ c,\ d,\ c^{-1},\ d^{-1},
$$
where equal labels are identified respecting the indicated orientations.
Let $M$ be the resulting quotient space.

Give a concrete construction showing that $M$ is homeomorphic to the closed orientable surface of genus $2$ (the surface of a doughnut with two holes).
:::

::: {.solution}

Write the boundary word of the octagon as
$$
[a,b][c,d]
=
aba^{-1}b^{-1}cdc^{-1}d^{-1}.
$$

::: pf

::: {.pf-step #s1-1}

Draw an embedded arc
$$
e
$$
inside the octagon joining the vertex between
$$
b^{-1}
\quad\text{and}\quad
c
$$
to the vertex between
$$
d^{-1}
\quad\text{and}\quad
a.
$$
This cuts the octagon into two disks
$$
P_1
\quad\text{and}\quad
P_2.
$$


::: pf-proof

The arc joins two distinct boundary vertices and is otherwise contained in
the interior of the octagon.
Hence it separates the disk into two closed disks meeting exactly along the
arc $e$.

The first piece contains the boundary edges
$$
a,b,a^{-1},b^{-1},
$$
while the second contains
$$
c,d,c^{-1},d^{-1}.
$$

:::

:::

::: {.pf-step #s1-2}

After performing the identifications
$$
a\sim a^{-1},
\qquad
b\sim b^{-1}
$$
inside $P_1$, the quotient of $P_1$ is a torus with the interior of a disk
removed.


::: pf-proof

Ignore the cutting edge $e$ momentarily.
The familiar square-polygon presentation
$$
aba^{-1}b^{-1}
$$
gives a torus after the four labeled sides are paired.

In $P_1$, the cutting arc $e$ is left unpaired.
Under the four side identifications, its two endpoints become the same point:
all vertices of the standard torus polygon are identified.
Thus the image of $e$ becomes a boundary circle rather than being filled by
the $2$-cell.

Equivalently, start with the usual torus polygon and remove a small open disk
around the unique vertex of the quotient.
The resulting surface is a once-punctured torus,
$$
T^2\setminus\operatorname{int}D^2.
$$

:::

:::

::: {.pf-step #s1-3}

Similarly, after identifying
$$
c\sim c^{-1},
\qquad
d\sim d^{-1},
$$
the quotient of $P_2$ is another once-punctured torus.


::: pf-proof

The boundary word
$$
cdc^{-1}d^{-1}
$$
is the standard torus word for the second pair of generators.
Again the cutting edge $e$ remains unpaired and becomes the boundary circle.
Hence
$$
P_2/{\sim}
\cong
T^2\setminus\operatorname{int}D^2.
$$

:::

:::

::: {.pf-step #s1-4}

In the original octagon, the two copies of the cutting arc $e$ are
glued to one another.
Therefore
$$
M
$$
is obtained by gluing two once-punctured tori along their boundary circles.


::: pf-proof

Cutting the octagon along $e$ creates two copies
$$
e_1\subset\partial P_1,
\qquad
e_2\subset\partial P_2.
$$
Recovering the original octagon identifies these two copies pointwise.

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, their images are precisely the boundary circles of the
two punctured tori.
Hence
$$
M
\cong
\bigl(
T^2\setminus\operatorname{int}D^2
\bigr)
\cup_{S^1}
\bigl(
T^2\setminus\operatorname{int}D^2
\bigr).
$$

:::

:::

::: {.pf-step #s1-5}

The space in step [](#s1-4){.pf-ref} is the connected sum
$$
T^2\#T^2.
$$


::: pf-proof

By definition, the connected sum of two closed surfaces is obtained by
removing an open disk from each and gluing the resulting boundary circles by
a homeomorphism.
That is exactly the construction in step [](#s1-4){.pf-ref}.
Thus
$$
M\cong T^2\#T^2.
$$

:::

:::

::: {.pf-step #s1-6}

The quotient has one $0$-cell, four $1$-cells, and one $2$-cell.


::: pf-proof

The edge identifications identify all eight vertices of the octagon to one
vertex.
The paired edge labels give four $1$-cells
$$
a,b,c,d.
$$
The interior of the octagon gives one $2$-cell.
Therefore the quotient CW structure has cell counts
$$
c_0=1,
\qquad
c_1=4,
\qquad
c_2=1.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\chi(M)
=
1-4+1
=
-2.
$$


::: pf-proof

Use the CW Euler-characteristic formula
$$
\chi
=
c_0-c_1+c_2.
$$
Substitute the cell counts from step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The quotient surface is orientable.


::: pf-proof

Each pair of equally labeled sides is identified with opposite boundary
orientation:
$$
a\text{ with }a^{-1},
\quad
b\text{ with }b^{-1},
\quad
c\text{ with }c^{-1},
\quad
d\text{ with }d^{-1}.
$$
Thus the orientation of the polygon extends across each edge identification.
Hence the resulting closed surface is orientable.

:::

:::

::: {.pf-step #s1-9}

A closed connected orientable surface of genus $g$ has Euler
characteristic
$$
2-2g.
$$
For $M$,
$$
2-2g=-2,
$$
so
$$
g=2.
$$


::: pf-proof

Solve:
$$
2-2g=-2
\Longrightarrow
-2g=-4
\Longrightarrow
g=2.
$$

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
M
\cong
T^2\#T^2,
}
$$
the closed orientable surface of genus $2$.


::: pf-proof

The concrete connected-sum construction is given in steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.
Steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} independently verify the genus from the quotient CW
structure.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required identification.

:::

:::

:::
