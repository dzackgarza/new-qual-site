---
schema: qual/card@1
id: P-LOMSQ
kind: problem
title: Cayley map $\mathbb{H}\to\mathbb{D}$ and the image of the first quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

::: problem
Find a fractional linear transformation $T$ which maps $\HH$ to $\DD$, and explicitly describe the image of the first quadrant under $T$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Find a Möbius transformation $T: \HH \to \DD$ and describe the image of the first quadrant $Q = \theset{x + iy \suchthat x > 0, y > 0}$ under $T$.

<1>1. $T(z) = \frac{z - i}{z + i}$ is a Möbius transformation mapping $\HH$ conformally onto $\DD$.
Proof: This is the standard Cayley map: it sends the boundary $\RR \cup \theset{\infty}$ of $\HH$ to the unit circle (for real $z$, $\abs{z - i} = \abs{z + i}$), sends $i \in \HH$ to $0 \in \DD$, and is a bijection of the Riemann sphere; Möbius maps send circles/lines to circles/lines and preserve the side of the boundary, so $\HH$ maps onto the component of the complement of the unit circle containing $0$, i.e. $\DD$.

<1>2. The first quadrant $Q$ is the intersection of $\HH$ with the right half-plane $\Re z > 0$, bounded by the two rays $\arg z = 0$ (positive real axis) and $\arg z = \pi/2$ (positive imaginary axis).
Proof: $Q = \theset{z \suchthat \Re z > 0, \Im z > 0}$.

<1>3. $T$ maps the positive real axis to the lower semicircle $\theset{e^{i\theta} \suchthat -\pi < \theta < 0}$ from $1$ to $-1$.
Proof: For $x > 0$ real, $T(x) = \frac{x - i}{x + i}$ has modulus 1 and $T(1) = \frac{1-i}{1+i} = -i$; as $x$ runs from $0^+$ to $\infty$, $T(x)$ moves on the unit circle from $T(0) = -1$ through $-i$ to $T(\infty) = 1$, i.e. along the lower semicircle.

<1>4. $T$ maps the positive imaginary axis to the real interval $(-1, 1)$.
Proof: For $y > 0$, $T(iy) = \frac{iy - i}{iy + i} = \frac{y-1}{y+1} \in (-1, 1)$, and as $y$ goes from $0^+$ to $\infty$ this runs over all of $(-1, 1)$ (from $-1$ to $1$).

<1>5. $T(Q)$ is the lower half-disk $\theset{w \in \DD \suchthat \Im w < 0}$.
Proof: $Q$ is the region between the two rays of <1>2; its image under the Möbius map $T$ is the region bounded by the two image curves of <1>3 and <1>4, namely the lower semicircle and the diameter $(-1, 1)$.
The point $i \in Q$ maps to $T(i) = 0$, which lies in the lower half of the disk (indeed $0$ is on the boundary between the two halves; take instead a sample point, e.g. $1 + i \in Q$ with $T(1+i) = \frac{1}{2+i} = \frac{2 - i}{5}$, which has negative imaginary part), so the image is the lower half-disk.

<1>6. Q.E.D. Proof: <1>1 gives the map $T(z) = \frac{z-i}{z+i}$ from $\HH$ onto $\DD$, and <1>5 describes the image of the first quadrant as $\DD \cap \theset{\Im w < 0}$.
:::
