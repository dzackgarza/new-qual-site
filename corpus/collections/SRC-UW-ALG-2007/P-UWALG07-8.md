---
schema: qual/card@1
id: P-UWALG07-8
kind: problem
title: Unit quaternions, $\SU(2)$, and $\SU(2)/U(1)\cong S^2$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Group Actions
relations: []
review: draft
---

::: {.problem}
Let $\quaternions$ be the ring of quaternions with standard basis $1,i,j,k$ and identify $\CC$ with the subring $\RR+\RR i$ of $\quaternions$.

(a) Use the action of $\quaternions$ on itself by left multiplication to explain why there is a ring homomorphism $\varphi:\quaternions\to M_2(\CC)$, where $M_2(\CC)$ denotes the ring of $2\times2$ matrices.
(Warning: there are two ways to view $\quaternions$ as a $\CC$-vector space, through right and left multiplication by elements in the subring $\RR+\RR i$.)

(b) Say why $\varphi$ is injective.

(c) The special unitary group $\SU(2)$ consists of all $2\times2$ complex matrices $u$ such that $\det(u)=1$ and $uu^*=u^*u=1$ where $u^*$ is the conjugate transpose, i.e., the transpose of the matrix whose entries are the complex conjugates of the entries in $u$.
Show that $\varphi$ restricts to an isomorphism between the group of unit quaternions (those of length one) and $\SU(2)$.

(d) Use this to prove that $\SU(2)$ acts transitively on the Riemann sphere $\CC\PP^1$ defined as the $1$-dimensional subspaces in $\CC^2$.
(Hint: use the action of $M_2(\CC)$ on $\CC^2$ by left multiplication.)

(e) Let $U(1)$ denote the image in $\SU(2)$ of the multiplicative subgroup of $\CC-\{0\}$ consisting of the complex numbers $z\in\CC\subset\quaternions$ of length one.
Show that the coset space $\SU(2)/U(1)$ is isomorphic to the $2$-sphere $S^2$.

Remark.
The solution to this problem gives a realization of the Hopf fibration $S^3\to S^2$ with fibers $S^1$ because the group of unit quaternions is isomorphic to the $3$-sphere $S^3$.
:::
