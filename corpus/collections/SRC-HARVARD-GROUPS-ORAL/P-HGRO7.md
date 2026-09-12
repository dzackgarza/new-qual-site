---
schema: qual/card@1
id: P-HGRO7
kind: problem
title: Every p-subgroup lies in a Sylow subgroup
classification:
  areas: [algebra]
  topics: [Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard group-theory oral-question extraction, Basic Group Theory, question on containment in a Sylow p-subgroup.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Prove that every $p$-subgroup of a finite group is contained in a Sylow $p$-subgroup.
:::

::: solution
Let $G$ be finite, let $P\le G$ be a $p$-subgroup, and let $S$ be any Sylow
$p$-subgroup of $G$.

<1>1. Let $P$ act by left multiplication on the coset space $G/S$.
::: proof
For $x\in P$ and $gS\in G/S$, define
\[
x\cdot gS=(xg)S.
\]
This is a well-defined group action.
:::

<1>2. This action has a fixed point.
::: proof
Write $|G|=p^a m$ with $p\nmid m$. Since $S$ is Sylow,
$|S|=p^a$, so
\[
|G/S|=m
\]
is not divisible by $p$.

Every $P$-orbit has cardinality a power of $p$. If there were no fixed point,
every orbit would have cardinality divisible by $p$, forcing $p\mid |G/S|$,
contrary to the preceding calculation. Hence some coset $gS$ is fixed by all
of $P$.
:::

<1>3. Therefore $P$ is contained in a Sylow $p$-subgroup.
::: proof
If $gS$ is fixed by $P$, then for every $x\in P$,
\[
xgS=gS,
\]
so $g^{-1}xg\in S$. Thus
\[
P\le gSg^{-1}.
\]
Since $gSg^{-1}$ is again a Sylow $p$-subgroup of $G$, this proves the claim.
:::
:::
