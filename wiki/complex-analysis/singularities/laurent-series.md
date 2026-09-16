---
title: Laurent series
order: 10
topics:
- Laurent Series
- Principal Parts
- Annuli
---

# Laurent series

A Taylor series expands a holomorphic function on a disc.
A Laurent series expands a holomorphic function on an annulus, with both positive and negative powers.

[[T-4XPWL]]

[[C-7S2CO]]

## Dependence on the annulus

A function holomorphic on several disjoint annuli centered at $z_0$ has a Laurent series about $z_0$ on each of them, and the series can differ.

::: {.example title="One function, two expansions"}
Let $f(z) = {1 \over z-1}$, holomorphic on $\CC\sm\ts{1}$, expanded about $z=0$.

On $\abs z < 1$, write it as a geometric series in $z$:
$$
{1\over z-1} = -{1\over 1-z} = -\sum_{k\geq 0} z^k
.$$

On $\abs z > 1$, factoring out $z$ gives a geometric series in $z\inv$:
$$
{1\over z-1} = {1\over z}\cdot{1 \over 1 - z\inv} = \sum_{k \geq 1} z^{-k}
.$$

Each series converges to $f$ on its annulus.

:::

## Computing Laurent series

By uniqueness of the Laurent expansion on a given annulus, any convergent expansion obtained from known series is the Laurent series, so the coefficient integrals are rarely evaluated directly.

- **Geometric series.** Write the expression as ${1 \over 1 - u}$ with $\abs u < 1$ on the given annulus, and expand.
  On $\abs{z}<1$ one takes $u$ a multiple of $z$, and on $\abs z>1$ a multiple of $z\inv$.

- **Products and compositions of known expansions.** For $f = g\cdot h$ with $g$ having a pole and $h$ holomorphic, expand $h$ as a Taylor series and multiply through by the finite principal part of $g$.

- **Poles of known order.** For $f$ with a pole of order $N$ at $z_0$, $(z-z_0)^N f(z)$ has a removable singularity at $z_0$; its Taylor series divided by $(z-z_0)^N$ is the Laurent series of $f$ on a punctured disc.

- **Partial fractions.** A rational function is a polynomial plus a sum of terms $c/(z-a)^j$, and each term is expanded on the given annulus.

## Residues and singularity type

- On a punctured disc about $z_0$, the coefficient $c_{-1}$ is the residue of $f$ at $z_0$, which enters [[complex-analysis/residues-and-contours/the-residue-theorem|the residue theorem]].

- On a punctured disc about $z_0$, the singularity is removable, a pole, or essential according as no, finitely many, or infinitely many coefficients $c_k$ with $k<0$ are nonzero ([[complex-analysis/singularities/classifying-a-singularity|Classifying a singularity]]).

## Exercises

[[FF-UQZNR]]

[[FF-5GLOZ]]
