---
schema: qual/card@1
id: E-Z13JH
kind: problem
title: Infinite sets are connected in the finite complement topology
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 4, printed p. 152, with the finite
    complement topology of Example 3 in §12; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.4, PDF p. 2. In a separation of an infinite set
    with the finite complement topology both sides would be infinite and both complements
    finite, which is impossible. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 3,
    Exercise 23.4, PDF p. 2). Checked against the book: §23 Exercise 4 as printed (p. 152)
    and the finite complement topology of §12 Example 3. The count is now a stated step:
    a nonempty open set has finite complement and is therefore infinite, which is what
    contradicts the finiteness of B as a subset of the complement of A. No repair to the
    printed statement.
---

::: {.exercise}

Show that if $X$ is an infinite set, it is connected in the finite complement topology.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.4, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps, with the cardinal count made explicit.

Throughout, $X$ is an infinite set carrying the finite complement topology, in which a set is open when it is empty or has finite complement (§12, Example 3), and a separation of $X$ is a pair of disjoint nonempty open sets whose union is $X$.

::: pf

::: {.pf-step #cardinal}
Every nonempty open $A\subset X$ is infinite, and $X-A$ is finite.

::: pf-proof
$A$ is open and nonempty, so by the definition of the finite complement topology $X-A$ is finite. Since $X=A\cup(X-A)$, the set $A$ is infinite. In particular $A\ne X$ and $X-A\ne\emptyset$.
:::

:::

::: {.pf-step}
$X$ is connected.

::: pf-proof
Suppose $X=A\cup B$ is a separation, so that $A$ and $B$ are disjoint, nonempty and open. By step [](#cardinal){.pf-ref} applied to $A$, the set $X-A$ is finite, and $B\subset X-A$ because $A$ and $B$ are disjoint, so $B$ is finite. But step [](#cardinal){.pf-ref} applied to $B$ says that $B$ is infinite. This contradiction shows that $X$ has no separation, hence is connected.
:::

:::

:::
:::
