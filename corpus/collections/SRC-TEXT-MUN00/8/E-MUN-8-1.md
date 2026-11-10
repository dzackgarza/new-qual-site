---
schema: qual/card@1
id: E-MUN-8-1
kind: problem
title: Defining the $n$-fold sum of a sequence by recursive definition
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
    Read against Munkres, Topology (2000), §8 Exercise 1, printed pp. 55-56; the stored
    statement matches, and Theorem 8.4 is stated in §8 immediately before the exercises.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.1,
    printed p. 94 (tmp/sources/munkres-solutions-whitman.pdf). His choice is
    rho(f) = f(m) + b_{m+1} for f : {1,...,m} -> R with a_0 = b_1.
---

::: {.exercise}

Let $(b_1, b_2, \ldots)$ be an infinite sequence of real numbers. The sum $\sum_{k=1}^n b_k$ is defined by induction as follows:
$$
\sum_{k=1}^{n} b_k = b_1 \ \text{ for } n = 1,
\qquad
\sum_{k=1}^{n} b_k = \left(\sum_{k=1}^{n-1} b_k\right) + b_n \ \text{ for } n > 1.
$$
Let $A$ be the set of real numbers; choose $\rho$ so that Theorem 8.4 applies to define this sum rigorously.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.1, printed p. 94** (`tmp/sources/munkres-solutions-whitman.pdf`); the choice of $\rho$ below is his.

Take $A=\RR$ and $a_0=b_1$, and for a function $f:\{1,\dots,m\}\to\RR$ set
$$
\rho(f)=f(m)+b_{m+1}.
$$
This is an element of $A$, defined for every nonempty section $\{1,\dots,m\}$, so Theorem 8.4 (the principle of recursive definition) applies and gives a unique $h:\ZZ_+\to\RR$ with
$$
h(1)=b_1,
\qquad
h(n)=\rho(h\restrict\{1,\dots,n-1\})=h(n-1)+b_n\quad(n>1).
$$
Defining $\sum_{k=1}^n b_k=h(n)$, the two clauses of the induction are satisfied, and $h$ is the unique function with those values.
:::
