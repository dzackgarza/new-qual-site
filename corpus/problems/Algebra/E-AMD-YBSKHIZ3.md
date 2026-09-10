---
schema: qual/card@1
id: E-AMD-YBSKHIZ3
kind: problem
title: $C_G(H)\subseteq N_G(H)\leq G$
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the subgroup and N/C assertions to the conjugation homomorphism.
---

::: {.exercise}
Let $G$ be a group and $H\le G$.

1. Prove that $C_G(H)$ and $N_G(H)$ are subgroups and that
\[
C_G(H)\subseteq N_G(H)\le G.
\]
2. Prove that $C_G(H)\trianglelefteq N_G(H)$ and state the $N/C$ theorem.
:::

::: {.solution}
The centralizer and normalizer are
\[
C_G(H)=\{g\in G:gh=hg\text{ for all }h\in H\},
\]
\[
N_G(H)=\{g\in G:gHg^{-1}=H\}.
\]
Both contain the identity and are closed under products and inverses, hence are subgroups. If $g\in C_G(H)$, then $ghg^{-1}=h$ for every $h\in H$, so $gHg^{-1}=H$. Thus
\[
C_G(H)\le N_G(H)\le G.
\]

Conjugation gives a homomorphism
\[
\Phi:N_G(H)\longrightarrow\operatorname{Aut}(H),
\qquad
\Phi(g)(h)=ghg^{-1}.
\]
Its kernel is exactly $C_G(H)$. Therefore
\[
C_G(H)\trianglelefteq N_G(H),
\]
and the first isomorphism theorem gives the $N/C$ theorem:
\[
N_G(H)/C_G(H)\cong\operatorname{im}\Phi\le\operatorname{Aut}(H).
\]
:::
