---
schema: qual/card@1
id: E-MUN-11-3
kind: problem
title: Whether the comparable elements of a point form a maximal chain
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 3 and Examples 1 and 2 of §11,
    printed pp. 68-70; the stored statement matches, and the two examples are described on
    the card so that it stands alone.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    The printed definition of B in the exercise omits x itself: since x is not strictly
    below or above itself, B as printed does not contain x. Dan Whitman records the same
    reading on his printed p. 120 and repairs it by adjoining x. The card states the
    printed set and this repair explicitly rather than answering about a set that does not
    contain the point it was built from.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.3,
    printed pp. 120-121 (tmp/sources/munkres-solutions-whitman.pdf). The answer - Example
    2 succeeds, Example 1 fails - and both witnesses are his: the disc of radius 2 centred
    at (1,0) is comparable with the unit disc at the origin but is not centred there, and
    in Example 2 the comparable points of (0,y_0) are exactly the horizontal line through
    it.
---

::: {.exercise}

Let $A$ be a set with a strict partial order $\prec$; let $x \in A$. Suppose that we wish to find a maximal simply ordered subset $B$ of $A$ that contains $x$. One plausible way of attempting to define $B$ is to let $B$ equal the set of all those elements of $A$ that are comparable with $x$;
$$
B = \{y \mid y \in A \text{ and either } x \prec y \text{ or } y \prec x\}.
$$
But this will not always work. In which of Examples 1 and 2 will this procedure succeed and in which will it not?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.3, printed pp. 120--121** (`tmp/sources/munkres-solutions-whitman.pdf`); the answer and both witnesses below are his, and so is the observation about the printed set.

First, the set as printed omits $x$: since $x\prec x$ never holds and $y=x$ satisfies neither clause, $x\notin B$. The candidate is therefore $B=\{y:x\prec y \text{ or } y\prec x\}\cup\{x\}$.

*Example 1: it fails.* Here $A$ is the collection of circular regions of the plane and $\prec$ is proper inclusion, so a maximal simply ordered subcollection is a nested family like the discs centred at the origin. Take $x$ to be the unit disc $C_{(0,0),1}$ centred at the origin. The disc $C_{(1,0),2}$ of radius $2$ centred at $(1,0)$ contains $x$: for $\abs{p}<1$,
$$
\abs{p-(1,0)}\le\abs{p}+\abs{(0,0)-(1,0)}<1+1=2,
$$
while $(1,0)\in C_{(1,0),2}$ and $(1,0)\notin x$. So $x\prec C_{(1,0),2}$, the disc lies in $B$, and it is not centred at the origin, whereas the nested family of discs about the origin is a maximal one containing $x$. Hence $B$ is not maximal — indeed it is not even a subfamily of that chain.

*Example 2: it succeeds.* Here $A=\RR^2$ and $(x_0,y_0)\prec(x_1,y_1)$ iff $y_0=y_1$ and $x_0<x_1$, so two points are comparable exactly when they lie on a common horizontal line, and the maximal simply ordered subsets are the horizontal lines $L_{y_0}=\{(t,y_0)\}$. Let $x=(0,y_0)$. If $(u,v)\in B$ then $(u,v)=x$ or $(u,v)\prec x$ or $x\prec(u,v)$, and in the last two cases the comparability forces $v=y_0$; so $B\subset L_{y_0}$. Conversely any $(u,y_0)\in L_{y_0}$ is either $x$ or comparable with $x$, so $L_{y_0}\subset B$. Hence $B=L_{y_0}$ is a maximal simply ordered set.
:::
