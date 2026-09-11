---
schema: qual/card@1
id: E-SS8.EX-4
kind: problem
title: "SS 8.4: No holomorphic surjection from the disc onto the plane"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
4. Does there exist a holomorphic surjection from the unit disc to $\mathbb { C } ?$

[Hint: Move the upper half-plane “down” and then square it to get C.]
:::

::: solution
Yes. Let
\[
h(z)=i\frac{1+z}{1-z},
\]
which maps $\mathbb D$ conformally onto the upper half-plane $\mathbb H$. Then
\[
g(z)=h(z)-i
\]
maps $\mathbb D$ onto the half-plane $\{w:\Im w>-1\}$.

Define
\[
F(z)=g(z)^2.
\]
This is holomorphic on $\mathbb D$. To prove surjectivity, let $\zeta\in\mathbb C$. Choose one square root $w$ of $\zeta$ with $\Im w\ge0$; one of the two square roots always has nonnegative imaginary part. Then $\Im w>-1$, so $w=g(z)$ for some $z\in\mathbb D$. Consequently
\[
F(z)=g(z)^2=w^2=\zeta.
\]
Thus $F:\mathbb D\to\mathbb C$ is a holomorphic surjection.
:::
