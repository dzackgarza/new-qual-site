---
schema: qual/card@1
id: P-RPSTO
kind: problem
title: Solvable groups have a nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Normal Subgroups
  - Commutators
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Show that if $G$ is solvable, then $G$ contains a nontrivial normal subroup.

  - What does this mean on the Galois theory side?

> Hint: consider the derived series.
:::

::: {.solution}
Taken literally, every nontrivial group $G$ contains a nontrivial normal subgroup, namely $G$ itself. The solvability hypothesis becomes meaningful if one asks for a **proper** nontrivial normal subgroup.

If $G$ is nonabelian and solvable, then
\[
1\ne [G,G]\ne G.
\]
Indeed, $[G,G]\ne1$ because $G$ is nonabelian, while $[G,G]\ne G$ because otherwise the derived series would be stationary at $G$ and could not reach $1$. Since $[G,G]$ is characteristic, it is normal. Thus every nonabelian solvable group has a proper nontrivial normal subgroup.

For abelian solvable groups this stronger assertion can fail: $C_p$ is simple. More generally, a nontrivial abelian group has a proper nontrivial subgroup unless it has prime order.

For a finite Galois extension $L/F$ with solvable Galois group $G$, a normal subgroup $H\trianglelefteq G$ corresponds to an intermediate field $L^H$ that is Galois over $F$. A proper nontrivial normal subgroup gives a proper nontrivial Galois intermediate field. The derived series gives the usual tower whose successive Galois groups are abelian.
:::
