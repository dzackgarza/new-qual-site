---
schema: qual/card@1
id: P-DXHST
kind: problem
title: 'Faithful transitive actions: trivial core of a stabilizer, and abelian transitive
  subgroups of $S_n$'
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Permutations
relations: []
review: draft
solved: false
---

::: problem
Suppose the group $G$ acts on the set $A$. 
Assume this action is faithful (recall that this means that the kernel of the homomorphism from $G$ to $\sym(A)$ which gives the action is trivial) and transitive (for all $a, b$ in $A$, there exists $g$ in $G$ such that $g \cdot a = b$.)

a.
For $a \in A$, let $G_a$ denote the stabilizer of $a$ in $G$. 
Prove that for any $a \in A$, 
$$
\Intersect_{\sigma\in G} \sigma G_a \sigma\inv = \theset{1}
.$$

b.
Suppose that $G$ is abelian. Prove that $|G| = |A|$. Deduce that every abelian transitive subgroup of $S_n$ has order $n$.
:::
