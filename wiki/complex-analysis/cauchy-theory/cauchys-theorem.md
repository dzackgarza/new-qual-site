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

::: {.slogan}
Closed path integrals of holomorphic functions vanish.

:::

::: {.proof title="Cauchy's theorem for $f$ with continuous derivative, by Stokes"}
$$
\oint_{\partial D} f(z) \dz =\int_{D} d(f(z) \dz)=\int_{D}\left(\frac{\partial f}{\partial z} \dz+\frac{\partial f}{\partial \bar{z}} d \bar{z}\right) \wedge \dz=\int_{D} \frac{\partial f}{\partial \bar z} \, d \bar{z} \wedge \dz=0
,$$
since $\dz\wedge\dz = 0$ and $\partial f/\partial\bar z = 0$ by the Cauchy–Riemann equations.

:::

::: {.remark title="Goursat's theorem"}
The Stokes argument uses continuity of $f'$, which the definition of holomorphy does not include.
Goursat's theorem proves $\int_{\bd T} f = 0$ for every triangle $T$ in the domain of a holomorphic $f$ by repeated bisection, with no continuity assumption on $f'$; continuity of $f'$ is then a consequence of the Cauchy integral formula.
The bisection proof is on [[complex-analysis/cauchy-theory/morera-and-converses|Morera and converses]].

:::

## Immediate consequences

- [[complex-analysis/cauchy-theory/the-integral-formula|The integral formula]] expresses $f$ inside a curve by an integral of $f$ over the curve.

- [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|Cauchy's estimates]] bound the derivatives of $f$, and Liouville's theorem follows.

- [[complex-analysis/residues-and-contours/the-residue-theorem|The residue theorem]] computes the integral of a function with isolated singularities inside the curve.

## Exercises

[[E-NKDKF]]
[[E-XXZVG]]
[[E-NSN6G]]
