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

[[FD-GK7JE]]

[[FE-O47RH]]

::: {.remark title="Holomorphic with nonvanishing derivative is conformal"}
Let $f$ be holomorphic at $z_0$ with $f'(z_0)\neq 0$, and let $\gamma$ be a smooth curve with $\gamma(0)=z_0$ and $\gamma'(0)\neq 0$.
By the chain rule $(f\circ\gamma)'(0) = f'(z_0)\,\gamma'(0)$, so $f$ multiplies every tangent vector at $z_0$ by the same nonzero complex number $f'(z_0)$: it rotates by $\arg f'(z_0)$ and scales by $\abs{f'(z_0)}$.
Hence the signed angle between two curves through $z_0$ equals the signed angle between their images.

:::

::: {.fact title="Checking conformality"}
Once holomorphy is known, it suffices to check $f'(p)\neq 0$.

:::

::: {.example title="Complex conjugation"}
The map $f(z)=\bar z$ has invertible real Jacobian $\operatorname{diag}(1,-1)$ at every point, but it fails the Cauchy--Riemann equations, so it has no complex derivative.
It reverses signed angles and is not conformal.

:::

::: {.remark title="Inverses"}
An injective holomorphic map $f$ on an open set $U$ has $f'\neq 0$ on $U$, and $f\inv\colon f(U)\to U$ is holomorphic ([[C-FVT4V]]).
The biholomorphisms of an open set $\Omega$ onto itself therefore form a group $\Aut_\CC(\Omega)$, computed for the disc on [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors and automorphisms]].

:::

## The transformations

[[D-FRVBV]]

::: {.remark title="As projective linear automorphisms"}
Since $\Aut(\CP^1) \cong \PGL_2(\CC)$, acting on projective coordinates gives a matrix representation:
$$
\matt a b c d \cdot \tv{z: 1}^t = \tv{ {az+b \over cz + d }: 1} = \tv{f(z): 1}
.$$
Nonzero scalar multiples of a matrix give the same transformation, so the inverse transformation is given by the adjugate matrix:
$$
{az + b\over cz+ d} \leadsto \matt a b c d \inv = \matt d {-b} {-c} a
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

[[PR-AQ6YR]]

[[FF-W4FFF]]

::: {.example title="Maps given by cross ratios"}
\envlist

- $z\mapsto(z, i, 1, -1)$ maps $\DD$ onto $\HH$.

- $z\mapsto(z, 0, -1, 1)$ maps $\DD \intersect \HH$ onto the first quadrant $Q_1$.

:::

## Classification and standard images

Möbius transformations map generalized circles to generalized circles, and hence map discs and half-planes onto discs and half-planes.
A branch of $z\mapsto z^\alpha$ on a sector of opening $\theta$ at $0$, with $\alpha\theta\leq 2\pi$, maps it onto a sector of opening $\alpha\theta$.
A branch of $\log$ maps the sector $\ts{\theta_1<\arg z<\theta_2}$ onto the strip $\ts{\theta_1<\Im w<\theta_2}$, and $\exp$ is its inverse.

The Cayley transform maps $\HH$ onto $\DD$.
Any two biholomorphisms of an open set onto $\DD$ differ by an automorphism of $\DD$, and the Riemann mapping theorem gives the existence of one for every simply connected open $\Omega\subsetneq\CC$.

[[T-77SHB]]

[[T-W26VL]]

[[T-55MPA]]

[[T-2KGOX]]

[[PR-FL6T7]]

A sector of opening $\theta$ is mapped onto a half-plane by a power map with $\alpha = \pi/\theta$, and then onto $\DD$ by the Cayley transform; it is mapped onto a strip by a branch of $\log$ whose argument interval is that of the sector.

::: {.remark}
The map $z\mapsto {z-i\over z+i}$ is also used as the Cayley transform; it is the composition of $F(z) = (i-z)/(i+z)$ from [[T-77SHB]] with $w\mapsto -w$:
$$
- {i-z \over i + z} = {z-i \over i+z} = {z-i \over z+i}
.$$

:::

[[PR-L5UH3]]

[[PR-PDYJC]]

[[PR-BPP7D]]

[[PR-PW4Z6]]

[[PR-XCDL5]]

::: {.remark title="The logarithm"}
The principal branch $\Log$ maps $\CC\sm\RR^{\leq 0}$ onto $\RR \cross (-\pi, \pi)$: the part of the circle of radius $R$ in the slit plane maps to the open vertical segment from $\ln R - i\pi$ to $\ln R + i\pi$, and rays from $0$ map to horizontal lines.

It also maps
$$
\begin{aligned}
\ts{ z \st \abs{z} < 1,\, \Im(z) > 0 } &\mapstofrom \RR^{<0} \cross (0, \pi ) \\
\ts{ z \st \abs{z} > 1,\, \Im(z) > 0 } &\mapstofrom \RR^{>0} \cross (0, \pi )
\end{aligned}.$$
On the boundary of the upper half disc: as $x$ runs from $0$ to $1$ in $\RR$, $\Log x$ runs from $-\infty$ to $0$; as $z$ runs from $1$ to $-1$ along $S^1\intersect\overline\HH$, $\Log z$ runs from $0$ to $i\pi$ vertically; as $x$ runs from $-1$ to $0$, $\Log x$, extended continuously from $\HH$, runs from $i\pi$ to $-\infty + i\pi$.

:::

[[PR-TQDIL]]

[[PR-FRVPJ]]

[[PR-3LBLV]]

Compositions of these maps between standard regions are on [[complex-analysis/conformal-maps/build-me-a-map|Build me a map]].
