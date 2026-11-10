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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.1, printed p. 75** (`tmp/sources/munkres-solutions-whitman.pdf`); his count of the injections as $n!/(n-m)!$ is the one used here, and his list of the 24 triples is the list below.

(a) An injective map is determined by the ordered triple
$$
(f(1),f(2),f(3)),
$$
whose entries must be distinct elements of $\{1,2,3,4\}$. The complete list is
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
These are all possibilities because one chooses $f(1)$ in $4$ ways, then $f(2)$ in $3$ remaining ways, then $f(3)$ in $2$ remaining ways, for $4\cdot3\cdot2=24$ maps.

None is surjective: each image contains exactly three points of a four-point codomain, so one codomain point is omitted. Hence none is bijective.

(b) For an injection
$$
f:\{1,\dots,8\}\to\{1,\dots,10\},
$$
there are successively
$$
10,9,8,7,6,5,4,3
$$
choices for the images of $1,\dots,8$. Thus the number of injective maps is
$$
10\cdot9\cdot8\cdot7\cdot6\cdot5\cdot4\cdot3
=\frac{10!}{2!}
=\boxed{1,814,400}.
$$
:::
