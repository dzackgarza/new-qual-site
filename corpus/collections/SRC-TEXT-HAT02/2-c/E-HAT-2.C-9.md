---
schema: qual/card@1
id: E-HAT-2.C-9
kind: problem
title: Countably many homotopy types of finite CW complexes
classification:
  areas:
  - topology
  topics:
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
---

::: {.problem}
Show that there are only countably many homotopy types of finite CW complexes.
:::

::: {.solution}
Hatcher's Theorem 2C.5 says that every finite CW complex is homotopy equivalent to a finite simplicial complex. It therefore suffices to count finite simplicial complexes up to isomorphism.

<1>1. For each positive integer $N$, there are only finitely many simplicial complexes with vertex set exactly
\[
\{1,\ldots,N\}.
\]
::: {.proof}
Such a simplicial complex is a collection of nonempty subsets of $\{1,\ldots,N\}$ closed under passage to nonempty subsets. There are only finitely many subsets of the finite power set, so only finitely many possible complexes.
:::

<1>2. Hence there are only countably many isomorphism classes of finite simplicial complexes.
::: {.proof}
Every finite simplicial complex has some finite number $N$ of vertices and, after labeling the vertices, appears among the finite collection in <1>1. Take the union over $N\in\mathbb N$.
:::

<1>3. Consequently there are only countably many homotopy types of finite CW complexes.
::: {.proof}
Every finite CW complex has, by Theorem 2C.5, the homotopy type of one of the countably many finite simplicial complexes in <1>2. Passing from isomorphism classes to homotopy types can only identify elements, not create new ones.
:::

Thus
\[
\boxed{\text{the set of homotopy types of finite CW complexes is countable}.}
\]
:::
