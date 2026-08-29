---
title: Computing residues
order: 20
---

# Computing residues

Once the contour is chosen the problem is arithmetic: find $c_{-1}$ at each enclosed singularity.
There are three ways, and the order below is the order to try them in.

## A simple pole

[[PR-2XFT4]]

[[PR-L4Y5F]]

For $f = g/h$ with $h$ vanishing simply at $z_0$, differentiating the denominator alone is fastest:

[[C-Q6BSL]]

:::{.proof}
Apply L'Hopital:
\[
(z-z_0) {g(z) \over h(z)} = {(z-z_0) g(z) \over h(z)} \equalsbecause{LH}
{g(z) + (z-z_0) g'(z) \over h'(z)} \converges{z\to z_0}\too {g(z_0) \over h'(z_0)}
.\]

:::

:::{.warnings}
Only the denominator is differentiated, not the numerator.
To remember this, rederive it from L'Hopital and use the product rule on $(z-z_0)g(z)$.

:::

:::{.example title="Residue of a simple pole"}
Let $f(z) = \frac{1}{1+z^2}$, so $g(z) = 1$ and $h(z) = 1+z^2$ with $h'(z) = 2z$ and $h'(i) = 2i \neq 0$.
Thus
\[
\Res_{z=i}{1\over 1+z^2} = \frac{1}{2i}
.\]

:::

A shortcut worth having when $z_0$ is a root of $p$, $p'$ or $q'$:
\[
\dd{}{z} {p(z) \over q(z)} = {p'(z)\over q(z)} - {p(z)q'(z) \over q^2(z)}
.\]

## A pole of higher order

[[PR-D3CDJ]]

[[FF-VOO4Q]]

## By the series

When the pole is high order or the derivative is unpleasant, expand and read off $c_{-1}$ directly.
This is often the fastest route for an essential singularity, where no formula applies at all.

[[T-VE5MW]]

[[T-ESKLY]]

[[C-ZTEH7]]

## The residue at infinity

:::{.concept}
For $\Gamma$ positively oriented about $z=0$,
\[
\Res_{z=\infty}f(z) = -{1\over 2\pi i}\oint_\Gamma f(z) \dz, \qquad \Res_{z=\infty}f(z) = \Res_{z=0} \qty{-{1\over z^2}f\qty{1\over z}}
.\]

:::

[[T-WFXQP]]

[[T-SSNLT]]

:::{.proof}

![](../../../../assets/assets/figures/2021-12-22_05-13-27.png)

:::

## Exercises

Doing it without a formula:

[[E-S6663]]
[[E-M5MWL]]
[[E-RGDJ7]]
[[E-M7K4C]]
[[E-AOQLK]]
[[E-TOZQJ]]
[[E-FCYUM]]

Applying the formulas:

[[E-YNZYA]]
[[E-ITVTT]]
[[E-U2A4C]]
[[E-V2VS5]]
[[E-SNRS5]]
[[E-ENWYG]]
[[E-PMURO]]
[[E-QF7KI]]
