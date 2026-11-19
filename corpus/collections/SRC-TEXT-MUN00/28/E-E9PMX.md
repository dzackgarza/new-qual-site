---
schema: qual/card@1
id: E-E9PMX
kind: problem
title: Nested closed sets in countably compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §28 Exercise 5, printed p. 181; the stored
    statement is the printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.5, PDF p. 19. The complements of a nested
    sequence of closed sets give a countable cover without a finite subcover, and conversely
    the partial unions give a nested sequence of closed sets. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the two-direction proof as a Lamport proof against the retained set: positron0802,
    Solutions to Topology, Chapter 3 (1 January 2021), Exercise 28.5, PDF p. 19, re-read in its
    text version (tmp/sources/positron-ch3.txt). Each direction is now a step with substeps. In
    the first the empty-finite-union point is proved rather than asserted: a finite union of the
    complements U_i is the complement of the intersection of the corresponding C_i, which is the
    smallest of them by nesting, hence not all of X. In the second the partial unions V_n give the
    nested closed sets C_n and the point of the intersection is shown to lie in no V_n, hence in
    no U_n, contradicting that the U_n cover. The statement is unchanged and both directions are
    proved, as the printed "if and only if" requires.
---

::: {.exercise}

Show that $X$ is countably compact if and only if every nested sequence $C_1 \supset C_2 \supset \cdots$ of closed nonempty sets of $X$ has a nonempty intersection.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.5, PDF p. 19** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both directions are theirs. Recall that $X$ is countably compact when every countable open cover of $X$ has a finite subcover.

::: pf

::: {.pf-step #nested-closed}
If $X$ is countably compact, then every nested sequence $C_{1}\supset C_{2}\supset\cdots$ of nonempty closed sets has $\bigcap_{n}C_{n}\ne\varnothing$.

::: pf-proof
Put $U_{n}=X-C_{n}$, which is open since $C_{n}$ is closed, and note first that no finite subcollection of $\{U_{n}\}$ covers $X$: for indices $i_{1},\dots,i_{k}$ the union $U_{i_{1}}\cup\cdots\cup U_{i_{k}}$ is the complement of $C_{i_{1}}\cap\cdots\cap C_{i_{k}}$, and that intersection is $C_{m}$ for $m=\max(i_{1},\dots,i_{k})$ because the sequence is nested, so the union is $X-C_{m}\ne X$ as $C_{m}\ne\varnothing$. Countable compactness applied to the countable open cover $\{U_{n}\}$ therefore gives the weaker statement that this cover has no finite subcover at all, hence does not cover $X$: there is $x\in X$ with $x\notin U_{n}$ for every $n$, that is $x\in C_{n}$ for every $n$.
:::

:::

::: {.pf-step #countably-compact}
Conversely, if every such nested sequence has nonempty intersection, then $X$ is countably compact.

::: pf-proof
Let $\{U_{n}\}$ be a countable open cover of $X$ and put $V_{n}=U_{1}\cup\cdots\cup U_{n}$ and $C_{n}=X-V_{n}$. Each $C_{n}$ is closed and $C_{1}\supset C_{2}\supset\cdots$. If no finite subcollection of $\{U_{n}\}$ covers $X$, then $V_{n}\ne X$ for every $n$, so every $C_{n}\ne\varnothing$, and the hypothesis gives $x\in\bigcap_{n}C_{n}$. Such an $x$ lies in no $V_{n}$, hence in no $U_{n}$, which contradicts that $\{U_{n}\}$ covers $X$. So some finite subcollection covers $X$.
:::

:::

::: {.pf-step #answer}
$X$ is countably compact if and only if every nested sequence of nonempty closed sets has nonempty intersection.

::: pf-proof
Step [](#nested-closed){.pf-ref} proves the implication from countable compactness to the intersection property, and step [](#countably-compact){.pf-ref} the converse, so the two conditions are equivalent.
:::

:::

:::
:::
