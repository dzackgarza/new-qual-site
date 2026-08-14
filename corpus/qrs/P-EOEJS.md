---
schema: qual/card@1
id: P-EOEJS
kind: problem
title: "Let $N$ be a positive integer, and let $G$ be a finite group of\u2026"
classification:
  areas:
  - algebra
  topics:
  - permutations
  - group-actions
  - simple-groups
relations: []
review: draft
---

Let $N$ be a positive integer, and let $G$ be a finite group of order $N$.

a. Let $\sym G$ be the set of all bijections from $G\to G$ viewed as a group under composition.
Note that $\sym G \cong S_N$.
Prove that the Cayley map
\[
C: G&\to \sym G\\
g &\mapsto (x\mapsto gx)
\]
is an injective homomorphism.

b. Let $\Phi: \sym G\to S_N$ be an isomorphism.
For $a\in G$ define $\eps(a) \in \theset{\pm 1}$ to be the sign of the permutation $\Phi(C(a))$.
Suppose that $a$ has order $d$.
Prove that $\eps(a) = -1 \iff d$ is even and $N/d$ is odd.

c. Suppose $N> 2$ and $n\equiv 2 \mod 4$.
Prove that $G$ is not simple.

> Hint: use part (b).
