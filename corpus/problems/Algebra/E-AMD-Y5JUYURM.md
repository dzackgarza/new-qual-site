---
schema: qual/card@1
id: E-AMD-Y5JUYURM
kind: problem
title: Maximal subgroups of a finite $p$-group are normal of index $p$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the normalizer condition and quotient maximality to prove normality and index p.
---

::: {.exercise}
Show that every maximal subgroup $M$ of a finite $p$-group $G$ is normal and has index $p$.
:::

::: {.solution}
Let $M$ be a maximal subgroup of the finite $p$-group $G$.

::: pf

::: {.pf-step #normalizer-condition}
If $H<G$ is a proper subgroup of the finite $p$-group $G$, then $H<N_G(H)$.

::: pf-proof
Let $H$ act on the left cosets $G/H$ by left multiplication. Since $[G:H]$ is a positive power of $p$, the number of fixed points is congruent to $[G:H]\equiv0\pmod p$. A coset $gH$ is fixed exactly when $g^{-1}Hg=H$, so the fixed-point set is $N_G(H)/H$. It contains the coset $H$, so it has at least one element, and divisibility by $p$ gives $[N_G(H):H]\ge p$.
:::

:::

::: {.pf-step #m-normal}
$M\trianglelefteq G$.

::: pf-proof
By step [](#normalizer-condition){.pf-ref}, $M<N_G(M)\le G$. Maximality of $M$ forces $N_G(M)=G$.
:::

:::

::: pf-step
$[G:M]=p$.

::: pf-proof
By step [](#m-normal){.pf-ref}, $G/M$ is a nontrivial finite $p$-group. By the correspondence theorem, maximality of $M$ means $G/M$ has no nontrivial proper subgroup. By Cauchy's theorem $G/M$ has a subgroup of order $p$, which must be all of $G/M$.
:::

:::

:::

:::
