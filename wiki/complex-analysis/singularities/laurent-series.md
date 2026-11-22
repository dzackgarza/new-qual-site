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

[[T-GROTS]]

## Dependence on the annulus

A function holomorphic on several disjoint annuli centered at $z_0$ has a Laurent series about $z_0$ on each of them, and the series can differ.

::: {.example title="One function, two expansions"}
Let $f(z) = {1\over z-1}$, holomorphic on $\CC\sm\theset{1}$, expanded about $z=0$.

On $\abs z<1$, write it as a geometric series in $z$:
$$
{1\over z-1} = -{1\over 1-z} = -\sum_{k\geq 0} z^k.
$$

On $\abs z>1$, factoring out $z$ gives a geometric series in $\inverseof z$:
$$
{1\over z-1} = {1\over z}\cdot{1\over 1-\inverseof z} = \sum_{k\geq 1} z^{-k}.
$$

Each series converges to $f$ on its annulus.
:::

## Computing Laurent series

By uniqueness of the Laurent expansion on a given annulus, any convergent expansion obtained from known series is the Laurent series, and its coefficients equal the coefficient integrals.
A geometric series in a multiple of $z$ or of $\inverseof z$ covers the annuli on which one term dominates: on $\abs z<1$ in a multiple of $z$, and on $\abs z>1$ in a multiple of $\inverseof z$.
For $f = g\cdot h$ with $g$ having a pole and $h$ holomorphic, expand $h$ as a Taylor series and multiply through by the finite principal part of $g$.
For $f$ with a pole of order $N$ at $z_0$, the function $(z-z_0)^Nf(z)$ has a removable singularity at $z_0$, and its Taylor series divided by $(z-z_0)^N$ is the Laurent series of $f$ on a punctured disc.
For a rational function, write it as a polynomial plus a sum of terms $c/(z-a)^j$ by partial fractions, and expand each term on the given annulus.

::: {.example title="A rational function on a punctured disc"}
Let $f(z) = {z\over (z-1)(z-2)}$, expanded about $z_0 = 1$.
Partial fractions give $f(z) = -{1\over z-1}+{2\over z-2}$, and on $0<\abs{z-1}<1$ the second term is
$$
{2\over z-2} = {2\over (z-1)-1} = -{2\over 1-(z-1)} = -2\sum_{k\geq 0} (z-1)^k,
$$
so the Laurent series is
$$
f(z) = -{1\over z-1} - 2\sum_{k\geq 0}(z-1)^k,
$$
with principal part $-1/(z-1)$ and residue $-1$ at $z_0 = 1$.
:::

## Residues and singularity type

[[D-C3JIU]]

The singularity is [[D-BQLJV|removable]], a [[D-AUD6K|pole]], or [[D-VKP6N|essential]] according as no, finitely many, or infinitely many coefficients $c_k$ with $k<0$ are nonzero, and the coefficient $c_{-1}$ is the residue that enters [[T-HRPNO|the residue theorem]].

## Exercises

[[FF-UQZNR]]

[[FF-5GLOZ]]
