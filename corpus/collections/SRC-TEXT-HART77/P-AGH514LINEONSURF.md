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
    PDF p. 2, downloaded to tmp/sources/ntu-ag2-chapter5.pdf, text version
    `tmp/sources/ntu-ag2-chapter5.md`. Its (a) is the
    card's step s1 and s2; its (b) is the card's step s3 and s4 with the surface
    x^{d-1}z + xz^{d-1} + y^{d-1}w + yw^{d-1} in place of
    xz^{d-1} + yw^{d-1} + x^d + y^d. Both surfaces are checked against the
    printed hypotheses: every monomial has degree d, the line x = y = 0 lies on
    the surface, and the four partial derivatives have no common projective
    zero in characteristic 0. The hypersurface adjunction K_X = (K_{P^3}+X)|_X
    is Hartshorne II.8.20 and the surface adjunction C.(C+K_X) = 2p_a(C)-2 is
    V.1.3, both on printed page 361. Yang Pi-Yeh, Hartshorne Solutions,
    exercise 5.1.4, printed p. 100, text version
    `tmp/sources/lfwin-hartshorne-solutions.md`, is not a solution of (b): it
    states the
    surface and asserts nonsingularity. Not checked: whether the exercise is
    meant for a singular X; under the standing convention opening V.1, printed
    page 357, a surface is nonsingular, which is what makes C^2 and K_X defined.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.1,
    exercise 1.4, printed page 367 (PDF page 382 of the extraction), and the
    National Taiwan University set's Exercise 4 (Yi-Tsung Wang), read in the text
    version tmp/sources/ntu-ag2-chapter5.md, Exercise 4, printed p. 2 of that set.
    On 2026-11-16 the solution was made a transcription of that argument: step s3
    now uses the published degree-d surface x^{d-1}z + xz^{d-1} + y^{d-1}w +
    yw^{d-1} in place of the card's earlier xz^{d-1} + yw^{d-1} + x^d + y^d, and
    step s4 solves the published set's four equations, which it states without
    solution. The check is complete: for d = 2 the four partial derivatives are
    2z, 2x, 2w and 2y, so the common zero is the origin; for d at least 3 the two
    equations of x and z force x = z = 0, since z = 0 gives x = 0 from the
    derivative in z, and z nonzero makes the two relations (d-1)x^{d-2} =
    -z^{d-2} and x^{d-2} = -(d-1)z^{d-2} give (d-1)^2 = 1, false for d at least 3;
    the same argument with y and w in place of x and z gives y = w = 0. The degree
    is d because every monomial has degree d, and the line x = y = 0 lies on the
    surface. Characteristic zero is used only through the nonvanishing of 2,
    d-1 and (d-1)^2 - 1. Part (a) is unchanged and is the same set's argument.
    Not checked: whether the exercise intends a possibly singular X; the standing
    convention opening V.1, printed page 357, is that a surface is nonsingular.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read Egbert's Exercise V.1.4 and Yang's Exercise 5.1.4 in their text
    versions on 2026-11-16 and corrected two statements of the published-solution
    remark. Egbert's sentence for (b) reads "The fermat hypersurface
    x^d+y^d+z^d+w^d=0 contains the line x - root(n) of ..." and breaks off inside
    the formula, so his entry is truncated and exhibits no surface; the earlier
    remark applied it to the pair x+y = z+w = 0, which his sentence does not name.
    The Fermat surface does carry a line in every degree: for any zeta with
    zeta^d = -1 the line x = zeta y, z = zeta w lies on it, the left side becoming
    (zeta^d + 1)(y^d + w^d), and such a zeta exists in characteristic zero for
    every d; only the pair x+y = z+w = 0 lies on it solely for odd d. Those lines
    are not x = y = 0. Yang's surface is x z^{d-1} + x^{d-1} z - y w^{d-1} -
    y^{d-1} w, the last two terms with minus signs, so it is not the National
    Taiwan University set's all-plus surface as the remark had said. Both
    published surfaces have degree d, contain x = y = 0, and have no common
    projective zero among their four partial derivatives, which is the content of
    steps s3 and s4; the minus signs do not affect the pair in y and w. Not
    checked: whether Egbert's truncated sentence completes, after a further change
    of coordinates, to a surface through x = y = 0; no step depends on it.
    Also corrected on the same reading: the events above call x+y = z+w = 0 a
    pair, and it is one line, two linear equations in P^3 cutting out a line;
    the remark now says so. The lines the Fermat surface carries are the
    x = zeta y, z = zeta w of the event above, one for each zeta with
    zeta^d = -1.
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
V\!\left(x^{d-1}z+xz^{d-1}+y^{d-1}w+yw^{d-1}\right), & d\geq2.
\end{cases}}
$$
Then $X_d$ is a degree-$d$ surface containing $L$.

::: pf-proof

For $d=1$, $X_1=V(x)$ is a plane, hence has degree one, and it contains
$L=V(x,y)$.

Suppose $d\geq2$ and set
$$
F_d=x^{d-1}z+xz^{d-1}+y^{d-1}w+yw^{d-1}.
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
&=(d-1)x^{d-2}z+z^{d-1}
=z\left((d-1)x^{d-2}+z^{d-2}\right),
&
\frac{\partial F_d}{\partial z}
&=x^{d-1}+(d-1)xz^{d-2}
=x\left(x^{d-2}+(d-1)z^{d-2}\right),\\
\frac{\partial F_d}{\partial y}
&=(d-1)y^{d-2}w+w^{d-1}
=w\left((d-1)y^{d-2}+w^{d-2}\right),
&
\frac{\partial F_d}{\partial w}
&=y^{d-1}+(d-1)yw^{d-2}
=y\left(y^{d-2}+(d-1)w^{d-2}\right),
\end{aligned}
$$
the factorizations being valid also for $d=2$, where $x^{d-2}=z^{d-2}=1$.
Because $\operatorname{char}k=0$, the integers $d-1$ and $(d-1)^2-1$ are
nonzero in $k$ for $d\geq3$, and $2\neq0$.

Suppose all four partial derivatives vanish at a point of $\PP^3$. For $d=2$
the four values are $2z$, $2x$, $2w$ and $2y$, so all four coordinates
vanish, which is impossible. Let $d\geq3$ and consider the pair
$\partial F_d/\partial x$, $\partial F_d/\partial z$, which involve only $x$ and
$z$.

If $z=0$, then $\partial F_d/\partial x=0$ holds automatically and
$\partial F_d/\partial z=x^{d-1}$ forces $x=0$. If $z\neq0$, then
$\partial F_d/\partial x=0$ gives
$$
(d-1)x^{d-2}=-z^{d-2},
$$
which forces $x\neq0$; then $\partial F_d/\partial z=0$ gives
$$
x^{d-2}=-(d-1)z^{d-2}.
$$
Multiplying the second relation by $d-1$ and comparing with the first gives
$$
(d-1)^2z^{d-2}=z^{d-2},
$$
so $(d-1)^2=1$, which for $d\geq3$ is false. Hence the alternative $z\neq0$
cannot occur, and
$$
x=z=0.
$$
The identical argument applied to the pair $\partial F_d/\partial y$,
$\partial F_d/\partial w$ gives
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
The exercise stands on printed p. 367 of Hartshorne, read off that page of `tmp/sources/hartshorne-1977-algebraic-geometry.pdf` (printed p. $N$ is PDF p. $N+15$; the pages of §V.1 carry no text layer and were read as a 110 dpi render, folio 367 in the footer); the statement above is that page's text, the characteristic-zero hypothesis of (b) and the line $x=y=0$ included.

Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, text version `tmp/sources/ntu-ag2-chapter5.md`, Exercise 4 (solution by Yi-Tsung Wang), printed p. 2 of that set: for (a), $\omega_X\cong\OO_X(d-4)$, so $K\sim(d-4)H$ and $C\cdot H=\deg C=1$, and adjunction $C^2=2g(C)-2-C\cdot K=2-d$; for (b), $X:x+y=0$ for $d=1$ and $X:x^{d-1}z+xz^{d-1}+y^{d-1}w+yw^{d-1}=0$ for $d\ge2$. That degree-$d$ surface contains $x=y=0$, and the four equations
$$
(d-1)x^{d-2}z+z^{d-1}=0,\quad x^{d-1}+(d-1)xz^{d-2}=0,\quad (d-1)y^{d-2}w+w^{d-1}=0,\quad y^{d-1}+(d-1)yw^{d-2}=0
$$
have only the solution $(0,0,0,0)\notin\PP^3$. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are that argument of (a). Step [](#s3){.pf-ref} is that surface, and step [](#s4){.pf-ref} is the check of its four equations, carried out case by case, which the published set states without the case analysis; for $d=1$ step [](#s3){.pf-ref} takes the plane $V(x)$, which contains $L=V(x,y)$, in place of the plane $x+y=0$.

Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, Exercise 5.1.4, printed p. 100, gives for (b) the surface $xz^{d-1}+x^{d-1}z-yw^{d-1}-y^{d-1}w$, whose last two terms carry minus signs and which is therefore not the National Taiwan University set's surface, and writes "Then $X$ is nonsingular" without checking the partial derivatives, so it does not supply part (b) either; the signs change nothing in step [](#s4){.pf-ref}, where $y$ and $w$ enter only through the pair of partial derivatives in them. Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.1.4, printed pp. 255--256, gives (a) as step [](#s2){.pf-ref} does and for (b) writes "The fermat hypersurface $x^d+y^d+z^d+w^d=0$ contains the line $x-\sqrt[n]{\ }$", where his text breaks off inside the formula, so his entry is incomplete and exhibits no surface for (b). The Fermat surface does contain lines in every degree: for any $\zeta$ with $\zeta^d=-1$ the line $x=\zeta y$, $z=\zeta w$ lies on it, since $x^d+y^d+z^d+w^d=(\zeta^d+1)(y^d+w^d)=0$ there, and such a $\zeta$ exists in characteristic zero for every $d$; only the line $x+y=z+w=0$ lies on it solely for odd $d$, because $x^d+(-x)^d=2x^d$ in even degree. Those lines are not the required $x=y=0$, and a linear change of coordinates carrying one of them there would have to be applied to his truncated sentence, which he never writes.
:::
