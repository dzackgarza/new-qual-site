---
schema: qual/card@1
id: E-MUN-5-2
kind: problem
title: Associativity of finite and infinite Cartesian products
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 2; the stored statement matches.
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
    Read against Munkres, Topology (2000), §5 Exercise 2, printed p. 38; both parts
    are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.2,
    printed pp. 68-69 (tmp/sources/munkres-solutions-whitman.pdf). His (a) splits at the
    last coordinate and his (b) is the pairing map (a_1,a_2,a_3,...) -> ((a_1,a_2),
    (a_3,a_4), ...); the card gives the same two maps with the inverse written directly,
    which is what proves bijectivity, rather than his coordinate-by-coordinate injectivity
    and surjectivity checks. His parity lemma (that i/2 or (i+1)/2 is a positive integer
    according as i is even or odd) is what the card's appeal to the displayed inverse
    replaces.
---

::: {.exercise}

(a) Show that if $n > 1$ there is bijective correspondence of
$$
A_{1} \times \dots \times A_{n} \quad \text{with} \quad (A_{1} \times \dots \times A_{n-1}) \times A_{n}.
$$

(b) Given the indexed family $\{A_{1}, A_{2}, \ldots\}$, let $B_{i} = A_{2i-1} \times A_{2i}$ for each positive integer $i$. Show there is bijective correspondence of $A_{1} \times A_{2} \times \cdots$ with $B_{1} \times B_{2} \times \cdots$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.2, printed pp. 68--69** (`tmp/sources/munkres-solutions-whitman.pdf`); the two bijections are his, and where he checks injectivity and surjectivity coordinate by coordinate the card exhibits the two-sided inverse.

(a) Define
$$
\Phi:A_1\times\cdots\times A_n
\longrightarrow
(A_1\times\cdots\times A_{n-1})\times A_n
$$
by
$$
\Phi(a_1,\dots,a_n)=((a_1,\dots,a_{n-1}),a_n).
$$
Its inverse is
$$
((a_1,\dots,a_{n-1}),a_n)\longmapsto(a_1,\dots,a_n),
$$
so $\Phi$ is bijective.

(b) For $B_i=A_{2i-1}\times A_{2i}$, define
$$
\Psi(a_1,a_2,a_3,a_4,\dots)
=((a_1,a_2),(a_3,a_4),\dots).
$$
This maps $\prod_{j\ge1}A_j$ into $\prod_{i\ge1}B_i$. Its inverse simply flattens the sequence of ordered pairs:
$$
((b_1,b_2),(b_3,b_4),\dots)
\longmapsto
(b_1,b_2,b_3,b_4,\dots).
$$
Thus the two infinite products are in bijective correspondence.
:::
