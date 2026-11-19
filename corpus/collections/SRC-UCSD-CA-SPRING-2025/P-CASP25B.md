---
schema: qual/card@1
id: P-CASP25B
kind: problem
title: "Mobius and conformal maps from a sector to the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
  - Conformal Maps
  - Sectors
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the two answers already on the card, exactly
    alpha = 1 for the Moebius case and every 0 < alpha <= 1 for the conformal case, both
    correct. Added: the verification that S(z) = (z-1)/(z+1) carries the imaginary axis to the
    circle and the right half-plane onto the disc (via S(1) = 0); a careful version of the
    Moebius obstruction, which the prose stated as "their two supporting lines would both have
    to map to that same generalized circle, impossible because a Moebius transformation is
    injective on generalized circles" — the card now notes that a ray's supporting line maps
    into the same circle as the ray, so two distinct lines would give two distinct circles
    inside the single circle dD; and the construction of the branch z^{1/alpha} through a
    logarithm with argument in (-alpha pi/2, alpha pi/2), with injectivity, the exact image and
    the holomorphic inverse. Not claimed: a retained solution set; the provenance names the
    examination paper.
---

::: {.problem}
Let $\alpha \in (0, 1]$ and $\Omega_\alpha \subset \CC$ denote the open region
$$
\Omega_\alpha := \left\{z = re^{i\theta} : \theta \in \left(-\frac{\alpha\pi}{2}, \frac{\alpha\pi}{2}\right), r > 0\right\}.
$$

(i) Determine for which $\alpha$ there is a Möbius transformation $S$ from $\Omega_\alpha$ onto $\DD$.
Prove nonexistence or give an explicit example if such exists.

(ii) Determine for which $\alpha$ there is a conformal map $f$ from $\Omega_\alpha$ onto $\DD$.
Prove nonexistence or give an explicit example if such exists.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2025 complex-analysis examination paper, which carries no solutions. The two answers — (i) a Möbius map exists exactly for $\alpha=1$; (ii) a conformal map exists for every $0<\alpha\le1$ — are the card's own and follow the card's previous prose, with the Möbius argument in (i) made precise and the branch $z^{1/\alpha}$ constructed in (ii) rather than named.

Throughout $0<\alpha\le1$ and $\Omega_\alpha=\theset{re^{i\theta}:\ -\alpha\pi/2<\theta<\alpha\pi/2,\ r>0}$.

::: pf

::: {.pf-step #alpha-one-mobius}
For $\alpha=1$, $S(z)=\dfrac{z-1}{z+1}$ maps $\Omega_1$ biholomorphically onto $\DD$.

::: pf-proof
$\Omega_1$ is the right half-plane $\theset{\operatorname{Re}z>0}$. The map $S$ is Möbius with $S(-1)=\infty$, so it is a biholomorphism of $\CC\setminus\set{-1}$ onto $\CC\setminus\set1$, and it carries the imaginary axis to the unit circle: for $z=it$, $\abs{z-1}=\abs{z+1}$. Hence it maps one of the two components of $\CC\setminus\theset{\operatorname{Re}z=0}$ onto one of the two components of $\CC\setminus\circlegroup$; since $S(1)=0$, the point $1\in\Omega_1$ goes to $0\in\DD$, so $\Omega_1$ maps onto $\DD$.

:::

:::

::: {.pf-step #mobius-structure}
Let $S$ be a Möbius transformation. Then $S(\Omega_\alpha)$ is a domain bounded by two rays lying on two distinct lines through a common point, unless the two boundary rays of $\Omega_\alpha$ are carried by $S$ onto arcs of a single generalized circle.

::: pf-proof
$\partial\Omega_\alpha$ for $\alpha<1$ consists of two rays $R_+$ and $R_-$ on distinct lines through $0$ (for $\alpha=1$ they form one line). A Möbius transformation carries generalized circles and lines to generalized circles or lines, and is a homeomorphism of the sphere carrying $\partial\Omega_\alpha$ onto $\partial S(\Omega_\alpha)$; it also carries the two boundary rays to two arcs (possibly rays or circles) meeting at $S(0)$ and at $S(\infty)$ if these are finite. If both rays map into one generalized circle $\Gamma$, then $S(\Omega_\alpha)$ is one of the two components of $\CC\setminus\Gamma$ — a generalized disk.

:::

:::

::: {.pf-step #no-mobius}
For $0<\alpha<1$ no Möbius transformation maps $\Omega_\alpha$ onto $\DD$.

::: pf-proof
Suppose $S$ does. By step [](#mobius-structure){.pf-ref} applied with $\DD$ in place of the image, the two boundary rays of $\Omega_\alpha$ must map into $\partial\DD$. Then the two supporting lines $L_+$, $L_-$ of the rays map into $\partial\DD$ as well: if a ray maps into a circle, its supporting line maps into the same circle, because the line is the unique generalized circle containing the ray together with the point at infinity and $S$ extends continuously to $\infty$; and $S$ is injective on the sphere. But $L_+$ and $L_-$ are distinct generalized circles meeting at $0$ and at $\infty$, and their images are distinct generalized circles meeting at $S(0)$ and $S(\infty)$ — while a single circle $\partial\DD$ cannot contain two distinct generalized circles. Contradiction.

:::

:::

::: {.pf-step #branch}
For $0<\alpha\le1$ the map $z\mapsto z^{1/\alpha}$ is a well-defined single-valued holomorphic branch on $\Omega_\alpha$, and it maps $\Omega_\alpha$ biholomorphically onto the right half-plane.

::: pf-proof
On $\Omega_\alpha$ define $\log z=\log\abs z+i\arg z$ with $\arg z\in(-\alpha\pi/2,\alpha\pi/2)$; this is holomorphic there (the principal branch of the logarithm composed with a rotation of the cut) and satisfies $e^{\log z}=z$. Then $z^{1/\alpha}\coloneqq\exp\bigl(\tfrac1\alpha\log z\bigr)$ is holomorphic, and it is injective with holomorphic inverse: if $z^{1/\alpha}=w^{1/\alpha}$ then taking $\alpha$-th powers gives $z=w$. Its image: writing $z=re^{i\theta}$, the image is $\exp\bigl(\tfrac1\alpha(\log r+i\theta)\bigr)=r^{1/\alpha}e^{i\theta/\alpha}$, and $\theta/\alpha$ ranges over $(-\pi/2,\pi/2)$ while $r^{1/\alpha}$ ranges over $(0,\infty)$; so the image is exactly the right half-plane. A holomorphic bijection with holomorphic inverse is conformal.

:::

:::

::: {.pf-step #part-ii}
For $0<\alpha\le1$, $f(z)=\dfrac{z^{1/\alpha}-1}{z^{1/\alpha}+1}$ maps $\Omega_\alpha$ conformally onto $\DD$.

::: pf-proof
Compose the biholomorphism of step [](#branch){.pf-ref} with $S$ of step [](#alpha-one-mobius){.pf-ref}: a composite of conformal maps is conformal, and the result is the displayed function. Its denominator does not vanish on $\Omega_\alpha$, since $z^{1/\alpha}$ lies in the right half-plane where the value $-1$ is not attained.

:::

:::

::: {.pf-step #conclusion}
(i) a Möbius transformation $\Omega_\alpha\to\DD$ exists iff $\alpha=1$, and then $S(z)=(z-1)/(z+1)$; (ii) a conformal map exists for every $0<\alpha\le1$, given by $f(z)=(z^{1/\alpha}-1)/(z^{1/\alpha}+1)$.

::: pf-proof
Steps [](#alpha-one-mobius){.pf-ref} and [](#no-mobius){.pf-ref} settle (i), and step [](#part-ii){.pf-ref} settles (ii). The two answers differ because a sector with $\alpha<1$ is conformally but not Möbius-equivalent to the disk: the exponent $1/\alpha$ is conformal but not Möbius, and no Möbius map can open the angle at $0$.

:::

:::

:::
:::
