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
---

::: {.exercise}

Show that $X$ is countably compact if and only if every nested sequence $C_1 \supset C_2 \supset \cdots$ of closed nonempty sets of $X$ has a nonempty intersection.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.5, PDF p. 19** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both directions are theirs.

*If $X$ is countably compact, nested closed nonempty sets meet.* Let $C_{1}\supset C_{2}\supset\cdots$ be closed and nonempty and put $U_{n}=X-C_{n}$, open. No finite subcollection of $\{U_{n}\}$ covers $X$, since $U_{i_{1}}\cup\cdots\cup U_{i_{n}}=X-C_{i_{1}}\cap\cdots\cap C_{i_{n}}\ne X$. So the countable cover does not cover $X$ either, and a point outside $\bigcup U_{n}$ lies in $\bigcap C_{n}$.

*Conversely.* Let $\{U_{n}\}$ be a countable open cover and put $V_{n}=U_{1}\cup\cdots\cup U_{n}$, $C_{n}=X-V_{n}$, so that $C_{1}\supset C_{2}\supset\cdots$ are closed. If no finite subcollection covers $X$ then every $C_{n}\ne\varnothing$, so $\bigcap C_{n}\ne\varnothing$ by hypothesis; a point of the intersection lies in no $V_{n}$, contradicting that the $U_{n}$ cover $X$. Hence some finite subcollection covers $X$.
:::
