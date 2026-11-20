---
schema: qual/card@1
id: E-PKY0P
kind: problem
title: Closure of the eventually-zero sequences in box and product topologies
classification:
  areas:
  - topology
  topics:
  - Closure
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 7, printed p. 118; the stored
    statement is the printed question, and the card answers both topologies with
    justification.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.7, printed pp.
    194-195. Both answers are his: the eventually-zero sequences are dense in the product
    topology, because a product basis element constrains only finitely many coordinates, and
    closed in the box topology, because at a point not eventually zero the product of
    intervals that stop short of 0 in each nonzero coordinate avoids R^infinity.
    (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with six steps, two for the product topology and three for the box topology, each carrying
    a `pf-proof`; the two answers and the attribution are unchanged. Cited by number only: the
    definition of the product topology by basis elements that constrain finitely many
    coordinates, and the closure criterion by basic neighbourhoods. One claim is corrected:
    the prose said each interval $U_n$ does not contain $0$, which is false in the case
    $x_n=0$, where $U_n=(-1,1)$ contains $0$; the claim now says it misses $0$ at the
    coordinates with $x_n\ne0$, which is what the argument uses. Checked: that the point
    $\mathbf y$ of the product case lies both in $\RR^\infty$ and in the given basis element,
    the three cases of $U_n$ with the strict inequalities in each, and that the box
    neighbourhood misses $\RR^\infty$ at the infinitely many nonzero coordinates.
---

::: {.exercise}

Let $\RR^\infty$ be the subset of $\RR^\omega$ consisting of all sequences that are "eventually zero," that is, all sequences $(x_1, x_2, \ldots)$ such that $x_i \neq 0$ for only finitely many values of $i$.
What is the closure of $\RR^\infty$ in $\RR^\omega$ in the box and product topologies?
Justify your answer.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.7, printed pp. 194--195** (`tmp/sources/munkres-solutions-whitman.pdf`); both answers and their proofs are his.

::: pf

::: pf-step

**Product topology.** Let $\mathbf{x}\in\RR^{\omega}$ and let $\prod U_{n}$ be a basis element containing $\mathbf{x}$, with $I$ the finite set of indices $n$ for which $U_{n}\ne\RR$. The point $\mathbf{y}$ defined by $y_{n}=x_{n}$ for $n\in I$ and $y_{n}=0$ otherwise lies in $\RR^{\infty}\cap\prod U_{n}$.

::: pf-proof

A basis element of the product topology is a product of open sets all but finitely many of which are the whole factor, which is the set $I$; it contains $\mathbf x$ because $x_n\in U_n$ for every $n$. Off $I$ we have $U_n=\RR$, so $y_n=0\in U_n$; on $I$ we have $y_n=x_n\in U_n$. Hence $\mathbf y\in\prod U_n$. And $\mathbf y$ vanishes off the finite set $I$, so $\mathbf y\in\RR^\infty$.

:::

:::

::: pf-step

So every neighbourhood of $\mathbf{x}$ meets $\RR^{\infty}$, hence $\mathbf{x}\in\overline{\RR^{\infty}}$; as $\mathbf{x}$ was arbitrary, $\RR^{\infty}$ is dense in $\RR^{\omega}$ with the product topology and $\overline{\RR^{\infty}}=\RR^{\omega}$.

::: pf-proof

A point lies in the closure of a set exactly when each of its basic neighbourhoods meets the set, and step 1 produces such a meeting inside an arbitrary basis element containing $\mathbf x$, hence inside an arbitrary neighbourhood. Since $\mathbf x$ was an arbitrary point of $\RR^\omega$ and $\RR^\infty\subseteq\RR^\omega$, the closure is the whole space.

:::

:::

::: pf-step

**Box topology.** Let $\mathbf{x}\notin\RR^{\infty}$, so $x_{n}\ne0$ for infinitely many $n$, and for each $n$ let
$$
U_{n}=\begin{cases}(-1,1),&x_{n}=0,\\ (x_{n}/2,\,2x_{n}),&x_{n}>0,\\ (2x_{n},\,x_{n}/2),&x_{n}<0.\end{cases}
$$
Then $U_{n}$ is an open interval containing $x_{n}$, and it does not contain $0$ at any $n$ with $x_{n}\ne0$.

::: pf-proof

Each $U_n$ is an open interval in $\RR$ and contains $x_n$: $(-1,1)$ contains $0=x_n$ in the first case; for $x_n>0$ we have $0<x_n/2<x_n<2x_n$, so $x_n\in(x_n/2,2x_n)$; for $x_n<0$ we have $2x_n<x_n<x_n/2<0$, so $x_n\in(2x_n,x_n/2)$. In the second and third cases the interval misses $0$, and those are exactly the cases $x_n\ne0$.

:::

:::

::: pf-step

Then $B=\prod U_{n}$ is a box basis element containing $\mathbf{x}$, and if $\mathbf{y}\in B$ then $y_{n}\ne0$ for each of the infinitely many $n$ with $x_{n}\ne0$, so $\mathbf{y}\notin\RR^{\infty}$.

::: pf-proof

In the box topology every product of open subsets of the factors is a basis element, so $B$ is one, and $\mathbf x\in B$ because $x_n\in U_n$ for every $n$. If $\mathbf y\in B$ then $y_n\in U_n$ for every $n$; at a coordinate with $x_n\ne0$ the interval $U_n$ misses $0$ by step 3, so $y_n\ne0$ there. Those coordinates are infinitely many by hypothesis, so $\mathbf y$ does not vanish eventually and $\mathbf y\notin\RR^\infty$.

:::

:::

::: pf-step

Hence $B$ is a neighbourhood of $\mathbf{x}$ disjoint from $\RR^{\infty}$, so $\mathbf{x}$ is not in the closure; as $\mathbf{x}\notin\RR^{\infty}$ was arbitrary, $\RR^{\infty}$ is closed in the box topology and $\overline{\RR^{\infty}}=\RR^{\infty}$.

::: pf-proof

Step 4 exhibits, for each point outside $\RR^\infty$, a neighbourhood disjoint from it; such a point therefore lies in the open complement, so the complement is open and $\RR^\infty$ is closed. A closed set equals its closure, and $\RR^\infty$ is nonempty, so the closure is $\RR^\infty$ itself.

:::

:::

::: pf-step

The two answers are: $\overline{\RR^{\infty}}=\RR^{\omega}$ in the product topology, and $\overline{\RR^{\infty}}=\RR^{\infty}$ in the box topology.

::: pf-proof

Steps 1 and 2 prove the first, steps 3--5 the second; the two topologies on $\RR^\omega$ give different closures of the same subset.

:::

:::

:::
:::
