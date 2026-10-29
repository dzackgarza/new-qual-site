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
Let $G$ be a group and $H \le G$ a subgroup. Show that the centralizer $C_G(H)$ is a normal subgroup of the normalizer $N_G(H)$ (i.e. $C_G(H) \trianglelefteq N_G(H)$), and that $N_G(H)/C_G(H)$ is isomorphic to a subgroup of $\Aut(H)$ (the $N/C$ Theorem).
:::

::: {.solution}
::: pf

::: {.pf-step #hom}
The map $\Phi\colon N_G(H)\to\Aut(H)$, $\Phi(n)(h)=nhn^{-1}$, is a homomorphism with kernel $C_G(H)$.

::: pf-proof
For $n\in N_G(H)$, $nHn^{-1}=H$, so conjugation by $n$ restricts to an automorphism of $H$, and $\Phi(nm)=\Phi(n)\Phi(m)$.
An element of $C_G(H)$ fixes $H$ pointwise under conjugation, so $C_G(H)\subseteq N_G(H)$, and $\ker\Phi=\{n\in N_G(H):nhn^{-1}=h\text{ for all }h\in H\}=C_G(H)$.
:::

:::

::: pf-step
$C_G(H)\trianglelefteq N_G(H)$ and $N_G(H)/C_G(H)$ is isomorphic to a subgroup of $\Aut(H)$.

::: pf-proof
A kernel is normal, and the first isomorphism theorem applied to step [](#hom){.pf-ref} gives $N_G(H)/C_G(H)\cong\im\Phi\le\Aut(H)$.
:::

:::

:::

:::
