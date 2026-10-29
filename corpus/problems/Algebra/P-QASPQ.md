---
schema: qual/card@1
id: P-QASPQ
kind: problem
title: Characteristic subgroups are normal
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Normal Subgroups
  - Subgroups
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
(1) Prove that if $H \operatorname{char} G$ (i.e. $H$ is a characteristic subgroup of $G$), then $H \trianglelefteq G$ ($H$ is a normal subgroup of $G$).

(2) Give an example showing that normality does not imply characteristic (so "characteristic" is strictly stronger than "normal").
:::

::: {.solution}

::: pf

::: pf-step
(1) If $H\operatorname{char}G$, then $H\trianglelefteq G$.

::: pf-proof
For $g\in G$, conjugation $\iota_g(x)=gxg^{-1}$ is an automorphism of $G$, so $gHg^{-1}=\iota_g(H)=H$.
:::

:::

::: pf-step
(2) In the Klein four-group $V_4=\{1,a,b,c\}$, the subgroup $\boxed{\langle a\rangle}$ is normal but not characteristic.

::: pf-proof
$V_4$ is abelian, so every subgroup is normal. Identifying $V_4$ with $\FF_2^2$ via $a\mapsto(1,0)$, $b\mapsto(0,1)$, the linear map swapping the two coordinates is an automorphism with $a\mapsto b$, so it sends $\langle a\rangle=\{1,a\}$ to $\langle b\rangle\ne\langle a\rangle$.
:::

:::

:::

:::
