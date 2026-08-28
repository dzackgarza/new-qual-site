---
schema: qual/card@1
id: E-SS2.EX-12
kind: exercise
title: "Let u be a real-valued function defined on the unit disc D"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
---

::: exercise
12. Let u be a real-valued function defined on the unit disc D. Suppose that $u$ is twice continuously diferentiable and harmonic, that is,

$$
\triangle u (x, y) = 0
$$

for all $( x , y ) \in \mathbb { D }$

(a) Prove that there exists a holomorphic function f on the unit disc such that

$$
\operatorname{Re} (f) = u.
$$

Also show that the imaginary part of f is uniquely defined up to an additive (real) constant.
[Hint: From the previous chapter we would have $f ^ { \prime } ( z ) =$ $2 \partial u / \partial z$ . Therefore, let $g ( z ) = 2 \partial u / \partial z$ and prove that $g$ is holomorphic. Why can one find $F$ with $F ^ { \prime } = g \ ?$ Prove that $\mathrm { R e } ( F )$ difers from u by a real constant.]

(b) Deduce from this result, and from Exercise 11, the Poisson integral representation formula from the Cauchy integral formula: If u is harmonic in the unit disc and continuous on its closure, then if $z = r e ^ { i \theta }$ one has

$$
u (z) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} P _ {r} (\theta - \varphi) u (\varphi) d \varphi
$$

where $P _ { r } ( \gamma )$ is the Poisson kernel for the unit disc given by

$$
P _ {r} (\gamma) = \frac {1 - r ^ {2}}{1 - 2 r \cos \gamma + r ^ {2}}.
$$
:::
