---
schema: qual/card@1
id: P-JX3FO
kind: problem
title: The kernel of a homomorphism is a normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Prove that the kernel of a homomorphism is a normal subgroup.
:::

::: {.solution}
Let $\phi:G\to H$ be a group homomorphism. Its kernel is
\[
\ker\phi=\{g\in G:\phi(g)=1_H\}.
\]
It is a subgroup: if $x,y\in\ker\phi$, then
\[
\phi(xy^{-1})=\phi(x)\phi(y)^{-1}=1_H.
\]

For normality, let $g\in G$ and $k\in\ker\phi$. Then
\[
\phi(gkg^{-1})=\phi(g)\phi(k)\phi(g)^{-1}=1_H,
\]
so $gkg^{-1}\in\ker\phi$. Therefore
\[
\ker\phi\trianglelefteq G.
\]
:::
