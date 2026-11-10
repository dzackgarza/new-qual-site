---
schema: qual/card@1
id: E-MUN-11-1
kind: problem
title: The rational-difference partial order and its maximal chains
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
    Read against Munkres, Topology (2000), §11 Exercise 1, printed p. 70; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.1,
    printed pp. 118-119 (tmp/sources/munkres-solutions-whitman.pdf). His answer is that
    the maximal simply ordered subsets are the cosets A_x = {y : x - y rational}; the
    two inclusions of A = B are his, with the irrationality of a rational plus an
    irrational doing the work in the second.
---

::: {.exercise}

If $a$ and $b$ are real numbers, define $a \prec b$ if $b - a$ is positive and rational. Show this is a strict partial order on $\RR$. What are the maximal simply ordered subsets?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.1, printed pp. 118--119** (`tmp/sources/munkres-solutions-whitman.pdf`); the identification of the maximal simply ordered subsets as the cosets of $\QQ$ is his.

*Strict partial order.* For any $a$, $a-a=0$ is not positive, so not $a\prec a$. If $a\prec b$ and $b\prec c$ then $b-a$ and $c-b$ are positive rationals, so $c-a=(c-b)+(b-a)$ is a positive rational, that is $a\prec c$.

*The maximal simply ordered subsets are the sets*
$$
A_x=\{y\in\RR\mid x-y\in\QQ\},\qquad x\in\RR,
$$
the cosets of $\QQ$ in $\RR$. First, each $A_x$ is simply ordered: if $y\ne z$ lie in $A_x$ then $x-y$ and $x-z$ are rational, so $z-y=(z-x)+(x-y)$ is rational and nonzero, hence either $z-y$ or $y-z$ is a positive rational and $y\prec z$ or $z\prec y$. And $A_x$ is maximal: if $z\notin A_x$ then $x-z\notin\QQ$ and so $z-y=(z-x)+(x-y)$ is irrational for every $y\in A_x$, since an irrational plus a rational is irrational; hence $z$ is incomparable with every element of $A_x$.

Conversely, let $B$ be maximal simply ordered. It is nonempty, since $\varnothing$ is simply ordered and is properly contained in $\{a\}$ for any $a$; choose $x\in B$ and let $A_x$ be the coset through $x$. If $y\in B$ then $y=x$ or, $B$ being simply ordered, $y\prec x$ or $x\prec y$; in each case $x-y$ is rational, so $y\in A_x$. Hence $B\subset A_x$. And if $y\in A_x$ then $x-y$ is rational and nonzero unless $y=x$, so $y$ is comparable with $x$; since $B$ is maximal and $B\cup\{y\}$ is then simply ordered, $y\in B$. Hence $B=A_x$.
:::
