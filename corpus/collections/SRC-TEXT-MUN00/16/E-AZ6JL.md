---
schema: qual/card@1
id: E-AZ6JL
kind: problem
title: Three topologies on the unit square
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Product Topology
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 10, printed p. 92; the stored
    statement is the printed one, I = [0,1] being a subspace of R.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 16.10, PDF pp. 5-6. The answer and the two
    witnesses for incomparability are his: I x (1/2,1] is product-open but no dictionary
    basis element at (1/2,1) stays inside it, and {1/2} x (0,1) is a dictionary interval but
    no product basis element at (1/2,1/2) stays inside it. The two inclusions into the
    subspace topology are proved on the card: the product lies in it by Exercise 16.9 and
    Theorem 16.3, and every dictionary basis element is the trace of a dictionary-open set
    of R x R, the half-open ones at the corners included. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Let $I = [0, 1]$.
Compare the product topology on $I \times I$, the dictionary order topology on $I \times I$, and the topology $I \times I$ inherits as a subspace of $\RR \times \RR$ in the dictionary order topology.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 16.10, PDF pp. 5--6** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the answer (the product and dictionary topologies are not comparable, and the subspace topology from $\RR\times\RR$ is strictly finer than both) and its two witnesses for the incomparability are his. The two inclusions into the subspace topology are proved below from Exercise 16.9 and Theorem 16.3, which positron0802 quotes from the preceding exercise. Whitman, printed pp. 156--158, gives the same answer.

On $I\times I$, with $I=[0,1]$, let $\mathcal{T}_{1}$ be the product topology, $\mathcal{T}_{2}$ the dictionary order topology, and $\mathcal{T}_{3}$ the topology inherited as a subspace of $\RR\times\RR$ in the dictionary order topology. Write $\prec$ for the dictionary order, and note that $I\times I$ has least element $(0,0)$ and greatest element $(1,1)$ in $\prec$.

*$\mathcal{T}_{1}$ and $\mathcal{T}_{2}$ are not comparable.* First, $\mathcal{T}_{2}\not\subset\mathcal{T}_{1}$. The set $U=I\times(\tfrac12,1]$ is a basis element of $\mathcal{T}_{1}$, since $(\tfrac12,1]$ is open in $I$, and it contains $(\tfrac12,1)$. Let $B$ be a $\mathcal{T}_{2}$-basis element containing $(\tfrac12,1)$; since $(\tfrac12,1)\ne(1,1)$, the set $B$ contains a point $(r,s)$ with $(\tfrac12,1)\prec(r,s)$, either as an endpoint of an interval or as its largest element when $B$ is a half-open interval ending at $(1,1)$. Then $r>\tfrac12$ or $r=\tfrac12$ and $s>1$, the second being impossible in $I\times I$; so $r>\tfrac12$. Hence $(\tfrac12,1)\prec(r,0)\prec(r,s)$, so $(r,0)\in B$, while $(r,0)\notin U$ because $0\notin(\tfrac12,1]$. Thus $B\not\subset U$ and $U\notin\mathcal{T}_{2}$.

Second, $\mathcal{T}_{1}\not\subset\mathcal{T}_{2}$. The set $V=\{\tfrac12\}\times(0,1)$ is the open interval $\big((\tfrac12,0),(\tfrac12,1)\big)$ in the dictionary order, so $V\in\mathcal{T}_{2}$, and $(\tfrac12,\tfrac12)\in V$. Let $A\times B$ be a $\mathcal{T}_{1}$-basis element containing $(\tfrac12,\tfrac12)$, so $A$ is open in $I$ and $\tfrac12\in A$; then $A$ contains some $x\ne\tfrac12$, and $(x,\tfrac12)\in A\times B$ while $(x,\tfrac12)\notin V$. So $A\times B\not\subset V$ and $V\notin\mathcal{T}_{1}$.

*$\mathcal{T}_{1}\subset\mathcal{T}_{3}$.* By Exercise 16.9 the dictionary order topology on $\RR\times\RR$ is the product topology $\RR_{d}\times\RR$, with $\RR_{d}$ discrete, and by Theorem 16.3 (printed p. 90) the subspace topology on $I\times I$ is then the product of the subspace topologies, $\RR_{d}\restrict_{I}\times\RR\restrict_{I}$, where $\RR_{d}\restrict_{I}$ is discrete and $\RR\restrict_{I}$ is the usual topology of $I$. A basis element of $\mathcal{T}_{1}$ is $A\times B$ with $A,B$ open in $I$, and
$$
A\times B=\bigcup_{x\in A}\{x\}\times B
$$
is a union of basis elements $\{x\}\times B$ of $\RR_{d}\restrict_{I}\times\RR\restrict_{I}$, hence lies in $\mathcal{T}_{3}$.

*$\mathcal{T}_{2}\subset\mathcal{T}_{3}$.* Every basis element of $\mathcal{T}_{2}$ is the trace on $I\times I$ of a basis element of the dictionary order topology of $\RR\times\RR$. An open interval $\big((a,b),(c,d)\big)$ of the square is the trace of the corresponding open interval of $\RR\times\RR$. The half-open interval $[(0,0),(c,d))$ of the square is the trace of the open interval $\big((0,-1),(c,d)\big)$ of $\RR\times\RR$, and the half-open interval $\big((a,b),(1,1)\big]$ is the trace of $\big((a,b),(1,2)\big)$. So each basis element of $\mathcal{T}_{2}$ is open in $\mathcal{T}_{3}$.

Finally, $\mathcal{T}_{1}\subset\mathcal{T}_{3}$ and $\mathcal{T}_{2}\subset\mathcal{T}_{3}$, and both inclusions are strict: $\mathcal{T}_{3}=\mathcal{T}_{1}$ would give $\mathcal{T}_{2}\subset\mathcal{T}_{1}$, and $\mathcal{T}_{3}=\mathcal{T}_{2}$ would give $\mathcal{T}_{1}\subset\mathcal{T}_{2}$, neither of which holds. So the subspace topology from $\RR\times\RR$ is strictly finer than both the product topology and the dictionary order topology on $I\times I$, which are incomparable with one another.
:::
