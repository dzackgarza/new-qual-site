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
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Show that $N_G(H) / C_G(H)$ is isomorphic to a subgroup of $\operatorname{Aut}(H)$." without introducing $G$ or $H$; the statement now declares $G$ a group and $H$ a subgroup.'
---

::: {.problem}
Let $G$ be a group and $H\le G$ a subgroup. Show that $N_G(H) / C_G(H)$ is isomorphic to a subgroup of $\Aut(H)$.
:::

::: {.solution}

::: pf

::: {.pf-step #hom}
There is a homomorphism $\Phi:N_G(H)\to\Aut(H)$ with $\Phi(g)(h)=ghg^{-1}$, and $\ker\Phi=C_G(H)$.

::: pf-proof
For $g\in N_G(H)$, conjugation by $g$ maps $H$ onto $gHg^{-1}=H$ and is a homomorphism with inverse conjugation by $g^{-1}$, so $\Phi(g)\in\Aut(H)$. Since $\Phi(gg')(h)=gg'hg'^{-1}g^{-1}=\Phi(g)\Phi(g')(h)$, $\Phi$ is a homomorphism. Its kernel is the set of $g$ with $ghg^{-1}=h$ for all $h\in H$, which is $C_G(H)$.
:::

:::

::: pf-step
$N_G(H)/C_G(H)\cong\im\Phi\le\Aut(H)$.

::: pf-proof
This is the first isomorphism theorem applied to $\Phi$ from step [](#hom){.pf-ref}.
:::

:::

:::

:::
