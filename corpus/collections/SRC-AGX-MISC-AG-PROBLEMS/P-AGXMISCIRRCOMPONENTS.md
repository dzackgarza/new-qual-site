---
schema: qual/card@1
id: P-AGXMISCIRRCOMPONENTS
kind: problem
title: Irreducible components of two algebraic sets
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Algebraic Sets
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked both set-theoretic decompositions directly from the equations.
    For (a), split y^4-x^2 into the branches x=±y^2 and solve the remaining
    equation on each. For (b), parametrize z^2=y^3 away from its origin and
    isolate the locus y=z=0. Verified that every listed component is
    irreducible and maximal among the irreducible subsets obtained.
---

::: {.problem}
Find the irreducible components of the following algebraic sets over $\CC$.

a. $V\big(y^4 - x^2,\ y^4 - x^2 y^2 + x y^2 - x^3\big) \subseteq \AA^2$.

b. $V\big(y^2 - xz,\ z^2 - y^3\big) \subseteq \AA^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #factorization-y4-x2}
In part (a), the first equation factors as
$$
y^4-x^2
=
(y^2-x)(y^2+x).
$$
Hence every point lies on one of the two branches
$$
x=y^2
\qquad\text{or}\qquad
x=-y^2.
$$

::: pf-proof
This is the displayed factorization over $\CC$.
:::

:::

::: {.pf-step #branch-neg-vanishes}
On the branch $x=-y^2$, the second equation vanishes identically.

::: pf-proof
Substituting $x=-y^2$ gives
$$
\begin{aligned}
y^4-x^2y^2+xy^2-x^3
&=
y^4-y^6-y^4+y^6\\
&=0.
\end{aligned}
$$
Thus the entire parabola
$$
C=V(x+y^2)
$$
lies in the algebraic set.
:::

:::

::: {.pf-step #branch-pos-roots}
On the branch $x=y^2$, the second equation vanishes exactly at
$$
(0,0),\qquad(1,1),\qquad(1,-1).
$$

::: pf-proof
Substituting $x=y^2$ gives
$$
\begin{aligned}
y^4-x^2y^2+xy^2-x^3
&=
y^4-y^6+y^4-y^6\\
&=
2y^4(1-y^2).
\end{aligned}
$$
Over $\CC$ this vanishes exactly when
$$
y=0,\quad y=1,\quad\text{or}\quad y=-1.
$$
Since $x=y^2$, these give the three displayed points.
:::

:::

::: {.pf-step #components-part-a}
The irreducible components in part (a) are
$$
\boxed{
V(x+y^2),\qquad
\{(1,1)\},\qquad
\{(1,-1)\}.
}
$$

::: pf-proof
By steps [](#factorization-y4-x2){.pf-ref}, [](#branch-neg-vanishes){.pf-ref} and [](#branch-pos-roots){.pf-ref}, the algebraic set is
$$
C\cup\{(1,1),(1,-1)\}.
$$
The point $(0,0)$ from step [](#branch-pos-roots){.pf-ref} already lies on $C$.

The curve $C$ is irreducible because
$$
\CC[x,y]/(x+y^2)\cong\CC[y]
$$
is an integral domain. Each singleton is irreducible and neither
$(1,1)$ nor $(1,-1)$ lies on $C$, since
$$
1+(\pm1)^2=2\ne0.
$$
Therefore none of the three listed irreducible closed subsets is contained
in another, so they are precisely the irreducible components.
:::

:::

::: {.pf-step #parametrize-z2-y3}
In part (b), every point satisfying
$$
z^2=y^3
$$
either has $y=z=0$, or can be written uniquely in the form
$$
y=t^2,\qquad z=t^3
$$
with $t=z/y$.

::: pf-proof
If $y=0$, then $z^2=0$, so $z=0$.

If $y\ne0$, put
$$
t=\frac zy.
$$
Then
$$
t^2
=
\frac{z^2}{y^2}
=
\frac{y^3}{y^2}
=y,
$$
and therefore
$$
t^3=ty=\frac zy\,y=z.
$$
:::

:::

::: {.pf-step #locus-yz-zero}
On the locus $y=z=0$, the first equation imposes no condition on
$x$, giving the line
$$
L=V(y,z).
$$

::: pf-proof
If $y=z=0$, then
$$
y^2-xz=0
$$
for every $x\in\CC$. Hence this locus is exactly the $x$-axis.
:::

:::

::: {.pf-step #away-from-origin-locus}
Away from $y=z=0$, the first equation forces $x=t$, so the
remaining points lie on
$$
C'=V(y-x^2,\ z-x^3).
$$

::: pf-proof
Using step [](#parametrize-z2-y3){.pf-ref},
$$
y=t^2,\qquad z=t^3
$$
with $t\ne0$. The equation
$$
y^2=xz
$$
becomes
$$
t^4=xt^3.
$$
Since $t\ne0$, this gives $x=t$. Thus such a point is
$$
(t,t^2,t^3).
$$
Conversely every point of this form satisfies both original equations,
including $t=0$. Its image is exactly
$$
V(y-x^2,z-x^3).
$$
:::

:::

::: {.pf-step #components-part-b}
The irreducible components in part (b) are
$$
\boxed{
V(y,z),\qquad
V(y-x^2,\ z-x^3).
}
$$

::: pf-proof
Steps [](#parametrize-z2-y3){.pf-ref}, [](#locus-yz-zero){.pf-ref} and [](#away-from-origin-locus){.pf-ref} show that the algebraic set is $L\cup C'$.
Moreover,
$$
\CC[x,y,z]/(y,z)\cong\CC[x]
$$
and
$$
\CC[x,y,z]/(y-x^2,z-x^3)\cong\CC[x],
$$
so both $L$ and $C'$ are irreducible.

They are distinct and neither contains the other: for example
$$
(1,0,0)\in L\sm C',
\qquad
(1,1,1)\in C'\sm L.
$$
Thus they are exactly the irreducible components.
:::

:::

::: pf-qed
Step [](#components-part-a){.pf-ref} gives the components in part (a), and step [](#components-part-b){.pf-ref} gives the
components in part (b).
:::

:::

:::
