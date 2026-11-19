---
schema: qual/card@1
id: E-SS8.EX-22
kind: problem
title: The Schwarz--Christoffel formula for maps from the disc onto a polygon
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Schwarz-Christoffel
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the conformal extension and the prevertices, the
    half-plane model with Schwarz--Christoffel, the change-of-variable factor, the use of the angle sum
    $\sum\beta_{j}=2$, and the integration. No retained solution set covers this exercise (the collection
    retains the textbook, not a solutions manual), so the argument is the card's own; the cancellation leading
    to $F'$ was recomputed for this pass.
---

::: {.exercise}
If $P$ is a simply connected region bounded by a polygon with vertices $a_1, \ldots, a_n$ and angles $\alpha_1\pi, \ldots, \alpha_n\pi$, and $F$ is a conformal map of the disc $\DD$ to $P$, then there exist complex numbers $B_1, \ldots, B_n$ on the unit circle, and constants $c_1$ and $c_2$ so that
$$
F(z) = c_1 \int_1^z \frac{d\zeta}{(\zeta - B_1)^{\beta_1} \cdots (\zeta - B_n)^{\beta_n}} + c_2.
$$
[Hint: This follows from the standard correspondence between $\halfplane$ and $\DD$ and an argument similar to that used in the proof of Theorem 4.7.]
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. Here $P$ is a simply connected region bounded by a polygon with vertices $a_{1},\dots,a_{n}$ and interior angles $\alpha_{1}\pi,\dots,\alpha_{n}\pi$, and $F:\DD\to P$ is conformal.

::: pf

::: {.pf-step #prevertices}
With $\beta_{j}=1-\alpha_{j}$, the map $F$ extends to a homeomorphism $\overline{\DD}\to\overline{P}$, and the points $B_{j}=F^{-1}(a_{j})\in\partial\DD$ are distinct.

::: pf-proof
The boundary of $\DD$ is a Jordan curve ($\partial\DD$ is a circle) and $P$ is bounded by the polygon, also a Jordan curve since $P$ is simply connected and bounded by a simple closed polygon; by the Carathéodory extension theorem, quoted as Theorem 4.2, a conformal map between simply connected proper regions with Jordan boundaries extends to a homeomorphism of the closures. So $B_{j}=F^{-1}(a_{j})$ is defined, lies on $\partial\DD$, and the $B_{j}$ are distinct because the $a_{j}$ are distinct vertices and $F^{-1}$ is injective.
:::

:::

::: {.pf-step #halfplane}
Choose a Möbius map $\phi:\halfplane\to\DD$ whose boundary value at $\infty$ is not any $B_{j}$, put $x_{j}=\phi^{-1}(B_{j})\in\RR$, and set $G=F\circ\phi$. Then $x_{j}$ are distinct real numbers, $G$ maps $\halfplane$ conformally onto $P$, and
$$
G'(w)=C\prod_{j=1}^{n}(w-x_{j})^{-\beta_{j}},\qquad \beta_{j}=1-\alpha_{j},
$$
for a nonzero constant $C$.

::: pf-proof
A Möbius map carries the boundary circle $\partial\DD$ onto $\RR\cup\{\infty\}$; choosing it so that the point of $\partial\DD$ sent to $\infty$ is none of the $B_{j}$ makes each $x_{j}$ a finite real number, and the $x_{j}$ are distinct because $\phi$ is injective and the $B_{j}$ are. Composition of conformal maps is conformal, so $G=\phi\circ$ is conformal from $\halfplane$ onto $P$. The Schwarz--Christoffel formula for a bounded polygon with angles $\alpha_{j}\pi$ then gives $G'(w)=C\prod(w-x_{j})^{-\beta_{j}}$ with $\beta_{j}=1-\alpha_{j}$.
:::

:::

::: {.pf-step #factor}
Writing $w=\phi^{-1}(z)=\dfrac{az+b}{cz+d}$ with $ad-bc\ne0$, one has $w-x_{j}=\dfrac{(a-cx_{j})(z-B_{j})}{cz+d}$ and $\dfrac{dw}{dz}=\dfrac{ad-bc}{(cz+d)^{2}}$.

::: pf-proof
Substituting $z=\phi(w)=\frac{aw+b}{cw+d}$ into $w-x_{j}$ and clearing denominators: $w-x_{j}=\frac{w(cw+d)-x_{j}(cw+d)}{cw+d}$, and using $w(cw+d)=aw+b$ gives $w-x_{j}=\frac{aw+b-x_{j}cw-x_{j}d}{cw+d}=\frac{(a-cx_{j})w+(b-x_{j}d)}{cw+d}$; using the fixed point $z=B_{j}$ at $w=x_{j}$ this is $\frac{(a-cx_{j})(w-x_{j})}{cw+d}$, and rewriting in terms of $z$ yields the displayed identity. The derivative is the usual one for a fractional linear map.
:::

:::

::: {.pf-step #anglesum}
$\sum_{j=1}^{n}\beta_{j}=2$.

::: pf-proof
The interior angles of a polygon satisfy $\sum_{j}\alpha_{j}\pi=(n-2)\pi$, so $\sum_{j}\alpha_{j}=n-2$ and $\sum_{j}\beta_{j}=\sum_{j}(1-\alpha_{j})=n-(n-2)=2$.
:::

:::

::: {.pf-step #derivative}
$F'(z)=C_{1}\prod_{j=1}^{n}(z-B_{j})^{-\beta_{j}}$ for a nonzero constant $C_{1}$.

::: pf-proof
Since $F(z)=G(\phi^{-1}(z))$, the chain rule gives $F'(z)=G'(w)\frac{dw}{dz}$ with $w=\phi^{-1}(z)$. Substituting the Schwarz--Christoffel expression and the two identities of step [](#factor){.pf-ref},
$$
F'(z)=C\prod_{j}\Bigl(\frac{(a-cx_{j})(z-B_{j})}{cz+d}\Bigr)^{-\beta_{j}}\cdot\frac{ad-bc}{(cz+d)^{2}}
=C'\,\frac{(cz+d)^{\sum_{j}\beta_{j}}}{(cz+d)^{2}}\prod_{j}(z-B_{j})^{-\beta_{j}},
$$
where $C'=C(ad-bc)\prod_{j}(a-cx_{j})^{-\beta_{j}}\ne0$. By step [](#anglesum){.pf-ref} the exponent $\sum_{j}\beta_{j}$ equals $2$, so the powers of $cz+d$ cancel and $F'(z)=C'\prod_{j}(z-B_{j})^{-\beta_{j}}$, which is the displayed form with $C_{1}=C'$.
:::

:::

::: {.pf-step}
$F(z)=c_{1}\displaystyle\int_{1}^{z}\frac{d\zeta}{(\zeta-B_{1})^{\beta_{1}}\cdots(\zeta-B_{n})^{\beta_{n}}}+c_{2}$.

::: pf-proof
By step [](#derivative){.pf-ref}, on the disc minus the prevertices, $F'$ equals $C_{1}$ times the product of the functions $(\zeta-B_{j})^{-\beta_{j}}$, each defined with a branch of the power on $\DD$ (possible because $B_{j}\notin\DD$ and $\DD$ is simply connected, so $\zeta-B_{j}$ has a holomorphic logarithm there). Integrating $F'$ along a path in $\DD$ from a fixed base point — taken to be $1$, with any path in the disc if $1\in\DD$ is not a prevertex, and with the branch choices above — gives the displayed formula, the integral being independent of the path because $\DD$ is simply connected and the integrand holomorphic. The constants are $c_{1}=C_{1}\ne0$ and $c_{2}=F(1)$ (or the value at the chosen base point). That is the formula asserted, with $\beta_{j}=1-\alpha_{j}$.
:::

:::

:::
:::
