---
schema: qual/card@1
id: P-AMD-YAHFRBZF
kind: problem
title: A characteristic subgroup of a normal subgroup is normal
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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 1(b).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    For each g∈G, normality of K makes conjugation by g restrict to an
    automorphism of K. Characteristicity of H in K forces this restricted
    automorphism to preserve H, so gHg^{-1}=H.
---

::: {.problem}
Let
\[
H\operatorname{char}K\normal G.
\]
Prove that $H\normal G$.
:::

::: {.solution}
<1>1. For each $g\in G$, conjugation by $g$ restricts to an automorphism of $K$.
::: {.proof}
Since $K\normal G$,
\[
gKg^{-1}=K
\]
for every $g\in G$.
Thus the conjugation automorphism
\[
c_g:G\longrightarrow G,
\qquad
c_g(x)=gxg^{-1},
\]
maps $K$ onto itself.
Therefore its restriction
\[
c_g|_K:K\longrightarrow K
\]
is an automorphism of $K$.
:::

<1>2. Every conjugation by an element of $G$ preserves $H$.
::: {.proof}
Because $H$ is characteristic in $K$, every automorphism of $K$ maps $H$ to itself.
Applying this to the automorphism $c_g|_K$ from <1>1 gives
\[
gHg^{-1}
=c_g(H)
=H
\]
for every $g\in G$.
:::

<1>3. Hence $H\normal G$.
::: {.proof}
The equality
\[
gHg^{-1}=H
\]
for all $g\in G$ is exactly the normality criterion.
:::
:::
