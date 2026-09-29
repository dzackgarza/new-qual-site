---
schema: qual/card@1
id: E-AMD-TM3LMADH
kind: problem
title: Nontrivial normal subgroups of a finite $p$-group meet the center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.exercise}
Show that in a finite $p\dash$group, every nontrivial normal subgroup intersects the center nontrivially.
:::

::: {.solution}
Let \(G\) be a finite \(p\)-group and let \(1\neq N\trianglelefteq G\).

::: pf

::: pf-step
The group \(G\) acts on the finite set \(N\) by conjugation.

::: pf-proof
For \(g\in G\) and \(x\in N\), define \(g\cdot x=gxg^{-1}\). Because \(N\trianglelefteq G\), one has \(gxg^{-1}\in N\), so this is a well-defined action on \(N\).
:::

:::

::: {.pf-step #fixed-points-eq-n-cap-z}
The fixed-point set for this action is exactly \(N\cap Z(G)\).

::: pf-proof
An element \(x\in N\) is fixed by every \(g\in G\) precisely when
\[
gxg^{-1}=x\qquad\text{for all }g\in G,
\]
which is equivalent to \(x\in Z(G)\). Since already \(x\in N\), the fixed points are exactly \(N\cap Z(G)\).
:::

:::

::: {.pf-step #nonfixed-orbits-div-by-p}
Every non-fixed orbit has cardinality divisible by \(p\).

::: pf-proof
For \(x\in N\), orbit-stabilizer gives
\[
|G\cdot x|=[G:C_G(x)].
\]
Since \(G\) is a finite \(p\)-group, every subgroup index is a power of \(p\). If \(x\) is not fixed, then \(C_G(x)\neq G\), so \([G:C_G(x)]\) is a positive power of \(p\), hence divisible by \(p\).
:::

:::

::: {.pf-step #congruence-mod-p}
Therefore
\[
|N|\equiv |N\cap Z(G)|\pmod p.
\]

::: pf-proof
Partition \(N\) into its \(G\)-orbits.
By step [](#fixed-points-eq-n-cap-z){.pf-ref}, the fixed points contribute \(|N\cap Z(G)|\) singleton orbits.
By step [](#nonfixed-orbits-div-by-p){.pf-ref}, every remaining orbit has size divisible by \(p\). Summing the orbit sizes gives the congruence.
:::

:::

::: {.pf-step #n-cap-z-div-by-p}
The integer \(|N\cap Z(G)|\) is divisible by \(p\).

::: pf-proof
Because \(N\) is a nontrivial subgroup of the finite \(p\)-group \(G\), its order is \(p^a\) for some \(a\ge1\); hence \(p\mid |N|\). Apply step [](#congruence-mod-p){.pf-ref}.
:::

:::

::: pf-step
Hence \(N\cap Z(G)\neq1\).

::: pf-proof
The subgroup \(N\cap Z(G)\) contains the identity, so its cardinality is positive.
By step [](#n-cap-z-div-by-p){.pf-ref} it is divisible by the prime \(p\), hence it has at least \(p>1\) elements.
Therefore it contains a nonidentity element.
:::

:::

:::

:::
