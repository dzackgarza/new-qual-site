---
schema: qual/card@1
id: P-APAS18D
kind: problem
title: $D_8$-orbits on diagonals of a regular octagon; rank of the Reynolds operator
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
  - Invariant Theory
relations: []
review: draft
---

::: {.problem}
Let $X$ be the set of the $20$ diagonals in a regular octogon.
The dihedral group $D_8$ of octogon symmetries acts on $X$; let $V=\CC[X]$ be the associated permutation representation of $D_8$.

(a) How many orbits are there in the action of $D_8$ on $X$?

(b) The Reynolds operator $R_{D_8}\colon V\to V$ is given by
$$
R_{D_8}(v)=\frac{1}{|G|}\sum_{g\in D_8}g\cdot v.
$$
What is the rank of $R_{D_8}$?
:::

::: {.solution}
Label the vertices of the octagon by $\ZZ/8\ZZ$, so that $D_8$ acts by $i\mapsto i+1$ and $i\mapsto -i$. For a pair $\{i,j\}$ of distinct vertices put $d(i,j)\coloneqq\min(\abs{i-j},8-\abs{i-j})$, computed with representatives in $\{0,\ldots,7\}$.

::: pf

::: {.pf-step #orbits}

(a) The action has $\boxed{3}$ orbits.

::: pf-proof

A pair is an edge when $d=1$, so the diagonals are the pairs with $d\in\{2,3,4\}$; there are $8+8+4=20$ of them. Rotations and reflections preserve $d$, so diagonals with different $d$ lie in different orbits. The rotation $i\mapsto i+k$ sends $\{0,d\}$ to $\{k,k+d\}$, so the rotations alone act transitively on the diagonals with a given $d$.

:::

:::

::: pf-step

(b) $\operatorname{rank}R_{D_8}=\boxed{3}$.

::: pf-proof

For $h\in D_8$, $hR_{D_8}(v)=\frac1{\abs{D_8}}\sum_{g}hg\cdot v=R_{D_8}(v)$, so the image of $R_{D_8}$ lies in $V^{D_8}$; and $R_{D_8}$ fixes every invariant vector. Hence $R_{D_8}$ is a projection onto $V^{D_8}$ and its rank is $\dim V^{D_8}$. A vector $\sum_x c_x x\in\CC[X]$ is invariant exactly when $c$ is constant on orbits, so $\dim V^{D_8}$ is the number of orbits, $3$ by step [](#orbits){.pf-ref}.

:::

:::

:::
:::
