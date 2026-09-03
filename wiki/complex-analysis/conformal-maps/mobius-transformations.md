---
title: Möbius transformations
order: 10
topics:
- Fractional Linear Transformations
- Mobius Transformations

---

# Möbius transformations

## What conformal means

[[D-TM4TE]]

[[FD-GK7JE]]

[[FE-O47RH]]

:::{.remark title="Holomorphic with nonvanishing derivative is conformal"}
Write $f(z+\eps) = f(z) + \eps f'(z) + \bigo(\eps^2)$, so that
\[
\Arg(f(z+\eps) - f(z)) \approx \Arg(\eps f'(z)) = \Arg(\eps) + \Arg(f'(z))\to \Arg(f'(z))
.\]
Every tangent vector at $z_0$ is rotated by approximately the same angle, so the angles between them are preserved.

:::

:::{.fact title="Checking conformality"}
Once holomorphy is known, it suffices to check $f'(p)\neq 0$.

:::

:::{.warnings}
Do not replace complex differentiability by invertibility of the real derivative.  The
map $f(z)=\bar z$ has an invertible real Jacobian, but it fails the Cauchy--Riemann
equations, has no complex derivative, and reverses orientation.  Thus the test
$f'(z)\neq0$ presupposes that \(f\) is holomorphic.

:::

:::{.remark title="Inverses come for free"}
A bijective holomorphic map has a holomorphic inverse, and this weakens: an *injective* holomorphic map has $f'(z)\neq 0$ throughout, and its inverse is well defined and holomorphic on the image.
The self-biholomorphisms of a domain $\Omega$ therefore form a group $\Aut_\CC(\Omega)$, computed for the disc in [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors and automorphisms]].

:::

## The transformations

[[D-FRVBV]]

:::{.remark title="As projective linear automorphisms"}
Since $\Aut(\CP^1) \cong \PGL_2(\CC)$, acting on projective coordinates gives a matrix representation:
\[
\matt a b c d \cdot \tv{z: 1}^t = \tv{ {az+b \over cz + d }: 1} = \tv{f(z): 1}
.\]
This is the fastest way to invert one: invert the matrix and ignore the determinant, which only scales every entry.
\[
{az + b\over cz+ d} \leadsto \matt a b c d \inv = \matt d {-b} {-c} a
\leadsto
{dw-b \over -cw + a}
.\]

:::

:::{.remark}
A Möbius transformation fixing three points is the identity, which is the uniqueness half of the next statement.

:::

[[PR-74KHY]]

## The cross ratio

[[PR-AQ6YR]]

[[FF-W4FFF]]

:::{.example}
\envlist

- $(z, i, 1, -1): \DD\to \HH$
- $(z, 0, -1, 1): \DD \intersect \HH \to Q_1$

:::

## Classification and standard images

The standard maps are best remembered as a small composition toolkit rather than as a
table of unrelated formulas.  Möbius transformations move discs and half-planes while
preserving generalized circles; power maps multiply arguments and therefore open or
close sectors; a chosen logarithm branch turns angular width into vertical width and
maps sectors to strips; exponentials reverse that last step.  Most exam maps are a
composition of two or three of these operations, chosen by following the boundary.

The Cayley transform is the basic disc/half-plane bridge.  After moving a distinguished
interior point to \(0\), disc automorphisms give the remaining normalization freedom;
the Riemann mapping theorem says that for a simply connected proper domain some such
biholomorphism with the disc exists even when no elementary formula is available.

[[T-77SHB]]

[[T-MEWTS]]

[[T-55MPA]]

[[T-2KGOX]]

[[PR-FL6T7]]

For explicit polygonal-looking domains, work with angles.  A power \(z^\alpha\) sends a
sector of opening \(\theta\) to one of opening \(\alpha\theta\); once a sector has been
straightened to a half-plane, use Cayley to reach the disc.  If the target is a strip,
choose a logarithm branch whose argument interval is exactly the desired vertical
interval.

:::{.remark}
The map $z\mapsto {z-i\over z+i}$ that is sometimes written instead is the composition of the above with $z\mapsto -z$:
\[
- {i-z \over i + z} = {z-i \over i+z} = {z-i \over z+i}
.\]

:::

[[PR-L5UH3]]

[[PR-PDYJC]]

[[PR-BPP7D]]

[[PR-PW4Z6]]

[[PR-XCDL5]]

:::{.remark title="The logarithm"}
This extends to $\CC\sm\RR^{\leq 0} \to \RR \cross (-\pi, \pi)$: circles of radius $R$ map to vertical segments joining $\ln R + i\pi$ to $\ln R - i\pi$, and rays map to horizontal lines.

Other images worth having:
\[
\ts{ z \st \abs{z} < 1,\, \Im(z) > 0 } &\mapstofrom \RR^{<0} \cross (0, \pi ) \\
\ts{ z \st \abs{z} > 1,\, \Im(z) > 0 } &\mapstofrom \RR^{>0} \cross (0, \pi )
.\]
For the upper half disc to the negative half strip, follow the boundary: as $x$ runs $0\to 1$ in $\RR$, $\log x$ runs $-\infty \to 0$; as $x$ runs from $-1$ to $1$ along $S^1\intersect\HH$, $\log x$ runs from $0$ to $i\pi$ vertically; as $x$ runs $-1 \to 0$, $\log x$ runs from $i\pi$ out to $-\infty + i\pi$ along the top.

:::

[[PR-TQDIL]]

[[PR-FRVPJ]]

[[PR-KKU6N]]

Which of these to reach for is [[complex-analysis/conformal-maps/build-me-a-map|Build me a map]].
