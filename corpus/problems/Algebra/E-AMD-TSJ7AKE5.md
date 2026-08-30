---
schema: qual/card@1
id: E-AMD-TSJ7AKE5
kind: exercise
title: The number of conjugates of $H$ equals $[G:N_G(H)]$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Given $H\subseteq G$, let $S(H)= \bigcup_{g\in G} gHg^{-1}$, so $\abs{S(H)}$ is the number of conjugates to $H$.
Show that $\abs{S(H)} = [G : N_G(H)]$.

- That is, the number of subgroups conjugate to $H$ equals the index of the normalizer of $H$.
:::

::: {.solution}
<1>1. $G$ acts on the set of subgroups by conjugation: $g\cdot H = gHg^{-1}$.
Proof: action.

<1>2. The orbit of $H$ is $S(H)=\{gHg^{-1}:g\in G\}$.
Proof: definition.

<1>3. The stabilizer of $H$ is $N_G(H)=\{g: gHg^{-1}=H\}$.
Proof: definition of normalizer.

<1>4. By orbit-stabilizer, $|S(H)|=[G:N_G(H)]$.
Proof: <1>2 and <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
