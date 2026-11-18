---
schema: qual/card@1
id: E-MUN-4-9
kind: problem
title: Archimedean property and density of $\QQ$ in $\RR$
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 9; the stored statement matches.
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
    Read against Munkres, Topology (2000), §4 Exercise 9, printed p. 35; the four parts
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.9,
    printed pp. 60-62 (tmp/sources/munkres-solutions-whitman.pdf). Both arguments reduce
    (a) to the well-ordering of Z_+; the card shifts A by the Archimedean property
    instead of by a chosen element as he does, then gets (b) from (a), (c) from (b), and
    (d) by scaling x - y above 1 and applying (c). Uniqueness in (b) is his: two such
    integers differ by an integer strictly between 0 and 1, which he shows impossible.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Munkres, *Topology* (2000), §4 Exercise 9, printed p. 35, the four parts matching the printed text. The argument is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.9, printed pp. 60--62. Added: the nonemptiness and boundedness of $\{m\in\ZZ: m<x\}$ used in (b) are now justified by the Archimedean property rather than asserted, and the uniqueness in (b) is its own step.
---

::: {.exercise}

(a) Show that every nonempty subset of $\ZZ$ that is bounded above has a largest element.

(b) If $x \notin \ZZ$, show there is exactly one $n \in \ZZ$ such that $n < x < n + 1$ .

(c) If $x - y > 1$, show there is at least one $n \in \ZZ$ such that $y < n < x$ .

(d) If $y < x$, show there is a rational number $z$ such that $y < z < x$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.9, printed pp. 60--62** (`tmp/sources/munkres-solutions-whitman.pdf`); (a) is his reduction of a set of integers bounded above to the well-ordering of $\ZZ_+$, and (b)--(d) are built from it in the order the book asks. The statement is Munkres, *Topology* (2000), §4 Exercise 9, printed p. 35.

::: pf

::: {.pf-step #a}
(a) Every nonempty subset $A\subset\ZZ$ bounded above has a largest element.

::: pf-proof
Choose $N\in\ZZ_+$ with $N>a$ for every $a\in A$, possible by the Archimedean property. Then $B\coloneqq\{N-a\st a\in A\}$ is a nonempty subset of $\ZZ_+$, so by well-ordering it has a smallest element $b_0=N-a_0$. For every $a\in A$ we have $N-a_0\le N-a$, hence $a\le a_0$, so $a_0$ is the largest element of $A$.
:::
:::

::: {.pf-step #b-exists}
(b) If $x\notin\ZZ$ there is $n\in\ZZ$ with $n<x<n+1$.

::: pf-proof
The set $A\coloneqq\{m\in\ZZ\st m<x\}$ is nonempty by the Archimedean property and is bounded above by $x$, so by part [](#a){.pf-ref} it has a largest element $n$. Then $n<x$. If $x\ge n+1$, then $n+1\le x$; equality would make $x$ an integer, contrary to the hypothesis, and strict inequality would put the integer $n+1$ into $A$, contradicting the maximality of $n$. Hence $n<x<n+1$.
:::
:::

::: {.pf-step #b-unique}
In (b) the integer $n$ is unique.

::: pf-proof
Let $m,n\in\ZZ$ both satisfy $m<x<m+1$ and $n<x<n+1$ and suppose $m<n$. Then $m+1\le n<x$, contradicting $x<m+1$. So $m=n$, and by symmetry no two distinct integers qualify.
:::
:::

::: {.pf-step #c}
(c) If $x-y>1$ there is $n\in\ZZ$ with $y<n<x$.

::: pf-proof
If $y\in\ZZ$, take $n=y+1$: then $y<n=y+1<x$. If $y\notin\ZZ$, step [](#b-exists){.pf-ref} gives $m$ with $m<y<m+1$, and taking $n=m+1$ gives $y<n=m+1<y+1<x$.
:::
:::

::: {.pf-step #d}
(d) If $y<x$ there is $z\in\QQ$ with $y<z<x$.

::: pf-proof
The difference $x-y$ is positive, so by the Archimedean property there is $n\in\ZZ_+$ with $n(x-y)>1$. Then $nx-ny>1$, so step [](#c){.pf-ref} gives an integer $m$ with $ny<m<nx$. Dividing by the positive integer $n$ gives $y<\tfrac mn<x$, and $\tfrac mn\in\QQ$.
:::
:::

::: {.pf-step}
All four assertions of the exercise hold.

::: pf-proof
Steps [](#a){.pf-ref}, [](#b-exists){.pf-ref} with [](#b-unique){.pf-ref}, [](#c){.pf-ref} and [](#d){.pf-ref} prove the four parts in the order asked.
:::
:::

:::
:::
