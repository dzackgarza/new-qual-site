---
schema: qual/card@1
id: E-AMD-F5ZHMJNK
kind: problem
title: $C_G(H)\trianglelefteq N_G(H)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Normal Subgroups
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
Show that $C_G(H) \trianglelefteq N_G(H)$ is a normal subgroup.
:::

::: {.solution}
Conjugation gives a homomorphism
\[
\Phi:N_G(H)\longrightarrow\operatorname{Aut}(H),
\qquad
\Phi(g)(h)=ghg^{-1}.
\]
It is well defined because every \(g\in N_G(H)\) satisfies \(gHg^{-1}=H\).

Its kernel is
\[
\ker\Phi
=\{g\in N_G(H):ghg^{-1}=h\text{ for all }h\in H\}
=C_G(H).
\]
Therefore \(C_G(H)\) is the kernel of a group homomorphism, hence
\[
\boxed{C_G(H)\trianglelefteq N_G(H).}
\]
:::
