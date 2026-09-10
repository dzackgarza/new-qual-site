---
schema: qual/card@1
id: P-2JEMA
kind: problem
title: $\Inn(G)\cong G/Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the duplicate inner-automorphism proof to the conjugation homomorphism.
---

::: {.exercise}
Show that
\[
\operatorname{Inn}(G)\cong G/Z(G).
\]
:::

::: {.solution}
Define
\[
\Phi:G\longrightarrow\operatorname{Aut}(G),
\qquad
\Phi(g)(x)=gxg^{-1}.
\]
Then $\Phi$ is a homomorphism and
\[
\operatorname{im}\Phi=\operatorname{Inn}(G).
\]
Moreover,
\[
g\in\ker\Phi
\iff gxg^{-1}=x\text{ for all }x\in G
\iff g\in Z(G).
\]
Thus $\ker\Phi=Z(G)$. The first isomorphism theorem gives
\[
G/Z(G)\cong\operatorname{Inn}(G).
\]
:::
