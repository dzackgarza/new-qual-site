---
title: Computing residues
order: 20
topics:
- Residues
---

# Computing residues

Recall that the [[D-C3JIU|residue]] of $f$ at $z_0$ is the coefficient $a_{-1}$ of the [[T-4XPWL|Laurent expansion]] at $z_0$; at a pole it is computed from the limit formulas ([[PR-L4Y5F]], [[T-ESKLY]]), and at an [[D-VKP6N|essential singularity]] it is read from the series.

## A simple pole

[[PR-L4Y5F]]

[[C-Q6BSL]]

::: {.example title="Residue of a simple pole"}
Let $f(z) = \frac{1}{1+z^2}$, so $g(z) = 1$ and $h(z) = 1+z^2$ with $h'(z) = 2z$ and $h'(i) = 2i \neq 0$.
Thus
$$
\Res_{z=i}{1\over 1+z^2} = \frac{1}{2i}
.$$

:::

## A pole of higher order

[[T-ESKLY]]

::: {.example title="A pole of order two"}
The function $f(z) = 1/\bigl(z^2(1-z)\bigr)$ has a [[D-AUD6K|pole of order $2$]] at $0$, and the formula with $n=2$ asks for one derivative of $z^2f(z) = 1/(1-z)$:
$$
\Res_{z=0}{1\over z^2(1-z)} = \lim_{z\to0}{d\over dz}\qty{1\over 1-z} = \lim_{z\to0}{1\over(1-z)^2} = 1.
$$
The same number is the coefficient of $z$ in the Taylor series $1/(1-z) = 1+z+z^2+\cdots$, read through $1/(z^2(1-z)) = z^{-2}+z^{-1}+1+\cdots$.
:::

## By the Laurent series

[[D-C3JIU]]

::: {.example title="Residue at an essential singularity"}
Since $e^{1/z} = \sum_{k\geq 0} z^{-k}/k!$ for $z\neq 0$, the coefficient of $\inverseof{z}$ is $1$, so $\Res_{z=0} e^{1/z} = 1$.

:::

## The residue at infinity

[[D-Q8XRV]]

[[T-WFXQP]]

::: {.example title="The residues of $z/(1+z^2)$ add to zero"}
For $f(z) = z/(1+z^2)$ the simple poles are at $\pm i$, with $\Res_{z=i}f = i/(2i) = 1/2$ and $\Res_{z=-i}f = -i/(-2i) = 1/2$.
With $w = 1/z$, the function whose residue at the origin gives the residue at infinity is
$$
-\frac{1}{w^2}f\qty{1\over w} = -{1\over w^2}\cdot{1/w\over 1+1/w^2} = -{1\over w(w^2+1)},
$$
whose residue at the origin is $-1$, so $\Res_{z=\infty}f = -1$, and $1/2+1/2-1 = 0$: the residues of $f$ on the sphere sum to zero.
:::

## Exercises

Doing it without a formula:

[[E-S6663]] [[E-M5MWL]] [[E-RGDJ7]] [[E-M7K4C]] [[E-AOQLK]] [[E-TOZQJ]] [[E-FCYUM]]

Applying the formulas:

[[E-YNZYA]] [[E-ITVTT]] [[E-U2A4C]] [[E-SS3.EX-1]] [[E-SS3.EX-6]] [[P-3JE4U]] [[E-QF7KI]]
