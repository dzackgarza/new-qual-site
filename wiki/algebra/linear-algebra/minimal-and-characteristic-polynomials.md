---
title: Minimal and characteristic polynomials
order: 20
topics:
- Minimal and Characteristic Polynomials
---

# Minimal and characteristic polynomials

Let $A$ be an $n\times n$ matrix over a field $F$, and make $V=F^n$ an $F[t]$-module by $p(t)\actson v \definedas p(A)v$.
The [[D-GK5SF|minimal polynomial]] $\min_A$ is the monic generator of the annihilator of this module, and the [[D-QFYAC|characteristic polynomial]] $\chi_A(t)=\det(tI-A)$ is the product of its invariant factors, the largest of which is $\min_A$.

[[PR-EDD7U]]

::: {.remark title="Notation"}
| Symbol | Meaning |
| --- | --- |
| $\min_A(x)$ | the minimal polynomial of $A$ |
| $\chi_A(x)$ | the characteristic polynomial of $A$ |
:::

[[D-GK5SF]]

[[D-QFYAC]]

## The relation between the two polynomials

[[T-SJCF7]]

::: {.remark title="The exponents"}
By [[PR-UFVPY]], $\min_A$ divides $\chi_A$ and has the same irreducible factors, so $\min_A$ is determined by the exponents of the irreducible factors of $\chi_A$ in it.
When $\chi_A$ splits, the exponent of $(t-\lambda)$ in $\min_A$ is the size of the largest Jordan block for $\lambda$, and in $\chi_A$ it is the sum of the sizes of those blocks; these do not determine the Jordan form in general, as for $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0)\oplus J_1(0)$.
:::

## Computing the minimal polynomial

[[PR-UFVPY]]

::: {.example title="Polynomial long division"}
For $f(x) \definedas x^3-6x^2+12x-8$, [[PR-RRTST|the rational root theorem]] restricts the rational roots to $\theset{\pm 8, \pm 4, \pm 2, \pm 1}$.
Since $f(2) = 0$, divide by $x-2$:

$$
\begin{aligned}
x^3-6x^2+12x-8 - x^2(x-2) &= -4x^2+12x-8,\\
-4x^2+12x-8 - (-4x)(x-2) &= 4x-8,\\
4x-8 - 4(x-2) &= 0.
\end{aligned}
$$

The quotient is $x^2-4x+4 = (x-2)^2$, so $f(x) = (x-2)^3$.
:::

## Invariant factors and cyclic operators

[[L-VDLNM]]

[[L-Y5KNM]]

[[PR-4GQIZ]]
