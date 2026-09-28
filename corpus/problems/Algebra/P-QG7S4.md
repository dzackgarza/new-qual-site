---
schema: qual/card@1
id: P-QG7S4
kind: problem
title: $N/C$ theorem
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Automorphisms
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $N_G(H) / C_G(H)$ is isomorphic to a subgroup of $\operatorname{Aut}(H)$.
:::

::: {.solution}
Conjugation by an element of $N_G(H)$ preserves $H$, so there is a homomorphism
\[
\Phi:N_G(H)\to\operatorname{Aut}(H),\qquad
\Phi(g)(h)=ghg^{-1}.
\]
Its kernel consists exactly of those $g$ commuting with every element of $H$, namely
\[
\ker\Phi=C_G(H).
\]
By the first isomorphism theorem,
\[
N_G(H)/C_G(H)\cong\operatorname{im}\Phi\le\operatorname{Aut}(H).
\]
:::
