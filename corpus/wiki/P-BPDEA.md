---
schema: qual/card@1
id: P-BPDEA
kind: problem
title: A quotient of a Hausdorff space that is not Hausdorff
classification:
  areas:
  - topology
  topics:
  - quotient-spaces
  - hausdorff-spaces
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Give an example of a quotient map in which the domain is Hausdorff, but the quotient is not.
:::

::: {.solution}
\envlist

- $\RR$ is clearly Hausdorff, and $\RR/\QQ$ has the indiscrete topology, and is thus non-Hausdorff.

- So take the quotient map $\pi:\RR \to \RR/\QQ$.

Direct proof that $\RR/\QQ$ isn't Hausdorff:

- Pick $[x] \subset U \neq [y] \subset V \in \RR/\QQ$ and suppose $U\cap V = \emptyset$.

- Pull back $U\to A, V\to B$ open disjoint sets in $\RR$

- Both $A, B$ contain intervals, so they contain rationals $p\in A, q\in B$

- Then $[p] = [q] \in U\intersect V$.
:::
