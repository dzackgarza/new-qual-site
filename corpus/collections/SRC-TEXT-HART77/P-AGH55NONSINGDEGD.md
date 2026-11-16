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
    3ab^2+1 = 48+1 = 49 = 0 modulo 7. So the source does not settle p = 7 with
    d = 4, and its conclusion fails there; read in k, however, its elimination
    settles every prime dividing d except p = 3, since d^2-3d+3 = 0 with p | d
    reads 3 = 0. The card's own equation
    x^{d-1}y+y^{d-1}z+z^d stands, with the Stacks tag 0BYA citation for
    p nmid d and p | d, p != 3. The cancellation is on printed p. 4.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The event above was corrected in place, and the remark with it. It had said
    that Shichijo settles no prime; that is false. Its elimination is
    (d-1)^2 = d-2, i.e. d^2-3d+3 = 0, and the step it takes wrongly is only the
    substitution of integers for the elements of k. Read in k the identity gives
    p = 3 when p | d, so the source's argument does settle p | d with p != 3;
    what stays open is p = 3 with 3 | d, which is the case the card's own
    equation covers. The p = 7, d = 4 counterexample above is not a
    counterexample to that: 7 does not divide 4, so it shows only that the
    source's equation can be singular when p nmid d, where the source's integer
    step was the error in a second way. Verified by the two substitutions: with
    p | d one has d = 0, so d^2-3d+3 = 3 in k; with p = 7 and d = 4 the same
    expression is 16-12+3 = 7 = 0 in F_7.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    The residual case p = 3, 3 | d now has a published proof, and step
    characteristic-p-nonsingular is transcribed from the two published ones.
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.5.5,
    printed p. 37 (PDF p. 52 of the checked-in extraction). Nils Matthes,
    answer 705947 to Mathematics Stack Exchange question 705657, read in
    tmp/sources/mse-705657-nonsingular-projective-variety-of-degree-d.md, gives
    the curve X^d + ZX^{d-1} + XY^{d-1} + YZ^{d-1} for char 3 and d divisible
    by 3, with the derivative computation quoted in the remark; recomputed its
    three partials (G_x = y^{d-1} - zx^{d-2}, G_y = z^{d-1} - xy^{d-2},
    G_z = x^{d-1} - yz^{d-2}) and the consequence G = x^d + 3T = x^d, so
    x = 0, then T = xy^{d-1} = 0. Supplied the one step he leaves implicit, that
    a zero coordinate forces all three to vanish, and rewrote the p | d, p != 3
    part from the Stacks Project tag 0BYA affine derivatives into homogeneous
    form, where the three terms of xy^{d-1} + yz^{d-1} + zx^{d-1} are equal and
    F = 3xy^{d-1}. Not checked: any source for the equation
    x^{d-1}y + y^{d-1}z + z^d, which stays on the card as a third example with
    its own two-line check and is not claimed to be published.
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
If $p>0$ and $p\mid d$, the plane curve of degree $d$
$$
\boxed{xy^{d-1}+yz^{d-1}+zx^{d-1}=0}
$$
is nonsingular when $p\ne3$, and the plane curve
$$
\boxed{x^d+zx^{d-1}+xy^{d-1}+yz^{d-1}=0}
$$
is nonsingular when $p=3$.

::: pf-proof
Both equations and both computations are published: the first is the Stacks Project, *Algebraic Curves*, Section 53.9, tag 0BYA, and the second is Nils Matthes, answer 705947 to Mathematics Stack Exchange question 705657.
Since $p\mid d$ one has $d=0$ and $d-1=-1\ne0$ in $k$, and both hold equally in every extension field of $k$; the computations below use nothing else about the field, so a curve nonsingular over $k$ is nonsingular over the algebraic closure.

*The first equation.*
For
$$
F=xy^{d-1}+yz^{d-1}+zx^{d-1}
$$
the partial derivatives are
$$
F_x=y^{d-1}-zx^{d-2},\qquad
F_y=z^{d-1}-xy^{d-2},\qquad
F_z=x^{d-1}-yz^{d-2},
$$
so a singular point of $F=0$ satisfies
$$
y^{d-1}=zx^{d-2},\qquad z^{d-1}=xy^{d-2},\qquad x^{d-1}=yz^{d-2}.
$$
If one coordinate of such a point were zero, all three would be: by the cyclic symmetry of the three equations it suffices to take $x=0$, and then the first gives $y^{d-1}=0$, so $y=0$, and the second gives $z^{d-1}=0$, so $z=0$.
Hence $xy^{d-1}$, $yz^{d-1}$ and $zx^{d-1}$ are nonzero at a singular point, and multiplying the three equations by $x$, $y$ and $z$ respectively gives
$$
xy^{d-1}=zx^{d-1},\qquad yz^{d-1}=xy^{d-1},\qquad zx^{d-1}=yz^{d-1},
$$
that is, the three terms of $F$ are equal.
Then
$$
0=F=xy^{d-1}+yz^{d-1}+zx^{d-1}=3xy^{d-1},
$$
which forces $3=0$ in $k$.
So for $p\ne3$ the curve has no singular point. This is the Stacks Project's computation written out: on the affine piece it uses, the equation is $x+x^{d-1}y+y^{d-1}$ with derivatives $1-x^{d-2}y$ and $x^{d-1}-y^{d-2}$, and its footnote argues that $x^{d-1}=y^{d-2}$ and $x\ne0$ from $1=x^{d-2}y$ give $0=x+x^{d-1}y+y^{d-1}=x+2x^{d-1}y$ and then $0=1+2x^{d-2}y=3$; the version above is the homogeneous one, and it also covers the two coordinates the affine chart drops.

*The second equation.*
Let $p=3$ and
$$
G=x^d+zx^{d-1}+xy^{d-1}+yz^{d-1};
$$
here $3\mid d>0$, so $d\ge3$, and $d-1=-1$ in $k$.
The partial derivatives are
$$
G_x=y^{d-1}-zx^{d-2},\qquad
G_y=z^{d-1}-xy^{d-2},\qquad
G_z=x^{d-1}-yz^{d-2},
$$
the same three expressions as for $F$, because $G=F+x^d$ and $\partial_x(x^d)=dx^{d-1}=0$ since $d=0$ in $k$. (The term $x^d$ is what lets the equation $G=0$ behave differently from $F=0$ although their partials agree.)
So a singular point again satisfies the three equations above, the three terms $xy^{d-1}$, $yz^{d-1}$, $zx^{d-1}$ are again equal, and again none of them is zero.
Writing $T$ for their common value,
$$
0=G=x^d+zx^{d-1}+xy^{d-1}+yz^{d-1}=x^d+3T=x^d,
$$
so $x=0$, and then $T=xy^{d-1}=0$, a contradiction.
Hence for $p=3$ this curve has no singular point.

The equation $x^{d-1}y+y^{d-1}z+z^d$ used here before this transcription is a third example, valid for every $p\mid d$: its partials $(d-1)x^{d-2}y$, $x^{d-1}+(d-1)y^{d-2}z$ and $y^{d-1}$ force $y=0$, then $x=0$, then $z=0$. It is not in the published sources found, and the two equations above replace it.
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
A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.5, printed pp. 3--4, takes the equation $x_0x_1^{d-1}+x_1x_2^{d-1}+x_2x_0^{d-1}$ and eliminates the two chart coordinates to reach $(d-1)^2/(d-2)=1$, that is $d^2-3d+3=0$, which it then solves over $\ZZ$: no integer satisfies it, and it concludes that the curve is nonsingular. The identity is one in $k$, so that step has to be replaced; when it is, the source's argument settles the case $p\mid d$, $p\ne3$. Indeed a singular point gives $(d-1)^2=(d-2)$ in $k$, and for $p\mid d$ the identity $d^2-3d+3=0$ reads $3=0$, so $p=3$. Two cases are left: $p=3$, which the replaced step does not reach, and $p\nmid d$, where the identity can hold and the source's conclusion can fail --- for $p=7$, $d=4$ it does, the point $(4:2:1)$ being a singular point of that curve over $\FF_7$, as the three reduced equations $a^3+ab^3+b=98$, $3a^2+b^3=56$ and $3ab^2+1=49$ at $(a,b)=(4,2)$ show.

The Stacks Project, *Algebraic Curves*, Section 53.9 (Plane curves), tag 0BYA, is the only published treatment found that writes out the case $p \mid d$ with its derivative check. It gives $F=T_0^d+T_1^d+T_2^d$ when $p\nmid d$, and $F=T_0^{d-1}T_1+T_1^{d-1}T_2+T_2^{d-1}T_0$ when $p\mid d$ and $p\neq3$, with the two partial derivatives $1-x^{d-2}y$ and $x^{d-1}-y^{d-2}$ on the affine piece $D_+(T_2)$, and it states that their common zero set together with the equation is empty; it then writes "We leave it to the reader to make examples in characteristic $3$".

That last clause is correct and is where that section's argument stops: on that affine piece $x=y^{d-1}$ makes both partials vanish for every $d-1\not\equiv0$, and the equation there reads
$$x+x^{d-1}y+y^{d-1}=2x+y^{d-1}=2y^{d-1}+y^{d-1}=3y^{d-1},$$
so a singular point of that curve exists over $k$ exactly when $3=0$ in $k$.

The case $p=3$ with $3\mid d$ is supplied in Nils Matthes, answer 705947 to Mathematics Stack Exchange question 705657, *Nonsingular projective variety of degree $d$*, text version `tmp/sources/mse-705657-nonsingular-projective-variety-of-degree-d.md`, asked precisely for this residual case: the curve $V(X^d+ZX^{d-1}+XY^{d-1}+YZ^{d-1})$, and his argument, quoted: "if $[x:y:z]\in C$ is a singular point, then, by considering the partial derivatives of the equation defining $C$, we obtain $zx^{d-2}=y^{d-1}$, $xy^{d-2}=z^{d-1}$ and $yz^{d-2}=x^{d-1}$. Multiplying these equalities by $x,y,z$ respectively, we obtain $zx^{d-1}=xy^{d-1}=yz^{d-1}$ and substituting this into the above equation yields $0=x^d+zx^{d-1}+xy^{d-1}+yz^{d-1}=x^d+3zx^{d-1}=x^d$ as we are in characteristic $3$. Hence $x=0$, but then by the above equalities, $y,z$ have to be equal to zero as well, which is impossible." He also records why the three-term equation cannot be repaired by rescaling its coefficients, and that the fourth term is available because $3\mid d$ makes the partials of $x^d$ vanish. Step [](#characteristic-p-nonsingular){.pf-ref} transcribes this, supplying the one inference he leaves implicit, that a zero coordinate forces all three to vanish.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), text version `tmp/sources/hartshorne-solutions-borcherds.md`, Exercise 5.5, PDF p. 7: "If the characteristic $p$ does not divide $d$ we can use $x^d+y^d+z^d=0$. Otherwise we can use $xy^{d-1}+yz^{d-1}+zx^{d-1}=0$."
William Troiani, *Hartshorne Exercise Solutions* (October 2020), text version `tmp/sources/hartshorne-solutions-troiani.md`, gives no solution to 5.5.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.5.5, PDF p. 45, text version `tmp/sources/hartshorne-solutions-egbert.md`: the same two equations as Borcherds.
The second equation of the published answers is singular whenever $3=0$ in $k$: at $(1:1:1)$ its value is $3$ and each of its three partial derivatives is $d$, so for $p=3$ and $3\mid d$ the point $(1:1:1)$ lies on the curve and is singular. That is why the case needs a different equation, and Matthes's four-term curve is one.
Agree with Borcherds, the Stacks Project and Matthes where they reach: Borcherds's Fermat curve for $p\nmid d$, the Stacks Project and Shichijo for $p\mid d$ with $p\ne3$ (the latter once its integer step is read in $k$), and Matthes for $p=3$ with $3\mid d$. What this card adds is the homogeneous computation of the first equation, which Stacks leaves at two affine derivatives, and the zero-coordinate step of the second.
:::
