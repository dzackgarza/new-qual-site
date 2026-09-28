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
If $H\operatorname{char}G$, then $H$ is fixed by every automorphism of $G$. In particular it is fixed by every inner automorphism
\[
\iota_g(x)=gxg^{-1},\qquad g\in G.
\]
Hence $gHg^{-1}=H$ for every $g\in G$, so $H\trianglelefteq G$.

The converse fails. In the Klein four-group
\[
V_4=\{1,a,b,c\},
\]
every subgroup is normal because $V_4$ is abelian. But $\langle a\rangle$ is not characteristic: an automorphism exchanging $a$ and $b$ sends $\langle a\rangle$ to $\langle b\rangle$.
:::
