---
schema: qual/card@1
id: P-Z6MHZ
kind: problem
title: Kummer extension
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Roots of Unity
  - Cyclic Groups
relations: []
review: draft
---

::: problem
What is a Kummer extension?
:::

::: solution
Let $K$ be a field, let $n\ge2$ be an integer with
\[
\operatorname{char}K\nmid n,
\]
and suppose $K$ contains the group $\mu_n$ of $n$th roots of unity.

A **Kummer extension of exponent dividing $n$** is an extension of the form
\[
L=K\bigl(\sqrt[n]{a_1},\ldots,\sqrt[n]{a_r}\bigr)
\]
for elements $a_i\in K^\times$, with $L/K$ finite.

Because $K$ contains $\mu_n$, each polynomial
\[
x^n-a_i
\]
splits over $L$ once one root is present. Hence $L/K$ is normal. Since $\operatorname{char}K\nmid n$, these polynomials are separable, so $L/K$ is Galois.

Every automorphism sends
\[
\sqrt[n]{a_i}\longmapsto \zeta_i\sqrt[n]{a_i}
\qquad(\zeta_i\in\mu_n),
\]
so the Galois group embeds into a finite product of copies of $\mu_n$. Therefore it is abelian and has exponent dividing $n$.

Conversely, Kummer theory says that every finite abelian Galois extension $L/K$ whose Galois group has exponent dividing $n$ is obtained in this way, under the same hypotheses on $K$.
:::
