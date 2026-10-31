---
schema: qual/card@1
id: P-UCTOP290-S4-9
kind: problem
title: Torus covers from subgroups of the integer lattice
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 9 against its extraction and PDF page image.
---

::: {.problem}
Identify the covers of $T^2=\RR^2/\ZZ^2$ corresponding to the
following subgroups of $\pi_1(T^2)=\ZZ^2$, and find their deck
transformation groups. The integers $p,q,r,s$ may be zero.

(a) $\langle(p,0)\rangle$.

(b) $\langle(p,0),(0,q)\rangle$.

(c) $\langle(p,q)\rangle$.

(d) $\langle(p,q),(r,s)\rangle$.
:::

::: {.solution}

For any subgroup $H\le\ZZ^2$, the cover is
$$
\RR^2/H\longrightarrow\RR^2/\ZZ^2=T^2,
$$
and its deck group is $\ZZ^2/H$. The quotient is a plane if
$H=0$, a cylinder if $H$ has rank $1$, and a torus if $H$ has rank
$2$. In a drawing, the generators of $H$ are the translation
vectors identifying points of the covering plane.

(a) If $p\ne0$, identify points separated by the horizontal vector
$(p,0)$. This gives a cylinder, with deck group
$$
\ZZ\oplus\ZZ/\abs{p}.
$$
If $p=0$, the cover is the plane and its deck group is $\ZZ^2$.

(b) If $p,q\ne0$, the rectangle of side lengths $\abs{p}$ and
$\abs{q}$ tiles a torus cover. Its deck group is
$$
\ZZ/\abs{p}\oplus\ZZ/\abs{q}.
$$
If exactly one of $p,q$ is nonzero, this is the cylinder of (a),
possibly with the two coordinate directions exchanged. If both
vanish, it is the plane.

(c) If $(p,q)\ne(0,0)$, put
$d=\gcd(\abs{p},\abs{q})$. The subgroup translates by $d$ times
the primitive vector $(p/d,q/d)$, so the cover is a cylinder and
its deck group is
$$
\ZZ\oplus\ZZ/d.
$$
For $(p,q)=(0,0)$ it is the plane.

(d) Write $\Delta=ps-qr$. If $\Delta\ne0$, the two vectors span
a rank-two lattice of index $\abs{\Delta}$. The cover is a torus.
Put
$$
d_1=\gcd(\abs{p},\abs{q},\abs{r},\abs{s}),
\qquad d_2=\abs{\Delta}/d_1.
$$
Smith normal form gives its deck group as
$$
\ZZ/d_1\oplus\ZZ/d_2.
$$
If $\Delta=0$ and at least one vector is nonzero, the subgroup
has rank $1$; the cover is a cylinder. With
$d=\gcd(\abs{p},\abs{q},\abs{r},\abs{s})$, its deck group is
$\ZZ\oplus\ZZ/d$. If both vectors vanish, the cover is the
plane with deck group $\ZZ^2$.

:::
