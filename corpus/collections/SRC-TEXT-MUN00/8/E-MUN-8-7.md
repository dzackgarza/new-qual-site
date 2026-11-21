---
schema: qual/card@1
id: E-MUN-8-7
kind: problem
title: The principle of recursive definition
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
    Read against Munkres, Topology (2000), §8 Exercise 7 and the statement of Theorem
    8.4, printed pp. 55-56; the stored statement reproduces the theorem the exercise
    asks to prove.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.7,
    printed pp. 98-99 (tmp/sources/munkres-solutions-whitman.pdf). His two lemmas are
    the ones below - a unique function on each section {1,...,n}, and agreement of any
    two such - and h is their union, with uniqueness by the least counterexample.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the two lemmas and the union argument are
    Whitman's (Exercise 8.7, printed pp. 98-99), as the card cites. Checked: the induction, the
    least-counterexample argument for agreement, that the union is a function and has domain Z_+,
    the recursion at each i, and uniqueness. Not checked: the cited pages, because tmp/sources
    holds no copy of the Whitman manual and the Munkres text is not retained in this VM.
---

::: {.exercise}

Prove Theorem 8.4 (the principle of recursive definition): let $A$ be a set, $a_0$ an element of $A$, and $\rho$ a function assigning to each function mapping a nonempty section of the positive integers into $A$ an element of $A$. Then there is a unique function $h:\ZZ_+\to A$ such that
$$
h(1)=a_0,
\qquad
h(i)=\rho(h\restrict\{1,\dots,i-1\}) \quad \text{for } i>1.
$$
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.7, printed ps 98-99, which the card cites; it is restructured into numbered steps below. The two lemmas and the union argument below are his. A section of the positive integers is a set $\set{1,\dots,n}$, and a function on it is admissible when it satisfies the recursion on its whole domain.

::: pf

::: {.pf-step #lem1}

For every $n\geq1$ there is an admissible $f:\set{1,\dots,n}\to A$.

::: pf-proof

Induction on $n$. For $n=1$ put $f(1)\coloneqq a_0$; there is no clause with $i>1$. Given admissible $f':\set{1,\dots,n}\to A$, define $f:\set{1,\dots,n+1}\to A$ by $f(i)\coloneqq f'(i)$ for $i\leq n$ and $f(n+1)\coloneqq\rho(f')$; then $f\restriction\set{1,\dots,n}=f'$, so $f$ inherits the clauses at $i\leq n$, and at $i=n+1$ its value is $\rho(f')=\rho(f\restriction\set{1,\dots,n})$ by construction.

:::

:::

::: {.pf-step #lem2}

Any two admissible functions agree on the intersection of their domains.

::: pf-proof

Let $f:\set{1,\dots,n}\to A$ and $g:\set{1,\dots,m}\to A$ be admissible and suppose they differ; let $i$ be the least element of $\set{1,\dots,\min(n,m)}$ with $f(i)\neq g(i)$. Then $i\neq1$, since $f(1)=a_0=g(1)$. For $1\leq j<i$ one has $f(j)=g(j)$, so the restrictions to $\set{1,\dots,i-1}$ coincide and $f(i)=\rho(f\restriction\set{1,\dots,i-1})=\rho(g\restriction\set{1,\dots,i-1})=g(i)$, a contradiction.

:::

:::

::: {.pf-step #union}

$h\coloneqq\bigcup_{n\geq1}f_n$ is a function $\ZZ_+\to A$.

::: pf-proof

Choose an admissible $f_n$ for each $n$ by step [](#lem1){.pf-ref}. Each $f_n$ is a set of ordered pairs, and by step [](#lem2){.pf-ref} any two agree on the intersection of their domains, so the union is a function; its domain contains $\set{1,\dots,n}$ for every $n$, hence is $\ZZ_+$, and its values lie in $A$.

:::

:::

::: {.pf-step #exists}

$h$ satisfies the recursion.

::: pf-proof

$h(1)=f_1(1)=a_0$. For $i>1$, $h$ agrees with $f_i$ on $\set{1,\dots,i}$, so $h\restriction\set{1,\dots,i-1}=f_i\restriction\set{1,\dots,i-1}$ and $h(i)=f_i(i)=\rho(f_i\restriction\set{1,\dots,i-1})=\rho(h\restriction\set{1,\dots,i-1})$.

:::

:::

::: {.pf-step #unique}

$h$ is unique.

::: pf-proof

If $h,h'$ both satisfy the recursion and differ, let $i$ be least with $h(i)\neq h'(i)$; then $i\neq1$, and $h(j)=h'(j)$ for $j<i$ gives equal restrictions, whence $h(i)=\rho(h\restriction\set{1,\dots,i-1})=\rho(h'\restriction\set{1,\dots,i-1})=h'(i)$, a contradiction.

:::

:::

::: {.pf-step #done}

There is exactly one $h:\ZZ_+\to A$ with $h(1)=a_0$ and $h(i)=\rho(h\restriction\set{1,\dots,i-1})$ for $i>1$.

::: pf-proof

Steps [](#exists){.pf-ref} and [](#unique){.pf-ref}.

:::

:::

:::

:::
