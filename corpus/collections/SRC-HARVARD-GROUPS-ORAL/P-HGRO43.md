---
schema: qual/card@1
id: P-HGRO43
kind: problem
title: Multiple and sharp transitivity
classification:
  areas: [algebra]
  topics: [Group Actions]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Define a $k$-transitive group action and a sharply $k$-transitive group action.
Discuss multiple transitivity.
:::

::: {.solution}
<1>1. A group action of $G$ on a set $X$ is $k$-transitive if for any two ordered $k$-tuples $(x_1, \ldots, x_k)$ and $(y_1, \ldots, y_k)$ of distinct elements of $X$, there is $g \in G$ with $g x_i = y_i$ for all $i$.
Proof: definition.

<1>2. The action is sharply $k$-transitive if it is $k$-transitive and the element $g$ in <1>1 is unique.
Proof: definition.

<1>3. Examples of multiple transitivity.
<2>1. $S_n$ acts $n$-transitively (and sharply $n$-transitively) on $\{1, \ldots, n\}$.
Proof: any permutation of $n$ distinct points is realized by a unique element of $S_n$.
<2>2. $A_n$ acts $(n-2)$-transitively on $\{1, \ldots, n\}$.
Proof: given two ordered $(n-2)$-tuples, there is a permutation sending one to the other, and it can be chosen even (adjusting by a transposition of the two remaining points if needed).
<2>3. $\operatorname{PGL}_2(k)$ acts sharply $3$-transitively on the projective line $\PP^1(k)$.
Proof: a Möbius transformation is determined by its values at three distinct points, and any three distinct points can be sent to any three distinct points.
<2>4. The affine group $\operatorname{AGL}_1(k)$ acts sharply $2$-transitively on $k$.
Proof: an affine map $x \mapsto ax + b$ is determined by its values at two points.

<1>4. Q.E.D.
Proof: <1>1–<1>3.
:::
