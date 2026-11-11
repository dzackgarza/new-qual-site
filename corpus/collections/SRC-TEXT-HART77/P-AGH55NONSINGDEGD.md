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
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Read the Stacks Project, Algebraic Curves, Section 53.9 (tag 0BYA), the
    only published treatment found of the case p | d: it proves the p-nmid-d
    and p|d, p != 3 cases and leaves characteristic 3 to the reader, so the
    equation of step characteristic-p-nonsingular is not taken from any
    source. Recomputed its three partials: y^{d-1}=0 forces y=0, then x=0,
    then z=0, so the curve is nonsingular in every characteristic dividing
    d, d=p=2 included; rechecked the three partials of the published
    equation xy^{d-1}+yz^{d-1}+zx^{d-1} at (1:1:1), each equal to d, so it
    is singular exactly when 3=0. Not checked: the geometric-irreducibility
    step beyond the product rule and I.7.2, and no other field than a
    general one.
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
Hence the projective hypersurface has no singular point by the Jacobian criterion [@Har77, Chapter I, §5].
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
The positive-degree plane curves $A=0$ and $B=0$ meet by [[P-AGH37HYPMEETS]].
At a point of intersection, every first partial derivative
$$
\partial(AB)=A\,\partial B+B\,\partial A
$$
vanishes.
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

::: {.remark title="Published solution"}
The Stacks Project, *Algebraic Curves*, Section 53.9 (Plane curves), tag 0BYA, is the only published treatment found that writes out the case $p \mid d$ with its derivative check. It gives $F=T_0^d+T_1^d+T_2^d$ when $p\nmid d$, and $F=T_0^{d-1}T_1+T_1^{d-1}T_2+T_2^{d-1}T_0$ when $p\mid d$ and $p\neq3$, with the two partial derivatives $1-x^{d-2}y$ and $x^{d-1}-y^{d-2}$ on the affine piece $D_+(T_2)$, and it states that their common zero set together with the equation is empty; it then writes "We leave it to the reader to make examples in characteristic $3$".

That last clause is correct and is where the published argument stops: on that affine piece $x=y^{d-1}$ makes both partials vanish for every $d-1\not\equiv0$, and the equation there reads
$$x+x^{d-1}y+y^{d-1}=2x+y^{d-1}=2y^{d-1}+y^{d-1}=3y^{d-1},$$
so a singular point of the curve exists over $k$ exactly when $3=0$ in $k$. Hence no published set covers $p=3$ with $3\mid d$, and the equation of step [](#characteristic-p-nonsingular){.pf-ref} is not in the literature found.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 5.5, PDF p. 7: "If the characteristic $p$ does not divide $d$ we can use $x^d+y^d+z^d=0$. Otherwise we can use $xy^{d-1}+yz^{d-1}+zx^{d-1}=0$."
William Troiani, *Hartshorne Exercise Solutions* (October 2020), gives no solution to 5.5.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.5.5, PDF p. 45: the same two equations as Borcherds.
The second equation of the published answers is singular whenever $3=0$ in $k$: at $(1:1:1)$ its value is $3$ and each of its three partial derivatives is $d$, so for $p=3$ and $3\mid d$ the point $(1:1:1)$ lies on the curve and is singular. The proof above uses $x^{d-1}y+y^{d-1}z+z^d$ in that case instead, whose partials are $(d-1)x^{d-2}y$, $x^{d-1}+(d-1)y^{d-2}z$ and $y^{d-1}$, and which is nonsingular in every characteristic dividing $d$, the case $d=p=2$ included.
Agree with Borcherds and Stacks where $p\nmid d$, and with Stacks where $p\mid d$ and $p\neq3$; the residual case $p=3$, $3\mid d$ is supplied here, and Stacks records it as left to the reader.
:::
