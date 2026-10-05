---
schema: qual/card@1
id: P-UCLAB16F-12
kind: problem
title: First-order characterization of differentiable convex functions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 12 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
We say that a function $f : \mathbb { R } \to \mathbb { R }$ is convex if and only if

$$
f { \big ( } t x + ( 1 - t ) y { \big ) } \leq t f ( x ) + ( 1 - t ) f ( y )
$$

for all $x , y \in \mathbb { R }$ and all $t \in [ 0 , 1 ]$ . Prove the following: Suppose $f : \mathbb { R } \to \mathbb { R }$ is differentiable.
Then f is convex if and only if

$$
f ( y ) \geq f ( x ) + ( y - x ) f ^ { \prime } ( x ) \quad \text { for all } x , y \in \mathbb { R } .
$$
:::

::: {.solution}
<1>1. Assume first that $f$ is convex.
Fix
\[
x,y\in\mathbb R
\]
and define
\[
g(t)=f(x+t(y-x)),
\qquad
0\le t\le1.
\]

::: {.proof}
The map
\[
t\longmapsto x+t(y-x)
\]
parametrizes the line segment from $x$ to $y$.
Since $f$ is differentiable, $g$ is differentiable.
:::

<1>2. For every
\[
0<t\le1,
\]
convexity gives
\[
g(t)
\le
(1-t)g(0)+tg(1).
\]

::: {.proof}
Since
\[
x+t(y-x)
=(1-t)x+ty,
\]
the defining convexity inequality gives
\[
f((1-t)x+ty)
\le
(1-t)f(x)+tf(y),
\]
which is exactly the displayed inequality.
:::

<1>3. For every
\[
0<t\le1,
\]
one has
\[
\frac{g(t)-g(0)}{t}
\le
g(1)-g(0).
\]

::: {.proof}
Subtract $g(0)$ from the inequality in step <1>2:
\[
g(t)-g(0)
\le
t(g(1)-g(0)).
\]
Divide by the positive number $t$.
:::

<1>4. Letting $t\downarrow0$ in step <1>3 gives
\[
g'(0)
\le
g(1)-g(0).
\]

::: {.proof}
Since $g$ is differentiable at $0$,
\[
g'(0)
=
\lim_{t\downarrow0}
\frac{g(t)-g(0)}{t}.
\]
The right-hand side of step <1>3 is independent of $t$, so passing to the limit gives the claim.
:::

<1>5. Therefore
\[
\boxed{
f(y)
\ge
f(x)+(y-x)f'(x)
}
\]
for all $x,y\in\mathbb R$.

::: {.proof}
By the chain rule,
\[
g'(0)
=(y-x)f'(x).
\]
Also
\[
g(1)-g(0)
=
f(y)-f(x).
\]
Substitute these into step <1>4 and rearrange.
:::

<1>6. Conversely, assume
\[
f(y)
\ge
f(x)+(y-x)f'(x)
\]
for all $x,y\in\mathbb R$.
Fix
\[
x,y\in\mathbb R,
\qquad
0\le t\le1,
\]
and set
\[
z=tx+(1-t)y.
\]

::: {.proof}
This introduces the point at which the convexity inequality is to be proved.
:::

<1>7. Applying the assumed first-order inequality with base point $z$ gives
\[
f(x)
\ge
f(z)+(x-z)f'(z)
\]
and
\[
f(y)
\ge
f(z)+(y-z)f'(z).
\]

::: {.proof}
Use the assumed inequality first with
\[
(x,y)=(z,x)
\]
and then with
\[
(x,y)=(z,y).
\]
:::

<1>8. Multiply the first inequality in step <1>7 by $t$, the second by $1-t$, and add.
Then
\[
tf(x)+(1-t)f(y)\ge f(z).
\]

::: {.proof}
The weighted sum gives
\[
\begin{aligned}
tf(x)+(1-t)f(y)
&\ge
tf(z)+(1-t)f(z)\\
&\quad+
\bigl(t(x-z)+(1-t)(y-z)\bigr)f'(z).
\end{aligned}
\]
The first two terms combine to $f(z)$.
Also
\[
\begin{aligned}
t(x-z)+(1-t)(y-z)
&=
tx+(1-t)y-z\\
&=
z-z\\
&=0.
\end{aligned}
\]
Thus the derivative term vanishes, leaving
\[
tf(x)+(1-t)f(y)\ge f(z).
\]
:::

<1>9. Since
\[
z=tx+(1-t)y,
\]
one has
\[
\boxed{
f(tx+(1-t)y)
\le
tf(x)+(1-t)f(y)
}.
\]

::: {.proof}
Substitute the definition of $z$ from step <1>6 into step <1>8.
This is exactly the defining inequality for convexity.
:::

<1>10. Therefore
\[
\boxed{
f\text{ is convex}
\iff
f(y)\ge f(x)+(y-x)f'(x)
\text{ for all }x,y\in\mathbb R
}.
\]

::: {.proof}
Steps <1>1--<1>5 prove the forward implication, and steps <1>6--<1>9 prove the reverse implication.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required equivalence.
:::
:::
