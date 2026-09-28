---
title: Computing residues
order: 20
topics:
- Residues
---

# Computing residues

For $f$ holomorphic on a punctured disc about $z_0$ with Laurent series $\sum_{k\in\ZZ} a_k(z-z_0)^k$, the residue $\Res_{z=z_0} f$ is $a_{-1} = \frac{1}{2\pi i}\oint_{\abs{z-z_0}=r} f(z)\dz$ for small $r$; at a pole this is the [[D-C3JIU|residue]] of the principal part.
At poles it is given by limit formulas, and at essential singularities it is read from the series.

## A simple pole

[[PR-L4Y5F]]

[[C-Q6BSL]]

::: {.proof}
Since $h(z_0)=0$ and $h'(z_0)\neq 0$, $z_0$ is at most a simple pole of $g/h$, and by L'Hôpital's rule
$$
(z-z_0) {g(z) \over h(z)} = {(z-z_0) g(z) \over h(z)} \to
{g(z_0) \over h'(z_0)} \quad\text{as } z\to z_0
,$$
because $\frac{d}{dz}\bigl((z-z_0)g(z)\bigr) = g(z) + (z-z_0)g'(z)$ equals $g(z_0)$ at $z_0$.

:::

::: {.example title="Residue of a simple pole"}
Let $f(z) = \frac{1}{1+z^2}$, so $g(z) = 1$ and $h(z) = 1+z^2$ with $h'(z) = 2z$ and $h'(i) = 2i \neq 0$.
Thus
$$
\Res_{z=i}{1\over 1+z^2} = \frac{1}{2i}
.$$

:::

## A pole of higher order

[[FF-VOO4Q]]

## By the Laurent series

At an essential singularity the residue is the coefficient $a_{-1}$ of the Laurent series.

::: {.example title="Residue at an essential singularity"}
Since $e^{1/z} = \sum_{k\geq 0} z^{-k}/k!$ for $z\neq 0$, the coefficient of $z\inv$ is $1$, so $\Res_{z=0} e^{1/z} = 1$.

:::

## The residue at infinity

[[PR-D3CDJ]]

::: {.remark title="Sum of residues"}
If $f$ is holomorphic on $\CC$ except for finitely many isolated singularities $z_1,\ldots,z_N$, then
$$
\sum_{j=1}^N \Res_{z=z_j} f + \Res_{z=\infty} f = 0
,$$
because for $\rho$ larger than every $\abs{z_j}$ the residue theorem gives $\frac{1}{2\pi i}\oint_{\abs z=\rho} f = \sum_j\Res_{z=z_j} f$, and the definition gives $-\Res_{z=\infty} f$ for the same integral.

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
