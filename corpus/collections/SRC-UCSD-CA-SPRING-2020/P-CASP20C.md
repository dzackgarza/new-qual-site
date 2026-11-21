---
schema: qual/card@1
id: P-CASP20C
kind: problem
title: "Mobius transformation from a half-disk to a quadrant"
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and the angle computation supplied. The prose said "the tangent is perpendicular to the horizontal line exactly when it is vertical, equivalently when a = 0" without computing the angle; the card now computes the interior angle at p_+ as arccos a from the two boundary directions (-1,0) and (-a,x_0), states what the corner points of D_a and of Q are, and argues that a Moebius map carries corners to corners and preserves angles, whence arccos a = pi/2. It also records that the same argument excludes any conformal map for a != 0, and proves the a = 0 map T(z) = (1+z)/(1-z) by computing Re T > 0 on the disk, the image of the diameter (positive real axis) and of the upper semicircle (positive imaginary axis). The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the answers (only a = 0, with that map) are correct.
---

::: {.problem}
For $a \in (-1, 1)$, let $D_a = \{z : \abs{z} < 1, \operatorname{Im} z > a\}$.
For each such $a$, either find a Möbius transformation of $D_a$ onto the quadrant $Q = \{w = re^{i\theta} : r > 0, 0 < \theta < \frac{\pi}{2}\}$, or show that such a transformation cannot exist.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Let $Q=\{re^{i\theta}:r>0,\ 0<\theta<\frac\pi2\}$ and $D_a=\{z:\abs z<1,\ \operatorname{Im}z>a\}$ for $a\in(-1,1)$.

::: pf

::: {.pf-step #corners}
$\partial D_a$ consists of the horizontal segment from $p_-=(-x_0,a)$ to $p_+=(x_0,a)$ and the circular arc from $p_+$ to $p_-$ along $\abs z=1$, where $x_0=\sqrt{1-a^2}>0$; these are smooth except at $p_\pm$.

::: pf-proof
$z\in\partial D_a$ iff $\abs z=1$ with $\operatorname{Im}z\ge a$, or $\operatorname{Im}z=a$ with $\abs z\le1$. The two conditions hold together exactly at the two points with $\operatorname{Im}z=a$ and $\abs z=1$, namely $p_\pm=(\pm\sqrt{1-a^2},a)$, which exist and are distinct because $\abs a<1$. The chord is a straight segment, the arc is a circular arc, and their endpoints are precisely $p_\pm$.
:::

:::

::: {.pf-step #angle}
The interior angle of $D_a$ at $p_+$ equals $\arccos a$, and the same holds at $p_-$.

::: pf-proof
Write $p_+=(\cos t_0,\sin t_0)$ with $\cos t_0=x_0>0$ and $\sin t_0=a$. The boundary direction of the chord at $p_+$ pointing into the region is $(-1,0)$. The tangent to the circle at $p_+$ pointing into the region is $(-\sin t_0,\cos t_0)=(-a,x_0)$, which is perpendicular to the radius $(\cos t_0,\sin t_0)$ and points along the arc. The cosine of the angle between $(-1,0)$ and $(-a,x_0)$ is $\frac{a}{\sqrt{a^2+x_0^2}}=a$, since $a^2+x_0^2=1$; so the angle is $\arccos a$. At $p_-$ the same computation with $x_0$ replaced by $-x_0$ gives the same value.
:::

:::

::: {.pf-step #qcorners}
The boundary of $Q$ is smooth except at $0$ and $\infty$, where the interior angle is $\frac\pi2$.

::: pf-proof
$\partial Q$ is the union of the open positive real axis and the open positive imaginary axis, each smooth; they meet at $0$ at a right angle. Under $w\mapsto1/w$, which is a biholomorphism of the sphere fixing $Q$ as a set up to the complementary quadrant, a neighbourhood of $0$ maps to a neighbourhood of $\infty$; so $\infty$ is a corner of the same angle $\frac\pi2$.
:::

:::

::: {.pf-step #necessary}
If a Möbius transformation maps $D_a$ onto $Q$, then $a=0$.

::: pf-proof
A Möbius transformation is a biholomorphism of the sphere, conformal wherever its derivative does not vanish, and it maps the corner points of a domain bijectively onto the corner points of the image, preserving each interior angle. So $\{p_+,p_-\}$ maps onto $\{0,\infty\}$, and steps [](#angle){.pf-ref} and [](#qcorners){.pf-ref} give $\arccos a=\frac\pi2$, that is $a=0$. (The same argument shows that for $a\ne0$ there is no conformal map onto $Q$ at all, not merely no Möbius one.)
:::

:::

::: {.pf-step #sufficient}
$T(z)=\dfrac{1+z}{1-z}$ maps $D_0$ biholomorphically onto $Q$.

::: pf-proof
$T$ is Möbius with pole $1\notin D_0$, so it is a biholomorphism of $\CC\setminus\{1\}$ onto $\CC\setminus\{1\}$. It maps $\DD$ onto the right half-plane: for $\abs z<1$, $\operatorname{Re}\frac{1+z}{1-z}=\frac{1-\abs z^2}{\abs{1-z}^2}>0$. On the real diameter $(-1,1)$ the image is real and positive, since $T(x)\in\RR$ for real $x$ and $T(0)=1$; on the upper semicircle, $\abs z=1$ gives $\operatorname{Re}T(z)=0$ and the image is on the imaginary axis, with $T(i)=(1+i)/(1-i)=i$. The upper half-disk is the part of $\DD$ where $\operatorname{Im}z>0$, and since $T$ maps the real diameter to the positive real axis and the upper semicircle to the positive imaginary axis, and is continuous and injective on $D_0$ with $D_0$ connected, its image is the region bounded by those two rays, namely $Q$.
:::

:::

::: {.pf-step}
A Möbius transformation exists if and only if $a=0$, and for $a=0$ it is $T(z)=\frac{1+z}{1-z}$.

::: pf-proof
Steps [](#necessary){.pf-ref} and [](#sufficient){.pf-ref}.
:::

:::

:::
:::
