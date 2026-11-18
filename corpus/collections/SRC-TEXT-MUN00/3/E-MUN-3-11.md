---
schema: qual/card@1
id: E-MUN-3-11
kind: problem
title: Uniqueness of the immediate predecessor, the immediate successor and the extreme elements
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 11, printed p. 29. The card uses
    the book's definitions: the open interval (a,b) is {x : a < x < b}, and a is the
    immediate predecessor of b, b the immediate successor of a, when that interval is
    empty.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.11,
    printed p. 31 (tmp/sources/munkres-solutions-whitman.pdf). His argument for the
    successor - two candidates are comparable, and the smaller lies in the open interval
    above the larger - is the one below, and the smallest and largest elements follow from
    the same comparison. The card also states the equivalence a < b iff not b <= a that
    he proves first.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 3.11, printed p. 31); statement unchanged. The equivalence a < b iff not b <= a, which he proves first and which (c) and (d) use, is step 1 and is cited from those steps. Page added: the order axioms and comparability are on printed p. 24, the exercise on printed p. 28. No mathematical repair was needed.

---

::: {.exercise}

Show that an element in an ordered set has at most one immediate successor and at most one immediate predecessor. Show that a subset of an ordered set has at most one smallest element and at most one largest element.

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.11, printed p. 31** (`tmp/sources/munkres-solutions-whitman.pdf`); the arguments below are his, including the equivalence of step 1, which he proves first and uses in (c) and (d).

Throughout $(A,<)$ is an ordered set, $b$ is an immediate successor of $a$ when $a<b$ and the open interval $(a,b)$ is empty, and the order is total and satisfies comparability: for distinct $a,b\in A$ exactly one of $a<b$, $b<a$ holds (§3, printed p. 24).

::: pf

::: {.pf-step #equivalence}
For $a,b\in A$, $a<b$ if and only if not $b\le a$.

::: pf-proof
If $a<b$ and $b\le a$, then either $b=a$, giving $a<a$, or $b<a$, giving $a<a$ by transitivity; both contradict nonreflexivity. Conversely if not $b\le a$ then $a\neq b$, since $b\le b$ always; so by comparability $a<b$ or $b<a$, and $b<a$ would give $b\le a$, which is excluded. Hence $a<b$.

:::

:::

::: {.pf-step #successor}
At most one element of $A$ is an immediate successor of a given $a\in A$.

::: pf-proof
Let $b_1\neq b_2$ both be immediate successors of $a$, so $a<b_1$, $a<b_2$ and both $(a,b_1)$ and $(a,b_2)$ are empty. The two are comparable; say $b_1<b_2$. Then $a<b_1<b_2$, so $b_1\in(a,b_2)$, contradicting the emptiness of $(a,b_2)$. The case $b_2<b_1$ is the same with the indices exchanged. Hence $b_1=b_2$.

:::

:::

::: {.pf-step #predecessor}
At most one element of $A$ is an immediate predecessor of a given $b\in A$.

::: pf-proof
This is step [](#successor){.pf-ref} with the order reversed. Explicitly, let $a_1\neq a_2$ both be immediate predecessors of $b$, so $a_1<b$, $a_2<b$ and $(a_1,b)$, $(a_2,b)$ are empty. They are comparable; say $a_1<a_2$. Then $a_1<a_2<b$, so $a_2\in(a_1,b)$, contradicting the emptiness of $(a_1,b)$.

:::

:::

::: {.pf-step #smallest}
A subset $A_0\subset A$ has at most one smallest element.

::: pf-proof
Let $a_1,a_2\in A_0$ both be smallest elements of $A_0$, and suppose $a_1\neq a_2$. They are comparable; say $a_1<a_2$. Then not $a_2\le a_1$ by step [](#equivalence){.pf-ref}, although $a_1\in A_0$ and $a_2$ is a smallest element of $A_0$, which requires $a_2\le a_1$. This is a contradiction, so $a_1=a_2$.

:::

:::

::: {.pf-step #largest}
A subset $A_0\subset A$ has at most one largest element.

::: pf-proof
Step [](#smallest){.pf-ref} with the order reversed: if $a_1,a_2\in A_0$ are both largest and $a_1<a_2$, then $a_1\in A_0$ forces $a_2\le a_1$, contradicting $a_1<a_2$ by step [](#equivalence){.pf-ref}.

:::

:::

:::

:::
