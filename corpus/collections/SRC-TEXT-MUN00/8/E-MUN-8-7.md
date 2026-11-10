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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.7, printed pp. 98--99** (`tmp/sources/munkres-solutions-whitman.pdf`); the two lemmas and the union argument below are his.

Call a function $f:\{1,\dots,n\}\to A$ *admissible* if $f(1)=a_0$ and $f(i)=\rho(f\restrict\{1,\dots,i-1\})$ for $1<i\le n$.

*Lemma 1. For every $n\ge1$ there is an admissible $f:\{1,\dots,n\}\to A$.* By induction on $n$: for $n=1$ take $f(1)=a_0$. If $f':\{1,\dots,n\}\to A$ is admissible, define $f:\{1,\dots,n+1\}\to A$ by $f(i)=f'(i)$ for $i\le n$ and $f(n+1)=\rho(f')$. Then $f\restrict\{1,\dots,n\}=f'$, so $f$ agrees with $f'$ where $f'$ is defined and therefore inherits its clauses; at $i=n+1$ the defining equation is $f(n+1)=\rho(f\restrict\{1,\dots,n\})=\rho(f')$ by construction. Hence $f$ is admissible.

*Lemma 2. Any two admissible functions agree on the intersection of their domains.* Let $f:\{1,\dots,n\}\to A$ and $g:\{1,\dots,m\}\to A$ be admissible, and if they differ let $i$ be the least point of $\{1,\dots,\min(n,m)\}$ with $f(i)\ne g(i)$. Then $i\ne1$ because $f(1)=a_0=g(1)$, and for $1\le j<i$ we have $f(j)=g(j)$, so $f\restrict\{1,\dots,i-1\}=g\restrict\{1,\dots,i-1\}$ and hence
$$
f(i)=\rho(f\restrict\{1,\dots,i-1\})=\rho(g\restrict\{1,\dots,i-1\})=g(i),
$$
a contradiction. So no such $i$ exists.

*Construction.* By Lemma 1 choose an admissible $f_n$ for each $n$, and let $h=\bigcup_{n\ge1}f_n$. By Lemma 2 any two of the $f_n$ agree where both are defined, so $h$ is a function; its domain is $\ZZ_+$ because $i\in\operatorname{dom}f_i$, and its values lie in $A$. For $i>1$ we have $h(j)=f_i(j)$ for $j\le i$ and hence $h\restrict\{1,\dots,i-1\}=f_i\restrict\{1,\dots,i-1\}$, so
$$
h(i)=f_i(i)=\rho(f_i\restrict\{1,\dots,i-1\})=\rho(h\restrict\{1,\dots,i-1\}),
$$
and $h(1)=f_1(1)=a_0$.

*Uniqueness.* If $h,h'$ both satisfy the recursion and $h\ne h'$, let $i$ be least with $h(i)\ne h'(i)$. Then $i\ne1$, and $h(j)=h'(j)$ for $j<i$, so the restrictions agree and $h(i)=\rho(h\restrict\{1,\dots,i-1\})=\rho(h'\restrict\{1,\dots,i-1\})=h'(i)$, a contradiction. Hence $h=h'$.
:::
