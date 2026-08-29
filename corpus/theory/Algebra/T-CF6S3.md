---
schema: qual/card@1
id: T-CF6S3
kind: theorem
title: Eisenstein's Criterion
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
---

:::{.theorem}
If \[
f(x) = \sum_{i=0}^n \alpha_i x^i = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0 \in \QQ[x]
.\]
then $f$ will be irreducible over $\QQ[x]$ (and thus over $\ZZ[x]$ by Gauss' lemma) if
$\exists p$ such that

- $p$ divides every coefficient *except* $a_n$ and
- $p^2$ does not divide $a_0$.

Note that if $f$ is monic, it suffices to find any prime dividing all of the non-leading terms.
:::
