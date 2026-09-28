---
schema: qual/card@1
id: P-QEZAI
kind: problem
title: $Z(G)\subseteq C_G(H)\subseteq N_G(H)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
- Show that $Z(G) \subseteq C_G(H) \subseteq N_G(H)$.
:::

::: {.solution}
If $z\in Z(G)$, then $zh=hz$ for every $h\in H$, so $z\in C_G(H)$. Hence
\[
Z(G)\subseteq C_G(H).
\]
If $g\in C_G(H)$, then for every $h\in H$,
\[
ghg^{-1}=h.
\]
Therefore $gHg^{-1}=H$, so $g\in N_G(H)$. Thus
\[
Z(G)\subseteq C_G(H)\subseteq N_G(H).
\]
:::
