---
schema: qual/card@1
id: PR-5PI25
kind: proposition
title: Subgroups of $S_n$ for $n$ prime containing an $n$-cycle
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Subgroups
  - Galois Theory
relations: []
review: draft
---

::: {.proposition}
Let $n$ be a prime and let $G \leq S_n$ contain an $n$-cycle.

(a) If $G$ contains a transposition, then $G = S_n$.

(b) If $n \geq 3$ and $G$ contains a $3$-cycle, then $G = A_n$ or $G = S_n$.
:::

::: {.example}
For composite $n$, a transposition and an $n$-cycle need not generate $S_n$.
In $S_4$, the elements $(1\,3)$ and $(1\,2\,3\,4)$ preserve the partition $\theset{\theset{1,3},\theset{2,4}}$, and they generate the dihedral group of order $8$.
The specific transposition $(1\,2)$ and the specific $n$-cycle $(1\,2\,\cdots\,n)$ do generate $S_n$ for every $n \geq 2$.
:::

::: {.example}
For composite $n$, a $3$-cycle and an $n$-cycle need not generate a group containing $A_n$.
In $S_6$, both $(1\,2\,3)$ and $(1\,4\,2\,5\,3\,6)$ preserve the partition $\theset{\theset{1,2,3},\theset{4,5,6}}$, so the group they generate lies in the stabilizer of that partition, which has order $72 < \abs{A_6} = 360$.
:::

::: {.remark}
For the Galois group $G \leq S_n$ of an irreducible separable polynomial $f$ of degree $n$, the action on the roots is transitive, so $n \divides \abs{G}$ by the orbit-stabilizer theorem.
If $n$ is prime, Cauchy's theorem gives an element of order $n$ in $G$, and every element of order $n$ in $S_n$ is an $n$-cycle.
:::
