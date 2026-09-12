---
schema: qual/card@1
id: P-TOPS07E
kind: problem
title: "Any map from S^2 to a surface of genus >= 1 has degree zero"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
On any closed orientable surface $\Sigma_g$ of genus $g \geq 1$, it is possible to find a pair of simple closed curves $\alpha, \beta \subset \Sigma_g$ (submanifolds homeomorphic to $S^1$) meeting transversely at exactly one point ($I(\alpha, \beta) = \pm 1$). Use this fact together with intersection theory to show that any smooth (or continuous) map $f: S^2 \to \Sigma_g$ has **degree zero**: $$\deg(f) = 0.$$
:::

::: solution
<1>1. Choose oriented simple closed curves $\alpha,\beta\subset\Sigma_g$ meeting transversely in one point. By hypothesis their algebraic intersection number is
$$
I(\alpha,\beta)=\pm1.
$$

<1>2. Let $a,b\in H^1(\Sigma_g;\mathbb Z)$ be the Poincaré duals of $[\alpha]$ and $[\beta]$.
<2>1. The cup-product interpretation of intersection number gives
$$
\langle a\smile b,[\Sigma_g]\rangle=I(\alpha,\beta)=\pm1.
$$
Thus $a\smile b$ is a generator of $H^2(\Sigma_g;\mathbb Z)$ up to sign.

<1>3. Let $f:S^2\to\Sigma_g$ be continuous. Since $H^1(S^2;\mathbb Z)=0$,
$$
f^*a=f^*b=0.
$$
Hence, by naturality of the cup product,
$$
f^*(a\smile b)=f^*a\smile f^*b=0.
$$

<1>4. On the other hand, the definition of degree gives
$$
\langle f^*(a\smile b),[S^2]\rangle
=\deg(f)\,\langle a\smile b,[\Sigma_g]\rangle
=\pm\deg(f).
$$
The left-hand side is zero by <1>3, so $\deg(f)=0$.
:::
