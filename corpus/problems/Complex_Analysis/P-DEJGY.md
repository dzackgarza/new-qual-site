---
schema: qual/card@1
id: P-DEJGY
kind: problem
title: Level curves of $\Re f$ and $\Im f$ meet orthogonally where $f'\neq0$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Cauchy-Riemann
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source opens part (a) with "$f(z)= u(x,y) +i v(x,y)$ be analytic", missing "Let", and part (b)(ii) asks for the angles between "$\mbox{\textrm Re}{(f)}=0$ and $\mbox{\textrm Im}{(f)}$" with no level for Im(f); the statement adds "Let" and the level Im(f) = 0.'
---

::: {.problem}
(a) Let $f(z)= u(x,y) +i v(x,y)$ be analytic in a domain $D\subset \CC$.
Let $z_0=(x_0,y_0)$ be a point in $D$ which is in the intersection of the curves $u(x,y)= c_1$ and $v(x,y)=c_2$, where $c_1$ and $c_2$ are constants.
Suppose that $f'(z_0)\neq 0$.
Prove that the lines tangent to these curves at $z_0$ are perpendicular.

(b) Let $f(z)=z^2$ be defined in $\CC$.

(i) Describe the level curves of $\operatorname{Re}(f)$ and of $\operatorname{Im}(f)$.

(ii) What are the angles of intersections between the level curves $\operatorname{Re}(f)=0$ and $\operatorname{Im}(f)=0$?
Is your answer in agreement with part a) of this question?
:::

::: {.solution}

::: pf

::: pf-step
(a) The tangent lines to $u=c_1$ and $v=c_2$ at $z_0$ are perpendicular.

::: pf-proof
By the Cauchy--Riemann equations, at $z_0$ we have $\nabla v=(v_x,v_y)=(-u_y,u_x)$, so $\nabla u\cdot\nabla v=-u_xu_y+u_yu_x=0$.
Both gradients have squared length $u_x^2+u_y^2=\abs{f'(z_0)}^2\ne0$, so both level curves are regular at $z_0$, and the tangent line to each is orthogonal to its gradient.
:::

:::

::: pf-step
(b)(i) With $u=x^2-y^2$ and $v=2xy$: for $c\ne0$, $u=c$ is the rectangular hyperbola $x^2-y^2=c$ and $v=c$ is the rectangular hyperbola $xy=c/2$; $u=0$ is the pair of lines $y=\pm x$, and $v=0$ is the pair of coordinate axes.

::: pf-proof
$z^2=(x+iy)^2=x^2-y^2+2ixy$.
:::

:::

::: pf-step
(b)(ii) The curves $\operatorname{Re}(f)=0$ and $\operatorname{Im}(f)=0$ meet only at $0$, at angles $\pi/4$; this agrees with part (a).

::: pf-proof
The lines $y=\pm x$ meet the coordinate axes only at the origin, at angles $\pi/4$ (equivalently $3\pi/4$).
Part (a) does not apply there, because $f'(0)=0$.
:::

:::

:::

:::
