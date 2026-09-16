---
schema: qual/card@1
id: FF-6MNV6
kind: fact
title: Sign of $(1\,2\,3\,4\,5\,6)(7\,8\,9)(10\,11)(12\,13\,14\,15)(16\,17\,18)$
prompts:
- What is the sign of the cycle $\sigma=(123456)(789)(10~11)(12~13~14~15)(16~17~18)$?
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
---

::: {.fact}
The permutation $\sigma=(1\,2\,3\,4\,5\,6)(7\,8\,9)(10\,11)(12\,13\,14\,15)(16\,17\,18)\in S_{18}$ has sign $\varepsilon(\sigma)=-1$.
:::

::: {.proof}
A cycle of length $\ell$ is a product of $\ell-1$ transpositions, so its sign is $(-1)^{\ell-1}$ ([[FD-GHDF2]]).
The disjoint cycles of $\sigma$ have lengths $6,3,2,4,3$, so
$$
\varepsilon(\sigma)=(-1)^{5+2+1+3+2}=(-1)^{13}=-1.
$$
Equivalently, $\sigma$ has three cycles of even length.
:::
