---
schema: qual/card@1
id: E-MUN-1-8
kind: problem
title: Power set of a finite set
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 8; the stored statement matches.
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
    Read against Munkres, Topology (2000), §1 Exercise 8, printed p. 14; the four
    questions are stored as printed, including the last one asking why P(A) is called
    the power set.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.8,
    printed pp. 8-9 (tmp/sources/munkres-solutions-whitman.pdf). Supplied the counting
    step it had asserted: the card previously said only that each element is included or
    omitted, which is not a proof for a set of n elements. It now carries Whitman's
    induction on the size of A, splitting the subsets of A according as they omit or
    contain a chosen x, which is what makes |P(A)| = 2|P(A - {x})| and hence 2^n.
---

::: {.exercise}

If a set $A$ has two elements, show that $\mathcal{P}(A)$ has four elements.
How many elements does $\mathcal{P}(A)$ have if $A$ has one element?
Three elements?
No elements?
Why is $\mathcal{P}(A)$ called the power set of $A$ ?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.8, printed pp. 8--9** (`tmp/sources/munkres-solutions-whitman.pdf`); the two-element count, the induction and the reading of the name below are his.

If $A=\{a,b\}$, then its subsets are exactly
$$
\varnothing,\qquad \{a\},\qquad \{b\},\qquad \{a,b\},
$$
so $\cardinality{\mathcal P(A)}=4$.

In general, a finite set $A$ with $n$ elements has exactly $2^n$ subsets. This is proved by induction on $n$. For $n=0$ the only subset of $\varnothing$ is $\varnothing$, so $\mathcal P(\varnothing)=\{\varnothing\}$ has the single element $2^0=1$. Now suppose the claim known for $n$, let $A$ have $n+1$ elements, and choose $x\in A$. A subset $B\subset A$ either omits $x$, in which case $B\subset A-\{x}$, or contains $x$, in which case $B=\{x\}\cup C$ with $C\subset A-\{x\}$. The two classes are disjoint and each is in bijection with $\mathcal P(A-\{x\})$, a set of $2^n$ elements by the inductive hypothesis. Hence
$$
\cardinality{\mathcal P(A)}=2\cdot 2^n=2^{n+1}.
$$
Therefore:
$$
\begin{array}{c|c}
\cardinality{A}&\cardinality{\mathcal P(A)}\\ \hline
0&1\\
1&2\\
2&4\\
3&8
\end{array}
$$
The name *power set* refers to this formula: its cardinality is the power $2^{\cardinality{A}}$ when $A$ is finite.
:::
