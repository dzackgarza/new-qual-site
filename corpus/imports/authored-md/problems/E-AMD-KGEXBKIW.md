---
schema: qual/card@1
id: E-AMD-KGEXBKIW
kind: exercise
title: Cyclic groups are solvable
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that every cyclic group is solvable.
:::

::: solution
**Goal:** Prove that every cyclic group $G$ is solvable.

<1>1. Cyclic groups are abelian:
    *Proof:*
    <2>1. Let $G = \langle g \rangle$. Then every element of $G$ is of the form $g^a$ for some integer $a$.
    <2>2. For any $g^a, g^b \in G$: $g^a g^b = g^{a+b} = g^{b+a} = g^b g^a$.
    <2>3. Thus $G$ is abelian.

<1>2. Abelian groups are solvable:
    *Proof:*
    <2>1. The derived subgroup of an abelian group is trivial: $[G, G] = \{e\}$.
    <2>2. The derived series is $G^{(0)} = G \supsetneq G^{(1)} = [G, G] = \{e\}$.
    <2>3. The derived series terminates at $\{e\}$ in one step, so $G$ is solvable.

<1>3. Conclusion:
    Every cyclic group is abelian, hence solvable. Q.E.D.
:::
