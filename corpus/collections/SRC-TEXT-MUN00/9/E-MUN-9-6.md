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

(a) Suppose $\mathcal A$ were the set of all sets. Every subset of $\mathcal A$ is itself a set, hence by the defining property of $\mathcal A$ it is an element of $\mathcal A$. Therefore
$$
\mathcal P(\mathcal A)\subset\mathcal A.
$$
The inclusion map would be an injection
$$
\mathcal P(\mathcal A)\hookrightarrow\mathcal A,
$$
contradicting Cantor's theorem, which says there is no injection from the power set of a set into the set itself. That theorem in the form used here is the diagonal argument: for any map $\psi:A\to\mathcal P(A)$ the set $D=\{a\in A:a\notin\psi(a)\}$ satisfies $D\ne\psi(a)$ for every $a$, since $a\in D$ exactly when $a\notin\psi(a)$; so no such $\psi$ is surjective, and an injection $\mathcal P(\mathcal A)\hookrightarrow\mathcal A$ would have a surjective left inverse $\mathcal A\to\mathcal P(\mathcal A)$. Hence a set of all sets cannot exist.

(b) Define
$$
\mathcal B=\{A\in\mathcal A:A\notin A\}.
$$
Since $\mathcal A$ is assumed to contain every set, $\mathcal B\in\mathcal A$. Ask whether $\mathcal B\in\mathcal B$. By definition,
$$
\mathcal B\in\mathcal B
\iff
\mathcal B\notin\mathcal B,
$$
a contradiction in either case. This is Russell's paradox and independently shows that the supposed set $\mathcal A$ cannot exist.
:::
