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

(a) Prove that $C_G(H)$ and $N_G(H)$ are subgroups and that
$$
C_G(H)\subseteq N_G(H)\le G.
$$

(b) Prove that $C_G(H)\trianglelefteq N_G(H)$ and state the $N/C$ theorem.
:::

::: {.solution}
The centralizer and normalizer are
$$
C_G(H)=\{g\in G:gh=hg\text{ for all }h\in H\},
\qquad
N_G(H)=\{g\in G:gHg^{-1}=H\}.
$$

::: pf

::: {.pf-step #subgroups}
(a) $C_G(H)$ and $N_G(H)$ are subgroups of $G$, and $C_G(H)\subseteq N_G(H)$.

::: pf-proof
Both sets contain the identity. If $g,g'\in N_G(H)$, then $(gg')H(gg')^{-1}=g(g'Hg'^{-1})g^{-1}=H$, and applying $g^{-1}$ to $gHg^{-1}=H$ gives $g^{-1}Hg=H$; so $N_G(H)$ is closed under products and inverses. The same computation with $ghg^{-1}=h$ for each $h\in H$ shows that $C_G(H)$ is a subgroup. If $g\in C_G(H)$, then $ghg^{-1}=h$ for every $h\in H$, so $gHg^{-1}=H$ and $g\in N_G(H)$.
:::

:::

::: {.pf-step #conjugation-hom}
Conjugation $\Phi:N_G(H)\to\Aut(H)$, $\Phi(g)(h)=ghg^{-1}$, is a homomorphism with kernel $C_G(H)$.

::: pf-proof
For $g\in N_G(H)$, the map $h\mapsto ghg^{-1}$ is an automorphism of $H$ because $gHg^{-1}=H$, and $\Phi(gg')=\Phi(g)\circ\Phi(g')$. An element $g$ lies in the kernel exactly when $ghg^{-1}=h$ for every $h\in H$, that is, when $g\in C_G(H)$.
:::

:::

::: pf-step
(b) $C_G(H)\trianglelefteq N_G(H)$, and the $N/C$ theorem holds: $N_G(H)/C_G(H)$ is isomorphic to a subgroup of $\Aut(H)$.

::: pf-proof
By step [](#conjugation-hom){.pf-ref}, $C_G(H)$ is a kernel, hence normal, and the first isomorphism theorem gives $N_G(H)/C_G(H)\cong\im\Phi\le\Aut(H)$.
:::

:::

:::

:::
