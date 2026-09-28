---
schema: qual/card@1
id: D-W3DSO
kind: definition
title: Discriminant of a polynomial
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Symmetric Functions
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and $f\in k[x]$ a monic polynomial of degree $n\geq 1$, and write $f=\prod_{i=1}^n (x-r_i)$ with roots $r_1,\ldots,r_n$, listed with multiplicity, in a splitting field of $f$ over $k$.
The \dfn{discriminant} of $f$ is
$$
\Delta_f \coloneqq \prod_{1\leq i<j\leq n} (r_i - r_j)^2 .
$$
:::

::: {.proposition}
$\Delta_f = 0$ if and only if $f$ has a repeated root.
:::

::: {.proof}
A product in a field vanishes if and only if one of its factors does, and $(r_i-r_j)^2=0$ if and only if $r_i=r_j$ for some $i<j$.
:::

::: {.proposition}
Let $f\in \RR[x]$ be a monic cubic with $\Delta_f\neq 0$.
Then $\Delta_f>0$ if and only if $f$ has three distinct real roots, and $\Delta_f<0$ if and only if $f$ has one real root and a pair of complex conjugate non-real roots.
:::

::: {.proof}
Since $\Delta_f\neq 0$, the roots $r_1,r_2,r_3\in\CC$ are distinct, and since $f$ has real coefficients, its non-real roots occur in conjugate pairs.
So either all three roots are real, or $r_1\in\RR$ and $r_{2,3}=a\pm bi$ with $a,b\in\RR$ and $b\neq 0$.
In the first case each factor $r_i-r_j$ is a nonzero real number, so $\Delta_f>0$.
In the second case $(r_1-r_2)(r_1-r_3)=\abs{r_1-r_2}^2>0$ and $(r_2-r_3)^2=(2bi)^2=-4b^2<0$, so
$$
\Delta_f=\bigl((r_1-r_2)(r_1-r_3)\bigr)^2(r_2-r_3)^2<0 .
$$
The two cases are exhaustive and give opposite signs, which proves both equivalences.
:::
