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
---

::: {.exercise}

Let $\RR^\infty$ be the subset of $\RR^\omega$ consisting of all sequences that are "eventually zero," that is, all sequences $(x_1, x_2, \ldots)$ such that $x_i \neq 0$ for only finitely many values of $i$.
What is the closure of $\RR^\infty$ in $\RR^\omega$ in the box and product topologies?
Justify your answer.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.7, printed pp. 194--195** (`tmp/sources/munkres-solutions-whitman.pdf`); both answers and their proofs are his.

**Product topology: $\overline{\RR^{\infty}}=\RR^{\omega}$.** Let $\mathbf{x}\in\RR^{\omega}$ and let $U$ be a neighbourhood of $\mathbf{x}$; choose a basis element $\prod U_{n}\subset U$ with $\mathbf{x}\in\prod U_{n}$, and let $I$ be the finite set of indices with $U_{n}\ne\RR$. Define $\mathbf{y}$ by $y_{n}=x_{n}$ for $n\in I$ and $y_{n}=0$ for $n\notin I$. Then $\mathbf{y}\in\RR^{\infty}$, and $\mathbf{y}\in\prod U_{n}$: for $n\in I$ because $y_{n}=x_{n}\in U_{n}$, and for $n\notin I$ because $y_{n}=0\in\RR=U_{n}$. So every neighbourhood of $\mathbf{x}$ meets $\RR^{\infty}$ and $\mathbf{x}\in\overline{\RR^{\infty}}$. Hence $\RR^{\infty}$ is dense in the product topology.

**Box topology: $\RR^{\infty}$ is closed.** Let $\mathbf{x}\notin\RR^{\infty}$, so $x_{n}\ne0$ for infinitely many $n$. For each $n$ let
$$
U_{n}=\begin{cases}(-1,1),&x_{n}=0,\\ (x_{n}/2,\,2x_{n}),&x_{n}>0,\\ (2x_{n},\,x_{n}/2),&x_{n}<0,\end{cases}
$$
an open interval containing $x_{n}$ that does not contain $0$. Then $B=\prod U_{n}$ is a box basis element containing $\mathbf{x}$. If $\mathbf{y}\in B$ then $y_{n}\in U_{n}$ for every $n$; in particular $y_{n}\ne0$ for each of the infinitely many $n$ with $x_{n}\ne0$, so $\mathbf{y}\notin\RR^{\infty}$. Hence $B$ is a neighbourhood of $\mathbf{x}$ disjoint from $\RR^{\infty}$, and $\mathbf{x}$ is not a limit point of $\RR^{\infty}$. So $\RR^{\infty}$ contains all its limit points and is closed; in the box topology $\overline{\RR^{\infty}}=\RR^{\infty}$.
:::
