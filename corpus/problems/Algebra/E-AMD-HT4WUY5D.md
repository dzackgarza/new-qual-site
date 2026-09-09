---
schema: qual/card@1
id: E-AMD-HT4WUY5D
kind: problem
title: Normality is not transitive
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Counterexamples
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
Give an example showing that normality is not transitive: i.e. $H\trianglelefteq K \trianglelefteq G$ with $H$ *not* normal in $G$.
:::

::: {.solution}
Take the dihedral group
\[
G=D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle
\]
of order $8$. Set
\[
K=\langle r^2,s\rangle=\{1,r^2,s,sr^2\},
\qquad
H=\langle s\rangle=\{1,s\}.
\]

Since $[G:K]=2$, we have $K\trianglelefteq G$. Since $[K:H]=2$, we have $H\trianglelefteq K$.

But
\[
rsr^{-1}=sr^2\notin H,
\]
so $rHr^{-1}\ne H$. Hence
\[
H\trianglelefteq K\trianglelefteq G
\quad\text{but}\quad
H\not\trianglelefteq G.
\]
Thus normality is not transitive.
:::
