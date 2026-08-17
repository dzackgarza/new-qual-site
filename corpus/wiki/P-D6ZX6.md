---
schema: qual/card@1
id: P-D6ZX6
kind: problem
title: "Maximal implies prime"
classification:
  areas:
  - algebra
  topics:
  - maximal-ideals
  - prime-ideals
  - ideals
relations: []
review: draft
solved: true
---
:::{.problem title="Maximal implies prime"}
Maximal $\implies$ prime, but generally not the converse.
:::

:::{.solution}

- Suppose $\mm$ is maximal, $ab\in \mm$, and $b\not\in \mm$.

- Then there is a containment of ideals $\mm \subsetneq \mm + (b) \implies \mm + (b) = R$.

- So
\[
1 = m + rb \implies a = am + r(ab)
,\]
  but $am\in \mm$ and $ab\in \mm \implies a\in \mm$.


*Counterexample*: 
$(0) \in \ZZ$ is prime since $\ZZ$ is a domain, but not maximal since it is properly contained in any other ideal.
:::
