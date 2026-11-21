---
schema: qual/card@1
id: E-K89XO
kind: problem
title: Projections from a product are open maps
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 4, printed p. 92, with the
    definition of the product topology and Theorem 15.1 on printed p. 87; the stored
    statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.4, printed p. 152.
    The proof is his: a point of pi_1(U) has a product basis element A x B around it inside
    U, and then the whole of A projects into pi_1(U). pi_2 is the same argument.
    (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the basis element of the product topology
    (Theorem 15.1), the containment A x B inside U, and the projection of A into pi_1(U),
    against Munkres §16 Exercise 4, printed p. 92, and Whitman's Exercise 16.4, printed p.
    152. The printed statement needed no repair.
---

::: {.exercise}

A map $f: X \to Y$ is said to be an open map if for every open set $U$ of $X$, the set $f(U)$ is open in $Y$.
Show that $\pi_1: X \times Y \to X$ and $\pi_2: X \times Y \to Y$ are open maps.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.4, printed p. 152** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument for $\pi_{1}$ is his, and $\pi_{2}$ is the same argument with the factors exchanged.

::: pf

::: {.pf-step #slice}
Let $U$ be open in $X\times Y$ and let $(x,y)\in U$. There is a basis element $A\times B$ of $X\times Y$ with $(x,y)\in A\times B\subset U$, where $A$ is open in $X$ and $B$ is open in $Y$.

::: pf-proof
By the definition of the product topology, the collection $\mathcal{B}=\{A\times B\mid A\text{ open in }X,\ B\text{ open in }Y\}$ is a basis for it (Theorem 15.1, printed p. 87). A basis element of a topology containing a point of an open set $U$ lies inside $U$ by the definition of a basis, so some $A\times B\in\mathcal{B}$ has $(x,y)\in A\times B\subset U$.
:::

:::

::: {.pf-step #proj1}
$\pi_{1}(U)$ is open in $X$.

::: pf-proof
Let $x\in\pi_{1}(U)$ and choose $y\in Y$ with $(x,y)\in U$. Let $A\times B$ be the basis element given by step [](#slice){.pf-ref}. Then $x\in A$, and for every $x'\in A$ the point $(x',y)$ lies in $A\times B\subset U$, so $x'=\pi_{1}(x',y)\in\pi_{1}(U)$. Hence $x\in A\subset\pi_{1}(U)$ with $A$ open in $X$. As $x$ was an arbitrary point of $\pi_{1}(U)$, that set is a union of open subsets of $X$, so it is open in $X$ because a topology is closed under unions.
:::

:::

::: {.pf-step #proj2}
$\pi_{2}(U)$ is open in $Y$.

::: pf-proof
The argument of step [](#proj1){.pf-ref} applies with the roles of $X$ and $Y$ and of the two coordinates exchanged: for $y\in\pi_{2}(U)$ choose $x$ with $(x,y)\in U$ and the same basis element $A\times B$, and then $y\in B\subset\pi_{2}(U)$ with $B$ open in $Y$.
:::

:::

::: {.pf-step}
$\pi_{1}$ and $\pi_{2}$ are open maps.

::: pf-proof
An open map is a map taking every open set of its domain to an open set of its codomain. Steps [](#proj1){.pf-ref} and [](#proj2){.pf-ref} show this for an arbitrary open $U\subset X\times Y$, for $\pi_{1}$ and for $\pi_{2}$ respectively.
:::

:::

:::
:::
