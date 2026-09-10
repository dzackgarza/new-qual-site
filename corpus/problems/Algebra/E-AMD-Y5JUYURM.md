---
schema: qual/card@1
id: E-AMD-Y5JUYURM
kind: problem
title: Maximal subgroups of a $p$-group are normal
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
We use the normalizer condition: if $H<G$ is a proper subgroup of a finite $p$-group, then
\[
H<N_G(H).
\]
Indeed, let $H$ act on the left cosets $G/H$ by left multiplication. Since $[G:H]$ is a positive power of $p$, the number of fixed points is divisible by $p$. A coset $gH$ is fixed exactly when $g^{-1}Hg=H$, so the fixed-point set is $N_G(H)/H$. It contains $H$, hence has at least one element; divisibility by $p$ therefore gives
\[
[N_G(H):H]\ge p,
\]
so $H<N_G(H)$.

Apply this to a maximal subgroup $M<G$. Then
\[
M<N_G(M)\le G.
\]
Maximality forces $N_G(M)=G$, hence $M\trianglelefteq G$.

Now $G/M$ is a nontrivial finite $p$-group. Since $M$ is maximal, $G/M$ has no nontrivial proper subgroup. By Cauchy's theorem, a nontrivial finite $p$-group has an element of order $p$; therefore $G/M$ itself must have order $p$. Hence
\[
[G:M]=p.
\]
:::
