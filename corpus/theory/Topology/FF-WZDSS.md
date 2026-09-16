---
schema: qual/card@1
id: FF-WZDSS
kind: fact
title: $\Ext^*_{\ZZ}(\ZZ/n, A)$
prompts:
- What is $\operatorname{Ext}^*_{\mathbf{Z}}(\mathbf{Z}/n, A)$?
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.fact}
Let $n\geq 1$, let $A$ be an abelian group, and let $A[n]\coloneqq\ts{a\in A \st na = 0}$.
The groups [[D-BYIZA|$\Ext^k_{\ZZ}(\ZZ/n, A)$]] are
$$
\Ext^0_{\ZZ}(\ZZ/n, A)\cong\Hom(\ZZ/n, A)\cong A[n],\qquad
\Ext^1_{\ZZ}(\ZZ/n, A)\cong A/nA,\qquad
\Ext^k_{\ZZ}(\ZZ/n, A) = 0\quad (k\geq 2)
$$
[@Hat02, §3.1, p. 195].
:::
