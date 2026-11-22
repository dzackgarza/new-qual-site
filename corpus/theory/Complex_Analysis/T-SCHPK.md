---
schema: qual/card@1
id: T-SCHPK
kind: theorem
title: Schwarz--Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Hyperbolic Metric
relations: []
review: draft
---

::: {.theorem}
Let $f\colon\DD\to\DD$ be [[D-E7A5W|holomorphic]].
Then for every $z\in\DD$,
$$
\frac{\abs{f'(z)}}{1-\abs{f(z)}^2}\leq\frac{1}{1-\abs z^2},
$$
equivalently $f$ does not increase the [[D-2HXLN|hyperbolic distance]]: $d_{\DD}(f(z),f(w))\leq d_{\DD}(z,w)$ for all $z,w\in\DD$.
Equality at one point forces $f$ to be an automorphism of $\DD$.

This is [@SS03, ch. 8, Exercise 13], part (b) for the derivative form and part (a) for the pseudo-hyperbolic form; the equality case is the [[T-DAETF|Schwarz lemma]] applied to $\psi_{f(z)}\circ f\circ\psi_z^{-1}$.
:::
