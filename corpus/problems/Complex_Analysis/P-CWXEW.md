---
schema: qual/card@1
id: P-CWXEW
kind: problem
title: "Conformal map from a slit lens to the upper half plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Find a bijective conformal map from $G$ to $\mathbb{H} = \{w \in \mathbb{C} \mid \operatorname{Im}(w) > 0\}$, where
$$G \coloneqq \{z \in \mathbb{C} \mid |z-1| < \sqrt{2}, \, |z+1| < \sqrt{2}\} \setminus [0, i).$$
:::

::: solution
The two boundary circles meet at $\pm i$ with interior angle $\pi/2$.
Set
\[
T_1(z)=\frac{z-i}{z+i}.
\]
This sends $i$ to $0$, $-i$ to $\infty$, and therefore sends the two boundary circles to two lines through the origin. Since $T_1(0)=-1$ lies in the image of the lens, the unslit lens maps to the sector
\[
\frac{3\pi}{4}<\arg w<\frac{5\pi}{4},
\]
whose angle is $\pi/2$. Moreover
\[
T_1(it)=\frac{t-1}{t+1}\in[-1,0)
\qquad(0\le t<1),
\]
so the slit maps to the radial segment $[-1,0)$.

Rotate by $T_2(w)=-w$. Then
\[
T_2T_1(G)
=\left\{\zeta:-\frac\pi4<\arg\zeta<\frac\pi4\right\}\setminus(0,1].
\]
Squaring is injective on this sector and gives
\[
u=\zeta^2\in\HH_R\setminus(0,1],
\qquad
\HH_R=\{u:\Re u>0\}.
\]

Next use the right-half-plane Cayley map
\[
v=\frac{u-1}{u+1}.
\]
It sends $\HH_R$ to $\DD$ and the removed interval $(0,1]$ to $(-1,0]$. Thus
\[
v\in\DD\setminus(-1,0].
\]
The principal square root
\[
s=\sqrt v
\]
maps this slit disk biholomorphically onto the right half-disk
\[
\{s:|s|<1,\ \Re s>0\}.
\]

Finally,
\[
q=\frac{s-i}{s+i}
\]
sends the right half-disk to the third quadrant, and $q\mapsto q^2$ sends that quadrant biholomorphically onto $\HH$.

Consequently an explicit conformal map $G\to\HH$ is the composition
\[
z
\mapsvia{T_1}\frac{z-i}{z+i}
\mapsvia{-}\zeta
\mapsvia{(\cdot)^2}u
\mapsvia{(u-1)/(u+1)}v
\mapsvia{\sqrt{\phantom v}}s
\mapsvia{(s-i)/(s+i)}q
\mapsvia{(\cdot)^2}q^2,
\]
where the square root is the principal branch on $\DD\setminus(-1,0]$.
:::
