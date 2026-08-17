---
schema: qual/card@1
id: P-3CTAR
kind: problem
title: "Find a conformal map from the intersection of $|z-1|<2$ and $|z+1|<2$ to the\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - conformal-maps
  - fractional-linear-transformations
relations: []
review: draft
---

::: problem
Find a conformal map from the intersection of $|z-1|<2$ and $|z+1|<2$ to the upper half plane.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Find a conformal map from $\Omega = \{z : \abs{z - 1} < 2\} \cap \{z : \abs{z + 1} < 2\}$ (the lens: intersection of two disks of radius 2 centered at $\pm 1$) onto the upper half-plane.

<1>1. Describe the lens: the two circles $\abs{z-1} = 2$ and $\abs{z+1} = 2$ meet at $z = \pm i\sqrt3$.
    Proof: Intersection of the two circles: $\abs{z-1}^2 = \abs{z+1}^2 = 4$ gives $-2z - 2\bar z + 2 = 2z + 2\bar z + 2$, i.e. $\Re z = 0$; then $\abs{z - 1}^2 = 1 + y^2 = 4$ gives $y = \pm\sqrt3$. So the intersection points are $\pm i\sqrt3$; the lens $\Omega$ is the region inside both disks.

<1>2. Map the lens to the unit disk via a Möbius transformation sending the two intersection points to $0$ and $\infty$.
    Proof: The Möbius map $w = \frac{z - i\sqrt3}{z + i\sqrt3}$ sends the two boundary circles (which pass through both intersection points) to two lines through $0$ and $\infty$: the circles through the preimages of $0$ and $\infty$ become straight lines through the origin. The two circles $\abs{z \pm 1} = 2$ become two lines through $0$ in the $w$-plane. Since both circles intersect the real axis at $z = 3$ and $z = -3$ (for $\abs{z-1}=2$: points $-1, 3$; for $\abs{z+1} = 2$: points $-3, 1$), the images are the two lines through $0$ making angle... the region between them is a wedge/angle.

<1>3. Determine the wedge: the two image lines are the rays through $0$ with arguments $\pm 2\arg$... compute directly: the image of the real segment $(-3, 3)$ (part of the boundary) — the map sends real $z$ to real $w$; the boundary circles map to lines through the origin at angles determined by a test point. Take the point $z = 0 \in \Omega$: $w(0) = \frac{-i\sqrt3}{i\sqrt3} = -1$. Take a boundary point on $\abs{z-1} = 2$, say $z = 3$: $w(3) = \frac{3 - i\sqrt3}{3 + i\sqrt3} = e^{-i\pi/3}$. Take $z = -3$: $w(-3) = \frac{-3 - i\sqrt3}{-3 + i\sqrt3} = e^{i\pi/3}$? Compute: $(-3 - i\sqrt3)/(-3 + i\sqrt3) = (3 + i\sqrt3)/(3 - i\sqrt3) = e^{i\pi/3}$? Indeed $\frac{3 + i\sqrt3}{3 - i\sqrt3} = \frac{(3+i\sqrt3)^2}{12} = \frac{6 + 6i\sqrt3}{12} = \frac{1 + i\sqrt3}{2} = e^{i\pi/3}$. So the boundary circles map to the lines through $0$ and $e^{\pm i\pi/3}$, i.e. the rays at angles $\pm\pi/3$. The lens (containing $w = -1$) maps to the wedge $\abs{\arg w} < \pi/3$? Since $-1$ has argument $\pi$, and the wedge between the two rays at $\pm \pi/3$ that contains the ray $\arg = \pi$ is the angle $\abs{\arg w} > \pi/3$ — wait, need care: the two lines through $0$ at angles $\pm\pi/3$ divide the plane into two wedges of angle $2\pi/3$ each. $w(0) = -1$ lies at angle $\pi$, which is in the wedge $\pi/3 < \arg w < 5\pi/3$, an angle-$4\pi/3$ region? Hmm — the lines at $\pm \pi/3$: the wedge containing $-1$ (angle $\pi$) is $\{\pi/3 < \arg w < 5\pi/3\}$, angle $4\pi/3$. So $\Omega$ maps to the wedge $W = \{\pi/3 < \arg w < 5\pi/3\}$.

<1>4. Map the wedge to the upper half-plane.
    Proof: Rotate by $e^{-i\pi/3}$ to get the wedge $\{0 < \arg < 4\pi/3\}$; then raise to the power $3/4$: $u = \qty(e^{-i\pi/3}w)^{3/4}$ maps the wedge of angle $4\pi/3$ to the upper half-plane $\Im u > 0$.

<1>5. Q.E.D.
    Proof: <1>2–<1>4 give the conformal map $z \mapsto \qty(e^{-i\pi/3} \frac{z - i\sqrt3}{z + i\sqrt3})^{3/4}$ from the lens onto $\HH$ (choosing the branch that sends the interior to the upper half-plane).

:::
