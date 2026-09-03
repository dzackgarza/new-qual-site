---
title: Cauchy's theorem
order: 10
topics:
- Cauchy's Theorem
- Cauchy Integral Theorem
- Green's Theorem

---

# Cauchy's theorem

## Contour integrals

[[D-6DAXB]]

## Cauchy–Goursat

[[T-2OVCI]]

[[FT-5JQUR]]

:::{.slogan}
Closed path integrals of holomorphic functions vanish.

:::

:::{.proof title="of Cauchy, by Stokes"}
\[
\oint_{\partial D} f(z) \dz =\int_{D} d(f(z) \dz)=\int_{D}\left(\frac{\partial f}{\partial z} \dz+\frac{\partial f}{\partial \bar{z}} d \bar{z}\right) \wedge \dz=\int_{D} \frac{\partial f}{\partial z} \dz \wedge \dz+0 \, d \bar{z} \wedge \dz=0
.\]

:::

:::{.remark title="Why Goursat is stated separately"}
The Stokes argument assumes $f'$ is continuous, which is not part of the definition of holomorphic.
Goursat's contribution is to prove the triangle case with no such assumption, by bisection; the continuity of $f'$ then follows from the theory rather than being needed to start it.
That proof is on [[complex-analysis/cauchy-theory/morera-and-converses|Morera and converses]], next to the theorem it is usually paired with.

:::

## Immediate consequences

- [[complex-analysis/cauchy-theory/the-integral-formula|The integral formula]] recovers $f$ inside a curve from $f$ on it.
- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy's estimates]] bound the derivatives, and Liouville follows.
- [[complex-analysis/residues-and-contours/the-residue-theorem|The residue theorem]] is the version for a function with singularities inside.

## Exercises

[[E-NKDKF]]
[[E-XXZVG]]
[[E-NSN6G]]
