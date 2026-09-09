---
schema: qual/card@1
id: P-HGRO13
kind: problem
title: A subgroup normalizer need not be normal
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Must the normalizer of a subgroup be a normal subgroup?
Prove the claim or give a counterexample.
:::

::: solution
No. Take $G=S_3$ and $H=\langle(12)\rangle$.

<1>1. The normalizer of $H$ is $H$ itself.
::: proof
For $g\in S_3$,
\[
gHg^{-1}=H
\]
if and only if $g(12)g^{-1}=(12)$. Conjugation relabels a transposition, so
this is equivalent to
\[
(g(1)\ g(2))=(12),
\]
which holds exactly when $g$ preserves the set $\{1,2\}$. The only such
permutations in $S_3$ are $e$ and $(12)$. Thus
\[
N_{S_3}(H)=H.
\]
:::

<1>2. The subgroup $N_{S_3}(H)=H$ is not normal in $S_3$.
::: proof
For example,
\[
(123)(12)(123)^{-1}=(23)\notin H.
\]
Hence $(123)H(123)^{-1}\ne H$.
:::

<1>3. Therefore a subgroup normalizer need not be normal in the ambient group.
::: proof
This follows from <1>1 and <1>2.
:::
:::
