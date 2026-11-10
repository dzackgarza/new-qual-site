---
schema: qual/card@1
id: E-MUN-2-3
kind: problem
title: Preimage and image for arbitrary unions and intersections
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 3; the stored statement matches.
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
    Read against Munkres, Topology (2000), §2 Exercise 3, printed p. 21; the stored
    statement matches: (b), (c), (f) and (g) of Exercise 2 for arbitrary unions and
    intersections.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 2.3,
    printed pp. 13-14 (tmp/sources/munkres-solutions-whitman.pdf). His four parts are
    the card's; the injective case of (g) is his argument that the points x_0 witnessing
    y in each f(A_0) agree, and it is where the nonemptiness of the index collection is
    used.
---

::: {.exercise}

Show that (b), (c), (f), and (g) of Exercise 2 hold for arbitrary unions and intersections.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 2.3, printed pp. 13--14** (`tmp/sources/munkres-solutions-whitman.pdf`); the four parts below are his, with the index set written as $I$ rather than as a collection $\mathcal A$.

Let $\{B_i\}_{i\in I}$ be subsets of $B$ and $\{A_i\}_{i\in I}$ subsets of $A$.

Preimages commute with arbitrary unions:
$$
\begin{aligned}
x\in f^{-1}\!\left(\bigcup_i B_i\right)
&\iff f(x)\in B_i\text{ for some }i\\
&\iff x\in\bigcup_i f^{-1}(B_i).
\end{aligned}
$$
Hence
$$
f^{-1}\!\left(\bigcup_iB_i\right)=\bigcup_i f^{-1}(B_i).
$$
Similarly,
$$
f^{-1}\!\left(\bigcap_iB_i\right)=\bigcap_i f^{-1}(B_i).
$$

Images commute with arbitrary unions:
$$
f\!\left(\bigcup_i A_i\right)=\bigcup_i f(A_i).
$$
For intersections one always has
$$
f\!\left(\bigcap_i A_i\right)\subset\bigcap_i f(A_i),
$$
since a point of the common domain intersection maps into every $f(A_i)$. Equality can fail for noninjective $f$: the two-set counterexample of [[E-MUN-2-2]](g) is a family indexed by $I=\{0,1\}$. If $f$ is injective and the index set is nonempty, equality holds: if $y\in\bigcap_i f(A_i)$, then for each $i$ there is $a_i\in A_i$ with $f(a_i)=y$; injectivity forces all $a_i$ to be the same point, lying in $\bigcap_iA_i$.
:::
