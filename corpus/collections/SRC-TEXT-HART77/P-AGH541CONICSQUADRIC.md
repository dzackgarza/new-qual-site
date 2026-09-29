---
schema: qual/card@1
id: P-AGH541CONICSQUADRIC
kind: problem
title: Conics through two base points and the quadric surface as a blown up plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Blowups
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.1 and the retained Egbert construction. After moving
    the two base points to [0:0:1] and [0:1:0], the conic system is spanned
    by x_0^2, x_0x_1, x_0x_2, x_1x_2 and maps to the smooth quadric
    y_0y_3=y_1y_2. On Bl_{P_1,P_2} P^2 the system is base-point free and
    contracts exactly the strict transform of x_0=0 to [0:0:0:1]. Projection
    from that point on the quadric has the same graph, proving that the
    blown-up plane is the blowup of the quadric at that point.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
The linear system of conics in $\PP^2$ with two assigned base points $P_1$ and $P_2$ (4.1) determines a morphism $\psi$ of $X^{\prime}$ (which is $\PP^2$ with $P_1$ and $P_2$ blown up) to a nonsingular quadric surface $Y$ in $\PP^3$, and furthermore $X^{\prime}$ via $\psi$ is isomorphic to $Y$ with one point blown up.
:::

::: {.solution}
After a projective change of coordinates, take
$$
P_1=[0:0:1],
\qquad
P_2=[0:1:0]
$$
in $\PP^2$ with coordinates $[x_0:x_1:x_2]$.

::: pf

::: {.pf-step #conics-through-two-points-basis}
The vector space of conics through $P_1$ and $P_2$ has basis
$$
x_0^2,
\qquad
x_0x_1,
\qquad
x_0x_2,
\qquad
x_1x_2.
$$

::: pf-proof
A general conic is a linear combination of
$$
x_0^2, x_1^2, x_2^2, x_0x_1, x_0x_2, x_1x_2.
$$
Vanishing at $P_1$ forces the coefficient of $x_2^2$ to be zero, and
vanishing at $P_2$ forces the coefficient of $x_1^2$ to be zero. The four
remaining monomials are linearly independent and give the displayed basis.
:::

:::

::: {.pf-step #rational-map-base-locus}
The corresponding rational map is
$$
\phi:\PP^2\dashrightarrow\PP^3,
\qquad
[x_0:x_1:x_2]
\longmapsto
[x_0^2:x_0x_1:x_0x_2:x_1x_2].
$$
Its base locus is exactly $\{P_1,P_2\}$.

::: pf-proof
All four coordinates vanish precisely when
$$
x_0=0,
\qquad
x_1x_2=0.
$$
On the line $x_0=0$, this gives exactly
$$
[0:0:1]=P_1
\qquad\text{or}\qquad
[0:1:0]=P_2.
$$
:::

:::

::: {.pf-step #lifts-to-morphism}
Let
$$
\pi:X'=\operatorname{Bl}_{\{P_1,P_2\}}\PP^2\longrightarrow\PP^2
$$
be the blowup. The rational map $\phi$ lifts to a morphism
$$
\psi:X'\longrightarrow\PP^3.
$$

::: pf-proof
If $H$ denotes the pullback of the class of a line and $E_1,E_2$ the two
exceptional curves, then the strict transforms of the conics through the
base points form the complete linear system
$$
|2H-E_1-E_2|.
$$
Blowing up the two simple base points removes the base locus, so this linear
system is base-point free and defines the asserted morphism.
:::

:::

::: {.pf-step #image-in-quadric}
The image of $\psi$ is contained in the quadric
$$
Y=V(y_0y_3-y_1y_2)\subseteq\PP^3.
$$

::: pf-proof
Write the four target coordinates in the order
$$
[y_0:y_1:y_2:y_3]
=
[x_0^2:x_0x_1:x_0x_2:x_1x_2].
$$
Then identically
$$
y_0y_3
=
x_0^2x_1x_2
=
(x_0x_1)(x_0x_2)
=
y_1y_2.
$$
Thus every point in the image satisfies the quadric equation.
:::

:::

::: {.pf-step #quadric-nonsingular}
The quadric $Y$ is nonsingular.

::: pf-proof
For
$$
F=y_0y_3-y_1y_2,
$$
the four partial derivatives are
$$
y_3,
\qquad
-y_2,
\qquad
-y_1,
\qquad
y_0.
$$
They vanish simultaneously only at the zero vector, which is not a point of
$\PP^3$. Hence $Y$ is nonsingular.
:::

:::

::: {.pf-step #birational-onto-quadric}
The morphism $\psi$ is birational onto $Y$.

::: pf-proof
On the dense open set $x_0\ne0$, scale so $x_0=1$. Then
$$
\phi([1:x_1:x_2])
=
[1:x_1:x_2:x_1x_2].
$$
Conversely, on the dense affine open $y_0\ne0$ of $Y$, the quadric equation
determines
$$
y_3=\frac{y_1y_2}{y_0},
$$
so projection to
$$
[y_0:y_1:y_2]
$$
recovers the original point of $\PP^2$. Thus $\psi$ is an isomorphism on
dense opens and is birational. Since its image is a closed irreducible
surface contained in the irreducible surface $Y$, the image is all of $Y$.
:::

:::

::: {.pf-step #exceptional-line-contracted}
Let $L\subseteq X'$ be the strict transform of the line
$$
x_0=0
$$
through $P_1$ and $P_2$. Then
$$
L\sim H-E_1-E_2,
\qquad
L^2=-1,
$$
and $\psi$ contracts $L$ to
$$
p=[0:0:0:1]\in Y.
$$

::: pf-proof
The class formula is the standard strict-transform formula, and therefore
$$
L^2
=
H^2+E_1^2+E_2^2
=
1-1-1
=-1,
$$
using the usual intersection convention
$$
H^2=1,
\qquad
E_i^2=-1,
\qquad
H\cdot E_i=E_1\cdot E_2=0.
$$

At a point $[0:x_1:x_2]$ of the original line away from the two base
points, one has $x_1x_2\ne0$, so
$$
\phi([0:x_1:x_2])=[0:0:0:1]=p.
$$
Hence its strict transform is contracted to $p$. Equivalently,
$$
(2H-E_1-E_2)\cdot(H-E_1-E_2)=2-1-1=0.
$$
:::

:::

::: {.pf-step #projection-inverse}
Projection from $p$ defines the rational inverse
$$
\rho:Y\dashrightarrow\PP^2,
\qquad
[y_0:y_1:y_2:y_3]
\longmapsto
[y_0:y_1:y_2].
$$

::: pf-proof
The map is defined away from $p$, the unique point of $Y$ at which
$$
y_0=y_1=y_2=0.
$$
On $y_0\ne0$, step [](#birational-onto-quadric){.pf-ref} shows directly that it is inverse to $\phi$.

On the quadric, the two ruling lines through $p$ are
$$
\{y_0=y_1=0\}
\qquad\text{and}\qquad
\{y_0=y_2=0\}.
$$
Projection contracts them to
$$
[0:0:1]=P_1
\qquad\text{and}\qquad
[0:1:0]=P_2,
$$
respectively. Thus $\rho$ is exactly the birational inverse whose two
exceptional images are the base points of $\phi$.
:::

:::

::: {.pf-step #graph-is-blowup-both-ways}
The graph of $\rho$ is simultaneously
$$
\operatorname{Bl}_pY
$$
and
$$
\operatorname{Bl}_{\{P_1,P_2\}}\PP^2=X'.
$$

::: pf-proof
For projection of a projective variety from a point $p$, the closure of the
graph is the blowup of the variety at the base point of that projection.
Hence the graph of $\rho$ is $\operatorname{Bl}_pY$.

On the other hand, the inverse rational map $\phi$ is defined by the conic
linear system whose only base points are $P_1,P_2$. Blowing them up gives
$X'$ and resolves $\phi$ to $\psi$. The pairs
$$
(\psi(q),\pi(q))\in Y\times\PP^2,
\qquad q\in X',
$$
form the closure of the graph of $\rho$, because on the common dense open
where $\phi$ and $\rho$ are inverse they give exactly that graph. Therefore
$$
X'\cong\operatorname{Bl}_pY.
$$
:::

:::

::: {.pf-step #morphism-and-isomorphism-summary}
Consequently the conic system gives the required morphism and
identification:
$$
\boxed{
X'\xrightarrow{\psi}Y\subseteq\PP^3,
\qquad
X'\cong\operatorname{Bl}_pY.}
$$

::: pf-proof
Steps [](#lifts-to-morphism){.pf-ref}, [](#image-in-quadric){.pf-ref}, [](#quadric-nonsingular){.pf-ref} and [](#birational-onto-quadric){.pf-ref} construct the morphism onto the nonsingular quadric.
Steps [](#exceptional-line-contracted){.pf-ref}, [](#projection-inverse){.pf-ref} and [](#graph-is-blowup-both-ways){.pf-ref} identify its unique contracted $(-1)$-curve and show that
the morphism is the blowdown inverse to blowing up the point $p\in Y$.
:::

:::

::: pf-qed
Steps [](#conics-through-two-points-basis){.pf-ref}, [](#rational-map-base-locus){.pf-ref}, [](#lifts-to-morphism){.pf-ref}, [](#image-in-quadric){.pf-ref}, [](#quadric-nonsingular){.pf-ref}, [](#birational-onto-quadric){.pf-ref}, [](#exceptional-line-contracted){.pf-ref}, [](#projection-inverse){.pf-ref}, [](#graph-is-blowup-both-ways){.pf-ref} and [](#morphism-and-isomorphism-summary){.pf-ref} prove both assertions of the exercise.
:::

:::
:::
