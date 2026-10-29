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
We say that a function $f : \RR \to \RR$ is convex if and only if

$$
f\big(tx + (1-t)y\big) \leq t f(x) + (1-t) f(y)
$$

for all $x, y \in \RR$ and all $t \in [0, 1]$. Prove the following: Suppose $f : \RR \to \RR$ is differentiable.
Then $f$ is convex if and only if

$$
f(y) \geq f(x) + (y - x) f'(x) \quad \text{for all } x, y \in \RR.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume first that $f$ is convex.
Fix
$$
x,y\in\RR
$$
and define
$$
g(t)=f(x+t(y-x)),
\qquad
0\le t\le1.
$$


::: pf-proof

The map
$$
t\longmapsto x+t(y-x)
$$
parametrizes the line segment from $x$ to $y$.
Since $f$ is differentiable, $g$ is differentiable.

:::

:::

::: {.pf-step #s1-2}

For every
$$
0<t\le1,
$$
convexity gives
$$
g(t)
\le
(1-t)g(0)+tg(1).
$$


::: pf-proof

Since
$$
x+t(y-x)
=(1-t)x+ty,
$$
the defining convexity inequality gives
$$
f((1-t)x+ty)
\le
(1-t)f(x)+tf(y),
$$
which is exactly the displayed inequality.

:::

:::

::: {.pf-step #s1-3}

For every
$$
0<t\le1,
$$
one has
$$
\frac{g(t)-g(0)}{t}
\le
g(1)-g(0).
$$


::: pf-proof

Subtract $g(0)$ from the inequality in step [](#s1-2){.pf-ref}:
$$
g(t)-g(0)
\le
t(g(1)-g(0)).
$$
Divide by the positive number $t$.

:::

:::

::: {.pf-step #s1-4}

Letting $t\downarrow0$ in step [](#s1-3){.pf-ref} gives
$$
g'(0)
\le
g(1)-g(0).
$$


::: pf-proof

Since $g$ is differentiable at $0$,
$$
g'(0)
=
\lim_{t\downarrow0}
\frac{g(t)-g(0)}{t}.
$$
The right-hand side of step [](#s1-3){.pf-ref} is independent of $t$, so passing to the limit gives the claim.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
f(y)
\ge
f(x)+(y-x)f'(x)
}
$$
for all $x,y\in\RR$.


::: pf-proof

By the chain rule,
$$
g'(0)
=(y-x)f'(x).
$$
Also
$$
g(1)-g(0)
=
f(y)-f(x).
$$
Substitute these into step [](#s1-4){.pf-ref} and rearrange.

:::

:::

::: {.pf-step #s1-6}

Conversely, assume
$$
f(y)
\ge
f(x)+(y-x)f'(x)
$$
for all $x,y\in\RR$.
Fix
$$
x,y\in\RR,
\qquad
0\le t\le1,
$$
and set
$$
z=tx+(1-t)y.
$$


::: pf-proof

This introduces the point at which the convexity inequality is to be proved.

:::

:::

::: {.pf-step #s1-7}

Applying the assumed first-order inequality with base point $z$ gives
$$
f(x)
\ge
f(z)+(x-z)f'(z)
$$
and
$$
f(y)
\ge
f(z)+(y-z)f'(z).
$$


::: pf-proof

Use the assumed inequality first with
$$
(x,y)=(z,x)
$$
and then with
$$
(x,y)=(z,y).
$$

:::

:::

::: {.pf-step #s1-8}

Multiply the first inequality in step [](#s1-7){.pf-ref} by $t$, the second by $1-t$, and add.
Then
$$
tf(x)+(1-t)f(y)\ge f(z).
$$


::: pf-proof

The weighted sum gives
$$
\begin{aligned}
tf(x)+(1-t)f(y)
&\ge
tf(z)+(1-t)f(z)\\
&\quad+
\bigl(t(x-z)+(1-t)(y-z)\bigr)f'(z).
\end{aligned}
$$
The first two terms combine to $f(z)$.
Also
$$
\begin{aligned}
t(x-z)+(1-t)(y-z)
&=
tx+(1-t)y-z\\
&=
z-z\\
&=0.
\end{aligned}
$$
Thus the derivative term vanishes, leaving
$$
tf(x)+(1-t)f(y)\ge f(z).
$$

:::

:::

::: {.pf-step #s1-9}

Since
$$
z=tx+(1-t)y,
$$
one has
$$
\boxed{
f(tx+(1-t)y)
\le
tf(x)+(1-t)f(y)
}.
$$


::: pf-proof

Substitute the definition of $z$ from step [](#s1-6){.pf-ref} into step [](#s1-8){.pf-ref}.
This is exactly the defining inequality for convexity.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
f\text{ is convex}
\iff
f(y)\ge f(x)+(y-x)f'(x)
\text{ for all }x,y\in\RR
}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} prove the forward implication, and steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} prove the reverse implication.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required equivalence.

:::

:::

:::
