---
schema: qual/card@1
id: E-AMD-2SZMALTL
kind: problem
title: Finite $p$-groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Nilpotent Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that every finite $p$-group is nilpotent.
:::

::: {.solution}
Let \(G\) be a finite \(p\)-group. We prove by induction on \(|G|\) that its upper central series reaches \(G\).

<1>1. Every nontrivial finite \(p\)-group has nontrivial center.
::: {.proof}
The class equation is
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)],
\]
where the sum runs over representatives of noncentral conjugacy classes. Each index in the sum is a nontrivial power of \(p\), hence divisible by \(p\). Since \(|G|\) is divisible by \(p\), so is \(|Z(G)|\). Thus \(|Z(G)|\ge p\).
:::

<1>2. The quotient \(G/Z(G)\) is a strictly smaller finite \(p\)-group.
::: {.proof}
By <1>1, \(|Z(G)|\ge p\), so
\[
|G/Z(G)|=|G|/|Z(G)|<|G|.
\]
:::

<1>3. The upper central series of \(G\) reaches \(G\).
::: {.proof}
Induct on \(|G|\). The trivial group is nilpotent. For nontrivial \(G\), the quotient \(G/Z(G)\) is nilpotent by induction. If its upper central series reaches \(G/Z(G)\) in \(c\) steps, then by the definition
\[
Z_{i+1}(G)/Z(G)=Z_i(G/Z(G))
\]
for the corresponding shifted series, so \(Z_{c+1}(G)=G\). Hence \(G\) is nilpotent.
:::

Therefore every finite \(p\)-group is nilpotent.
:::
