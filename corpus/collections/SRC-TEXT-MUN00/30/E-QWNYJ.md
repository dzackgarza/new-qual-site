---
schema: qual/card@1
id: E-QWNYJ
kind: problem
title: Countable products of separable spaces are separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Amit Rajaraman, "Munkres Solutions" (MA 406
    course notes, last updated 31 March 2021), Exercise 4.30.10, printed p. 13
    (tmp/sources/munkres-solutions-amitrajaraman-ma406.pdf), checked against Munkres, Topology
    (2000), Section 30 Exercise 10, printed p. 194. His construction is the one on the card: a
    point of the product is in D when every coordinate is in the chosen countable dense set and
    all but finitely many coordinates equal the chosen base point, which is a countable union of
    countable sets, and density is read off a basis element that restricts finitely many
    coordinates. What was added: the empty-factor case, which he does not mention and which the
    card settles first. "Doug's World", printed p. 3, leaves Problem 30.10 with an empty solution.
---

::: {.exercise}

Show that if $X$ is a countable product of spaces having countable dense subsets, then $X$ has a countable dense subset.
:::

::: {.solution}
Let
$$
X=\prod_{n=1}^\infty X_n,
$$
If some $X_n$ is empty, then $X$ is empty and is separable. Otherwise choose for each $n$ a countable dense set $D_n\subset X_n$ and a basepoint $a_n\in D_n$. Let $D\subset X$ consist of all sequences $x=(x_n)$ such that $x_n\in D_n$ for every $n$ and $x_n=a_n$ for all but finitely many $n$.

The set $D$ is countable: it is a countable union, over finite subsets $F\subset\ZZ_+$, of the countable products $\prod_{n\in F}D_n$.

It is dense. A basic nonempty open set in the product topology restricts only finitely many coordinates, say $n\in F$, with $x_n\in U_n$. Since $D_n$ is dense, choose $d_n\in D_n\cap U_n$ for $n\in F$, and set all other coordinates equal to $a_n$. The resulting point lies in $D$ and in the basic open set. Hence $D$ is countable dense.
:::
