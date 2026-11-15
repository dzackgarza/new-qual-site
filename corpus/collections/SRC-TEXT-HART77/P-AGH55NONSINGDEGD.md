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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    A. Shichijo, R.Hartshorne "Algebraic Geometry" 演習問題への解答
    (2020/March), Chapter 1 section 5, Exercise 5.5, printed pp. 3--4, read in
    the MinerU extraction tmp/sources/shitijyou-ch1-section5.md, is recorded as
    a source searched and not as a proof. It takes the same equation as
    Borcherds and the Stacks Project, F = x_0x_1^{d-1}+x_1x_2^{d-1}+x_2x_0^{d-1},
    reduces nonvanishing of the Jacobian to the three equations
    a^{d-1}+ab^{d-1}+b = 0, (d-1)a^{d-2}+b^{d-1} = 0, (d-1)ab^{d-2}+1 = 0 on the
    chart x_0 = 1, and eliminates a, b to reach (d-1)^2/(d-2) = 1, which it then
    solves in the integers: d^2-3d+3 = 0 has no integral root, so it concludes
    that the equation is nonsingular. That last step is the defect. The equation
    (d-1)^2/(d-2) = 1 is an identity in k, not in Z, and it holds in k whenever
    its two sides agree there. For p = 7, d = 4 it reads 9/2 = 1, which in F_7 is
    2/2 = 1, and the point (x_0:x_1:x_2) = (4:2:1) is on the curve and singular
    over F_7: on the chart x_0 = 1 it is (a,b) = (4,2), and
    a^3+ab^3+b = 64+32+2 = 98 = 0, 3a^2+b^3 = 48+8 = 56 = 0 and
    3ab^2+1 = 48+1 = 49 = 0 modulo 7. So the source does not settle p = 3, and its
    elimination does not settle any prime either; the card's own equation
    x^{d-1}y+y^{d-1}z+z^d stands, with the Stacks tag 0BYA citation for
    p nmid d and p | d, p != 3. The cancellation is on printed p. 4.
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
A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.5, printed pp. 3--4, takes the equation $x_0x_1^{d-1}+x_1x_2^{d-1}+x_2x_0^{d-1}$ and eliminates the two chart coordinates to reach $(d-1)^2/(d-2)=1$, which it then solves over $\ZZ$. That last step is where its argument fails: the identity is one in $k$, and in characteristic $7$ with $d=4$ it holds, the point $(4:2:1)$ being a singular point of that curve over $\FF_7$, as the three reduced equations $a^3+ab^3+b=98$, $3a^2+b^3=56$ and $3ab^2+1=49$ at $(a,b)=(4,2)$ show. So the source proves nothing for $p\mid d$, characteristic $3$ included.

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
