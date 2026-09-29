---
schema: qual/card@1
id: P-GYTYV
kind: problem
title: $C_G(H) \subseteq N_G(H) \leq G$
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
- Show that $C_G(H) \subseteq N_G(H) \leq G$.
:::

::: {.solution}
Recall
\[
C_G(H)=\{g\in G:gh=hg\text{ for all }h\in H\}
\]
and
\[
N_G(H)=\{g\in G:gHg^{-1}=H\}.
\]

::: pf

::: pf-step

One has
\[
C_G(H)\subseteq N_G(H).
\]

::: pf-proof

If $g\in C_G(H)$, then for every $h\in H$,
\[
ghg^{-1}=h.
\]
Thus conjugation by $g$ fixes every element of $H$, so $gHg^{-1}=H$ and $g\in N_G(H)$.

:::

:::

::: pf-step

One has
\[
N_G(H)\le G.
\]

::: pf-proof

The identity normalizes $H$. If $g_1,g_2\in N_G(H)$, then
\[
(g_1g_2)H(g_1g_2)^{-1}
=g_1(g_2Hg_2^{-1})g_1^{-1}
=g_1Hg_1^{-1}
=H,
\]
so $g_1g_2\in N_G(H)$. If $g\in N_G(H)$, then $gHg^{-1}=H$, and conjugating this equality by $g^{-1}$ gives $g^{-1}Hg=H$, so $g^{-1}\in N_G(H)$.

:::

:::

:::

Therefore
\[
C_G(H)\subseteq N_G(H)\le G.
\]
:::
