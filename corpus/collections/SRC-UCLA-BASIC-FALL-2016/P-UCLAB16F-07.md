---
schema: qual/card@1
id: P-UCLAB16F-07
kind: problem
title: Volume of a region cut from a ball by a sphere and a plane
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 7 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Determine the volume of the region in $\RR^3$ determined by the following inequalities:

$$
x^2 + y^2 + z^2 \leq 4, \qquad x^2 - 2x + y^2 + z^2 \geq 0, \quad \text{and} \quad z \geq x.
$$
:::

::: {.solution}

Let
$$
B_2=\{(x,y,z):x^2+y^2+z^2\le4\}
$$
and
$$
B_1=\{(x,y,z):(x-1)^2+y^2+z^2\le1\}.
$$

::: pf

::: {.pf-step #s1-1}

The second inequality is equivalent to being outside the interior of $B_1$.


::: pf-proof

Complete the square:
$$
x^2-2x+y^2+z^2
=
(x-1)^2+y^2+z^2-1.
$$
Thus
$$
x^2-2x+y^2+z^2\ge0
$$
if and only if
$$
(x-1)^2+y^2+z^2\ge1.
$$

:::

:::

::: {.pf-step #s1-2}

The small ball $B_1$ is contained in the large ball $B_2$.


::: pf-proof

Write a point of $B_1$ as
$$
p=e_1+u,
\qquad
e_1=(1,0,0),
\qquad
\norm{u}\le1.
$$
Then
$$
\norm{p}
\le
\norm{e_1}+\norm{u}
\le
1+1
=2.
$$
Hence $p\in B_2$.

:::

:::

::: {.pf-step #s1-3}

The plane
$$
z=x
$$
passes through the center of $B_2$ and divides $B_2$ into two congruent halves.


::: pf-proof

The plane contains the origin.
Reflection across this plane preserves Euclidean distance from the origin and interchanges the halfspaces
$$
z\ge x
\qquad\text{and}\qquad
z\le x.
$$
Thus the two pieces of the centered ball $B_2$ have equal volume.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\operatorname{Vol}(B_2\cap\{z\ge x\})
=
\frac12\cdot\frac43\pi(2)^3
=
\frac{16\pi}{3}.
$$


::: pf-proof

The volume of a radius-$2$ ball is
$$
\frac43\pi 2^3
=
\frac{32\pi}{3}.
$$
Apply step [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

Let
$$
\nu=\frac1{\sqrt2}(-1,0,1),
$$
the unit normal pointing into the halfspace $z\ge x$.
For the center
$$
c=(1,0,0)
$$
of $B_1$,
$$
\nu\cdot c=-\frac1{\sqrt2}.
$$


::: pf-proof

The inequality
$$
z\ge x
$$
is
$$
(-1,0,1)\cdot(x,y,z)\ge0.
$$
Normalizing gives $\nu$.
Then
$$
\nu\cdot c
=
\frac1{\sqrt2}(-1,0,1)\cdot(1,0,0)
=
-\frac1{\sqrt2}.
$$

:::

:::

::: pf-step

In coordinates centered at $c$ with first coordinate
$$
s=\nu\cdot(p-c),
$$
the portion
$$
B_1\cap\{z\ge x\}
$$
is the spherical cap
$$
\frac1{\sqrt2}\le s\le1.
$$


::: pf-proof

For $p\in B_1$,
$$
\norm{p-c}\le1.
$$
The halfspace condition is
$$
\nu\cdot p\ge0.
$$
Since
$$
\nu\cdot p
=
\nu\cdot(p-c)+\nu\cdot c
=
s-\frac1{\sqrt2},
$$
this condition becomes
$$
s\ge\frac1{\sqrt2}.
$$
Inside the unit ball centered at $c$, the coordinate $s$ ranges from $-1$ to $1$.

:::

:::

::: {.pf-step #s1-7}

The volume of this cap is
$$
\boxed{
\operatorname{Vol}(B_1\cap\{z\ge x\})
=
\frac{\pi}{12}(8-5\sqrt2)
}.
$$


::: pf-proof

At fixed coordinate $s$, the cross-section of the unit ball is a disk of radius
$$
\sqrt{1-s^2},
$$
so its area is
$$
\pi(1-s^2).
$$
Hence
$$
\begin{aligned}
\operatorname{Vol}(B_1\cap\{z\ge x\})
&=
\pi\int_{1/\sqrt2}^{1}(1-s^2)\,ds\\
&=
\pi
\left[
s-\frac{s^3}{3}
\right]_{1/\sqrt2}^{1}\\
&=
\pi
\left(
\frac23-\frac1{\sqrt2}+\frac1{6\sqrt2}
\right)\\
&=
\frac{\pi}{12}(8-5\sqrt2).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-8}

The required region has volume
$$
\boxed{
\frac{16\pi}{3}
-
\frac{\pi}{12}(8-5\sqrt2)
=
\frac{\pi}{12}(56+5\sqrt2)
}.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, the desired region is
$$
\bigl(B_2\cap\{z\ge x\}\bigr)
\setminus
B_1.
$$
Since $B_1\subseteq B_2$, the part removed is exactly
$$
B_1\cap\{z\ge x\}.
$$
Subtract the cap volume from step [](#s1-7){.pf-ref} from the half-ball volume in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested volume.

:::

:::

:::
