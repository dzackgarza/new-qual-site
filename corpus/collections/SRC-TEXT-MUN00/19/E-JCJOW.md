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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked both implications against Munkres §19
    Exercise 9, printed p. 119, with the choice axiom in the form of Lemma 9.2 (printed p.
    60): the choice function gives a point of the product, and a point of the product of the
    family indexed by a partition of a set gives a set meeting each member in exactly one
    point. Whitman, Exercise 19.9, printed p. 197. The printed statement needed no repair.
---

::: {.exercise}

Show that the choice axiom is equivalent to the statement that for any indexed family $\theset{A_\alpha}_{\alpha \in J}$ of nonempty sets, with $J \neq \varnothing$, the cartesian product

$$
\prod_{\alpha \in J} A_\alpha
$$

is not empty.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.9, printed p. 197** (`tmp/sources/munkres-solutions-whitman.pdf`); both directions are his.

::: pf

::: {.pf-step #choice-implies}
The choice axiom implies that $\prod_{\alpha\in J}A_{\alpha}\ne\varnothing$ for every indexed family of nonempty sets with $J\ne\varnothing$.

::: pf-proof
By the choice axiom in the form of Lemma 9.2 (printed p. 60) there is a choice function $c$ on the collection $\mathcal{A}=\{A_{\alpha}\mid\alpha\in J\}$, that is a function with domain $\mathcal{A}$ and $c(A)\in A$ for every $A\in\mathcal{A}$; the collection is nonempty because $J\ne\varnothing$ and every $A_{\alpha}$ is nonempty. Put $x_{\alpha}=c(A_{\alpha})$. Then $x_{\alpha}\in A_{\alpha}$ for every $\alpha\in J$, so $\mathbf{x}=(x_{\alpha})_{\alpha\in J}$ is an element of $\prod_{\alpha\in J}A_{\alpha}$.
:::

:::

::: {.pf-step #products-imply}
If every such product is nonempty, then the choice axiom holds.

::: pf-proof
Let $\mathcal{A}$ be a collection of pairwise disjoint nonempty sets with $\mathcal{A}\ne\varnothing$; it suffices to produce a set consisting of exactly one element of each member of $\mathcal{A}$. The family $\{A\}_{A\in\mathcal{A}}$ indexed by $\mathcal{A}$ consists of nonempty sets and has nonempty index set, so by hypothesis $\prod_{A\in\mathcal{A}}A\ne\varnothing$: there is $(x_{A})_{A\in\mathcal{A}}$ with $x_{A}\in A$ for each $A$. Let $C=\{x_{A}\mid A\in\mathcal{A}\}$, a subset of $\bigcup_{A\in\mathcal{A}}A$. For $A\in\mathcal{A}$ one has $x_{A}\in C\cap A$, so $C\cap A\ne\varnothing$. If $y\in C\cap A$ then $y=x_{B}$ for some $B\in\mathcal{A}$, and $y\in B$ because $x_{B}\in B$; if $B\ne A$ then $y$ would lie in the two disjoint members $A$ and $B$ of $\mathcal{A}$, so $B=A$ and $y=x_{A}$. Hence $C\cap A=\{x_{A}\}$ for every $A\in\mathcal{A}$, which is the choice axiom.
:::

:::

::: {.pf-step}
The two statements are equivalent.

::: pf-proof
Steps [](#choice-implies){.pf-ref} and [](#products-imply){.pf-ref} are the two implications.
:::

:::

:::
:::
