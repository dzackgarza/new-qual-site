---
schema: qual/card@1
id: P-UCTOP290-S6-5
kind: problem
title: Represent a singular homology class by a simplicial circuit
classification:
  areas:
  - topology
  topics:
  - Singular Homology
  - Simplicial Homology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 5 in its checked-in extraction and page image.
---

::: {.problem}
Given $c\in H_n(X;\ZZ)$, construct a finite
simplicial complex $K$, a class
$\mu\in H_n(K;\ZZ)$, and a map $f:K\to X$
with $f_*\mu=c$. Arrange that the set of
points of $K$ without a neighborhood
homeomorphic to $\RR^n$ lies in a
subcomplex of dimension at most $n-2$.
:::

::: {.solution}

Represent $c$ by a finite singular cycle
$z=\sum_j m_j\sigma_j$. Take $\abs{m_j}$
oriented copies of the standard $n$-simplex
for each $\sigma_j$, reversing orientation
when $m_j<0$. Each oriented face is labeled
by the restriction of its singular simplex
to that face. Since $\partial z=0$, every
positively oriented occurrence of each
singular $(n-1)$-simplex can be paired with
a negatively oriented occurrence of the
same simplex. Glue each paired pair of faces
by the identity of their parameter
simplices.

The quotient is a finite $\Delta$-complex.
Subdivide it to obtain a simplicial complex
$K$. The maps $\sigma_j$ agree on glued
faces, so they define a continuous
$f:K\to X$. The sum of the oriented
top-dimensional simplices is a cycle
$\mu$: every codimension-one face appears
twice with opposite induced signs. By
construction, $f_*\mu$ is represented by
$z$, hence equals $c$.

At an interior point of a top simplex, the
local model is $\RR^n$. At an interior
point of a codimension-one face, the two
paired half-space neighborhoods join to
give $\RR^n$. Thus any nonmanifold point
lies in the $(n-2)$-skeleton. For $n=1$
the construction produces disjoint circles;
for $n=0$ it produces finitely many points.
:::
