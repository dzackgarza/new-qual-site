---
schema: qual/card@1
id: T-C5VEI
kind: theorem
title: Casorati--Weierstrass theorem
slogan: 'At an essential singularity, every punctured neighborhood maps densely into $\CC$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Casorati-Weierstrass
  - Essential Singularities
relations: []
review: draft
---

::: {.theorem ref="Casorati"}
Let $\Omega\subseteq\CC$ be open, $z_0\in\Omega$, and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega\sm\theset{z_0}$ with an [[D-VKP6N|essential singularity]] at $z_0$.
Then for every punctured neighborhood $V=D_\varepsilon(z_0)\sm\theset{z_0}\subseteq\Omega$ of $z_0$, the image $f(V)$ is dense in $\CC$.

Equivalently, for every $w_0\in\CC$ there is a sequence $z_n\to z_0$, $z_n\neq z_0$, with $f(z_n)\to w_0$.
:::

::: {.remark title="Variations"}
A nonconstant [[D-E7A5W|entire]] function $f$ has dense image $f(\CC)$.
If $f$ is a polynomial, it is surjective by the fundamental theorem of algebra.
Otherwise $g(w)\coloneqq f(1/w)$ has an essential singularity at $w=0$, since its Laurent expansion at $0$ has infinitely many terms of negative index, and the theorem applied to $g$ shows that $f(\theset{\abs z>1})$ is already dense in $\CC$.
:::
