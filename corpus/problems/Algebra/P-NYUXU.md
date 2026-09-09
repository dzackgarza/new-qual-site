---
schema: qual/card@1
id: P-NYUXU
kind: problem
title: Number of conjugates of a subgroup equals $[G:N_G(H)]$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Orbit-Stabilizer
relations: []
review: draft
---

::: problem
Let $G$ act by conjugation on its set of subgroups. Show that the number of subgroups conjugate to $H\le G$ is
\[
[G:N_G(H)].
\]
:::

::: {.solution}
Let
\[
\mathcal O(H)=\{gHg^{-1}:g\in G\}
\]
be the conjugacy orbit of $H$.

<1>1. The stabilizer of $H$ is its normalizer.
::: {.proof}
By definition,
\[
\operatorname{Stab}_G(H)
=\{g\in G:gHg^{-1}=H\}
=N_G(H).
\]
:::

<1>2. Apply orbit-stabilizer.
::: {.proof}
Orbit-stabilizer gives a bijection
\[
G/N_G(H)\longrightarrow \mathcal O(H),\qquad gN_G(H)\longmapsto gHg^{-1}.
\]
Hence
\[
|\mathcal O(H)|=[G:N_G(H)].
\]
Thus the number of conjugates of $H$ is the index of its normalizer.
:::
:::
