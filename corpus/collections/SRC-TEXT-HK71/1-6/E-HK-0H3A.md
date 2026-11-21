---
schema: qual/card@1
id: E-HK-0H3A
kind: problem
title: Invertibility of upper-triangular matrices
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze Exercise 1.6.9.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
An $n \times n$ matrix $A$ is called upper-triangular if $A_{ij} = 0$ for $i > j$, that is, if every entry below the main diagonal is 0. Prove that an upper-triangular (square) matrix is invertible if and only if every entry on its main diagonal is different from 0.
:::


::: {.solution}

The argument is the card's own: the determinant of an upper-triangular matrix is the product of its diagonal entries, and over a field invertibility is nonvanishing of the determinant with no zero divisors.

Let $A$ be an $n\times n$ matrix over a field $F$ with $A_{ij}=0$ for $i>j$.

::: pf

::: {.pf-step #determinant}
$\det A=A_{11}A_{22}\cdots A_{nn}$.

::: pf-proof
In the Leibniz expansion $\det A=\sum_{\sigma}\operatorname{sgn}(\sigma)\prod_{i=1}^{n}A_{i,\sigma(i)}$, a term is nonzero only if $A_{i,\sigma(i)}\ne0$ for every $i$, that is only if $\sigma(i)\ge i$ for every $i$, since entries strictly below the diagonal vanish. Summing these inequalities over $i$ gives $\sum_{i}\sigma(i)\ge\sum_{i}i$, and the two sums are equal because $\sigma$ is a permutation; hence every inequality is an equality, $\sigma(i)=i$ for all $i$. So the identity permutation is the only one contributing, and its sign is $+1$; the remaining product is $A_{11}A_{22}\cdots A_{nn}$. Equivalently, argue by rows from the bottom: row $n$ has no nonzero entry in columns $<n$, so a nonzero term uses column $n$ there, and then row $n-1$ cannot use column $n$ and so uses column $n-1$, and so on.
:::

:::

::: {.pf-step #invertible}
$A$ is invertible if and only if $\det A\ne0$.

::: pf-proof
Over a field, a square matrix is invertible exactly when its determinant is nonzero: if $A$ is invertible then $\det A\det A^{-1}=1$, and if $\det A\ne0$ the adjugate formula $A\cdot\operatorname{adj}(A)=\det(A)I$ exhibits an inverse.
:::

:::

::: {.pf-step #conclusion}
$A$ is invertible if and only if $A_{ii}\ne0$ for every $i$.

::: pf-proof
By steps [](#determinant){.pf-ref} and [](#invertible){.pf-ref}, $A$ is invertible exactly when $A_{11}\cdots A_{nn}\ne0$, and in a field a product is nonzero exactly when every factor is: if some $A_{ii}=0$ the product vanishes, and if no factor vanishes the product does not, $F$ having no zero divisors. Hence
$$
\boxed{A\text{ invertible}\iff A_{ii}\ne0\ \text{for all } i.}
$$
:::

:::

:::
:::
