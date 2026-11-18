---
schema: qual/card@1
id: E-MUN-9-6
kind: problem
title: Paradoxes of the set of all sets
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 6; the stored statement matches.
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
    Read against Munkres, Topology (2000), §9 Exercise 6, printed p. 61; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.6, printed pp. 105-106 (tmp/sources/munkres-solutions-whitman.pdf). Part (a) is his: every subset of the supposed set of all sets is a set, hence an element of it, so the power set injects into it, which Cantor forbids. Part (b) is his Russell set. Added one sentence to (a): the diagonal set D = {a : a not in psi(a)} shows directly that no map psi : A -> P(A) is surjective, which is the form of Cantor's theorem being used.
---

::: {.exercise}

Most of the famous paradoxes of naive set theory are associated in some way or other with the concept of the "set of all sets."
None of the rules we have given for forming sets allows us to consider such a set.
And for good reason—the concept itself is self-contradictory.
For suppose that $\mathcal{A}$ denotes the "set of all sets."

(a) Show that $\mathcal{P}(\mathcal{A}) \subset \mathcal{A}$; derive a contradiction.

(b) (Russell's paradox.)
Let $\mathcal{B}$ be the subset of $\mathcal{A}$ consisting of all sets that are not elements of themselves;
$$
\mathcal{B} = \{A \mid A \in \mathcal{A} \text{ and } A \notin A \}.
$$
(Of course, there may be no set $A$ such that $A \in A$; if such is the case, then $\mathcal{B} = \mathcal{A}$.) Is $\mathcal{B}$ an element of itself or not?
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.6, printed pp. 105--106** (`tmp/sources/munkres-solutions-whitman.pdf`); the two contradictions below are his, with the diagonal set stated explicitly in (a).

::: pf

::: {.pf-step #cantor}

No map $\psi:A\to\mathcal{P}(A)$ is surjective.

::: pf-proof

Given $\psi$, put $D=\{a\in A:a\notin\psi(a)\}$, a subset of $A$. For any $a\in A$, the equivalence $a\in D\iff a\notin\psi(a)$ shows $a\in D$ exactly when $a\notin\psi(a)$, so $D\ne\psi(a)$; thus $D$ is an element of $\mathcal{P}(A)$ that is not a value of $\psi$, and $\psi$ is not surjective. This is Cantor's diagonal argument.

:::

:::

::: {.pf-step #power}

(a) If $\mathcal{A}$ were the set of all sets, then $\mathcal{P}(\mathcal{A})\subset\mathcal{A}$, which is impossible.

::: pf-proof

Every subset of $\mathcal{A}$ is a set, and $\mathcal{A}$ contains every set, so each element of $\mathcal{P}(\mathcal{A})$ is an element of $\mathcal{A}$; that is the inclusion. The inclusion map $\mathcal{P}(\mathcal{A})\to\mathcal{A}$ is then an injection, and an injection $j:\mathcal{P}(\mathcal{A})\to\mathcal{A}$ would have a left inverse $r:\mathcal{A}\to\mathcal{P}(\mathcal{A})$ with $r\circ j=\mathrm{id}$, which is surjective, contradicting step [](#cantor){.pf-ref} applied to $A=\mathcal{A}$. Hence
$$
\boxed{\mathcal{P}(\mathcal{A})\subset\mathcal{A}\ \text{is contradictory: no set of all sets exists.}}
$$

:::

:::

::: {.pf-step #russell}

(b) With $\mathcal{B}=\{A\in\mathcal{A}:A\notin A\}$, both $\mathcal{B}\in\mathcal{B}$ and $\mathcal{B}\notin\mathcal{B}$ lead to contradiction.

::: pf-proof

Under the supposition that $\mathcal{A}$ is the set of all sets, $\mathcal{B}$ is a set, hence $\mathcal{B}\in\mathcal{A}$, so the defining condition applies to $A=\mathcal{B}$:
$$
\mathcal{B}\in\mathcal{B}\iff \mathcal{B}\in\mathcal{A}\ \text{and}\ \mathcal{B}\notin\mathcal{B}\iff\mathcal{B}\notin\mathcal{B}.
$$
If $\mathcal{B}\in\mathcal{B}$ then the equivalence gives $\mathcal{B}\notin\mathcal{B}$; if $\mathcal{B}\notin\mathcal{B}$ then, $\mathcal{B}$ being in $\mathcal{A}$, the equivalence gives $\mathcal{B}\in\mathcal{B}$. Either alternative is self-contradictory, which again shows that the supposed set of all sets cannot exist.

:::

:::

:::

:::
