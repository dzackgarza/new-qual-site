---
schema: qual/card@1
id: E-AWEWJ
kind: problem
title: An affine coordinate homeomorphism of R^omega
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Given sequences $(a_1, a_2, \ldots)$ and $(b_1, b_2, \ldots)$ of real numbers with $a_i > 0$ for all $i$, define $h: \mathbb{R}^\omega \to \mathbb{R}^\omega$ by the equation

$$
h((x_1, x_2, \dots)) = (a_1 x_1 + b_1, a_2 x_2 + b_2, \dots).
$$

Show that if $\mathbb{R}^\omega$ is given the product topology, $h$ is a homeomorphism of $\mathbb{R}^\omega$ with itself.
What happens if $\mathbb{R}^\omega$ is given the box topology?
:::

::: {.solution}
For each $i$, let
\[
h_i:\mathbb R\to\mathbb R,\qquad h_i(x)=a_ix+b_i.
\]
Since $a_i>0$, $h_i$ is a homeomorphism with inverse
\[
h_i^{-1}(y)=\frac{y-b_i}{a_i}.
\]
The map $h$ is the product map $\prod_i h_i$.

For the product topology, the inverse image of a basic set
\[
\prod_iU_i,
\]
with $U_i=\mathbb R$ except for finitely many $i$, is
\[
\prod_i h_i^{-1}(U_i),
\]
which is again basic product-open. The same statement holds for $h^{-1}$, so $h$ is a homeomorphism.

Exactly the same proof works for the box topology: now every coordinate may be restricted, but
\[
h^{-1}\left(\prod_iU_i\right)=\prod_i h_i^{-1}(U_i)
\]
is a basic box-open set, and likewise for the inverse map. Thus $h$ is a homeomorphism for both the product and box topologies.
:::
