---
schema: qual/card@1
id: P-HPSTB
kind: problem
title: Inner automorphisms preserve conjugacy of subgroups
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Conjugacy
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Show that any automorphism (and in particular, every inner automorphism) sends conjugate subgroups to conjugate subgroups.
:::

::: solution
Suppose $H_2=gH_1g^{-1}$ and let $\varphi\in\operatorname{Aut}(G)$. Then
\[
\varphi(H_2)
=\varphi(gH_1g^{-1})
=\varphi(g)\,\varphi(H_1)\,\varphi(g)^{-1}.
\]
Thus $\varphi(H_1)$ and $\varphi(H_2)$ are conjugate subgroups of $G$. In particular, this holds for every inner automorphism.
:::
