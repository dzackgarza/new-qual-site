---
schema: qual/card@1
id: E-R3LKO
kind: problem
title: When the inclusion induces an isomorphism on fundamental groups
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
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 7, printed p. 366,
    with Theorem 58.7, Theorem 58.3 and Corollary 58.5. Parts (a) and (b) are the two sufficient conditions, and the card's counterexample for the converse is $D^2$ with $A=S^1$ and a constant map, where $j_*:\ZZ\to0$ is not an isomorphism. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Let $A$ be a subspace of $X$; let $j: A \to X$ be the inclusion map, and let $f: X \to A$ be a continuous map.
Suppose there is a homotopy $H: X \times I \to X$ between the map $j \circ f$ and the identity map of $X$.

(a) Show that if $f$ is a retraction, then $j_*$ is an isomorphism.

(b) Show that if $H$ maps $A \times I$ into $A$, then $j_*$ is an isomorphism.

(c) Give an example in which $j_*$ is not an isomorphism.
:::

::: {.solution}
Fix $a_0\in A$ and put $x_0=j(a_0)$. A homotopy equivalence induces an isomorphism on fundamental groups at these basepoints: its homotopy inverse and the path traced by the basepoint during the homotopy give the inverse after change of basepoint.

(a) If $f$ is a retraction, then $fj=\operatorname{id}_A$. Together with $jf\simeq\operatorname{id}_X$, this makes $j$ and $f$ homotopy inverse maps. Hence $j_*:\pi_1(A,a_0)\to\pi_1(X,x_0)$ is an isomorphism.

(b) If $H(A\times I)\subset A$, then restricting $H$ to $A\times I$ gives a homotopy in $A$ from $fj$ to $\operatorname{id}_A$. Thus $j$ and $f$ are again homotopy inverse maps, and $j_*$ is an isomorphism. The path $t\mapsto H(a_0,t)$ lies in $A$ and supplies the basepoint change when $f(a_0)\ne a_0$.

(c) Let $X=D^2$, $A=S^1=\partial D^2$, and let $f:D^2\to S^1$ be a constant map. Then $jf$ is constant and is homotopic to $\operatorname{id}_{D^2}$ because $D^2$ is contractible. But
$$
j_*:\pi_1(S^1)\cong\ZZ\longrightarrow\pi_1(D^2)=0
$$
is not an isomorphism.
:::
