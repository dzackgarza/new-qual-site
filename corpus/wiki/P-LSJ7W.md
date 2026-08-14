---
schema: qual/card@1
id: P-LSJ7W
kind: problem
title: "Consider the quotient space"
classification:
  areas:
  - topology
  topics:
  - homology
  - quotient-spaces
  - manifolds
relations: []
review: draft
---
a.
Consider the quotient space 
\[
T^2 = \RR^2 / \sim \qtext{where} (x, y) \sim (x + m, y + n) \text{ for } m, n \in \ZZ
,\]
and let $A$ be any $2 \times 2$ matrix whose entries are integers such that $\det A = 1$. 

Prove that the action of $A$ on $\RR^2$ descends via the quotient $\RR^2 \to T^2$ to induce a homeomorphism $T^2 \to T^2$.

b.
Using this homeomorphism of $T^2$, we define a new quotient space 
\[
T_A^3 \definedas {T^2\cross \RR \over \sim} \qtext{where} ((x, y), t) \sim (A(x, y), t + 1)
\]

Compute $H_1 (T_A^3 )$ if $A=\left(\begin{array}{ll} 1 & 1 \\ 0 & 1 \end{array}\right).$

