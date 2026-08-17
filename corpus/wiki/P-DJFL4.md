---
schema: qual/card@1
id: P-DJFL4
kind: problem
title: An endomorphism of $\RR^5$ with eigenvalue $0$ is neither injective nor surjective
classification:
  areas:
  - algebra
  topics:
  - rank-and-nullity
  - eigenvalues-and-eigenvectors
  - linear-algebra
relations: []
review: draft
solved: false
---

::: problem
Since 0 is an eigenvalue, there exists an eigenvector $\vector v$ such that $L\vector v = 0 \vector v = 0$.
But then $\vector v \in \ker(L)$, so $\dim\ker(L) \geq 1$.
Since $\ker(L) \neq 0$, $L$ can not be injective.

By the rank-nullity theorem, we must also have $5 = \dim\ker(L) + \dim \im (L)$.
But then $\dim \im (L) \leq 5 = \dim \RR^5$, so $L$ can not be surjective either.
:::
