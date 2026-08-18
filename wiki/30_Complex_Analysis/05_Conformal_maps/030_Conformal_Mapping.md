---
order: 30
---

# Conformal Maps / Linear Fractional Transformations

![](../../../../assets/assets/figures/2021-10-29_02-33-08.png)

[[D-PCDNH]]

:::{.remark}
There is an oft-used weaker condition that $f'(z) \neq 0$ for any point.
Note that that this condition alone doesn't necessarily imply $f$ is holomorphic, since anti-holomorphic maps may have nonzero derivatives.
For example, take $f(z) = \bar{z}$, so $f(x+iy) = x-iy$ -- this does not satisfy the Cauchy-Riemann equations.

:::

:::{.remark}
A bijective holomorphic map automatically has a holomorphic inverse.
This can be weakened: an injective holomorphic map satisfies $f'(z) \neq 0$ and $f ^{-1}$ is well-defined on its range and holomorphic.

:::

[[D-DKJEU]]

[[PR-74KHY]]

:::{.example title="?"}
\envlist

- $(z, i, 1, -1): \DD\to \HH$
- $(z, 0, -1, 1): \DD \intersect \HH \to Q_1$.

:::

[[T-77SHB]]

[[T-MEWTS]]

[[T-55MPA]]

## By Type

:::{.remark title="Notation"}

| Notation                                                     | Definition                                             |
|--------------------------------------------------------------|--------------------------------------------------------|
| $\DD \da \ts{z \st \abs{z} \leq 1}$                          | The unit disc                                          |
| $\HH \da \ts{x+iy \st y > 0}$                                | The upper half-plane                                   |
| $X_{1\over 2}$                                               | A "half version of $X$", see examples                  |
| $\HH_{1\over 2}$                                             | The first quadrant                                     |
| $\DD_{1\over 2}$                                             | The portion of the first quadrant inside the unit disc |
| $L \definedas \theset{x + iy \suchthat x\in \RR,\, 0<y<\pi}$ | The horizontal strip                                   |
|                                                              |                                                        |
|                                                              |                                                        |

:::

[[T-2KGOX]]

[[PR-FL6T7]]

:::{.remark}
Some write a similar map:
\[
\HH^\circ &\to \DD^\circ \\
z &\mapsto {z-i \over z+i}
.\]
This is just a composition of the above map with the flip $z\mapsto -z$:
\[
- {i-z \over i + z} = {z-i \over i+z} = {z-i \over z+i}
.\]

:::

[[PR-L5UH3]]

[[PR-PDYJC]]

[[PR-BPP7D]]

[[PR-PW4Z6]]

[[PR-XCDL5]]

:::{.remark}
This extends to a function $\CC\sm\RR^{\leq 0} \to \RR \cross (-\pi, \pi)$.
Circles of radius $R$ are mapped to vertical line segments connecting $\ln(R) + i\pi$ to $\ln(R) - i\pi$, and rays are mapped to horizontal lines.

:::

:::{.remark}
One can find other specific images of the logarithm:
\[
\ts{ z \st \abs{z} < 1,\, \Im(z) > 0 } &\mapstofrom \RR^{<0} \cross (0, \pi ) \\
\ts{ z \st \abs{z} > 1,\, \Im(z) > 0 } &\mapstofrom \RR^{>0} \cross (0, \pi ) \\
.\]

For the upper half-disc to the negative horizontal half-strip:
  - As $x$ travels $0\to 1$ in $\RR$, $\log(x)$ travels from $-\infty\to 0$.
  - As $x$ travels from $-1$ to $1$ along $S^1\intersect \HH$, $\log(x)$ travels from $0\to i\pi$ vertically.
  - As $x$ travels from $-1\to 0$, $\log(x)$ travels from $0+i\pi\to i-\infty+i\pi$ along the top of the strip.

:::

[[PR-TQDIL]]

[[PR-FRVPJ]]

[[PR-KKU6N]]

## Exercises

[[E-YCHOS]]
