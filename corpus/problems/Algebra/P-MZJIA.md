---
schema: qual/card@1
id: P-MZJIA
kind: problem
title: $C_G(H)$ is normal in $N_G(H)$
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
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a group and $H \le G$ a subgroup. Show that the centralizer $C_G(H)$ is a normal subgroup of the normalizer $N_G(H)$ (i.e. $C_G(H) \trianglelefteq N_G(H)$), and that $N_G(H)/C_G(H)$ is isomorphic to a subgroup of $\operatorname{Aut}(H)$ (the $N/C$ Theorem).
:::

::: {.solution}
For $n\in N_G(H)$, conjugation restricts to an automorphism of $H$. Hence
\[
\Phi:N_G(H)\longrightarrow \operatorname{Aut}(H),\qquad
\Phi(n)(h)=nhn^{-1}
\]
is a homomorphism. Its kernel is precisely
\[
\ker\Phi=\{n\in N_G(H):nhn^{-1}=h\ \forall h\in H\}=C_G(H).
\]
Therefore $C_G(H)\trianglelefteq N_G(H)$, and the first isomorphism theorem gives
\[
N_G(H)/C_G(H)\cong \operatorname{im}\Phi\le \operatorname{Aut}(H).
\]
This is the $N/C$ theorem.
:::
