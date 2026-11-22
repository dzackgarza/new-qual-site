---
title: Cauchy's theorem
order: 10
topics:
- Cauchy's Theorem
- Cauchy Integral Theorem

---

# Cauchy's theorem

## Contour integrals

[[D-6DAXB]]

[[D-YKB3V]]

## Cauchy--Goursat

[[T-2OVCI]]

::: {.slogan}
Closed path integrals of holomorphic functions on a [[D-GFM35|simply connected]] region vanish.

:::

[[T-B3BDO]]

Goursat's theorem is the triangle form of [[T-2OVCI|Cauchy's theorem]]: it assumes no continuity of $f'$, and continuity of $f'$ is a consequence of [[T-LA2UI|the Cauchy integral formula]].

::: {.example title="Holomorphy is what the vanishing uses"}
On the circle $\abs z = 1$,
$$
\oint_{\abs z=1} e^z \dz = 0, \qquad \oint_{\abs z=1}\bar z\,\dz = 2\pi i \neq 0 .
$$
The first vanishes by [[T-2OVCI|Cauchy's theorem]], its integrand being entire.
On the circle $\bar z = 1/z$, so the second is the integral whose nonvanishing shows that $1/z$ has no primitive on $\CC\smz$; $\bar z$ is real analytic, so what the second integrand fails is holomorphy, not smoothness.
Both values come out of the parametrization: $\int_0^{2\pi} e^{e^{it}}ie^{it}\,dt = 0$ and $\int_0^{2\pi} e^{-it}ie^{it}\,dt = 2\pi i$.
:::

## Immediate consequences

- [[complex-analysis/cauchy-theory/the-integral-formula|The integral formula]] expresses $f$ inside a curve by an integral of $f$ over the curve.

- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy's estimates]] bound the derivatives of $f$, and [[T-QHIHJ|Liouville's theorem]] follows.

- [[complex-analysis/residues-and-contours/the-residue-theorem|The residue theorem]] computes the integral of a function with isolated singularities inside the curve.

## Problems

[[E-NKDKF]]
[[P-AZOFF-D03]]
[[E-QLRNW]]
