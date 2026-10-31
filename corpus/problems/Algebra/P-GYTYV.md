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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Source did not say what G and H are; the statement now declares G a group and H a subgroup of G.
---

::: {.problem}
Let $G$ be a group and $H\le G$ a subgroup. The centralizer of $H$ is $C_G(H)=\{g\in G \st hg=gh \text{ for all } h\in H\}$. Show that $C_G(H)$ is a subgroup of $N_G(H)$.
:::

::: {.solution}
Recall
$$
C_G(H)=\{g\in G \st gh=hg\text{ for all }h\in H\}
$$
and
$$
N_G(H)=\{g\in G \st gHg^{-1}=H\}.
$$

::: pf

::: {.pf-step #c-in-n}

One has
$$
C_G(H)\subseteq N_G(H).
$$

::: pf-proof

If $g\in C_G(H)$, then for every $h\in H$,
$$
ghg^{-1}=h.
$$
Thus conjugation by $g$ fixes every element of $H$, so $gHg^{-1}=H$ and $g\in N_G(H)$.

:::

:::

::: {.pf-step #n-subgroup}

One has
$$
N_G(H)\le G.
$$

::: pf-proof

The identity normalizes $H$. If $g_1,g_2\in N_G(H)$, then
$$
(g_1g_2)H(g_1g_2)^{-1}
=g_1(g_2Hg_2^{-1})g_1^{-1}
=g_1Hg_1^{-1}
=H,
$$
so $g_1g_2\in N_G(H)$. If $g\in N_G(H)$, then $gHg^{-1}=H$, and conjugating this equality by $g^{-1}$ gives $g^{-1}Hg=H$, so $g^{-1}\in N_G(H)$.

:::

:::

::: {.pf-step #c-subgroup}

One has
$$
C_G(H)\le G.
$$

::: pf-proof

The identity commutes with every $h\in H$. If $g_1,g_2\in C_G(H)$ and $h\in H$, then
$$
(g_1g_2)h=g_1hg_2=h(g_1g_2),
$$
so $g_1g_2\in C_G(H)$. If $g\in C_G(H)$, then multiplying $gh=hg$ on both sides by $g^{-1}$ gives $hg^{-1}=g^{-1}h$, so $g^{-1}\in C_G(H)$.

:::

:::

::: pf-qed

By step [](#c-subgroup){.pf-ref}, $C_G(H)$ is a subgroup of $G$; by step [](#c-in-n){.pf-ref} it is contained in $N_G(H)$, which is a subgroup of $G$ by step [](#n-subgroup){.pf-ref}. A subgroup of $G$ contained in the subgroup $N_G(H)$ is a subgroup of $N_G(H)$.

:::

:::

:::
