---
schema: qual/card@1
id: E-LRAPM
kind: problem
title: Compact closed intervals imply the least upper bound property
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 1, printed p. 177, with Theorem 27.4
    and Theorem 26.2; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.1, PDF pp. 15-16. The closure of a bounded set
    is compact, the identity attains a maximum there, and that maximum is the least upper
    bound. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Prove that if $X$ is an ordered set in which every closed interval is compact, then $X$ has the least upper bound property.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.1, PDF pp. 15--16** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $X$ be an ordered set in which every closed interval is compact, and let $A\subset X$ be nonempty and bounded above. Then $\overline A$ is closed, and it is contained in the closed interval $[\inf,\sup]$ spanned by $A$ and an upper bound, hence compact (closed in a compact space). Applying Theorem 27.4 (the extreme value theorem) to the inclusion $\overline A\to X$, the function $x\mapsto x$ attains a maximum at some $b\in\overline A$: $a\le b$ for all $a\in A$.

We show $b$ is the least upper bound of $A$. Suppose $c<b$ and $a\le c$ for all $a\in A$. Then $c\in\overline A$: if a neighbourhood $(c-\varepsilon,c+\varepsilon)$ missed $A$, then $(b-c-\varepsilon,b+\varepsilon)$ would be a neighbourhood of $b$ missing $A$, contrary to $b\in\overline A$. Since $b$ is an upper bound of $\overline A$, $c\le b$, contradicting $c<b$. So $b$ is the least upper bound of $A$.
:::
