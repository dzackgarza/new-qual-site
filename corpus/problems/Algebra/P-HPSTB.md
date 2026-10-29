---
schema: qual/card@1
id: P-HPSTB
kind: problem
title: Automorphisms preserve conjugacy of subgroups
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

::: {.problem}
Show that any automorphism (and in particular, every inner automorphism) sends conjugate subgroups to conjugate subgroups.
:::

::: {.solution}
Let $G$ be a group, let $\varphi\in\Aut(G)$, and let $H_1,H_2\le G$ with $H_2=gH_1g^{-1}$ for some $g\in G$.

::: pf

::: pf-step
$\varphi(H_2)=\varphi(g)\,\varphi(H_1)\,\varphi(g)^{-1}$, so $\varphi(H_1)$ and $\varphi(H_2)$ are conjugate in $G$.

::: pf-proof
Since $\varphi$ is a homomorphism,
$$
\varphi(H_2)
=\varphi(gH_1g^{-1})
=\varphi(g)\,\varphi(H_1)\,\varphi(g)^{-1}.
$$
Inner automorphisms are automorphisms, so the conclusion holds for them in particular.
:::

:::

:::

:::
