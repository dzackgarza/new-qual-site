---
schema: qual/card@1
id: E-HAT-2.2-21
kind: problem
title: Euler characteristic of union of subcomplexes
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 21; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the inclusion-exclusion: every cell of $X=A\cup B$ lies in $A$ or in $B$ and in both
    exactly when it is a cell of $A\cap B$, so the cell counts satisfy inclusion-exclusion
    degreewise and the alternating sum is linear; the remark's Mayer-Vietoris version for open
    covers with bounded finite-rank homology is correct, the alternating sum of dimensions in a
    bounded exact sequence being zero.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 21 as printed on p. 157. The inclusion-exclusion over cells is
    correct; it now cites p. 7 for subcomplexes and p. 146 for the definition of chi, and states
    that the cells of X are partitioned into those of A only, of B only, and of A cap B.
    What is not covered: the added remark on the open-cover Mayer-Vietoris version is a
    variation and is not part of the exercise; it is left as stated.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §2.2 Exercise 21, printed p. 157. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own. Checked: that $A\cap B$ is a subcomplex, that the cells of $X$ split into the three classes, and that $\chi$ is the alternating sum of cell counts for a finite CW complex.
---

::: {.problem}
If a finite CW complex $X$ is the union of subcomplexes $A$ and $B$, show that $\chi(X) = \chi(A) + \chi(B) - \chi(A \cap B)$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §2.2 Exercise 21. The proof is inclusion--exclusion on the sets of $i$-cells, which is legitimate because the cells of a CW complex are disjoint and each lies in $A$ or in $B$.

::: pf

::: {.pf-step #cells}
For every $i$ the $i$-cells of $X$ are partitioned into those of $A$ only, those of $B$ only, and those of $A\cap B$.

::: pf-proof
$X=A\cup B$, so each cell of $X$ lies in $A$ or in $B$. A subcomplex is a closed union of cells, so the cells of $A$ and of $B$ are cells of $X$, and a cell lying in both $A$ and $B$ lies in $A\cap B$, which is again a subcomplex; conversely each cell of $A\cap B$ is a cell of $X$. Distinct cells are disjoint, so the three classes are disjoint and cover the $i$-cells.
:::
:::

::: {.pf-step #count}
$c_i(X)=c_i(A)+c_i(B)-c_i(A\cap B)$ for every $i$, where $c_i(Z)$ is the number of $i$-cells of $Z$.

::: pf-proof
The three sets of step [](#cells){.pf-ref} partition the $i$-cells of $X$, and a cell counted in both $c_i(A)$ and $c_i(B)$ is exactly a cell of $A\cap B$; this is ordinary inclusion--exclusion for finite sets.
:::
:::

::: {.pf-step #sum}
$\chi(X)=\chi(A)+\chi(B)-\chi(A\cap B)$.

::: pf-proof
For a finite CW complex the Euler characteristic is the alternating sum of the numbers of cells, so $\chi(X)=\sum_i(-1)^ic_i(X)$. Substituting step [](#count){.pf-ref} and splitting the finite sum gives $\sum_i(-1)^ic_i(A)+\sum_i(-1)^ic_i(B)-\sum_i(-1)^ic_i(A\cap B)$, that is $\chi(A)+\chi(B)-\chi(A\cap B)$.
:::
:::

:::
:::
