---
schema: qual/card@1
id: P-ALGS08A
kind: problem
title: "A finite group is not the union of conjugates of a proper subgroup"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared the statement with Problem 1 on page 1 of the official Spring 2008 algebra exam and with the UCSD group-theory review sheet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked the conjugate count against the normalizer index and the strict union bound for a proper subgroup.
---

::: problem
Let $G$ be a finite group and $H$ a proper subgroup.
Show that $G$ is not the set-theoretic union of the conjugates of $H$.
:::

::: {.solution}
<1>1. The number of distinct conjugates of $H$ is at most $[G:H]$.
::: {.proof}
The conjugation action of $G$ on its subgroups has stabilizer
\[
N_G(H)=\{g\in G:gHg^{-1}=H\}
\]
at $H$.
Hence the number $r$ of distinct conjugates of $H$ is
\[
r=[G:N_G(H)].
\]
Since $H\le N_G(H)$,
\[
r=[G:N_G(H)]\le [G:H].
\]
:::

<1>2. The union of those conjugates has strictly fewer than $|G|$ elements.
::: {.proof}
List the distinct conjugates as $H_1,\ldots,H_r$.
Each has $|H|$ elements, and every one contains the identity.
Therefore
\[
\left|\bigcup_{i=1}^r H_i\right|
\le 1+r(|H|-1).
\]
Put $m=[G:H]$.
Because $H$ is proper, $m>1$, and <1>1 gives $r\le m$.
Thus
\[
\left|\bigcup_{i=1}^r H_i\right|
\le 1+m(|H|-1)
=m|H|-(m-1)
=|G|-(m-1)
<|G|.
\]
Consequently the conjugates of $H$ cannot cover $G$.
:::
:::
