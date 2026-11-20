---
schema: qual/card@1
id: E-MUN-6-4
kind: problem
title: Finite simply ordered sets have a largest element
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 4; the stored statement matches.
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
    Read against Munkres, Topology (2000), §6 Exercise 4, printed p. 44; both parts are
    stored as printed, including the hint to induct on the cardinality.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.4,
    printed pp. 76-78 (tmp/sources/munkres-solutions-whitman.pdf), both inductions on the
    cardinality: removing one element, applying the hypothesis, and comparing that
    element with the largest element of the rest. The card's (b) extends the order
    isomorphism of A' by the largest element, which is his construction. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two inductions, which is what Queue D asks for on this card. Each part is a step proved by its base and its inductive step, and two places the prose ran together are now written out: the trichotomy that decides between a < m and m < a in part (a), and the verification that the extension sending the largest element to n+1 still preserves order in part (b). Statement re-read against Munkres, Topology (2000), §6 Exercise 4, printed p. 44, and the argument against Dan Whitman's set, Exercise 6.4, printed pp. 76-78. No statement repair.
---

::: {.exercise}

Let $A$ be a nonempty finite simply ordered set.

(a) Show that $A$ has a largest element.
[Hint: Proceed by induction on the cardinality of $A$ .]

(b) Show that $A$ has the order type of a section of the positive integers.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.4, printed pp. 76--78** (`tmp/sources/munkres-solutions-whitman.pdf`); both inductions on $\cardinality{A}$ are his, as is the extension of the order isomorphism of $A-\{M\}$ by the largest element. The statement is Munkres, *Topology*, 2nd ed. (2000), §6 Exercise 4.

::: pf

::: {.pf-step #part-a}
(a) A nonempty finite simply ordered set $A$ has a largest element.

::: pf-proof

::: {.pf-step #a-base}
The assertion holds when $\cardinality{A}=1$.

::: pf-proof
The unique element $a$ of $A$ satisfies $a\le a$, so it is an element of $A$ that every element of $A$ is at most; that is the definition of a largest element.
:::

:::

::: {.pf-step #a-step}
If every nonempty simply ordered set of cardinality $n$ has a largest element, then so does every such set of cardinality $n+1$.

::: pf-proof
Let $\cardinality{A}=n+1$ and choose $a\in A$. Then $A-\{a\}$ has cardinality $n$ and is nonempty, so by the inductive hypothesis it has a largest element $m$. Since the order on $A$ is simple, exactly one of $a<m$, $a=m$, $m<a$ holds, and $a\ne m$; if $a<m$ then $m$ is the largest element of $A$, because every element of $A-\{a\}$ is at most $m$ and $a<m$, and if $m<a$ then $a$ is the largest element of $A$.
:::

:::

The base of step [](#a-base){.pf-ref} and the induction of step [](#a-step){.pf-ref} give the assertion for every $n\ge1$ by induction on $\cardinality{A}$, which is part (a).
:::

:::

::: {.pf-step #part-b}
(b) $A$ has the order type of a section of the positive integers.

::: pf-proof

::: {.pf-step #b-base}
$A$ is order-isomorphic to $\{1\}$ when $\cardinality{A}=1$.

::: pf-proof
The map sending the unique element of $A$ to $1$ is a bijection, and it preserves order because $\{1\}$ has no two distinct elements to compare.
:::

:::

::: {.pf-step #b-step}
If every nonempty simply ordered set of cardinality $n$ has the order type of $\{1,\dots,n\}$, then every such set of cardinality $n+1$ has the order type of $\{1,\dots,n+1\}$.

::: pf-proof
Let $\cardinality{A}=n+1$. By step [](#part-a){.pf-ref}, $A$ has a largest element $M$; then $A'=A-\{M\}$ has cardinality $n$ and is nonempty, so by the inductive hypothesis there is an order-preserving bijection $\phi:A'\to\{1,\dots,n\}$. Extend it by $\Phi(M)=n+1$ and $\Phi\restrictionof{A'}=\phi$. Then $\Phi$ is a bijection $A\to\{1,\dots,n+1\}$, since $M\notin A'$ and $n+1\notin\{1,\dots,n\}$; and it preserves order: for $a,a'\in A'$ this is the order preservation of $\phi$, for $a\in A'$ and $a'=M$ it is $a<M$ together with $\phi(a)\le n<n+1$, and there is no element above $M$.
:::

:::

The base of step [](#b-base){.pf-ref} and the induction of step [](#b-step){.pf-ref} give the assertion for every $n\ge1$; a section of the positive integers is a set $\{1,\dots,n\}$, so $A$ has the order type of one. This is part (b).
:::

:::

:::
:::
