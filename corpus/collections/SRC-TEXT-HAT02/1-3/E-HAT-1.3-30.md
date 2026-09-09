---
schema: qual/card@1
id: E-HAT-1.3-30
kind: problem
title: "Cayley graph of $\\mathbb{Z} * \\mathbb{Z}_2$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 30; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Described the Cayley graph as the 3-regular tree with bi-infinite a-lines and b-edges forming a perfect matching.
---

Draw the Cayley graph of the group $\mathbb{Z} * \mathbb{Z}_2 = \langle a, b \mid b^2 \rangle$.


::: {.solution}
Let
\[
G=\mathbb Z*\mathbb Z_2
=\langle a,b\mid b^2=1\rangle.
\]
Use the generating set
\[
\{a,a^{-1},b\}.
\]

<1>1. Every vertex of the Cayley graph has three incident edge ends: an $a$-edge leaving it, an $a$-edge entering it, and one $b$-edge.
::: {.proof}
From a vertex $g$ there are edges to
\[
ga,\qquad ga^{-1},\qquad gb.
\]
Since $b=b^{-1}$, the $b$-edge from $g$ to $gb$ is the same undirected edge when viewed from $gb$.
:::

<1>2. The $a$-edges form disjoint bi-infinite lines, one for each right coset of $\langle a\rangle$.
::: {.proof}
Starting from $g$ and traversing only $a$-edges gives precisely
\[
\{ga^n:n\in\mathbb Z\},
\]
with consecutive vertices joined by $a$-edges.
No nonzero power of $a$ is trivial, so this is a bi-infinite line.
:::

<1>3. The $b$-edges join these $a$-lines in a perfect matching, and the resulting graph has no cycles.
::: {.proof}
Every vertex lies on exactly one $b$-edge because $b^2=1$.
If there were a cycle, reading its labels and cancelling immediate reversals would give a nonempty reduced word in the free product
\[
\mathbb Z*\mathbb Z_2
\]
representing the identity, contradicting the free-product normal-form theorem.
:::

<1>4. Thus the Cayley graph is the infinite $3$-regular tree.
::: {.proof}
By <1>1 every vertex has valence three, and by <1>3 the connected Cayley graph is acyclic.
Equivalently, draw a bi-infinite $a$-line through the identity; from every vertex attach one $b$-edge to a new bi-infinite $a$-line, and repeat indefinitely.
This is the requested drawing up to graph isomorphism.
:::
:::
