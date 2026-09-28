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

1.  from $\{ z: |z - 1/2| > 1/2, \text{Re}(z)>0 \}$ to $\mathbb H$

2.  from $\{ z: |z - 1/2| > 1/2, |z| <1  \}$ to $\mathbb D$

3.  from the intersection of the disk $|z + i| < \sqrt{2}$ with
    ${\mathbb H}$ to ${\mathbb D}$.

4.  from ${\mathbb D}  \backslash [a, 1)$ to
    ${\mathbb D} \backslash [0, 1)$ ($0<a<1)$. 

    > Short solution possible using Blaschke factors.

5.  from $\{ z: |z| < 1, \text{Re}(z) > 0 \} \backslash (0, 1/2]$ to
    $\mathbb H$.

:::

::: {.solution}
**Part 1.**
The region is bounded by $i\RR$ and the circle $S=\theset{\abs{z-1/2}=1/2}$, which meet at $0$ and $\infty$. Let $f(z)=1/z$ and write $z=x+iy$. Then $\Re f(z)=x/\abs z^2$, so $\Re z>0$ if and only if $\Re f(z)>0$, and
\[
\abs{z-1/2}>1/2 \iff x^2+y^2>x \iff \Re f(z)<1
.\]
So $f$ maps the region onto the strip $0<\Re(w)<1$:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_18-14-29.png)

The remaining steps are:

- Dilate and rotate to $0<\Im(w) < \pi$ using $w\mapsto i\pi w$.
- Exponentiate using $w\mapsto e^w$ to get $\HH$.

The composite is $z\mapsto e^{i\pi/z}$.

**Part 2.**
The region is a lune with vertex $1$, where the circles $\abs z=1$ and $\abs{z-1/2}=1/2$ are tangent.
Send $1\to \infty$ with $f(z) \da {1\over z-1}$. For $z=x+iy$,
\[
\Re f(z)={x-1\over\abs{z-1}^2},
\qquad
\Re f(z)>-1\iff x^2+y^2>x,
\qquad
\Re f(z)<-{1\over2}\iff x^2+y^2<1
,\]
so $f$ maps the region onto the strip $-1<\Re(w) < -{1\over 2}$. For instance

- ${1\over 2}(1+i) \mapsto -(1+i)$
- $0\mapsto -1$
- $i\mapsto -{1\over 2}(1+i)$
- $-1\mapsto -{1\over 2}$

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_18-32-10.png)

The remaining steps are:

- Translate by $w\mapsto w+{1\over 2}$ to get $-{1\over 2}<\Re(w) < 0$.
- Rotate and dilate by $w\mapsto -2i\pi w$ to get $0<\Im(w) < \pi$.
- Exponentiate by $w\mapsto e^w$ to get $\HH$.
- Apply the Cayley map $w\mapsto {w-i\over w+i}$ to get $\DD$.

**Part 3.**
The circle $\abs{z+i}=\sqrt2$ passes through $\pm1$ and meets $i\RR$ in $\HH$ at $z_3 \da i(\sqrt{2} - 1)$, so the region is a lune with vertices $\pm 1$ bounded by $(-1,1)$ and the arc through $z_3$.
Take $f(z)={z+1\over z-1}$, so that

- $-1\mapsto 0$
- $1\mapsto \infty$
- $0\mapsto -1$


::: {.claim}
$z_3\mapsto w_0$ where $\arg(w_0) = -3\pi/4$
:::


::: {.proof}
Let $z_3 = ic$ where $c\da \sqrt{2} -1$, then
\[
f(z_3) 
&= -{1+z_3\over 1-z_3} \\
&= -{1+ic \over 1-ic} \\
&= -{(1+ic)^2 \over 1+c^2} \\
&= -\qty{ {1-c^2 \over 1+c^2} + i{2c\over 1+c^2} }
.\]
Now $c^2 = 3-2\sqrt 2$ and $1-c^2 = -2+2\sqrt{2}$, so
\[
{ 2c\over 1-c^2} = {2(\sqrt 2 - 1) \over -2 + 2\sqrt 2 } = 1
,\]
so the argument is $\arctan(1) = { \pi \over 4}$ or $-{3\pi \over 4}$.
Since $1-c^2>0$ and $2c>0$, the negative sign places $f(z_3)$ in the third quadrant, so the argument is $-{3\pi \over 4}$.
:::

The segment $(-1,1)$ maps onto the negative real axis, and the arc through $z_3$ maps onto the ray from $0$ through $w_0$. The image of the region is the sector between these rays containing $f(0.2i)=(-0.96-0.4i)/1.04$, namely $-\pi<\Arg(w)<-3\pi/4$:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-31_20-01-07.png)

Now

- Flip this with $w\mapsto -w$ to get $0<\Arg(w) < \pi/4$.
- Rotate clockwise with $w\mapsto e^{-i\pi/8}w$ to get $-\pi/8<\Arg(w) < \pi/8$.
- Dilate the argument to a half-plane with $w\mapsto w^{\pi/(2\theta_0)}=w^4$, where $\theta_0 = \pi/8$, to get $-\pi/2<\Arg(w) < \pi/2$.
- Rotate with $w\mapsto iw$ to get $\HH$.
- Apply the Cayley map $w\mapsto {w-i\over w+i}$.

**Part 4.**
The Blaschke-type map
\[
\varphi(z)={z-a\over1-az}
\]
is an automorphism of $\DD$ since $a\in(0,1)$ is real. It maps $\RR$ to $\RR$, is increasing on $(-1,1)$ since $\varphi'(x)=(1-a^2)/(1-ax)^2>0$, and satisfies $\varphi(a)=0$ and $\varphi(1)=1$. So $\varphi([a,1))=[0,1)$ and $\varphi$ maps $\DD\setminus[a,1)$ onto $\DD\setminus[0,1)$.

**Part 5.**
Let $U$ be the region.

- The squaring map $z\mapsto z^2$ sends the right half-disk $\theset{\abs z<1,\ \Re z>0}$ bijectively onto $\DD\setminus(-1,0]$, and sends the slit $(0,1/2]$ onto $(0,1/4]$. So it maps $U$ onto $\DD\setminus(-1,1/4]$.
- As in Part 4, $z\mapsto {z-1/4\over1-z/4}$ is an automorphism of $\DD$, increasing on $(-1,1)$, with $-1\mapsto-1$ and $1/4\mapsto0$. It maps $\DD\setminus(-1,1/4]$ onto $\DD\setminus(-1,0]$.
- The map $z\mapsto -z$ gives $\DD\setminus[0,1)$.
- The branch of $z\mapsto z^{1/2}$ with argument in $(0,\pi)$ maps $\DD\setminus[0,1)$ onto the upper half-disk $\DD\intersect\HH$.
- The map $z\mapsto -{1\over2}\qty{z+z\inv}$ sends $\DD\intersect\HH$ onto $\HH$, as in [[E-FCTXH]].
:::
