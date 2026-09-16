---
schema: qual/card@1
id: P-IT7OC
kind: problem
title: A subgroup that meets every conjugacy class is the whole group
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a finite group and let $H \le G$ be a subgroup.
Prove that if $H$ meets every conjugacy class of $G$ (i.e. $\bigcup_{g \in G} g H g^{-1} = G$), then $H = G$ (Jordan's Theorem on permutation groups).
:::

::: {.solution}
Suppose $H<G$ is proper and put $n=[G:H]\ge2$. Let $k$ be the number of distinct conjugates of $H$. Since
\[
k=[G:N_G(H)]\le [G:H]=n,
\]
and every conjugate contains the identity,
\[
\left|\bigcup_{g\in G}gHg^{-1}\right|
\le 1+k(|H|-1)
\le 1+n(|H|-1).
\]
Using $n|H|=|G|$,
\[
1+n(|H|-1)=|G|-(n-1)<|G|.
\]
Therefore the union of the conjugates of a proper subgroup cannot be all of $G$.

Hence, if
\[
\bigcup_{g\in G}gHg^{-1}=G,
\]
then $H$ cannot be proper, so $H=G$. Equivalently, a proper subgroup of a finite group misses at least one conjugacy class.
:::
