---
sort: 99
title: "Exercises: Conformal Maps"
---

# Exercises: Conformal Maps 

See also [[30_Complex_Analysis/09_Quals/105_Conformal Maps|Qual conformal map questions]].

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

[[E-Z23VB]]
[[E-G55QF]]

## Discs and Planes

### $\HH\to\DD$

[[P-IIONX]]

### $\HH\to\DD$, cross-ratio

[[E-W6MWU]]

### $\DD\to\HH$

[[E-4H3JY]]

### Upper half-disc to $\DD$

[[E-PGGNF]]

### Upper half-disc to $\HH$

[[E-6BH7D]]

### $\DD^c \intersect \HH \to\HH$

[[E-PQ7NC]]

## Slits

[[E-YAYQB]]

### 8
[[P-DQTVL]]

### 9
[[P-IJQ5Z]]

### 10
[[P-A6PQA]]

## 11
[[P-CWXEW]]

## Strips

### Horizontal strip to $\HH$

[[P-RMH6X]]

## Lunes

### Intersection of circles

[[E-UUBBS]]

### Lune with one intersection point

[[E-VS4XE]]

### 4
[[P-K7XDT]]

### 5
[[P-5UKXY]]

### 6
[[P-PYCCN]]

### 13
[[P-64ZUP]]

## Sectors

[[E-PYJZO]]

## Joukowski-Type Regions

[[E-NZY3B]]

## Misc

[[E-H64WF]]
[[E-3GIQS]]

### 7
[[P-EEUV6]]

### 12
[[P-K4WSJ]]
