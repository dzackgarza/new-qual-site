---
schema: qual/card@1
id: P-UGAP11F-08
kind: problem
title: Level sets and gradients of $x^2-y^2$
classification:
  areas: [prelim]
  topics:
  - Multivariable Calculus
  - Differentiation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Draw representative level sets
$$
f^{-1}(c),\qquad c\in\RR,
$$
for
$$
f(x,y)=x^2-y^2.
$$
Next compute and draw $\nabla f$ at a representative collection of points in $\RR^2$. Explain how gradients and level sets must be related in general.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The level set
$$
f^{-1}(c)
=
\{(x,y):x^2-y^2=c\}
$$
has three different forms according to the sign of $c$.


::: pf-proof

If $c>0$, then
$$
\frac{x^2}{c}
-\frac{y^2}{c}
=1,
$$
so the level set is a hyperbola opening to the right and left, with vertices
$$
(\pm\sqrt c,0)
$$
and asymptotes
$$
y=\pm x.
$$

If $c<0$, write
$$
c=-a
$$
with $a>0$. Then
$$
\frac{y^2}{a}
-\frac{x^2}{a}
=1,
$$
so the level set is a hyperbola opening upward and downward, with vertices
$$
(0,\pm\sqrt a)
$$
and the same asymptotes
$$
y=\pm x.
$$

If $c=0$, then
$$
x^2-y^2
=(x-y)(x+y)
=0,
$$
so
$$
f^{-1}(0)
=
\{y=x\}
\cup
\{y=-x\}.
$$
These descriptions determine the requested representative sketches.

:::

:::

::: {.pf-step #s1-2}

The gradient is
$$
\boxed{
\nabla f(x,y)
=(2x,-2y)}.
$$


::: pf-proof

Since
$$
f_x=2x,
\qquad
f_y=-2y,
$$
the definition of the gradient gives the formula.

:::

:::

::: {.pf-step #s1-3}

Representative gradient vectors include
$$
\begin{array}{c|c}
(x,y)&\nabla f(x,y)\\
\hline
(1,0)&(2,0)\\
(-1,0)&(-2,0)\\
(0,1)&(0,-2)\\
(0,-1)&(0,2)\\
(1,1)&(2,-2)\\
(-1,1)&(-2,-2)
\end{array}
$$
and
$$
\nabla f(0,0)=0.
$$


::: pf-proof

Substitute the listed points into the formula from step [](#s1-2){.pf-ref}. These vectors give representative arrows for the gradient sketch.

:::

:::

::: {.pf-step #s1-4}

At every regular point of a level set, the gradient is perpendicular to the level set.


::: pf-proof

Let
$$
\gamma:(-\varepsilon,\varepsilon)\to\RR^2
$$
be a smooth curve lying in the level set
$$
f^{-1}(c).
$$
Then
$$
f(\gamma(t))=c
$$
for all $t$, so differentiating gives
$$
0
=
\frac d{dt}f(\gamma(t))
=
\nabla f(\gamma(t))
\cdot
\gamma'(t).
$$
Thus the gradient is orthogonal to every tangent vector
$$
\gamma'(t)
$$
of the level set.

At a point where
$$
\nabla f\ne0,
$$
the level set is locally a smooth curve, so this means the gradient is a normal vector to that curve.

:::

:::

::: {.pf-step #s1-5}

For the present function, the only critical point is the origin.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\nabla f(x,y)=0
$$
if and only if
$$
x=0,
\qquad
y=0.
$$
At the origin the zero level set is the crossing of the two lines
$$
y=\pm x,
$$
so there is no single tangent line there. This is exactly where the usual nonzero-gradient normal-vector picture fails.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} describe the level sets and gradient field, while steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} establish their general geometric relation and identify the exceptional critical point.

:::

:::

:::
