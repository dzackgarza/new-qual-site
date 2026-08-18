---
order: 31
title: "Standard Examples: Conformal Maps"
sort: 10
---

# Standard Examples: Conformal Maps

:::{.remark}
A summary:

- $z\mapsto -z$ is a reflection about $y=x$, so for example sends $\HH \to Q_{34}$ and $\DD \intersect \HH \to \DD \intersect Q_{34}$ and vice-versa.
- $z\mapsto 1/z$: write as $Re^{it} \mapsto R\inv e^{-it}$, which is reflection about $\RR$ and inversion through $S^1$.
- $\DD\to \DD$:  $\lambda {z-a\over 1-\bar{a}z}$ for rotations $\lambda \in S^1$ 
- $\HH\to \DD$: the Cayley map $z\mapsto {z-i\over z+i}$
- Horizontal strips to $\HH$: use $z\mapsto e^z$ for $0<\Im(z) < \pi \to \HH$
	-   These send $\ts{\Im(z) \in (-\pi, \pi) }\too \CC\sm\RR_{\leq 0}$.
- Sectors to $\HH$: for $0<\Arg(z) < {\pi \over n}$, use $z\mapsto z^{n}$ to get $\HH$.
	- Some variants:
		- Unfolding a half-plane: 
		![Squaring](../../../../assets/assets/figures/2021-12-10_20-25-14.png)
		Generally, $$\ts{\Arg(z) \in (-\theta_0, \theta_0) } \mapsvia{z^a} \ts{\Arg(z) \in (-a\theta_0, a\theta_0) }$$
		- Unfolding a symmetric sector:
		![Symmetric sector to right half-plane](../../../../assets/assets/figures/2021-12-10_20-24-49.png)

		  $$z\mapsto z^{\pi \over 2\theta_0}: \ts{\Arg(z) \in (-\theta_0, \theta_0)}\to \ts{\Arg(z) \in (-\pi/2, \pi/ 2)}.$$

- Half-discs to planes: the Joukowski maps $z\mapsto z+z\inv$
- Bigons/lunar domains: map the intersection points $z_0\to 0, z_1\to\infty$ to get strips.
  ![](../../../../assets/assets/figures/2021-12-10_17-12-12.png)
  - In general, take the line through the centers and intersection points. 
    Call the intersection of the two circles $a$, the line with the small circle $b$, and the last $c$, and take $(z; c,b,a)$ to get $0<\Re(z) < 1$.

Some tips:

- A computational shortcut: $z\inv = {\bar{z}\over \abs{z}^2}$. 
  Use this to quickly compute images, e.g. for $\abs{z-1} = 1$ under $f(z) = 1/z$, write $f(1+i)={1\over 1+i} = {1-i \over 2}$.
- The locus of points equidistant to two fixed points is the perpendicular bisector.
- Seems obvious, but *use* that conformal maps preserve angles.
  You can use tangent vectors to reason about angles of intersection (even at $z=\infty$).
  E.g. Since $\abs{z-i}=1$ intersects $\RR$ in a parallel way, since the tangent vectors at zero will line up.
  So any conformal map must send them to parallel lines or circles with intersection angle zero.
  - Similarly if two circles intersect orthogonally, they must go to orthogonal lines or a line orthogonally intersecting a circle.
- $z\mapsto 1/z$ corresponds to a rotation of $\CP^1$ around the $x\dash$axis by $\pi$. 

:::

# The Big 9 Conformal Maps

## $\HH$ and $\DD$

[[PR-OOHFS]]

[[PR-TWG7E]]

## Sectors 

[[PR-AQFRA]]

## Logs and Exponentials

:::{.remark}
The exponential generally sends boxes to sectors, so
\[
\ts{z \st \Re(z) \in [a, b], \Im(z)\in [c, d]}\mapsto \ts{Re^{i\theta} \st R \in [e^a, e^b], \theta\in [c, d]}
.\]

Pictures of the situation:

![](../../../../assets/assets/figures/2021-12-10_16-47-00.png)

![](../../../../assets/assets/figures/2021-12-10_16-47-30.png)

:::

[[PR-3CDLG]]

[[PR-SF23E]]

[[PR-PELLF]]

[[PR-7TLAS]]

## Joukowski Maps

:::{.remark}
A nice resource: <https://complex-analysis.com/content/joukowsky_airfoil.html>

![](../../../../assets/assets/figures/2021-12-29_03-07-40.png)

![](../../../../assets/assets/figures/2021-12-29_23-56-30.png)

In general, $z\mapsto z+z\inv$ has the following effects:

- $\abs{z} = 1$ is mapped onto $[-2, 2]$
- $\DD \intersect \HH$ is mapped to $Q_{34}$
- $\DD^c \intersect \HH$ is mapped to $\HH$
- $\DD^c$ is mapped to $\CC\sm[-2, 2]$

:::

[[PR-IK6LA]]

[[PR-OTMIR]]

[[PR-3LBLV]]

