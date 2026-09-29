---
schema: qual/card@1
id: P-AGH55NONSINGDEGD
kind: problem
title: A nonsingular plane curve of each degree in each characteristic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Nonsingular Varieties
  - Characteristic p
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the existence request with the retained Hartshorne I.5.5 transcription. The solution gives explicit equations in the two cases p does or does not divide d and checks the Jacobian after arbitrary field extension, so the examples are geometrically nonsingular in every characteristic.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
For every degree $d > 0$, and every $p = 0$ or a prime number, give the equation of a nonsingular curve of degree $d$ in $\PP^2$ over a field $k$ of characteristic $p$.
:::

::: {.solution}
Let $[x:y:z]$ be homogeneous coordinates on $\PP_k^2$.
We give equations whose Jacobian has no common projective zero even after extending the ground field, so the resulting curves are geometrically nonsingular.

::: pf

::: {.pf-step #fermat-nonsingular}
If $p=0$ or $p\nmid d$, the Fermat equation
$$
\boxed{x^d+y^d+z^d=0}
$$
defines a nonsingular plane curve of degree $d$.

::: pf-proof
Put
$$
F=x^d+y^d+z^d.
$$
Its partial derivatives are
$$
F_x=d x^{d-1},\qquad
F_y=d y^{d-1},\qquad
F_z=d z^{d-1}.
$$
Under the stated hypothesis $d$ is nonzero in $k$.
Thus simultaneous vanishing of the three partials forces
$$
x=y=z=0,
$$
which is not a projective point.
Hence the projective hypersurface has no singular point by the Jacobian criterion [@Har10a, Chapter I, §5].
The same argument works over every extension field of $k$.
:::

:::

::: {.pf-step #characteristic-p-nonsingular}
If $p>0$ and $p\mid d$, the equation
$$
\boxed{x^{d-1}y+y^{d-1}z+z^d=0}
$$
defines a nonsingular plane curve of degree $d$.

::: pf-proof
Now $d=0$ in $k$, while $d-1=-1$ is nonzero.
For
$$
G=x^{d-1}y+y^{d-1}z+z^d
$$
the partial derivatives are
$$
\begin{aligned}
G_x&=(d-1)x^{d-2}y,\\
G_y&=x^{d-1}+(d-1)y^{d-2}z,\\
G_z&=y^{d-1}.
\end{aligned}
$$
Suppose all three vanish at a projective point of $G=0$.
The equation $G_z=0$ gives $y=0$.
Then $G_y=x^{d-1}=0$, so $x=0$.
At such a point the defining equation becomes
$$
G(0,0,z)=z^d,
$$
forcing $z=0$.
Again this is not a projective point.
Thus no singular point exists.
This calculation also remains valid after any field extension.
For the smallest possible case $d=p=2$, the same formulas read
$$
G=xy+yz+z^2,\qquad
(G_x,G_y,G_z)=(y,x+z,y),
$$
and give the same conclusion.
:::

:::

::: {.pf-step #geometrically-irreducible}
In either case the nonsingular hypersurface is a curve, i.e. a geometrically irreducible one-dimensional projective variety.

::: pf-proof
Each displayed equation is a nonzero homogeneous polynomial of positive degree in $\PP^2$, so every irreducible component has dimension one.
If the polynomial became reducible over an algebraic closure, write it as $AB$ with $A,B$ nonconstant homogeneous polynomials.
The positive-degree plane curves $A=0$ and $B=0$ meet by the projective-plane intersection argument in [[P-AGH31CONICS]], step <1>5.
At a point of intersection, every first partial derivative
$$
\partial(AB)=A\,\partial B+B\,\partial A
$$
vanish.
That would contradict steps [](#fermat-nonsingular){.pf-ref} or [](#characteristic-p-nonsingular){.pf-ref}.
Thus the hypersurface is geometrically irreducible and nonsingular, hence is a plane curve of degree $d$ in the sense of the statement.
:::

:::

::: pf-qed
Step [](#fermat-nonsingular){.pf-ref} covers all characteristics not dividing $d$, and step [](#characteristic-p-nonsingular){.pf-ref} covers the complementary positive-characteristic case.
Step [](#geometrically-irreducible){.pf-ref} verifies that the resulting smooth hypersurfaces are curves.
:::

:::
:::
