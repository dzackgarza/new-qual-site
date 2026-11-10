---
schema: qual/card@1
id: E-ZYJGG
kind: problem
title: Absolute retracts
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S35.pdf, Exercise 35.6, page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S35.pdf, Internet Archive snapshot 20220130234235),
    checked against Munkres, Topology (2000), Section 35 Exercise 6, printed p. 223, its hint, Theorem
    34.2, Theorem 37.3 and Theorem 35.1. Part (a) is the card's: a homeomorphism from the closed copy
    Y_0 extends to Z and postcomposition with its inverse retracts Z onto Y_0. Part (b) is Moller's:
    a compact Hausdorff space imbeds as a closed subspace of the cube [0,1]^J, the cube has the
    universal extension property with the Tychonoff theorem assumed, and by (a) and Exercise 35.5(b)
    a retract of it does too. What was corrected: Moller writes that the space "is a retract of the
    UEP space [0,1]^J, hence is itself a UEP space [Ex 31.5.(b)]", citing Exercise 31.5, which is
    about the equalizer of two maps; the retract argument is Exercise 35.5(b), and the card cites it.
---

::: {.exercise}

Let $Y$ be a normal space.
Then $Y$ is said to be an absolute retract if for every pair of spaces $(Y_0, Z)$ such that $Z$ is normal and $Y_0$ is a closed subspace of $Z$ homeomorphic to $Y$, the space $Y_0$ is a retract of $Z$.

(a) Show that if $Y$ has the universal extension property, then $Y$ is an absolute retract.

(b) Show that if $Y$ is an absolute retract and $Y$ is compact, then $Y$ has the universal extension property.
[Hint: Assume the Tychonoff theorem, so you know $[0, 1]^J$ is normal.
Imbed $Y$ in $[0, 1]^J$.]
:::

::: {.solution}
(a) Assume $Y$ has the universal extension property. Let $Y_0$ be a closed subspace of a normal space $Z$, and let
$$
h:Y_0\to Y
$$
be a homeomorphism. By the universal extension property, $h$ extends to a continuous map $H:Z\to Y$. Then
$$
r=h^{-1}\circ H:Z\to Y_0
$$
is continuous and satisfies $r\restrict_{Y_0}=\operatorname{id}_{Y_0}$. Thus $Y_0$ is a retract of $Z$, so $Y$ is an absolute retract.

(b) Assume $Y$ is compact and an absolute retract. Since $Y$ is normal, it is completely regular, so it embeds in a cube
$$
e:Y\hookrightarrow[0,1]^J.
$$
Compactness of $Y$ and Hausdorffness of the cube imply $e(Y)$ is closed. By the Tychonoff theorem the cube is compact Hausdorff, hence normal. Since $Y$ is an absolute retract, there is a retraction
$$
r:[0,1]^J\to e(Y).
$$

Now let $A$ be a closed subspace of a normal space $X$, and let $f:A\to Y$ be continuous. Each coordinate of $e\circ f:A\to[0,1]^J$ extends to $X$ by Tietze. Combining these coordinate extensions gives a continuous map
$$
F:X\to[0,1]^J
$$
extending $e\circ f$. Then
$$
e^{-1}\circ r\circ F:X\to Y
$$
extends $f$. Thus $Y$ has the universal extension property.
:::
