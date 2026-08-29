---
schema: qual/card@1
id: P-EMAL1
kind: problem
title: "Matrix is conjugate to its transpose"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Prove that any square matrix is conjugate to its transpose matrix.
(You may prove it over $\mathbb{C}$.)
:::

::: {.solution}
<1>1. Over $\mathbb{C}$, $A$ is similar to its Jordan canonical form $J$.
Proof: Jordan canonical form.

<1>2. $A^t$ is similar to $J^t$.
Proof: transposing the similarity $A = PJP^{-1}$ gives $A^t = (P^{-1})^t J^t P^t$.

<1>3. $J$ and $J^t$ are similar: each Jordan block $J_k(\lambda)$ is similar to its transpose $J_k(\lambda)^t$.
Proof: a Jordan block $J_k(\lambda)$ is similar to its transpose via the reversal (anti-diagonal) permutation matrix $R$ (with $1$'s on the anti-diagonal), since $R J_k(\lambda) R = J_k(\lambda)^t$.

<1>4. Hence $J$ is similar to $J^t$.
Proof: <1>3 (apply the reversal matrix blockwise).

<1>5. Therefore $A$ is similar to $A^t$.
Proof: <1>1, <1>2, <1>4 (similarity is transitive).

<1>6. Q.E.D.
Proof: <1>5.
:::
