---
title: Minimal and characteristic polynomials
order: 20
topics:
- Minimal and Characteristic Polynomials
---

# Minimal and characteristic polynomials

Let $A$ be an $n\times n$ matrix over a field $F$, and make $V=F^n$ an $F[t]$-module by $p(t)\actson v \da p(A)v$.
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

[[FD-GOB47]]

## The relation between the two polynomials

[[T-SJCF7]]

::: {.proposition}
$\min_A$ divides $\chi_A$, and $\min_A$ and $\chi_A$ have the same irreducible factors; in particular they have the same roots.
:::

::: {.proof}
By Cayley--Hamilton, $\chi_A(A) = 0$, so $\min_A$ divides $\chi_A$.
Let $p_1\divides p_2\divides\cdots\divides p_m$ be the invariant factors of $V$, so that $\chi_A = p_1\cdots p_m$ and $\min_A = p_m$.
Every irreducible factor of $\chi_A$ divides some $p_i$, hence divides $p_m = \min_A$.
For the roots directly: if $A\vector v_i = \lambda_i\vector v_i$ with $\vector v_i\neq\vector 0$, then
$$
\min_A(\lambda_i)\vector v_i = \min_A(A)\vector v_i = \vector 0,
$$
so $\min_A(\lambda_i) = 0$.
:::

::: {.remark title="The exponents"}
Since $\min_A$ divides $\chi_A$ and has the same irreducible factors, $\min_A$ is determined by the exponents of the irreducible factors of $\chi_A$ in it.
When $\chi_A$ splits, the exponent of $(t-\lambda)$ in $\min_A$ is the size of the largest Jordan block for $\lambda$, and in $\chi_A$ it is the sum of the sizes of those blocks; these do not determine the Jordan form in general, as for $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0)\oplus J_1(0)$.
:::

## Computing the minimal polynomial

[[PR-UFVPY]]

::: {.remark title="Computation"}
If $\chi_A = \prod_i q_i^{e_i}$ with the $q_i$ distinct monic irreducibles, then $\min_A = \prod_i q_i^{f_i}$ with $1\leq f_i\leq e_i$, and $\min_A$ is the polynomial of this form of least degree with $\min_A(A)=0$.
:::

::: {.example title="Polynomial long division"}
For $f(x) \da x^3-6x^2+12x-8$, the rational root theorem restricts the rational roots to $\ts{\pm 8, \pm 4, \pm 2, \pm 1}$.
Since $f(2) = 0$, divide by $x-2$:

![](../../../assets/figures/2021-07-24_18-32-38.png)

The quotient is $x^2-4x+4 = (x-2)^2$, so $f(x) = (x-2)^3$.
:::

## Invariant factors and cyclic operators

[[L-VDLNM]]

[[L-Y5KNM]]

[[PR-OF7ZW]]
