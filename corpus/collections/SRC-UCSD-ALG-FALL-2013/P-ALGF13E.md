---
schema: qual/card@1
id: P-ALGF13E
kind: problem
title: Charpoly equals minpoly iff rational form is a companion matrix
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Rational Canonical Form
relations: []
review: draft
---

::: problem
Let $A \in M_n(F)$, where $F$ is any field.
Let $V = F^n$ and let $\phi \colon V \to V$ be the linear transformation given by the matrix $A$.
Show that the following are equivalent:

(i) $\mathrm{charpoly}(A) = \mathrm{minpoly}(A)$.

(ii) The rational canonical form of $A$ is a companion matrix of a polynomial $f \in F[x]$.

(iii) There exists $v \in V$ such that the elements $\{v, \phi(v), \phi^2(v), \ldots, \phi^{n-1}(v)\}$ span $V$ over $F$.
:::
