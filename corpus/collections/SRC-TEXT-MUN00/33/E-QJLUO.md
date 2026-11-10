---
schema: qual/card@1
id: E-QJLUO
kind: problem
title: Separating compact sets from closed sets in completely regular spaces
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Compactness
relations: []
review: draft
audit:
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The source states f(A)={0} and f(B)={1}. For an empty set, its image is empty; the intended assertion is pointwise separation.'
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S33.pdf, Exercise 33.8, page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S33.pdf, Internet Archive snapshot 20200331153844),
    checked against Munkres, Topology (2000), Section 33 Exercise 8, printed p. 213, Exercise 18.8
    (the maximum of finitely many continuous real-valued functions is continuous) and Theorem 33.1.
    Moller's construction is the card's: finitely many functions g_i with A inside the union of the
    sets {g_i < 1/2} and g_i equal to 1 on B, then g the sum (the card takes the maximum), then
    f = 2 max{0, g - 1/2}. No correction to the mathematics was needed; the maximum is used in place
    of the sum because it keeps the values in [0,1] without dividing by the number of terms.
---

::: {.exercise}

Let $X$ be completely regular; let $A$ and $B$ be disjoint closed subsets of $X$.
Show that if $A$ is compact, there is a continuous function $f: X \to [0, 1]$ such that $f(a)=0$ for every $a\in A$ and $f(b)=1$ for every $b\in B$.
:::

::: {.solution}
If $A=\varnothing$, take $f=1$. If $B=\varnothing$, take $f=0$. Assume both are nonempty below.

For each $a\in A$, complete regularity gives a continuous function
$$
u_a:X\to[0,1]
$$
with
$$
u_a(a)=1,\qquad u_a(B)=\{0\}.
$$
The open sets
$$
U_a=\{x:u_a(x)>1/2\}
$$
cover compact $A$. Choose $a_1,\dots,a_n$ such that $A\subset U_{a_1}\cup\cdots\cup U_{a_n}$. Set
$$
u(x)=\max\{u_{a_1}(x),\dots,u_{a_n}(x)\}.
$$
Then $u$ is continuous, $u=0$ on $B$, and $u>1/2$ on $A$. Finally define
$$
f(x)=\max\{0,1-2u(x)\}.
$$
Then $f:X\to[0,1]$ is continuous, $f=0$ on $A$, and $f=1$ on $B$.
:::
