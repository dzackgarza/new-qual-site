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
