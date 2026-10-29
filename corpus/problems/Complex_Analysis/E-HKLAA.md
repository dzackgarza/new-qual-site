---
schema: qual/card@1
id: E-HKLAA
kind: problem
title: Conformal maps of lunes, slit disks, and half-disks
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
  - Blaschke Factors
relations: []
review: draft
---

::: {.problem}
Find a conformal map

(a) from $\theset{ z \st \abs{z - 1/2} > 1/2,\ \Re(z)>0 }$ to $\HH$

(b) from $\theset{ z \st \abs{z - 1/2} > 1/2,\ \abs{z} <1 }$ to $\DD$

(c) from the intersection of the disk $\abs{z + i} < \sqrt{2}$ with $\HH$ to $\DD$.

(d) from $\DD \setminus [a, 1)$ to $\DD \setminus [0, 1)$ ($0<a<1$).

(e) from $\theset{ z \st \abs{z} < 1,\ \Re(z) > 0 } \setminus (0, 1/2]$ to $\HH$.
:::

::: {.hint}
Part (d) has a short solution using Blaschke factors.
:::

::: {.solution}
Write $z=x+iy$.

::: pf

::: pf-step
(a) $\boxed{z\mapsto e^{i\pi/z}}$.

::: pf-proof
The region is bounded by $i\RR$ and the circle $\abs{z-1/2}=1/2$, which meet at $0$ and $\infty$.
For $f(z)=1/z$, $\Re f(z)=x/\abs z^2$, so $\Re z>0$ if and only if $\Re f(z)>0$, and $\abs{z-1/2}>1/2$ if and only if $x^2+y^2>x$, that is, $\Re f(z)<1$.
So $f$ maps the region onto the strip $0<\Re w<1$:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_18-14-29.png)

Then $w\mapsto i\pi w$ maps the strip onto $0<\Im w<\pi$, and $w\mapsto e^w$ maps that strip onto $\HH$.
:::

:::

::: pf-step
(b) $\boxed{z\mapsto C\qty{\exp\qty{-2\pi i\qty{{1\over z-1}+{1\over2}}}}}$, where $C(w)\coloneqq{w-i\over w+i}$.

::: pf-proof
The region is a lune with vertex $1$, where the circles $\abs z=1$ and $\abs{z-1/2}=1/2$ are tangent.
For $f(z)\coloneqq{1\over z-1}$,
$$
\Re f(z)={x-1\over\abs{z-1}^2},
\qquad
\Re f(z)>-1\iff x^2+y^2>x,
\qquad
\Re f(z)<-{1\over2}\iff x^2+y^2<1
,$$
so $f$ maps the region onto the strip $-1<\Re w < -{1\over 2}$; for instance ${1\over 2}(1+i) \mapsto -(1+i)$, $0\mapsto -1$, $i\mapsto -{1\over 2}(1+i)$ and $-1\mapsto -{1\over 2}$:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_18-32-10.png)

Then $w\mapsto w+{1\over 2}$ gives $-{1\over 2}<\Re w < 0$, $w\mapsto -2\pi i w$ gives $0<\Im w < \pi$, $w\mapsto e^w$ gives $\HH$, and the Cayley map $C$ gives $\DD$.
:::

:::

::: pf-step
(c) $\boxed{z\mapsto C\qty{i\qty{e^{-i\pi/8}\cdot{z+1\over1-z}}^4}}$, with $C$ as in (b).

::: pf-proof
The circle $\abs{z+i}=\sqrt2$ passes through $\pm1$ and meets $i\RR\intersect\HH$ at $z_3 \coloneqq ic$ with $c\coloneqq\sqrt{2} - 1$, so the region is a lune with vertices $\pm 1$ bounded by $(-1,1)$ and the arc through $z_3$.
Let $f(z)\coloneqq{z+1\over z-1}$, so that $-1\mapsto 0$, $1\mapsto \infty$ and $0\mapsto -1$.
Then
$$
f(z_3) = -{1+ic \over 1-ic} = -{(1+ic)^2 \over 1+c^2} = -\qty{ {1-c^2 \over 1+c^2} + i{2c\over 1+c^2} }
.$$
Since $c^2 = 3-2\sqrt 2$, $1-c^2 = 2\sqrt{2}-2 = 2c>0$, so $f(z_3)$ is a negative multiple of $1+i$ and has argument $-3\pi/4$.
The segment $(-1,1)$ maps onto the negative real axis, and the arc through $z_3$ onto the ray of argument $-3\pi/4$.
The image of the region is the sector between these rays containing $f(0.2i)=(-0.96-0.4i)/1.04$, namely $-\pi<\Arg w<-3\pi/4$:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_20-01-07.png)

Then $w\mapsto -w$ gives $0<\Arg w < \pi/4$, $w\mapsto e^{-i\pi/8}w$ gives $\abs{\Arg w} < \pi/8$, $w\mapsto w^4$ gives $\abs{\Arg w} < \pi/2$, $w\mapsto iw$ gives $\HH$, and $C$ gives $\DD$.
Since $-f(z)={z+1\over1-z}$, the composite is the boxed map.
:::

:::

::: {.pf-step #part-d}
(d) $\boxed{\varphi(z)\coloneqq{z-a\over1-az}}$.

::: pf-proof
Since $a\in(0,1)$ is real, $\varphi$ is an automorphism of $\DD$ that maps $\RR$ to $\RR$.
It is increasing on $(-1,1)$ since $\varphi'(x)=(1-a^2)/(1-ax)^2>0$, and $\varphi(a)=0$, $\varphi(1)=1$.
So $\varphi([a,1))=[0,1)$, and $\varphi$ maps $\DD\setminus[a,1)$ onto $\DD\setminus[0,1)$.
:::

:::

::: pf-step
(e) The composite of the following five conformal bijections maps the region $U$ onto $\HH$.

::: pf-proof
- The map $z\mapsto z^2$ sends the right half-disk $\theset{\abs z<1,\ \Re z>0}$ onto $\DD\setminus(-1,0]$ and the slit $(0,1/2]$ onto $(0,1/4]$, so it maps $U$ onto $\DD\setminus(-1,1/4]$.

- As in step [](#part-d){.pf-ref}, $z\mapsto {z-1/4\over1-z/4}$ is an automorphism of $\DD$, increasing on $(-1,1)$, with $-1\mapsto-1$ and $1/4\mapsto0$, so it maps $\DD\setminus(-1,1/4]$ onto $\DD\setminus(-1,0]$.

- The map $z\mapsto -z$ gives $\DD\setminus[0,1)$.

- The branch of $z\mapsto z^{1/2}$ with argument in $(0,\pi)$ maps $\DD\setminus[0,1)$ onto the upper half-disk $\DD\intersect\HH$.

- The map $z\mapsto -{1\over2}\qty{z+z^{-1}}$ sends $\DD\intersect\HH$ onto $\HH$, as in [[P-UGCNF]].
:::

:::

:::

:::
