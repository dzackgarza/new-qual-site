---
schema: qual/card@1
id: E-AMD-JRUQKWKO
kind: problem
title: $H$ characteristic in $K\trianglelefteq G$ implies $H\trianglelefteq G$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Automorphisms
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $H \leq K \trianglelefteq G$ and $H$ is characteristic in $K$, then $H \trianglelefteq G$.
:::

::: solution
Let $g\in G$. Since $K\trianglelefteq G$, conjugation by $g$ restricts to an automorphism
\[
c_g:K\longrightarrow K,
\qquad
k\longmapsto gkg^{-1}.
\]
Because $H$ is characteristic in $K$, every automorphism of $K$ preserves $H$. Hence
\[
gHg^{-1}=c_g(H)=H.
\]
This holds for every $g\in G$, so
\[
H\trianglelefteq G.
\]
:::
