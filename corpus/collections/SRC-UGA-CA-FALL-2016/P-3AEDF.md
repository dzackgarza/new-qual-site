---
schema: qual/card@1
id: P-3AEDF
kind: problem
title: Harmonic conjugate of a $C^2$ harmonic function on a disc
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Cauchy-Riemann
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $u(x,y)$ be harmonic and have continuous partial derivatives of order two in an open disc of radius $R>0$.

a.
Let two points $(a,b), (x,y)$ in this disk be given. Show that the following integral is independent of the path in this disk joining these points:
$$
v(x,y) = \int_{(a,b)}^{(x,y)} \left( -\frac{\partial u}{\partial y}\,dx + \frac{\partial u}{\partial x}\,dy\right)
.$$

b. 
In parts:

- Prove that $u(x,y)+i v(x,y)$ is an analytic function in this disc.
- Prove that $v(x,y)$ is harmonic in this disc.
:::

::: {.solution}

Let $D$ be the open disk, and let $P=-u_y$ and $Q=u_x$. Since $u\in C^2(D)$, both $P$ and $Q$ lie in $C^1(D)$.

::: pf

::: {.pf-step #closed}

$Q_x=P_y$ on $D$.

::: pf-proof

$Q_x-P_y=u_{xx}+u_{yy}=\Delta u=0$, because $u$ is harmonic.

:::

:::

::: {.pf-step #indep}

The integral defining $v(x,y)$ is independent of the piecewise smooth path in $D$ from $(a,b)$ to $(x,y)$.

::: pf-proof

The disk $D$ is convex, hence star-shaped about its center. By Step [](#closed){.pf-ref} the $C^1$ form $\omega=P\,dx+Q\,dy$ is closed, so the Poincaré lemma on a star-shaped domain gives a $C^2$ function $F$ on $D$ with $dF=\omega$. For any piecewise smooth path $\gamma$ in $D$ from $(a,b)$ to $(x,y)$,
$$
\int_\gamma\omega=F(x,y)-F(a,b),
$$
which does not depend on $\gamma$.

:::

:::

::: {.pf-step #grad}

$v_x=-u_y$ and $v_y=u_x$ on $D$.

::: pf-proof

By Step [](#indep){.pf-ref}, $v(x,y)=F(x,y)-F(a,b)$, so $\nabla v=\nabla F=(P,Q)=(-u_y,u_x)$.

:::

:::

::: {.pf-step #analytic}

$u+iv$ is analytic on $D$.

::: pf-proof

By Step [](#grad){.pf-ref}, $u_x=v_y$ and $u_y=-v_x$, which are the Cauchy–Riemann equations. The partial derivatives $u_x,u_y,v_x,v_y$ are continuous on $D$, so $u$ and $v$ are real differentiable. A function whose real and imaginary parts are real differentiable and satisfy the Cauchy–Riemann equations is complex differentiable at every point of $D$.

:::

:::

::: {.pf-step #harm}

$v$ is harmonic on $D$.

::: pf-proof

By Step [](#grad){.pf-ref}, $v_x$ and $v_y$ are $C^1$, so $v\in C^2(D)$, and
$$
v_{xx}+v_{yy}=-u_{yx}+u_{xy}=0
$$
by equality of mixed partial derivatives of the $C^2$ function $u$.

:::

:::

::: pf-qed

Step [](#indep){.pf-ref} proves (a), and Steps [](#analytic){.pf-ref} and [](#harm){.pf-ref} prove the two claims of (b).

:::

:::

:::
