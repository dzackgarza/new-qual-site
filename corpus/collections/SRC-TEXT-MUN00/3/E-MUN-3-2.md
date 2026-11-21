---
schema: qual/card@1
id: E-MUN-3-2
kind: problem
title: The restriction of an equivalence relation is an equivalence relation
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 2, printed p. 28: for a relation
    C on A and A_0 a subset of A, the restriction of C to A_0 is C cap (A_0 x A_0), and
    the exercise asks that the restriction of an equivalence relation be an equivalence
    relation. The stored statement matches, including the definition of restriction.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.2,
    printed p. 19 (tmp/sources/munkres-solutions-whitman.pdf). His proof of the three
    properties is the one below, with the observation that C_0 is a relation on A_0
    because it lies in A_0 x A_0.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2, with the restriction, reflexivity,
    symmetry, transitivity and the conclusion as separate steps. Re-read against the
    retained solution at the cited page, Whitman Exercise 3.2 printed p. 19, and the
    argument and conclusion are unchanged. The printed book text was not re-read; the
    statement's source check on this card is the earlier event.
---

::: {.exercise}

Let $C$ be a relation on a set $A$. If $A_0 \subset A$, define the restriction of $C$ to $A_0$ to be the relation $C \cap (A_0 \times A_0)$. Show that the restriction of an equivalence relation is an equivalence relation.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.2, printed p. 19** (`tmp/sources/munkres-solutions-whitman.pdf`); the three verifications below are his, one per step, with the observation that $C_0$ is a relation on $A_0$ because it lies in $A_0\times A_0$.

Let $C$ be an equivalence relation on a set $A$ and let $A_0\subset A$, and put $C_0=C\cap(A_0\times A_0)$.

::: pf

::: {.pf-step #relation}
$C_0$ is a relation on $A_0$, and $C_0\subset C$.

::: pf-proof
$C_0\subset A_0\times A_0$, which is exactly what it means for $C_0$ to be a relation on $A_0$; and $C_0\subset C$ because $C_0$ is an intersection having $C$ as one of its members.
:::

:::

::: {.pf-step #reflexive}
For every $a\in A_0$ one has $aC_0a$.

::: pf-proof
Let $a\in A_0$. Then $a\in A$ because $A_0\subset A$, so $aCa$ by reflexivity of $C$ on $A$, and $(a,a)\in A_0\times A_0$ because both coordinates lie in $A_0$. Hence $(a,a)\in C\cap(A_0\times A_0)=C_0$, that is $aC_0a$.
:::

:::

::: {.pf-step #symmetric}
For all $a,b\in A_0$, $aC_0b$ implies $bC_0a$.

::: pf-proof
Let $a,b\in A_0$ with $aC_0b$. Then $aCb$ by step [](#relation){.pf-ref}, so $bCa$ by symmetry of $C$; and $(b,a)\in A_0\times A_0$ because both coordinates lie in $A_0$. Hence $(b,a)\in C\cap(A_0\times A_0)=C_0$.
:::

:::

::: {.pf-step #transitive}
For all $a,b,c\in A_0$, $aC_0b$ and $bC_0c$ together imply $aC_0c$.

::: pf-proof
Let $a,b,c\in A_0$ with $aC_0b$ and $bC_0c$. Then $aCb$ and $bCc$ by step [](#relation){.pf-ref}, so $aCc$ by transitivity of $C$; and $(a,c)\in A_0\times A_0$ because both coordinates lie in $A_0$. Hence $(a,c)\in C\cap(A_0\times A_0)=C_0$.
:::

:::

::: {.pf-step}
$C_0$ is an equivalence relation on $A_0$.

::: pf-proof
By step [](#relation){.pf-ref} $C_0$ is a relation on $A_0$, and it is reflexive, symmetric and transitive by steps [](#reflexive){.pf-ref}, [](#symmetric){.pf-ref} and [](#transitive){.pf-ref}. That is the definition of an equivalence relation on $A_0$, so the restriction of the equivalence relation $C$ to $A_0$ is again an equivalence relation.
:::

:::

:::
:::
