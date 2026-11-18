---
schema: qual/card@1
id: E-MUN-6-1
kind: problem
title: Injective maps between finite sets of different sizes
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 1; the stored statement matches.
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
    Read against Munkres, Topology (2000), §6 Exercise 1, printed p. 44; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.1,
    printed p. 75 (tmp/sources/munkres-solutions-whitman.pdf). He counts the injections
    from {1,...,m} to {1,...,n} as n!/(n-m)! by induction and then lists all 24 of the
    case at hand; the card lists the same 24 triples and counts them as 4*3*2, and gives
    10!/2! = 1814400 for part (b) as he does. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §6 Exercise 1, printed pp. 44--45, and the count $n!/(n-m)!$ and the list of the twenty-four triples are transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.1, printed p. 75. The list was rechecked to contain all $4\cdot3\cdot2$ triples with distinct entries and no repetitions.
---

::: {.exercise}

(a) Make a list of all the injective maps

$$
f: \{1, 2, 3 \} \longrightarrow \{1, 2, 3, 4 \}.
$$

Show that none is bijective.
(This constitutes a direct proof that a set $A$ of cardinality three does not have cardinality four.)

(b) How many injective maps

$$
f: \{1, \dots , 8 \} \longrightarrow \{1, \dots , 10 \}
$$

are there?
(You can see why one would not wish to try to prove directly that there is no bijective correspondence between these sets.)
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.1, printed p. 75** (`tmp/sources/munkres-solutions-whitman.pdf`); his count of the injections as $n!/(n-m)!$ is the one used here and his list of the 24 triples is the list below. The statement is Munkres, *Topology* (2000), §6 Exercise 1, printed pp. 44--45.

::: pf

::: {.pf-step #triples}
An injective map $f:\{1,2,3\}\to\{1,2,3,4\}$ is determined by, and determines, the ordered triple $(f(1),f(2),f(3))$ of distinct elements of $\{1,2,3,4\}$.

::: pf-proof
The values of $f$ at the three domain points determine the map, and injectivity says precisely that the three values are pairwise distinct.
:::
:::

::: {.pf-step #list}
The twenty-four triples with pairwise distinct entries from $\{1,2,3,4\}$ are
$$
\begin{array}{llll}
(1,2,3),&(1,2,4),&(1,3,2),&(1,3,4),\\
(1,4,2),&(1,4,3),&(2,1,3),&(2,1,4),\\
(2,3,1),&(2,3,4),&(2,4,1),&(2,4,3),\\
(3,1,2),&(3,1,4),&(3,2,1),&(3,2,4),\\
(3,4,1),&(3,4,2),&(4,1,2),&(4,1,3),\\
(4,2,1),&(4,2,3),&(4,3,1),&(4,3,2).
\end{array}
$$

::: pf-proof
Choose $f(1)$ in $4$ ways, then $f(2)$ among the $3$ remaining values, then $f(3)$ among the $2$ remaining, giving $4\cdot3\cdot2=24$ triples; the list exhibits one triple for each such choice, and reading it off shows no entry repeats within a triple.
:::
:::

::: {.pf-step #a}
(a) There are exactly twenty-four injective maps $\{1,2,3\}\to\{1,2,3,4\}$, and none is bijective.

::: pf-proof
Steps [](#triples){.pf-ref} and [](#list){.pf-ref} give the twenty-four maps and no others. Each has an image of three points inside a four-point set, so it omits one point of the codomain and is not surjective, hence not bijective.
:::
:::

::: {.pf-step #b}
(b) There are $10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3=1\,814\,400$ injective maps $\{1,\dots,8\}\to\{1,\dots,10\}$.

::: pf-proof
As in step [](#triples){.pf-ref}, an injection is an ordered $8$-tuple of distinct values from a $10$-element set, counted by choosing the values successively: $10$ choices for $f(1)$, then $9$, and so on down to $3$ choices for $f(8)$. The product is $10!/2!=1\,814\,400$.
:::
:::

:::
:::
