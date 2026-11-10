---
schema: qual/card@1
id: E-JCJOW
kind: problem
title: Choice axiom and nonempty cartesian products
classification:
  areas:
  - topology
  topics:
  - Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 9, printed p. 118, with the choice
    axiom and Lemma 9.2 in §9; the stored statement is the printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.9, printed p. 197.
    Both directions are his: a choice function evaluated at the members of the family is an
    element of the product, and from an element of the product of a disjoint family the set
    of its coordinates meets each member in exactly one point. (tmp/sources/munkres-
    solutions-whitman.pdf).
---

::: {.exercise}

Show that the choice axiom is equivalent to the statement that for any indexed family $\theset{A_\alpha}_{\alpha \in J}$ of nonempty sets, with $J \neq \varnothing$, the cartesian product

$$
\prod_{\alpha \in J} A_\alpha
$$

is not empty.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.9, printed p. 197** (`tmp/sources/munkres-solutions-whitman.pdf`); both directions are his.

**Choice axiom implies nonempty products.** Let $\{A_{\alpha}\}_{\alpha\in J}$ be an indexed family of nonempty sets with $J\ne\varnothing$. By the choice axiom in the form of Lemma 9.2 (printed p. 60) there is a choice function $c$ on the collection $\mathcal{A}=\{A_{\alpha}\mid\alpha\in J\}$ with $c(A)\in A$ for every $A\in\mathcal{A}$. Put $x_{\alpha}=c(A_{\alpha})$; then $x_{\alpha}\in A_{\alpha}$ for every $\alpha$, so $\mathbf{x}=(x_{\alpha})_{\alpha\in J}$ is an element of $\prod_{\alpha\in J}A_{\alpha}$.

**Nonempty products imply the choice axiom.** Let $\mathcal{A}$ be a collection of pairwise disjoint nonempty sets with $\mathcal{A}\ne\varnothing$. The family $\{A\}_{A\in\mathcal{A}}$ indexed by $\mathcal{A}$ consists of nonempty sets and its index set is nonempty, so by hypothesis $\prod_{A\in\mathcal{A}}A\ne\varnothing$: there is $(x_{A})_{A\in\mathcal{A}}$ with $x_{A}\in A$ for each $A$. Let $C=\{x_{A}\mid A\in\mathcal{A}\}\subset\bigcup_{A\in\mathcal{A}}A$. For $A\in\mathcal{A}$ we have $x_{A}\in C\cap A$, so $C\cap A\ne\varnothing$; and if $y\in C\cap A$ then $y=x_{B}$ for some $B\in\mathcal{A}$, so $x_{B}\in A$; but $x_{B}\in B$ and, if $B\ne A$, the disjointness of distinct members would be contradicted. Hence $B=A$ and $y=x_{A}$. So $C\cap A=\{x_{A}\}$ for every $A\in\mathcal{A}$: $C$ consists of exactly one element from each member of $\mathcal{A}$, which is the choice axiom.
:::
