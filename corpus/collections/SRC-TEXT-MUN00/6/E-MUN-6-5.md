---
schema: qual/card@1
id: E-MUN-6-5
kind: problem
title: Finiteness of Cartesian products
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §6 Exercise 5, printed p. 44; the question is
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.5,
    printed p. 78 (tmp/sources/munkres-solutions-whitman.pdf). His answer is the card's:
    with one factor empty the product is empty while the other factor may be infinite,
    and with both factors nonempty the injections a -> (a, b_0) and b -> (a_0, b) into
    the finite product make each factor finite. No defect found.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 6.5, printed p. 78); statement and answer unchanged. The two halves are separated because only the second uses both factors nonempty: the counterexample step needs B empty, and the injection step needs b_0 and a_0 to exist. Pages added and checked against the retained PDF: the definition of finite is on printed p. 39, Corollary 6.6 (a subset of a finite set is finite) on printed p. 43, ordered pairs on printed p. 11, and the exercise on printed p. 44.

---

::: {.exercise}
If $A \times B$ is finite, does it follow that $A$ and $B$ are finite?

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.5, printed p. 78** (`tmp/sources/munkres-solutions-whitman.pdf`); the counterexample with an empty factor and the argument for nonempty factors, with the two injections into the product, are his.

Throughout, a set is finite when it is empty or in bijection with a section $\{1,\dots,n\}$ of $\ZZ_+$ (definition, printed p. 39), and a subset of a finite set is finite (Corollary 6.6, printed p. 43); the exercise is on printed p. 44.

::: pf

::: {.pf-step #counterexample}
The answer to the question as asked is no: $A\times B$ can be finite with $A$ infinite.

::: pf-proof
Take $A=\ZZ_+$ and $B=\varnothing$. Then $A\times B=\varnothing$ because there is no pair with second coordinate in $B$, and $\varnothing$ is finite, being in bijection with the section $\{1,\dots,0\}$. The set $A=\ZZ_+$ is infinite, since it is not in bijection with any of its sections, as $\ZZ_+$ is not finite (printed p. 39).

:::

:::

::: {.pf-step #nonempty}
If $A\times B$ is finite and both $A$ and $B$ are nonempty, then $A$ and $B$ are finite.

::: pf-proof

::: {.pf-step #injections}
For $b_0\in B$ and $a_0\in A$ the maps $a\mapsto(a,b_0)$ and $b\mapsto(a_0,b)$ are injective, with images in $A\times B$.

::: pf-proof
$(a,b_0)=(a',b_0)$ gives $a=a'$, and $(a_0,b)=(a_0,b')$ gives $b=b'$; equal ordered pairs have equal coordinates (§1, printed p. 11).

:::

:::

::: {.pf-step #subsets}
$A$ and $B$ are each in bijection with a subset of the finite set $A\times B$, hence are finite.

::: pf-proof
The first injection of step [](#injections){.pf-ref} identifies $A$ with its image, a subset of $A\times B$, and a subset of a finite set is finite (Corollary 6.6, printed p. 43); the same holds for $B$ with the second injection.

:::

:::

:::

:::

:::

:::
