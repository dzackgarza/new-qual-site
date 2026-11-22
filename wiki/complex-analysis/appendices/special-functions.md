---
order: 121
title: Special functions
---

# Special functions

## Transforms

[[D-5LZQ4]]

::: {.remark title="Normalization"}
The [[D-5LZQ4|Fourier transform]] puts the $2\pi$ in the exponent, so in this normalization the inversion formula of [[T-DTXIA]] reads
$$
f(x) = \int_\RR e^{2\pi i\xi x} \hat{f}(\xi) \dxi
$$
for $f\in L^1(\RR)$ with $\widehat f\in L^1(\RR)$, at every Lebesgue point of $f$; the transform is the two-sided Laplace integral $\int_\RR e^{-px}f(x)\dx$ evaluated at $p=2\pi i\xi$.
:::

[[D-LAPLC]]

## The Gamma function

[[D-Q3MYK]]

[[PR-NLV6Q]]

[[PR-FBQ6F]]

[[PR-YQZI3]]

[[T-GAMRF]]

## The Beta function

[[D-2WZLB]]

[[E-SS6.EX-7]]

## The Riemann zeta function

[[D-HJYH3]]

[[PR-K4KTF]]

[[PR-QHFCK]]

The Dirichlet series, the Euler product and the nonvanishing on $\Re s>1$ are on [[D-HJYH3]]; the meromorphic continuation and the functional equation are [[PR-K4KTF]] and [[PR-QHFCK]].

## The Weierstrass $\wp$-function

[[D-LGP2Q]]

[[T-WPELL]]

## Elliptic functions

Recall that for a lattice $\Lambda=\omega_1\ZZ+\omega_2\ZZ$ with $\omega_1/\omega_2\notin\RR$, an [[D-CRVWEIER|elliptic function]] is a meromorphic function $f$ on $\CC$ with $f(z+\omega)=f(z)$ for every $\omega\in\Lambda$.

[[E-4NGIV]]

[[E-WXHMJ]]

## Infinite series and products

::: {.fact title="Infinite products"}
Let $z_j\in\CC$ with $z_j\neq -1$ for every $j$, and let $\Log$ be the principal branch of the logarithm.

- $\prod_{j=1}^\infty(1+z_j)$ converges to a nonzero limit if and only if $\sum_{j=1}^\infty\Log(1+z_j)$ converges.

- $\prod_{j=1}^\infty(1+z_j)$ converges absolutely, meaning that $\sum_{j=1}^\infty\abs{\Log(1+z_j)}$ converges, if and only if $\sum_{j=1}^\infty\abs{z_j}$ converges.

The first is [@Ahl73, ch. 5, §2.2, Theorem 5], that $\prod(1+a_n)$ converges simultaneously with the series $\sum\log(1+a_n)$ whose terms are the principal values of the logarithm, which is the $\Log$ above. The second is [@Ahl73, ch. 5, §2.2, Theorem 6], that the product converges absolutely if and only if $\sum\abs{a_n}$ converges.
:::

[[T-IEJFA]]

[[T-2WJ4U]]

[[E-DR5LY]]

[[T-RSM4V]]

[[E-SS3.EX-12]]
[[P-CM16-S2-14]]
[[E-26QQP]]
[[E-VA3OK]]
