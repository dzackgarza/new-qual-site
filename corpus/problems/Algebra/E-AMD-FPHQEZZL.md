---
schema: qual/card@1
id: E-AMD-FPHQEZZL
kind: problem
title: $\Inn(G)\cong G/Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Isomorphism Theorems
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

::: {.exercise}
Show that $\operatorname{Inn}(G) \cong G / Z(G)$.
:::

::: {.solution}
Define
\[
\Phi:G\to\Aut(G),\qquad \Phi(g)(x)=gxg^{-1}.
\]
Then
\[
\Phi(gh)=\Phi(g)\Phi(h),
\]
so $\Phi$ is a homomorphism. Its image is, by definition, $\Inn(G)$.

Moreover,
\[
g\in\ker\Phi
\iff gxg^{-1}=x\ \text{for all }x\in G
\iff g\in Z(G).
\]
Thus $\ker\Phi=Z(G)$. The first isomorphism theorem gives
\[
\boxed{G/Z(G)\cong\Inn(G)}.
\]
:::
