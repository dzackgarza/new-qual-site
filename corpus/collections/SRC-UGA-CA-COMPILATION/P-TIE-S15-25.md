---
schema: qual/card@1
id: P-TIE-S15-25
kind: problem
title: The Joukowski map $-\frac12(z+1/z)$ from the upper half-disk to the upper half-plane
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 25.
---

::: {.problem}
Prove that $f ( z ) = - \frac { 1 } { 2 } \left( z + \frac { 1 } { z } \right)$ is a conformal map from half disc $\left\{ z = x + i y : \ \abs{ z } < 1 , \ y > 0 \right\}$ to upper half plane $\halfplane \overset { \cdot } { = } \left\{ z = \overset { \cdot } { x } + i y : \ y > 0 \right\}$
:::

::: {.solution}

Let
$$
D
\coloneqq
\{z:\abs z<1,\ \operatorname{Im}z>0\},
$$
and
$$
f(z)
\coloneqq
-\frac12
\left(
z+\frac1z
\right).
$$

::: pf

::: {.pf-step #s1-1}

The function $f$ is holomorphic on $D$ and
$$
f'(z)\ne0
$$
for every $z\in D$.


::: pf-proof

The point $0$ is not contained in $D$, so $f$ is holomorphic there. Moreover,
$$
f'(z)
=
-\frac12
\left(
1-\frac1{z^2}
\right)
=
\frac{1-z^2}{2z^2}.
$$
Thus $f'(z)=0$ only when
$$
z=\pm1,
$$
and both points lie on the boundary of $D$. Hence $f'(z)\ne0$ throughout $D$.

:::

:::

::: {.pf-step #s1-2}

The map $f$ sends $D$ into the upper half-plane $\HH$.


::: pf-proof

Write
$$
z=x+iy.
$$
Since
$$
\frac1z
=
\frac{x-iy}{\abs z^2},
$$
one has
$$
\operatorname{Im}
\left(
z+\frac1z
\right)
=
y-\frac{y}{\abs z^2}
=
-\frac{y(1-\abs z^2)}{\abs z^2}.
$$
Therefore
$$
\operatorname{Im}f(z)
=
\frac{y(1-\abs z^2)}
{2\abs z^2}.
$$
For $z\in D$,
$$
y>0,
\qquad
\abs z<1,
$$
so the right-hand side is positive. Hence
$$
f(D)\subset\HH.
$$

:::

:::

::: {.pf-step #s1-3}

The map $f$ is injective on $D$.


::: pf-proof

Suppose
$$
f(z_1)=f(z_2).
$$
Then
$$
z_1+\frac1{z_1}
=
z_2+\frac1{z_2}.
$$
Rearranging,
$$
(z_1-z_2)
\left(
1-\frac1{z_1z_2}
\right)
=0.
$$
Thus either
$$
z_1=z_2
$$
or
$$
z_1z_2=1.
$$
But for $z_1,z_2\in D$,
$$
\abs{z_1z_2}<1,
$$
so the second alternative is impossible. Hence $z_1=z_2$.

:::

:::

::: {.pf-step #s1-4}

For every $w\in\HH$, the equation
$$
f(z)=w
$$
has exactly one solution $z\in D$.


::: pf-proof

The equation $f(z)=w$ is equivalent to
$$
z+\frac1z=-2w,
$$
hence to
$$
z^2+2wz+1=0.
$$
Its two roots, say $z_1,z_2$, satisfy
$$
z_1z_2=1.
$$
Neither root lies on the unit circle: if $\abs z=1$, then
$$
\operatorname{Im}f(z)=0
$$
by the formula in step [](#s1-2){.pf-ref}, contradicting $w\in\HH$.

Therefore exactly one root has modulus less than $1$, because the moduli of the two roots multiply to $1$. Let $z$ denote that root. Since
$$
\abs z<1
$$
and
$$
\operatorname{Im}f(z)
=
\frac{\operatorname{Im}z\,(1-\abs z^2)}
{2\abs z^2}
>0,
$$
it follows that
$$
\operatorname{Im}z>0.
$$
Thus $z\in D$.

The other root has modulus greater than $1$, so it does not lie in $D$. Hence the solution in $D$ is unique.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
f:D\longrightarrow\HH
}
$$
is a conformal bijection.


::: pf-proof

Step [](#s1-1){.pf-ref} gives holomorphy and nonvanishing derivative. Step [](#s1-2){.pf-ref} shows that the image lies in $\HH$, step [](#s1-3){.pf-ref} proves injectivity, and step [](#s1-4){.pf-ref} proves surjectivity. Hence $f$ is a conformal map of $D$ onto $\HH$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
