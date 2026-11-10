---
schema: qual/card@1
id: E-MUN-8-2
kind: problem
title: Defining the $n$-fold product of a sequence by recursive definition
classification:
  areas:
  - topology
  topics:
  - Recursive Definition
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §8 Exercise 2, printed p. 56; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.2,
    printed p. 94 (tmp/sources/munkres-solutions-whitman.pdf). His choice is
    rho(f) = f(m) * b_{m+1} with a_0 = b_1.
---

::: {.exercise}

Let $(b_1, b_2, \ldots)$ be an infinite sequence of real numbers. We define the product $\prod_{k=1}^n b_k$ by the equations
$$
\prod_{k=1}^{1} b_k = b_1,
\qquad
\prod_{k=1}^{n} b_k = \left(\prod_{k=1}^{n-1} b_k\right)\cdot b_n \quad \text{for } n > 1.
$$
Use Theorem 8.4 to define this product rigorously.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.2, printed p. 94** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice of $\rho$ below is his.

Take $A=\RR$, $a_0=b_1$, and for $f:\{1,\dots,m\}\to\RR$ set
$$
\rho(f)=f(m)\cdot b_{m+1}\in\RR .
$$
By Theorem 8.4 there is a unique $p:\ZZ_+\to\RR$ with
$$
p(1)=b_1,
\qquad
p(n)=\rho(p\restrict\{1,\dots,n-1\})=p(n-1)\cdot b_n\quad(n>1),
$$
and setting $\prod_{k=1}^n b_k=p(n)$ gives exactly the two defining equations.
:::
