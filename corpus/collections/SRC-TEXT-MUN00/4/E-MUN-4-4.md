---
schema: qual/card@1
id: E-MUN-4-4
kind: problem
title: Largest element of finite subsets of $\{1, \ldots, n\}$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 4, printed p. 34; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.4,
    printed p. 50 (tmp/sources/munkres-solutions-whitman.pdf). The induction is his: a
    nonempty subset of {1, ..., n+1} either contains n+1, which is then its largest
    element, or lies in {1, ..., n}. Part (b) is his remark that the induction is about
    one fixed initial segment and gives no bound for an arbitrary subset of Z_+, with
    Z_+ itself as the example of a subset with no largest element.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two parts, which is what Queue D asks for on this card. The induction is split into its base and its inductive step, each a substep with its own proof; (b) is the step that says why the finite-segment statement does not give the infinite one, with the unboundedness of the positive integers made explicit. Statement re-read against Munkres, Topology (2000), §4 Exercise 4, printed p. 34, and the argument against Dan Whitman's set, Exercise 4.4, printed p. 50. No statement repair.
---

::: {.exercise}

(a) Prove by induction that given $n \in \ZZ_+$, every nonempty subset of $\{1, \ldots, n\}$ has a largest element.

(b) Explain why you cannot conclude from (a) that every nonempty subset of $\ZZ_{+}$ has a largest element.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.4, printed p. 50** (`tmp/sources/munkres-solutions-whitman.pdf`); the induction and the answer to (b) are his. The statement is Munkres, *Topology*, 2nd ed. (2000), §4 Exercise 4.

::: pf

::: {.pf-step #part-a}
(a) For every $n\in\ZZ_+$, every nonempty subset of $\{1,\dots,n\}$ has a largest element.

::: pf-proof

::: {.pf-step #base}
The assertion holds for $n=1$.

::: pf-proof
The only nonempty subset of $\{1\}$ is $\{1\}$ itself, whose largest element is $1$.
:::

:::

::: {.pf-step #induction}
If the assertion holds for $n$, it holds for $n+1$.

::: pf-proof
Let $A\subseteq\{1,\dots,n+1\}$ be nonempty. If $n+1\in A$ then $n+1$ is the largest element of $A$, since every element of $A$ is at most $n+1$. If $n+1\notin A$ then $A\subseteq\{1,\dots,n\}$, so $A$ has a largest element by the inductive hypothesis. Either way $A$ has a largest element.
:::

:::

The base of step [](#base){.pf-ref} and the induction of step [](#induction){.pf-ref} establish the assertion for every $n\in\ZZ_+$ by the principle of induction, which is part (a).
:::

:::

::: {.pf-step #part-b}
(b) It does not follow that every nonempty subset of $\ZZ_+$ has a largest element: such a subset need not be contained in any one initial segment $\{1,\dots,n\}$, and $\ZZ_+$ itself has no largest element.

::: pf-proof
Part (a) is a statement about the subsets of a fixed finite set $\{1,\dots,n\}$ for a given $n$, so the induction produces one assertion per $n$ and never a statement about all subsets of $\ZZ_+$; a subset of $\ZZ_+$ that is not contained in any $\{1,\dots,n\}$ is outside the scope of every one of them, and an unbounded subset is exactly such a set. Concretely, if $m\in\ZZ_+$ then $m+1\in\ZZ_+$ and $m+1>m$, so no $m$ is the largest element of $\ZZ_+$.
:::

:::

:::
:::
