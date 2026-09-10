---
schema: qual/card@1
id: E-HAT-1.B-8
kind: problem
title: "Finite graph products of finitely generated groups"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.B, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the standard maximal-tree presentation of a graph of groups: finitely many vertex generators and stable letters generate, while finite vertex presentations and finitely generated edge groups give finitely many relations.
---

Show that a finite graph product of finitely generated groups is finitely generated, and similarly for finitely presented groups.


::: {.solution}
Let $\Gamma$ be a finite connected graph of groups and choose a maximal tree $T$ in its underlying graph.

<1>1. If all vertex groups are finitely generated, then the graph product $\pi_1(K\Gamma)$ is finitely generated.
::: {.proof}
For each vertex $v$, choose a finite generating set $S_v$ for the vertex group $G_v$.
The standard graph-of-groups presentation has generators
\[
\bigcup_v S_v
\]
together with one stable letter $t_e$ for each unoriented edge $e$ not in the maximal tree $T$.
There are finitely many vertices and finitely many such edges because $\Gamma$ is finite.
Thus this is a finite generating set for $\pi_1(K\Gamma)$.
:::

<1>2. Suppose now that every vertex group is finitely presented and every edge group is finitely generated.
Then the graph product is finitely presented.
::: {.proof}
Choose for each vertex group a finite presentation
\[
G_v=\langle S_v\mid R_v\rangle
\]
and for each edge group $G_e$ a finite generating set $C_e$.
Start with the finitely many vertex generators and stable letters from <1>1.
Impose:

1. the finitely many vertex relators $R_v$;
2. for each tree edge $e$ and each $c\in C_e$, the relation identifying the two images of $c$ in the endpoint vertex groups;
3. for each non-tree edge $e$ and each $c\in C_e$, the HNN relation
   \[
   t_e\,\iota_{e,0}(c)\,t_e^{-1}=\iota_{e,1}(c).
   \]

These relations suffice for every element of an edge group because they hold on a generating set and both endpoint maps are homomorphisms.
Since the graph is finite, only finitely many relations occur.
Thus the graph product is finitely presented.
:::

<1>3. In particular, a finite graph product of finitely presented groups is finitely presented.
::: {.proof}
A finitely presented edge group is finitely generated, so the hypotheses of <1>2 are satisfied when all groups in the finite graph of groups are finitely presented.
:::
:::
