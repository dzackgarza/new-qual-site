---
schema: qual/card@1
id: P-HCAO3
kind: problem
title: Prime ideals need not be maximal
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Give an example of a commutative ring with identity that has a prime ideal which is not maximal.
:::

::: {.solution}
<1>1. Example: The ring of integers $\mathbb{Z}$ and the zero ideal: <2>1. Let $R = \mathbb{Z}$ and consider the zero ideal $\mathfrak{p} = \{0\} = \langle 0 \rangle$.
<2>2. The quotient ring $R / \mathfrak{p} = \mathbb{Z} / \langle 0 \rangle \cong \mathbb{Z}$ is an integral domain because the product of any two non-zero integers is non-zero.
Therefore $\langle 0 \rangle$ is a prime ideal of $\mathbb{Z}$.
<2>3. The quotient ring $\mathbb{Z}$ is not a field (for example, $2 \in \mathbb{Z}$ is not invertible since $\frac{1}{2} \notin \mathbb{Z}$). Alternatively, $\langle 0 \rangle \subsetneq \langle 2 \rangle \subsetneq \mathbb{Z}$, so $\langle 0 \rangle$ is strictly contained in the proper ideal $\langle 2 \rangle$.
Therefore $\langle 0 \rangle$ is not a maximal ideal.

<1>2. Second Example: Polynomial ring $k[x, y]$ and the principal ideal $\langle x \rangle$: <2>1. Let $k$ be any field and $R = k[x, y]$.
Consider the principal ideal $\mathfrak{p} = \langle x \rangle$.
<2>2. The quotient ring $R / \mathfrak{p} = k[x, y] / \langle x \rangle \cong k[y]$ is a polynomial ring in one variable over a field, which is an integral domain.
Thus $\langle x \rangle$ is a prime ideal.
<2>3. In $k[y]$, the non-zero element $y$ has no multiplicative inverse, so $k[y]$ is not a field.
Equivalently, there is a strict chain of proper ideals:
\[
\langle x \rangle \subsetneq \langle x, y \rangle \subsetneq k[x, y].
\]
Because $k[x, y] / \langle x, y \rangle \cong k$ is a field, $\langle x, y \rangle$ is maximal, while $\langle x \rangle$ is not.

<1>3. Conclusion: In $\mathbb{Z}$, the zero ideal $\langle 0 \rangle$ is prime but not maximal; in $k[x, y]$, $\langle x \rangle$ is prime but not maximal.
Q.E.D.
:::
