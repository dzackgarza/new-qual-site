---
schema: qual/card@1
id: P-BGJF6
kind: problem
title: "A splitting field of $f$ over $F$ is an extension $L \\geq F$ that cont\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
A splitting field of $f$ over $F$ is an extension $L \geq F$ that contains every root of $f$, so that $f$ can be decomposed as a product of linear factors i.e. $f(x) = \prod_{i=1}^{\deg f} (x-\alpha_i)^{m_i}$ in $L[x]$.

### Part 2

If $E \geq F$ is a finite extension, then it is algebraic and $E = F[\alpha_1, \cdots, \alpha_n]$. 
So we can let $g(x) = \prod_{i=1}^n (x-\alpha_i)$. 
By construction, each $\alpha_i$ is a root, and so $E$ is a splitting field for $g$.

### Part 3

Since $E$ was shown to be a splitting field, it only remains to show that it is separable.
But this follows from the fact that each $\alpha_i$ is a separable *element*, since their minimal polynomial over $F$ is $g$.
So $E$ is a Galois extension.

