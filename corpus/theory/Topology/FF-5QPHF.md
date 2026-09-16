---
schema: qual/card@1
id: FF-5QPHF
kind: fact
title: $\Tor^{\ZZ}_*(\ZZ/n, A)$
prompts:
- What is $\operatorname{Tor}^{\mathbf{Z}}_*(C_n, A)$?
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.fact}
Let $n\geq 1$, let $C_n\coloneqq\ZZ/n$, let $A$ be an abelian group, and let $A[n]\coloneqq\ts{a\in A \st na = 0}$.
The groups [[D-4VGLT|$\Tor^{\ZZ}_k(C_n, A)$]] are
$$
\Tor^{\ZZ}_0(C_n, A)\cong C_n\otimes_{\ZZ}A\cong A/nA,\qquad
\Tor^{\ZZ}_1(C_n, A)\cong A[n],\qquad
\Tor^{\ZZ}_k(C_n, A) = 0\quad (k\geq 2)
$$
[@Hat02].
:::
