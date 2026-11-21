---
title: Minimal and characteristic polynomials
order: 20
topics:
- Minimal and Characteristic Polynomials
---

# Minimal and characteristic polynomials

Let $A$ be an $n\times n$ matrix over a field $F$, and make $V=F^n$ an $F[t]$-module by $p(t)\actson v \coloneqq p(A)v$.
The [[D-GK5SF|minimal polynomial]] $\min_A$ is the monic generator of the annihilator of this module, so a divisibility between minimal polynomials is a containment of annihilators, and the [[D-QFYAC|characteristic polynomial]] $\chi_A(t)=\det(tI-A)$ is the product of the module's invariant factors.

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

::: {.remark title="The two polynomials do not determine the operator"}
The pair $(\min_A,\chi_A)$ does not determine the Jordan form: $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0)\oplus J_1(0)$ share the characteristic polynomial $x^4$ and the minimal polynomial $x^2$, as the block-counting data on [[algebra/linear-algebra/jordan-canonical-form|Jordan canonical form]] show.
:::

## Computing the minimal polynomial

[[PR-UFVPY]]

::: {.example title="Polynomial long division"}
For $f(x) \coloneqq x^3-6x^2+12x-8$, [[PR-RRTST|the rational root theorem]] restricts the rational roots to $\theset{\pm 8, \pm 4, \pm 2, \pm 1}$.
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
