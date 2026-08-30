---
title: Build me a map
order: 0
problems:
  topics:
  - Conformal Maps
  - Conformal Mappings
  - Conformal Equivalence
  - Geometry
---

# Build me a map

"Find a conformal map from $\Omega_1$ to $\Omega_2$" is answered by composition, not by cleverness.
There is a short list of maps between standard regions, and the work is routing from one region to another through the list.

Nearly every route passes through $\HH$ or $\DD$, so the practical algorithm is: get to $\HH$, then to $\DD$ if the target is a disc.

## Notation

| Symbol | Region |
| --- | --- |
| $\DD \da \ts{z \st \abs z < 1}$ | the open unit disc |
| $\HH \da \ts{z \st \Im z > 0}$ | the open upper half plane |
| $Q_i$ | the $i$th quadrant, so $Q_1 \da \ts{z \st \Re z, \Im z > 0}$ |
| $Q_{ij} \da Q_i \union Q_j$ | so $\HH = Q_{12}$ and $Q_{14}$ is the right half plane |
| $L \da \ts{x+iy \st 0 < y < \pi}$ | the horizontal strip |

Everything here is open; boundaries are not included.

## The moves

- **$\HH \to \DD$**: the Cayley map $z\mapsto {z-i \over z+i}$.
  The variant ${i-z\over i+z}$ is the same map composed with $z\mapsto -z$.

- **$\DD \to \DD$**: $\lambda\, {z-a\over 1-\bar a z}$ for $\lambda \in S^1$.
  These are all of them, which is [[Complex_Analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors and automorphisms]].

- **Sector $\to \HH$**: $z\mapsto z^n$ opens $\ts{0 < \Arg z < \pi/n}$ to $\HH$.
  In general $z \mapsto z^a$ sends $\ts{\Arg z \in (-\theta_0, \theta_0)}$ to $\ts{\Arg z \in (-a\theta_0, a\theta_0)}$, so $a = \pi/2\theta_0$ opens a symmetric sector to a half plane.

  ![Squaring](../../../../assets/assets/figures/2021-12-10_20-25-14.png)

  ![Symmetric sector to right half-plane](../../../../assets/assets/figures/2021-12-10_20-24-49.png)

- **Strip $\to \HH$**: $z\mapsto e^z$ on $0 < \Im z < \pi$.
  On $\Im z \in (-\pi,\pi)$ it gives $\CC\sm\RR_{\leq 0}$.
  The exponential sends boxes to sectors:
  \[
  \ts{\Re z \in [a,b],\ \Im z \in [c,d]} \mapsto \ts{Re^{i\theta} \st R\in[e^a,e^b],\ \theta\in[c,d]}
  .\]

- **Half disc $\to$ half plane**: the Joukowski map $z\mapsto z + z\inv$.
  It sends $\abs z = 1$ onto $[-2,2]$, $\DD\intersect\HH$ to $Q_{34}$, $\DD^c \intersect \HH$ to $\HH$, and $\DD^c$ to $\CC\sm[-2,2]$.

- **Lune, or any region bounded by two arcs $\to$ strip**: send the two cusps to $0$ and $\infty$.
  A cross ratio does it, and the image is a sector; if the arcs are tangent it is a strip.

  ![](../../../../assets/assets/figures/2021-12-10_17-12-12.png)

- **Slit region**: aim for $\CC\sm[0,\infty) \mapsvia{\sqrt z} \HH$.

- **Reflections and inversions**: $z\mapsto -z$ reflects, so $\HH \to Q_{34}$.
  $z\mapsto 1/z$ is $Re^{it}\mapsto R\inv e^{-it}$, a reflection about $\RR$ composed with inversion in $S^1$, and is a rotation of $\CP^1$ by $\pi$ about the real axis.

## Routing

Read the target region's *corners and boundary arcs*, since those are what the moves act on.

| The region has | Send it through |
| --- | --- |
| a corner of angle $\theta_0$ | $z^{\pi/\theta_0}$, opening it to a half plane |
| two boundary arcs meeting at two points | a cross ratio taking those points to $0,\infty$ |
| two tangent circles | the tangency to $\infty$, giving parallel lines |
| a slit | $\sqrt z$ |
| a strip | $e^z$ |
| a circular boundary and you want a disc | the Cayley map, then Blaschke factors to place the points |

## Tips that save the computation

- $z\inv = \bar z/\abs z^2$ makes images quick to compute: under $f(z)=1/z$, the point $1+i$ on $\abs{z-1}=1$ goes to ${1-i\over 2}$.

- Conformal maps preserve angles, so use tangent vectors, including at $\infty$.
  Circles meeting orthogonally must map to orthogonally meeting circles or lines; circles meeting tangentially map to parallel lines or tangent circles.

- Conformal maps send generalized circles to generalized circles, where a line is a circle through $\infty$.

- Arcs between two points map to arcs between the images.

- The locus equidistant from two points is the perpendicular bisector.

- Inverting a map: set $f(z) = w$ and solve for $z$.

- To remember the cross ratio $(z; a, b, c)$ sending $a\mapsto 1$, $b \mapsto 0$, $c\mapsto \infty$: put $z-b$ in the numerator to send $b\to 0$, put $z-c$ in the denominator to send $c\to\infty$, and cancel with $a-c$ over $a-b$ so that $a\mapsto 1$.

- $\RR = \ts{\tan t \st t \in (-\pi/2,\pi/2)}$, which is occasionally the parameterization a problem wants.

## The standard maps, as statements

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
