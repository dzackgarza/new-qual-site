---
schema: qual/card@1
id: P-APA24D
kind: problem
title: Induced matrix $1$-norm equals the maximum absolute column sum
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $A \in M_{m,n}(\mathbb{C}) = \mathbb{C}^{m \times n}$. Prove
\[
\|A\|_1 = \max_{1 \leq j \leq n} \sum_{i=1}^{m} |a_{ij}|
\]
from the definition of the induced matrix $1$-norm in terms of vector $1$-norms:
\[
\|A\|_1 = \max_{\substack{x \in \mathbb{C}^n \\ \|x\|_1 = 1}} \|A x\|_1.
\]
:::
