---
schema: qual/card@1
id: E-MUN-3-14
kind: problem
title: The converse relation of an order relation, and the converse of the least upper bound theorem
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 14, printed p. 29: for a relation
    C on A, D is defined by (b,a) in D iff (a,b) in C; (a) C is symmetric iff C = D,
    (b) D is an order relation if C is, (c) the converse of the theorem of Exercise 13.
    The stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.14,
    printed pp. 35-36 (tmp/sources/munkres-solutions-whitman.pdf). His three parts are
    the ones below; (c) is the greatest-lower-bound-to-least-upper-bound mirror of
    Exercise 13, through the set of upper bounds.
---

::: {.exercise}

If $C$ is a relation on a set $A$, define a new relation $D$ on $A$ by letting $(b, a) \in D$ if $(a, b) \in C$.

(a) Show that $C$ is symmetric if and only if $C = D$.

(b) Show that if $C$ is an order relation, $D$ is also an order relation.

(c) Prove the converse of the theorem in Exercise 13.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.14, printed pp. 35--36** (`tmp/sources/munkres-solutions-whitman.pdf`); the three parts below are his.

(a) If $C$ is symmetric, then
$$
(a,b)\in C \iff (b,a)\in C \iff (a,b)\in D,
$$
so $C=D$. Conversely, if $C=D$ and $(a,b)\in C$, then $(b,a)\in D=C$, so $C$ is symmetric.

(b) Let $C$ be an order relation; $D$ is a relation on $A$ by construction.

*Comparability.* If $a\ne b$ then $aCb$ or $bCa$, hence $bDa$ or $aDb$.

*Nonreflexivity.* $(a,a)\notin C$, so $(a,a)\notin D$; otherwise $(a,a)\in C$ by the definition of $D$.

*Transitivity.* If $aDb$ and $bDc$ then $bCa$ and $cCb$, so $cCa$ by transitivity of $C$, that is $aDc$.

(c) Conversely, suppose $A$ has the greatest lower bound property; we show it has the least upper bound property. Let $A_0\subset A$ be nonempty and bounded above, and let $B_0$ be the set of upper bounds of $A_0$, which is nonempty. Any $a\in A_0$ satisfies $a\le x$ for every $x\in B_0$, so $a$ is a lower bound of $B_0$ and $B_0$ is bounded below. Let $c=\inf B_0$.

For $x\in A_0$, every $y\in B_0$ has $x\le y$, so $x$ is a lower bound of $B_0$ and $x\le c$; hence $c$ is an upper bound of $A_0$. If $y$ is any upper bound of $A_0$ then $y\in B_0$ and $c\le y$. So $c=\sup A_0$, and $A$ has the least upper bound property.
:::
