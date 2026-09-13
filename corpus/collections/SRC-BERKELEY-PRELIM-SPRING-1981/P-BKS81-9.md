---
schema: qual/card@1
id: P-BKS81-9
kind: problem
title: Equivalent invertibility criteria for $W\mapsto AW+WA$ on skew-symmetric matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction writes the second condition using undefined symbols a,b,c. Since the same sentence names the eigenvalues lambda_1,lambda_2,lambda_3 and the three conditions are asserted equivalent, the card records the corresponding pairwise eigenvalue sums and leaves this reconstruction explicit here.
---

:::{.problem}
Let $A$ be a real symmetric $3\times3$ matrix with eigenvalues $\lambda_1,\lambda_2,\lambda_3$.
Show that the following are equivalent:

1. $\operatorname{tr}A$ is not an eigenvalue of $A$.
2. $(\lambda_1+\lambda_2)(\lambda_2+\lambda_3)(\lambda_1+\lambda_3)\ne0$.
3. The map $L:S\to S$ is an isomorphism, where $S$ is the space of real $3\times3$ skew-symmetric matrices and
   \[
   L(W)=AW+WA.
   \]
:::
