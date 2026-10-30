---
schema: qual/card@1
id: P-FPMMA
kind: problem
title: Level sets and gradients of $xy$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Differentiation
relations: []
review: draft
---

::: {.problem}
Draw representative level sets
$$
f^{-1}(c),\qquad c\in\RR,
$$
for
$$
f(x,y)=xy.
$$
Next compute and draw the gradient $\nabla f$ at a representative collection of points in $\RR^2$. Explain how these two objects must be related in general.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $c\neq0$ the level set $f^{-1}(c)$ is the hyperbola $y=c/x$, lying in the first and third quadrants when $c>0$ and in the second and fourth quadrants when $c<0$. The level set $f^{-1}(0)$ is the union of the two coordinate axes.

::: pf-proof

If $c\neq0$, then $xy=c$ forces $x\neq0$, so $f^{-1}(c)=\theset{(x,c/x)\suchthat x\neq0}$. Its two branches have the coordinate axes as asymptotes, and $x$ and $y$ have the same sign exactly when $c>0$. If $c=0$, then $xy=0$ holds exactly when $x=0$ or $y=0$.

:::

:::

::: {.pf-step #s2}

$\nabla f(x,y)=(y,x)$. For example,
$$
\nabla f(1,1)=(1,1),\quad
\nabla f(2,\tfrac12)=(\tfrac12,2),\quad
\nabla f(1,-1)=(-1,1),\quad
\nabla f(0,1)=(1,0),\quad
\nabla f(0,0)=(0,0).
$$
At each point the gradient is the reflection of the position vector in the line $y=x$; it vanishes only at the origin, and it points toward increasing values of $xy$.

::: pf-proof

$\partial f/\partial x=y$ and $\partial f/\partial y=x$. The sample values follow by substitution.

:::

:::

::: {.pf-step #s3}

In the drawings, each gradient vector is perpendicular to the level curve through its base point. For example, the tangent to $y=1/x$ at $(1,1)$ has direction $(1,-1)$, which is orthogonal to $\nabla f(1,1)=(1,1)$.

::: pf-proof

A tangent vector to $y=c/x$ at $(x_0,c/x_0)$ is $(1,-c/x_0^2)=(1,-y_0/x_0)$, and
$$
(y_0,x_0)\cdot\bigl(1,-y_0/x_0\bigr)=y_0-y_0=0.
$$
On the axes, the tangent to the $x$-axis at $(x_0,0)$ is $(1,0)$ and $\nabla f=(0,x_0)$; the tangent to the $y$-axis at $(0,y_0)$ is $(0,1)$ and $\nabla f=(y_0,0)$. Both products vanish.

:::

:::

::: {.pf-step #s4}

In general, if $f:\RR^2\to\RR$ is $C^1$, then at every point $p$ of a level set $f^{-1}(c)$ the gradient $\nabla f(p)$ is orthogonal to the level set: it is orthogonal to $\gamma'(t_0)$ for every differentiable curve $\gamma$ in $f^{-1}(c)$ with $\gamma(t_0)=p$. When $\nabla f(p)\neq0$, it points in the direction of fastest increase of $f$.

::: pf-proof

If $f(\gamma(t))=c$ for all $t$, the chain rule gives
$$
0=\frac{d}{dt}f(\gamma(t))\Big|_{t=t_0}=\nabla f(p)\cdot\gamma'(t_0).
$$
For a unit vector $u$, the directional derivative is $D_uf(p)=\nabla f(p)\cdot u$, which by the Cauchy--Schwarz inequality is largest when $u=\nabla f(p)/\abs{\nabla f(p)}$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} describe the level sets and gradients to be drawn, and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give their relation: the gradient is everywhere normal to the level sets.

![First-quadrant level curves of $xy$ with gradient vectors.](../../assets/Prelim/figures/2019-06-16-23-42-19.png)

:::

:::

:::
