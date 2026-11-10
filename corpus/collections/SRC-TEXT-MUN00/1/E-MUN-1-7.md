---
schema: qual/card@1
id: E-MUN-1-7
kind: problem
title: Expressing sets using union, intersection, and difference
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 7; the stored statement matches.
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
    Read against Munkres, Topology (2000), §1 Exercise 7, printed p. 14; D, E and F are
    stored exactly as the book writes them, including the implication in F rather than a
    set difference.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.7,
    printed pp. 8-9 (tmp/sources/munkres-solutions-whitman.pdf). His answers are
    D = A meet (B union C), E = (A meet B) union C and F = A - (B - C); the chain of
    equivalences for F on the card is his, and so is the remark that D and E are not
    equal in general although they look alike. Added the equivalent form
    (A - B) union (A meet C) of F, which is the same set written without using the
    preceding difference.
---

::: {.exercise}

Given sets $A, B$, and $C$, express each of the following sets in terms of $A, B$, and $C$, using the symbols $\cup, \cap,$ and $-$.
$$
D = \{x \mid x \in A \text{ and } (x \in B \text{ or } x \in C) \},
$$
$$
E = \{x \mid (x \in A \text{ and } x \in B) \text{ or } x \in C \},
$$
$$
F = \{x \mid x \in A \text{ and } (x \in B \Rightarrow x \in C) \}.
$$
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.7, printed pp. 8--9** (`tmp/sources/munkres-solutions-whitman.pdf`); the two immediate translations and the chain of equivalences for $F$ below are his, as is the warning that $D$ and $E$ are not equal in general even though they look alike.

Directly translating the logical connectives gives
$$
D=A\cap(B\cup C)
$$
and
$$
E=(A\cap B)\cup C.
$$
For $F$, use
$$
(x\in B\Rightarrow x\in C)
\iff (x\notin B\text{ or }x\in C).
$$
Thus, among points of $A$, the only points excluded are those lying in $B-C$. Therefore
$$
\boxed{F=A-(B-C).}
$$
Equivalently,
$$
F=(A-B)\cup(A\cap C).
$$
:::
