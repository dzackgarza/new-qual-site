---
schema: qual/card@1
id: P-7QSIF
kind: problem
title: Normal $p$-subgroups lie in every Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent reproduction of Hungerford II.5.6.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a finite group and $H \trianglelefteq G$ a normal subgroup of order $p^k$.
Show that $H$ is contained in every Sylow $p$-subgroup of $G$.
:::

::: solution
Let $P$ be an arbitrary Sylow $p$-subgroup of $G$.

<1>1. There exists $g\in G$ such that $H\le gPg^{-1}$.
::: proof
The subgroup $H$ is a $p$-subgroup. By Sylow's containment theorem, every
$p$-subgroup of $G$ is contained in a conjugate of a Sylow $p$-subgroup. Hence
$H\le gPg^{-1}$ for some $g\in G$.
:::

<1>2. One has $H\le P$.
::: proof
Conjugating the inclusion in <1>1 by $g^{-1}$ gives
\[
g^{-1}Hg\le P.
\]
Since $H\trianglelefteq G$, normality gives $g^{-1}Hg=H$. Therefore $H\le P$.
:::

<1>3. Thus $H$ is contained in every Sylow $p$-subgroup of $G$.
::: proof
The Sylow subgroup $P$ was arbitrary.
:::
:::
