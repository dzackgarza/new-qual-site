---
schema: qual/card@1
id: E-AMD-E3N4BHJH
kind: problem
title: A maximal ideal is prime; $(0)$ in $\ZZ$ is prime but not maximal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
  - Ideals
relations: []
review: draft
---

::: {.exercise}
Show that every maximal ideal is prime, and give an example of a prime ideal that is not maximal.
:::

::: {.solution}
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
