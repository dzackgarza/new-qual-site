---
schema: qual/card@1
id: E-AMD-IBDKWV2J
kind: exercise
title: Abelian groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Nilpotent Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that every abelian group is nilpotent.
:::

::: solution
**Goal:** Prove that every abelian group $G$ is a nilpotent group of nilpotency class at most $1$.

<1>1. Lower central series verification:
    *Proof:*
    <2>1. By definition, a group $G$ is nilpotent if its lower central series:
        $$G_0 = G, \quad G_{k+1} = [G, G_k]$$
        terminates in the trivial subgroup $\{e\}$ in finitely many steps.
    <2>2. For any $x, y \in G$, the commutator is $[x, y] = x y x^{-1} y^{-1}$.
    <2>3. Because $G$ is abelian, $x y = y x$, so:
        $$[x, y] = x x^{-1} y y^{-1} = e.$$
    <2>4. Thus $G_1 = [G, G] = \{e\}$.
    <2>5. The lower central series terminates at $k = 1$ (or $k = 0$ if $G = \{e\}$).

<1>2. Upper central series verification (equivalent characterization):
    *Proof:*
    <2>1. The upper central series is defined by $Z_0(G) = \{e\}$ and $Z_{k+1}(G) / Z_k(G) = Z(G / Z_k(G))$.
    <2>2. Since $G$ is abelian, its center is the entire group: $Z_1(G) = Z(G) = G$.
    <2>3. The upper central series reaches $G$ at step $1$.

<1>3. Conclusion:
    Every abelian group is nilpotent. Q.E.D.
:::
