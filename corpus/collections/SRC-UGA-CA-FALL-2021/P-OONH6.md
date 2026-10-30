---
schema: qual/card@1
id: P-OONH6
kind: problem
title: Conformal map from the intersection of $\abs{z-1}<2$ and $\abs{z+1}<2$ to the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map from the intersection of $\abs{z-1}<2$ and $\abs{z+1}<2$ to the upper half plane.
:::

::: {.solution}

Let
$$
D=\{z\in\CC:\abs{z-1}<2,\ \abs{z+1}<2\}.
$$

::: pf

::: pf-step

The two boundary circles meet at
$$
\boxed{\pm i\sqrt3}.
$$


::: pf-proof

At an intersection point $z=x+iy$ one has
$$
(x-1)^2+y^2=4,
\qquad
(x+1)^2+y^2=4.
$$
Subtracting gives $x=0$. Substituting back gives $1+y^2=4$, hence
$y=\pm\sqrt3$.

:::

:::

::: {.pf-step #s1-2}

The Möbius transformation
$$
T(z)=\frac{z-i\sqrt3}{z+i\sqrt3}
$$
sends the two boundary circles of $D$ to two lines through the origin.


::: pf-proof

The points $i\sqrt3$ and $-i\sqrt3$ lie on both boundary circles.
Under $T$ they go to $0$ and $\infty$, respectively. Möbius
transformations send generalized circles to generalized circles, so each
boundary circle maps to a generalized circle through $0$ and $\infty$,
hence to a straight line through the origin.

:::

:::

::: {.pf-step #s1-3}

These two image lines have arguments
$$
\arg w=\frac{\pi}{3}
\qquad\text{and}\qquad
\arg w=\frac{2\pi}{3}
\pmod\pi.
$$


::: pf-proof

The point $1$ lies on $\abs{z+1}=2$, and
$$
T(1)=\frac{1-i\sqrt3}{1+i\sqrt3}=e^{-2\pi i/3}.
$$
Thus that boundary circle maps to the line of argument $\pi/3$ modulo
$\pi$. Likewise, $-1$ lies on $\abs{z-1}=2$, and
$$
T(-1)=\frac{-1-i\sqrt3}{-1+i\sqrt3}=e^{2\pi i/3},
$$
so the other boundary circle maps to the line of argument $2\pi/3$
modulo $\pi$.

:::

:::

::: {.pf-step #s1-4}

The image of $D$ under $T$ is
$$
\boxed{\left\{w:\frac{2\pi}{3}<\arg w<\frac{4\pi}{3}\right\}}.
$$


::: pf-proof

The two image lines bound sectors of opening angles $\pi/3$ and
$2\pi/3$. Since $0\in D$ and $T(0)=-1$, the image sector must contain
the negative real axis. Therefore it is the sector with arguments between
$2\pi/3$ and $4\pi/3$.

:::

:::

::: {.pf-step #s1-5}

Multiplication by $-1$ sends this sector biholomorphically onto
$$
S=\left\{w:-\frac{\pi}{3}<\arg w<\frac{\pi}{3}\right\}.
$$


::: pf-proof

Multiplication by $-1$ shifts arguments by $\pi$ modulo $2\pi$, sending
the interval $(2\pi/3,4\pi/3)$ to $(-\pi/3,\pi/3)$.

:::

:::

::: {.pf-step #s1-6}

On $S$, choose the branch of the logarithm with
$$
-\frac{\pi}{3}<\Arg w<\frac{\pi}{3}.
$$
Then
$$
P(w)=w^{3/2}=\exp\left(\frac32\Log w\right)
$$
maps $S$ conformally and bijectively onto the right half-plane.


::: pf-proof

The chosen branch of $\Log$ is holomorphic on $S$. Multiplication of the
argument by $3/2$ sends
$$
\left(-\frac{\pi}{3},\frac{\pi}{3}\right)
\longrightarrow
\left(-\frac{\pi}{2},\frac{\pi}{2}\right),
$$
while multiplication of the logarithmic modulus by $3/2$ is bijective
on $\RR$. Hence $P$ is a conformal bijection from $S$ onto
$\{\zeta:\Re\zeta>0\}$.

:::

:::

::: {.pf-step #s1-7}

A conformal map from $D$ onto the upper half-plane is
$$
\boxed{
F(z)
=i\left(-\frac{z-i\sqrt3}{z+i\sqrt3}\right)^{3/2}}
$$
where the power uses the branch specified in step [](#s1-6){.pf-ref}.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref}, the expression inside the power maps $D$
conformally and bijectively onto $S$. Step [](#s1-6){.pf-ref} maps $S$ onto the right
half-plane. Multiplication by $i$ rotates the right half-plane onto
$$
\HH=\{z:\Im z>0\}.
$$
Thus the displayed composition is the required conformal bijection.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives an explicit conformal map from the stated intersection
onto the upper half-plane.

:::

:::

:::
