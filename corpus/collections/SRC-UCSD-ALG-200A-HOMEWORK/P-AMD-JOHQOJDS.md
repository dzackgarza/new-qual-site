---
schema: qual/card@1
id: P-AMD-JOHQOJDS
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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 1(a).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Every inner automorphism c_g:x↦gxg^{-1} is an automorphism of G.
    Characteristicity therefore gives c_g(H)=H for every g, which is exactly
    normality.
---

::: {.problem}
Let $H$ be characteristic in $G$.
Prove that $H\normal G$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For each $g\in G$, conjugation by $g$ is an automorphism of $G$.

::: pf-proof

Define
\[
c_g:G\longrightarrow G,
\qquad
c_g(x)=gxg^{-1}.
\]
Then $c_g$ is a homomorphism, and its inverse is $c_{g^{-1}}$.
Hence
\[
c_g\in\operatorname{Aut}(G).
\]

:::

:::

::: {.pf-step #s2}

Every conjugation automorphism preserves $H$.

::: pf-proof

Since $H$ is characteristic in $G$, every automorphism of $G$ carries $H$ to itself.
Applying this to the automorphism $c_g$ from step [](#s1){.pf-ref} gives
\[
c_g(H)=H
\]
for every $g\in G$.

:::

:::

::: pf-step

Therefore $H\normal G$.

::: pf-proof

By step [](#s2){.pf-ref},
\[
gHg^{-1}=H
\]
for every $g\in G$.
This is exactly the definition of normality.

:::

:::

:::

:::
