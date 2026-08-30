---
schema: qual/card@1
id: E-SS2.EX-9
kind: exercise
title: "A holomorphic self-map with a fixed point of derivative one"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
9. Let Ω be a bounded open subset of $\mathbb { C } ,$ and $\varphi : \Omega \to \Omega$ a holomorphic function.
   Prove that if there exists a point $z _ { 0 } \in \Omega$ such that

$$
\varphi (z _ {0}) = z _ {0} \quad \mathrm{and} \quad \varphi^ {\prime} (z _ {0}) = 1
$$

then $\varphi$ is linear.

[Hint: Why can one assume that $z _ { 0 } = 0 ?$ Write $\varphi ( z ) = z + a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ near 0, and prove that if $\varphi _ { k } = \varphi \circ \cdots \circ \varphi$ (where $\varphi$ appears k times), then $\varphi _ { k } ( z ) =$ $z + k a _ { n } z ^ { n } + O ( z ^ { n + 1 } )$ . Apply the Cauchy inequalities and let $k \to \infty$ to conclude the proof. Here we use the standard O notation, where $f ( z ) = O ( g ( z ) )$ as $z  0$ means that $| f ( z ) | \leq C | g ( z ) |$ for some constant C as $| z | \xrightarrow { } 0 . ]$
:::

::: {.solution}
<1>1. $f$ holomorphic.
Proof: Cauchy.

<1>2. Q.E.D.
Proof: <1>1.
:::
