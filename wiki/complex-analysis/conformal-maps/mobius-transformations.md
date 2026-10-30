---
title: Möbius transformations
order: 10
topics:
- Fractional Linear Transformations
- Mobius Transformations

---

# Möbius transformations

## Conformal maps

[[D-TM4TE]]

[[FE-O47RH]]

::: {.example title="Complex conjugation"}
The map $f(z)=\bar z$ has invertible real Jacobian $\operatorname{diag}(1,-1)$ at every point, but it fails the Cauchy--Riemann equations, so it has no complex derivative.
It reverses signed angles and is not conformal.

:::

The group $\Aut_\CC(\DD)$ is computed on [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors and automorphisms]].

## The transformations

[[D-FRVBV]]

::: {.remark title="As projective linear automorphisms"}
Since $\Aut(\CP^1) \cong \PGL_2(\CC)$, acting on projective coordinates gives a matrix representation:
$$
\matt a b c d \cdot \thevector{z: 1}^t = \thevector{ {az+b \over cz + d }: 1} = \thevector{f(z): 1}
.$$
Nonzero scalar multiples of a matrix give the same transformation, so the inverse transformation is given by the adjugate matrix:
$$
{az + b\over cz+ d} \leadsto \inverseof{\matt a b c d} = \matt d {-b} {-c} a
\leadsto
{dw-b \over -cw + a}
.$$

:::

::: {.remark}
A Möbius transformation $z\mapsto (az+b)/(cz+d)$ fixing three distinct points of $\CC$ is the identity: its fixed points in $\CC$ are the roots of $cz^2 + (d-a)z - b = 0$, and a polynomial of degree at most $2$ with three roots is zero, so $c=b=0$ and $a=d$.
This gives the uniqueness in [[PR-74KHY]].

:::

[[PR-74KHY]]

## The cross ratio

[[FF-W4FFF]]

::: {.example title="Maps given by cross ratios"}
\envlist

- $z\mapsto(z, i, 1, -1)$ maps $\DD$ onto $\HH$.

- $z\mapsto(z, 0, -1, 1)$ maps $\DD \intersect \HH$ onto the first quadrant $Q_1$.

:::

## Classification and standard images

Möbius transformations map generalized circles to generalized circles, and hence map discs and half-planes onto discs and half-planes.
A branch of $z\mapsto z^\alpha$ on a sector of opening $\theta$ at $0$, with $\alpha\theta\leq 2\pi$, maps it onto a sector of opening $\alpha\theta$.
A branch of $\log$ maps the sector $\theset{\theta_1<\arg z<\theta_2}$ onto the strip $\theset{\theta_1<\Im w<\theta_2}$, and $\exp$ is its inverse.

The Cayley transform maps $\HH$ onto $\DD$.
Any two biholomorphisms of an open set onto $\DD$ differ by an automorphism of $\DD$, and the Riemann mapping theorem gives the existence of one for every simply connected open $\Omega\subsetneq\CC$.

[[PR-FL6T7]]

[[T-W26VL]]

[[T-4MDS6]]

[[T-2KGOX]]

A sector of opening $\theta$ is mapped onto a half-plane by a power map with $\alpha = \pi/\theta$, and then onto $\DD$ by the Cayley transform; it is mapped onto a strip by a branch of $\log$ whose argument interval is that of the sector.

::: {.remark}
The map $z\mapsto {z-i\over z+i}$ is also used as the Cayley transform; it is the composition of $F(z) = (i-z)/(i+z)$ from [[PR-FL6T7]] with $w\mapsto -w$:
$$
- {i-z \over i + z} = {z-i \over i+z} = {z-i \over z+i}
.$$

:::

[[PR-L5UH3]]

[[PR-AQFRA]]

[[PR-BPP7D]]

[[PR-PW4Z6]]

[[PR-XCDL5]]

::: {.remark title="The logarithm"}
The principal branch $\Log$ maps $\CC\sm\RR^{\leq 0}$ onto $\RR \cross (-\pi, \pi)$: the part of the circle of radius $R$ in the slit plane maps to the open vertical segment from $\ln R - i\pi$ to $\ln R + i\pi$, and rays from $0$ map to horizontal lines.

It also maps
$$
\begin{aligned}
\theset{ z \st \abs{z} < 1,\, \Im(z) > 0 } &\mapstofrom \RR^{<0} \cross (0, \pi ) \\
\theset{ z \st \abs{z} > 1,\, \Im(z) > 0 } &\mapstofrom \RR^{>0} \cross (0, \pi )
\end{aligned}.$$
On the boundary of the upper half disc: as $x$ runs from $0$ to $1$ in $\RR$, $\Log x$ runs from $-\infty$ to $0$; as $z$ runs from $1$ to $-1$ along $S^1\intersect\overline\HH$, $\Log z$ runs from $0$ to $i\pi$ vertically; as $x$ runs from $-1$ to $0$, $\Log x$, extended continuously from $\HH$, runs from $i\pi$ to $-\infty + i\pi$.

:::

[[PR-TQDIL]]

[[PR-OTMIR]]

[[PR-3LBLV]]

Compositions of these maps between standard regions are on [[complex-analysis/conformal-maps/build-me-a-map|Build me a map]].
