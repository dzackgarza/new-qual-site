---
schema: qual/card@1
id: P-AGH514LINEONSURF
kind: problem
title: Self-intersection of a line on a degree $d$ surface in $\PP^3$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.4 in the collection source order, the retained Egbert
    companion solution, the surface adjunction formula, the hypersurface
    canonical-class computation, and the projective Jacobian criterion. The
    retained companion uses adjunction for part (a) and points to a Fermat
    hypersurface for part (b). The proof below verifies part (a) independently
    and gives an explicit degree-d hypersurface containing the specified line,
    with nonsingularity checked directly from its partial derivatives.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.1,
    exercise 1.4, printed page 367 (PDF page 382 of the checked-in extraction).
    Located a complete published solution outside the twelve retained sets:
    Algebraic Geometry II, National Taiwan University, 2020 Spring (course of
    Chin-Lung Wang), Chapter V Surfaces homework, Exercise 4 (Yi-Tsung Wang),
    PDF p. 2, downloaded to tmp/sources/ntu-ag2-chapter5.pdf. Its (a) is the
    card's step s1 and s2; its (b) is the card's step s3 and s4 with the surface
    x^{d-1}z + xz^{d-1} + y^{d-1}w + yw^{d-1} in place of
    xz^{d-1} + yw^{d-1} + x^d + y^d. Both surfaces are checked against the
    printed hypotheses: every monomial has degree d, the line x = y = 0 lies on
    the surface, and the four partial derivatives have no common projective
    zero in characteristic 0. The hypersurface adjunction K_X = (K_{P^3}+X)|_X
    is Hartshorne II.8.20 and the surface adjunction C.(C+K_X) = 2p_a(C)-2 is
    V.1.3, both on printed page 361. Yang Pi-Yeh, Hartshorne Solutions,
    exercise 5.1.4, printed p. 100, is not a solution of (b): it states the
    surface and asserts nonsingularity. Not checked: whether the exercise is
    meant for a singular X; under the standing convention opening V.1, printed
    page 357, a surface is nonsingular, which is what makes C^2 and K_X defined.
---

::: {.problem}
(a) If a surface $X$ of degree $d$ in $\PP^3$ contains a straight line $C=\PP^1$, show that $C^2=2-d$.

(b) Assume $\operatorname{char} k=0$, and show for every $d \geqslant 1$, there exists a nonsingular surface $X$ of degree $d$ in $\PP^3$ containing the line $x=y=0$.
:::

::: {.solution}
Let $H$ denote the hyperplane class on $X$, and let
$$
L=V(x,y)\subseteq\PP^3.
$$

::: pf

::: {.pf-step #s1}

The canonical class of $X$ is
$$
K_X=(d-4)H,
$$
and $H\cdot C=1$.

::: pf-proof

Since $X\subseteq\PP^3$ is a nonsingular hypersurface of degree $d$, hypersurface
adjunction gives
$$
K_X=(K_{\PP^3}+X)\restrict_X=(-4H+dH)\restrict_X=(d-4)H.
$$
The curve $C$ is a line in $\PP^3$, so its degree with respect to the hyperplane
class is one. Hence
$$
H\cdot C=1.
$$

:::

:::

::: {.pf-step #s2}

The self-intersection of $C$ is
$$
\boxed{C^2=2-d}.
$$

::: pf-proof

The curve $C\cong\PP^1$ has genus zero. The surface adjunction formula
[[T-SRFADJ]] therefore gives
$$
-2
=
2g(C)-2
=
C\cdot(C+K_X).
$$
Using step [](#s1){.pf-ref},
$$
-2
=
C^2+(d-4)H\cdot C
=
C^2+d-4.
$$
Thus
$$
C^2=2-d.
$$
This proves part (a).

:::

:::

::: {.pf-step #s3}

For every $d\geq1$, define
$$
\boxed{
X_d=
\begin{cases}
V(x), & d=1,\\[2mm]
V\!\left(xz^{d-1}+yw^{d-1}+x^d+y^d\right), & d\geq2.
\end{cases}}
$$
Then $X_d$ is a degree-$d$ surface containing $L$.

::: pf-proof

For $d=1$, $X_1=V(x)$ is a plane, hence has degree one, and it contains
$L=V(x,y)$.

Suppose $d\geq2$ and set
$$
F_d=xz^{d-1}+yw^{d-1}+x^d+y^d.
$$
Every monomial of $F_d$ has degree $d$, so $X_d=V(F_d)$ is a degree-$d$
hypersurface. On $L$ one has $x=y=0$, hence $F_d=0$. Thus
$$
L\subseteq X_d.
$$

:::

:::

::: {.pf-step #s4}

For every $d\geq1$, the surface $X_d$ in step [](#s3){.pf-ref} is nonsingular.

::: pf-proof

The case $d=1$ is immediate because $X_1$ is a plane.

Let $d\geq2$. The first partial derivatives of $F_d$ are
$$
\begin{aligned}
\frac{\partial F_d}{\partial x}
&=z^{d-1}+d x^{d-1},
&
\frac{\partial F_d}{\partial z}
&=(d-1)xz^{d-2},\\
\frac{\partial F_d}{\partial y}
&=w^{d-1}+d y^{d-1},
&
\frac{\partial F_d}{\partial w}
&=(d-1)yw^{d-2}.
\end{aligned}
$$
Because $\operatorname{char}k=0$, both $d$ and $d-1$ are nonzero in $k$.
Suppose all four partial derivatives vanish at a projective point.

If $d=2$, the equation
$$
\frac{\partial F_d}{\partial z}=x=0
$$
followed by $\partial F_d/\partial x=0$ gives $z=0$.
If $d>2$, the equation $xz^{d-2}=0$ gives either $x=0$ or $z=0$; in the
first case $\partial F_d/\partial x=0$ gives $z=0$, while in the second case it
gives $d x^{d-1}=0$, hence $x=0$. Thus in every case
$$
x=z=0.
$$
The identical argument applied to the $y,w$ derivatives gives
$$
y=w=0.
$$
This is impossible for a point of $\PP^3$. Hence the gradient of $F_d$ never
vanishes at a projective point, so the projective Jacobian criterion
[[P-AGH58JACOBIANRANK]] shows that $X_d$ is nonsingular.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a). Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} construct, for every $d\geq1$, a
nonsingular degree-$d$ surface containing the line $x=y=0$, proving part (b).

:::

:::

:::

::: {.remark title="Published solution"}
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 4 (solution by Yi-Tsung Wang), PDF p. 2: for (a), $\omega_X\cong\OO_X(d-4)$, so $K\sim(d-4)H$ and $C\cdot H=\deg C=1$, and adjunction $C^2=2g(C)-2-C\cdot K=2-d$; for (b), $X:x+y=0$ for $d=1$ and $X:x^{d-1}z+xz^{d-1}+y^{d-1}w+yw^{d-1}=0$ for $d\ge2$. That degree-$d$ surface contains $x=y=0$, and the four equations
$$
(d-1)x^{d-2}z+z^{d-1}=0,\quad x^{d-1}+(d-1)xz^{d-2}=0,\quad (d-1)y^{d-2}w+w^{d-1}=0,\quad y^{d-1}+(d-1)yw^{d-2}=0
$$
have only the solution $(0,0,0,0)\notin\PP^3$. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are that argument of (a). Step [](#s3){.pf-ref} replaces their surface by $xz^{d-1}+yw^{d-1}+x^d+y^d$, and step [](#s4){.pf-ref} is their argument of (b).

Yang Pi-Yeh, *Hartshorne Solutions*, Exercise 5.1.4, printed p. 100, states the same surface as the National Taiwan University set for (b) and writes "Then $X$ is nonsingular" without checking the partial derivatives, so it does not supply part (b). Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.1.4, PDF pp. 255--256, gives (a) as step [](#s2){.pf-ref} does and for (b) writes "the Fermat hypersurface $x^d+y^d+z^d+w^d=0$ contains the line $x-n^{\cdots}$", where the text layer breaks off: on that hypersurface $x+y=z+w=0$ lies on it only for odd $d$, because $x^d+(-x)^d=2x^d$ in even degree.
:::
