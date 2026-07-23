---
sort: 99
title: "Exercises: Conformal Maps"
---

# Exercises: Conformal Maps 

See also [[30_Complex Analysis/999_Quals/105_Conformal Maps|Qual conformal map questions]].

:::{.remark title="Tips and tricks"}
Notation:

- Almost everything is an *open* set, so don't include boundaries in definitions.
- $\DD \da \ts{z \st \abs{z} < 1}$ is the open unit disc.
- $\HH \da \ts{z \st \Im(z) > 0}$ is the open upper half-plane.
- $Q_i$ is the $i$th quadrant, e.g. $Q_1 \da \ts{z \st \Re(z), \Im(z) > 0}$.
- $Q_{ij} \da Q_i \union Q_j$ is the union of two quadrants.
    E.g. $\HH = Q_{23}$, or $Q_{14}$ is the right half-plane.

Tips:

- If just mapping the disc to itself, use the hypberolic translations
\[
\psi_a \da {z-a\over 1-\bar a z}
.\]

- For lunes (regions bounded by arcs): map the cusps to $0$ and $\infty$ to get a sector.

- For discs with slits: aim for $\CC\sm[0, \infty) \mapsvia{\sqrt z} \HH$.

- For circles with tangencies: send the tangent point to $\infty$ to get parallel lines.

- Remembering the cross ratio: the order $1,0,\infty$ is very important (as images of $a, b, c$).
  - Send $b\to 0$ by including $z-b$ in the numerator.
  - Send $c\to \infty$ by including $z-c$ in the denominator.
  - Send $a\to 1$ by canceling the terms just added: 
    - Cancel $z-c$ in the denominator with $a - c$ in the numerator.
    - Cancel $z-b$ in the numerator with a $a - b$ in the denominator.
- Inverting conformal maps: just set $f(z) = w$ and solve for $w$.
- Conformal maps preserve generalized spheres, i.e. circles get mapped to circles (which could be lines on $\CP^1$). 
- Orthogonal circles must go to orthogonal circles.
- Arcs between two points must go to arcs between their images

- $\RR =\ts{\tan(t) \st t\in (-\pi/2, \pi/ 2)}$.
:::

## Cross-Ratios

[[E-OK4UE]]
[[E-E7SSK]]

## Discs and Planes

### $\HH\to\DD$ #complex/exercise/completed

[[P-IIONX]]
### $\HH\to\DD$, cross-ratio #complex/exercise/completed

[[E-W6MWU]]
### $\DD\to\HH$ #complex/exercise/completed

[[E-4H3JY]]
### Upper half-disc to $\DD$ #complex/exercise/completed

[[E-PGGNF]]
### Upper half-disc to $\HH$ #complex/exercise/completed

[[E-6BH7D]]
### $\DD^c \intersect \HH \to\HH$ #complex/exercise/completed

[[E-PQ7NC]]

## Slits

[[E-E37VJ]]
### 8 #complex/exercise/work
[[P-DQTVL]]
### 9 #complex/exercise/work
[[P-IJQ5Z]]
### 10 #complex/exercise/work
[[P-A6PQA]]
## 11 #complex/exercise/work
[[P-CWXEW]]
## Strips

### Horizontal strip to $\HH$ #complex/exercise/completed

[[P-RMH6X]]
## Lunes

### Intersection of circles

[[E-NP5Q4]]
### Lune with one intersection point

[[E-DPJWS]]
### 4 #complex/exercise/work
[[P-K7XDT]]
### 5 #complex/exercise/work
[[P-5UKXY]]
### 6 #complex/exercise/work
[[P-PYCCN]]
### 13 #complex/exercise/work
[[P-64ZUP]]
## Sectors

[[E-444IZ]]
## Joukowski-Type Regions

[[E-IHR33]]
## Misc

[[E-2QR3V]]
[[E-6VJ2Z]]
### 7 #complex/exercise/work
[[P-EEUV6]]
### 12 #complex/exercise/work
[[P-K4WSJ]]
