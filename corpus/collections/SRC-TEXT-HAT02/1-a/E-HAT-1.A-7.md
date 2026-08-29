---
schema: qual/card@1
id: E-HAT-1.A-7
kind: exercise
title: Nontrivial normal subgroup of infinite index in finitely generated free group is not finitely generated
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

If $F$ is a finitely generated free group and $N$ is a nontrivial normal subgroup of infinite index, show, using covering spaces, that $N$ is not finitely generated.

::: {.solution}
<1>1. Let $F = \pi_1(X)$ where $X$ is a finite wedge of circles (a finite graph with one vertex).
Proof: a finitely generated free group is the fundamental group of a finite wedge of circles.

<1>2. $N$ corresponds to a connected covering space $p: \tilde X \to X$ with $p_*(\pi_1(\tilde X)) = N$.
Proof: the fundamental theorem of covering spaces.

<1>3. Since $N$ is normal, $\tilde X$ is a normal (regular) covering, and its deck group is $F/N$, which is infinite (since $N$ has infinite index).
Proof: a normal subgroup corresponds to a regular covering, and the deck group is $F/N$.

<1>4. $\tilde X$ is a graph (a covering of a graph is a graph), and it is infinite.
Proof: the deck group $F/N$ is infinite, so $\tilde X$ has infinitely many sheets, hence infinitely many vertices.

<1>5. $\pi_1(\tilde X) = N$ is the fundamental group of an infinite graph.
Proof: <1>2.

<1>6. The fundamental group of an infinite graph is not finitely generated.
<2>1. An infinite graph has infinitely many edges.
Proof: a finite graph has finitely many edges; $\tilde X$ is infinite, so it has infinitely many edges.
<2>2. The fundamental group of a graph is free on the edges not in a maximal tree.
Proof: standard fact.
<2>3. An infinite graph has a maximal tree whose complement has infinitely many edges, so its fundamental group is free on infinitely many generators.
Proof: <2>1 and <2>2.
<2>4. Hence $\pi_1(\tilde X)$ is not finitely generated.
Proof: a free group on infinitely many generators is not finitely generated.

<1>7. Therefore $N$ is not finitely generated.
Proof: <1>5 and <1>6.

<1>8. Q.E.D.
Proof: <1>7.
:::
