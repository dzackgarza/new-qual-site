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
---

::: {.problem}
a. If a surface $X$ of degree $d$ in $\PP^3$ contains a straight line $C=\PP^1$, show that $C^2=2-d$.

b. Assume $\operatorname{char} k=0$, and show for every $d \geqslant 1$, there exists a nonsingular surface $X$ of degree $d$ in $\PP^3$ containing the line $x=y=0$.
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
K_X=(K_{\PP^3}+X)|_X=(-4H+dH)|_X=(d-4)H.
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
