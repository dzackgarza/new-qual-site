---
schema: qual/card@1
id: P-HCAO35
kind: problem
title: A one-dimensional normal domain which is not Noetherian
classification:
  areas:
  - algebra
  topics:
  - Integral Closure
  - Krull Dimension
  - Noetherian Rings
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Give an example of a one-dimensional integrally closed domain which is not Noetherian.
:::

::: {.solution}
<1>1. Construction of the ring $R$: <2>1. Let $R = \overline{\mathbb{Z}}$ be the ring of all algebraic integers in $\mathbb{C}$, which is the integral closure of $\mathbb{Z}$ in the algebraic closure $\overline{\mathbb{Q}}$.

<1>2. Proof that $R$ is an integrally closed domain: <2>1. $R \subset \overline{\mathbb{Q}}$ is a subring of a field, hence an integral domain.
Its fraction field is $\operatorname{Frac}(R) = \overline{\mathbb{Q}}$.
<2>2. By transitivity of integral extensions, if $\alpha \in \overline{\mathbb{Q}}$ is integral over $R = \overline{\mathbb{Z}}$, then $\alpha$ is integral over $\mathbb{Z}$, which means $\alpha \in \overline{\mathbb{Z}} = R$.
Thus $R$ is integrally closed in its fraction field.

<1>3. Proof that $\dim(R) = 1$: <2>1. The extension $\mathbb{Z} \subset \overline{\mathbb{Z}}$ is an integral extension of commutative rings.
By the Cohen–Seidenberg Going-Up and Incomparability Theorems, integral extensions preserve Krull dimension:
\[
\dim(\overline{\mathbb{Z}}) = \dim(\mathbb{Z}) = 1.
\]
In particular, every non-zero prime ideal of $\overline{\mathbb{Z}}$ is maximal.

<1>4. Proof that $R$ is not Noetherian: <2>1. Consider the ascending sequence of principal ideals in $\overline{\mathbb{Z}}$:
\[
I_n = \left\langle 2^{1/2^n} \right\rangle \subset \overline{\mathbb{Z}} \quad (n = 1, 2, 3, \ldots).
\]
<2>2. Since $2^{1/2^n} = \left(2^{1/2^{n+1}}\right)^2$, we have $I_n \subseteq I_{n+1}$.
The inclusion is strict ($I_n \subsetneq I_{n+1}$) because:
\[
\frac{2^{1/2^{n+1}}}{2^{1/2^n}} = 2^{-1/2^{n+1}} \notin \overline{\mathbb{Z}}
\]
(its minimal polynomial is $x^{2^{n+1}} - \frac{1}{2}$, which does not have integer coefficients).
<2>3. Thus we have an infinite strictly ascending chain of ideals:
\[
I_1 \subsetneq I_2 \subsetneq I_3 \subsetneq \cdots \subsetneq I_n \subsetneq \cdots
\]
Therefore $R = \overline{\mathbb{Z}}$ does not satisfy the ascending chain condition on ideals, so $R$ is not Noetherian.

<1>5. Conclusion: $R = \overline{\mathbb{Z}}$ is a 1-dimensional, integrally closed domain that is not Noetherian.
Q.E.D.
:::
