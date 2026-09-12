---
schema: qual/card@1
id: P-DEJGY
kind: problem
title: (a) $f(z)= u(x,y) +i v(x,y)$ be analytic in a domain
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Cauchy-Riemann
  - Harmonic Functions
relations: []
review: draft
---

::: problem
(a) $f(z)= u(x,y) +i v(x,y)$ be analytic in a domain $D\subset {\mathbb C}$.
Let $z_0=(x_0,y_0)$ be a point in $D$ which is in the intersection of the curves $u(x,y)= c_1$ and $v(x,y)=c_2$, where $c_1$ and $c_2$ are constants.
Suppose that $f'(z_0)\neq 0$.
Prove that the lines tangent to these curves at $z_0$ are perpendicular.

(b) Let $f(z)=z^2$ be defined in ${\mathbb C}$.
(i)   Describe the level curves of $\mbox{\textrm Re}{(f)}$ and of $\mbox{Im}{(f)}$.

(ii)  What are the angles of intersections between the level curves $\mbox{\textrm Re}{(f)}=0$ and $\mbox{\textrm Im}{(f)}$?
Is your answer in agreement with part a) of this question?
:::

::: solution
(a) Since $f'(z_0)\ne0$, the Cauchy--Riemann equations give
\[
\nabla u=(u_x,u_y),
\qquad
\nabla v=(v_x,v_y)=(-u_y,u_x),
\]
at $z_0$. Thus
\[
\nabla u\cdot\nabla v=-u_xu_y+u_yu_x=0,
\]
and both gradients are nonzero because
$|f'(z_0)|^2=u_x^2+u_y^2$. The tangent line to a regular level curve is
orthogonal to its gradient, so the tangent lines to $u=c_1$ and $v=c_2$ are
perpendicular.

(b) For $f(z)=z^2$,
\[
u(x,y)=x^2-y^2,
\qquad
v(x,y)=2xy.
\]
Hence $u=c$ consists of the rectangular hyperbolas $x^2-y^2=c$, while
$v=c$ consists of the rectangular hyperbolas $2xy=c$; the zero levels are
the lines $y=\pm x$ and the coordinate axes, respectively.

Part (ii) is incomplete in the source because it writes only
``$\operatorname{Im}(f)$'' rather than specifying a level. Under the natural
reading $\operatorname{Im}(f)=0$, the curves $\operatorname{Re}(f)=0$ are
$y=\pm x$, while $\operatorname{Im}(f)=0$ gives the $x$- and $y$-axes. Every
intersection angle is therefore $\pi/4$ (or its supplementary angle
$3\pi/4$). The origin is exceptional for part (a), since $f'(0)=0$, so there
is no contradiction with the orthogonality theorem there.
:::
