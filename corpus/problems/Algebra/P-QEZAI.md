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
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Show that $Z(G) \subseteq C_G(H) \subseteq N_G(H)$." as a bullet without introducing $G$ or $H$; the statement now declares $G$ a group and $H$ a subgroup.'
---

::: {.problem}
Let $G$ be a group and $H\le G$ a subgroup. Show that $Z(G) \subseteq C_G(H) \subseteq N_G(H)$.
:::

::: {.solution}

::: pf

::: pf-step
$Z(G)\subseteq C_G(H)$.

::: pf-proof
If $z\in Z(G)$, then $zh=hz$ for every $h\in G$, in particular for every $h\in H$, so $z\in C_G(H)$.
:::

:::

::: pf-step
$C_G(H)\subseteq N_G(H)$.

::: pf-proof
If $g\in C_G(H)$, then $ghg^{-1}=h$ for every $h\in H$, so $gHg^{-1}=H$ and $g\in N_G(H)$.
:::

:::

:::

:::
