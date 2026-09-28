---
title: Build me a map
order: 0
topics:
- Conformal Maps
- Conformal Mappings
- Conformal Equivalence
- Geometry
---

# Build me a map

A conformal map between two regions is usually written as a composition of maps between standard regions, most often passing through $\HH$ or $\DD$.

## Notation

| Symbol | Region |
| --- | --- |
| $\DD \coloneqq \ts{z \st \abs z < 1}$ | the open unit disc |
| $\HH \coloneqq \ts{z \st \Im z > 0}$ | the open upper half plane |
| $Q_i$ | the $i$th open quadrant, so $Q_1 \coloneqq \ts{z \st \Re z> 0,\ \Im z > 0}$ |
| $Q_{ij}$ | the interior of $\overline{Q_i \union Q_j}$, so $\HH = Q_{12}$ and $Q_{14}$ is the right half plane |
| $L \coloneqq \ts{x+iy \st 0 < y < \pi}$ | the horizontal strip |

All regions in the table are open.

## Maps between standard regions

- **$\HH \to \DD$.** The Cayley map $z\mapsto {z-i \over z+i}$.
  The map $z\mapsto{i-z\over i+z}$ is its composition with $w\mapsto -w$.

- **$\DD \to \DD$.** The automorphisms $z\mapsto\lambda\, {z-a\over 1-\bar a z}$ with $a\in\DD$ and $\lambda \in S^1$; by [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors and automorphisms]], every automorphism of $\DD$ has this form.

- **Sector $\to \HH$.** $z\mapsto z^n$ maps $\ts{0 < \Arg z < \pi/n}$ onto $\HH$.
  More generally, for $0<a\theta_0\leq\pi$, a branch of $z \mapsto z^a$ maps $\ts{\Arg z \in (-\theta_0, \theta_0)}$ onto $\ts{\Arg w \in (-a\theta_0, a\theta_0)}$, so $a = \pi/(2\theta_0)$ maps a symmetric sector onto the right half plane.

  ![Squaring](../../../../assets/assets/figures/2021-12-10_20-25-14.png)

  ![Symmetric sector to right half-plane](../../../../assets/assets/figures/2021-12-10_20-24-49.png)

- **Strip $\to \HH$.** $z\mapsto e^z$ maps $L$ onto $\HH$, and maps $\ts{-\pi<\Im z<\pi}$ onto $\CC\sm\RR_{\leq 0}$.
  For $b-a>0$ and $0<d-c\leq 2\pi$, the exponential maps rectangles to annular sectors:
  $$
  \ts{\Re z \in [a,b],\ \Im z \in [c,d]} \mapsto \ts{Re^{i\theta} \st R\in[e^a,e^b],\ \theta\in[c,d]}
  .$$

- **Half disc $\to$ half plane.** The Joukowski map $z\mapsto z + z\inv$ maps $\abs z = 1$ onto $[-2,2]$, $\DD\intersect\HH$ onto $Q_{34}$, $\overline{\DD}^c \intersect \HH$ onto $\HH$, and $\overline{\DD}^c$ onto $\CC\sm[-2,2]$.

- **Region bounded by two circular arcs $\to$ sector or strip.** A Möbius transformation sending the two intersection points of the arcs to $0$ and $\infty$ maps the region onto a sector.
  If the arcs are tangent at one point, a Möbius transformation sending that point to $\infty$ maps the region onto a strip.

  ![](../../../../assets/assets/figures/2021-12-10_17-12-12.png)

- **Slit plane $\to \HH$.** The branch of $\sqrt z$ with argument in $(0,\pi)$ maps $\CC\sm[0,\infty)$ onto $\HH$.

- **Reflections and inversions.** $z\mapsto -z$ maps $\HH$ onto $Q_{34}$.
  The map $z\mapsto 1/z$ sends $Re^{it}$ to $R\inv e^{-it}$; it is reflection in $\RR$ composed with inversion in $S^1$, and on $\CP^1$ it is the rotation by $\pi$ about the axis through $\pm 1$.

## Boundary features

| The region has | Map |
| --- | --- |
| a corner of angle $\theta_0$ at $0$ | $z^{\pi/\theta_0}$, to a half plane |
| two boundary arcs meeting at two points | a Möbius transformation taking those points to $0$ and $\infty$ |
| two tangent boundary circles | a Möbius transformation taking the point of tangency to $\infty$, giving parallel lines |
| a slit along a ray | a branch of $\sqrt z$ |
| a strip | $e^z$ |
| a half-plane, with target $\DD$ | the Cayley map, then an automorphism of $\DD$ |

## Computational facts

- $z\inv = \bar z/\abs z^2$; for example, under $z\mapsto 1/z$ the point $1+i$ on $\abs{z-1}=1$ goes to ${1-i\over 2}$.

- Conformal maps preserve angles between curves, including at $\infty$ on $\CP^1$.
  Circles meeting orthogonally map to generalized circles meeting orthogonally, and tangent circles map to tangent circles or parallel lines.

- Möbius transformations map generalized circles to generalized circles, where a line is a circle through $\infty$, and map an arc between two points onto an arc between their images.

- The cross ratio sending $a\mapsto 1$, $b \mapsto 0$, $c\mapsto \infty$ is
  $$
  (z; a, b, c) = \frac{z-b}{z-c}\cdot\frac{a-c}{a-b}
  .$$

- $t\mapsto\tan t$ is a bijection $(-\pi/2,\pi/2)\to\RR$, which parameterizes the real line by a bounded interval.

## Standard maps

$\HH$ and $\DD$:

[[PR-OOHFS]]

[[PR-TWG7E]]

Sectors:

[[PR-AQFRA]]

Logs and exponentials:

![](../../../../assets/assets/figures/2021-12-10_16-47-00.png)

![](../../../../assets/assets/figures/2021-12-10_16-47-30.png)

[[PR-3CDLG]]

[[PR-SF23E]]

[[PR-PELLF]]

[[PR-7TLAS]]

Joukowski maps:

![](../../../../assets/assets/figures/2021-12-29_03-07-40.png)

![](../../../../assets/assets/figures/2021-12-29_23-56-30.png)

[[PR-IK6LA]]

[[PR-OTMIR]]

[[PR-3LBLV]]

## Exercises

Cross ratios:

[[E-Z23VB]]
[[E-G55QF]]

Discs and planes:

[[P-IIONX]]
[[E-W6MWU]]
[[E-4H3JY]]
[[E-PGGNF]]
[[E-6BH7D]]
[[E-PQ7NC]]

Slits:

[[E-YAYQB]]
[[P-DQTVL]]
[[P-IJQ5Z]]
[[P-A6PQA]]
[[P-CWXEW]]

Strips:

[[P-RMH6X]]

Lunes:

[[E-UUBBS]]
[[E-VS4XE]]
[[P-K7XDT]]
[[P-5UKXY]]
[[P-PYCCN]]
[[P-64ZUP]]

Sectors:

[[E-PYJZO]]

Joukowski regions:

[[E-NZY3B]]

Mixed:

[[E-H64WF]]
[[E-3GIQS]]
[[P-EEUV6]]
[[P-K4WSJ]]
[[E-YCHOS]]
[[E-JPAJE]]
[[E-PIB7A]]
[[E-KZB33]]
