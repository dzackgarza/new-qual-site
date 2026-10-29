---
schema: qual/card@1
id: P-APAS18F
kind: problem
title: Induced Specht product for $S_5$; dimensions of $\operatorname{End}_{S_5}(V)$ and its center
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
For a partition $\lambda\vdash n$, let $S^\lambda$ be the corresponding irreducible representation of the symmetric group $S_n$ over $\CC$.

(a) Calculate the decomposition of the induced module
$$
V=\bigl(S^{(1,1)}\otimes S^{(2)}\otimes S^{(1)}\bigr)\uparrow_{S_2\times S_2\times S_1}^{S_5}
$$
into irreducible $S_5$-modules.

(b) What is the dimension of the endomorphism ring $\operatorname{End}_{S_5}(V)$ as a $\CC$-vector space?

(c) What is the dimension of the center of the endomorphism ring $\operatorname{End}_{S_5}(V)$ as a $\CC$-vector space?
:::

::: {.solution}
Induction from a Young subgroup corresponds to multiplication of Schur functions, and $S^{(1,1)}$, $S^{(2)}$, $S^{(1)}$ have Frobenius characteristics $s_{(1,1)}$, $s_{(2)}$, $s_{(1)}$, so the Frobenius characteristic of $V$ is $s_{(1,1)}s_{(2)}s_{(1)}$.

::: pf

::: {.pf-step #decomposition}

(a) $V\cong S^{(4,1)}\oplus S^{(3,2)}\oplus 2S^{(3,1,1)}\oplus S^{(2,2,1)}\oplus S^{(2,1,1,1)}$.

::: pf-proof

By the Pieri rule, $s_{(1,1)}s_{(2)}$ adds a horizontal strip of two boxes to $(1,1)$, giving $s_{(3,1)}+s_{(2,1,1)}$; the shape $(2,2)$ is excluded because its two new boxes share a column. Multiplying by $s_{(1)}$ adds one box in every possible way: $s_{(3,1)}s_{(1)}=s_{(4,1)}+s_{(3,2)}+s_{(3,1,1)}$ and $s_{(2,1,1)}s_{(1)}=s_{(3,1,1)}+s_{(2,2,1)}+s_{(2,1,1,1)}$. As a check, the hook length formula gives dimensions $4+5+2\cdot6+5+4=30=5!/(2!\,2!\,1!)=\dim V$.

:::

:::

::: pf-step

(b) $\dim\operatorname{End}_{S_5}(V)=\boxed{8}$.

::: pf-proof

By Schur's lemma, $\operatorname{End}_{S_5}\bigl(\bigoplus_\lambda (S^\lambda)^{m_\lambda}\bigr)\cong\prod_\lambda M_{m_\lambda}(\CC)$, of dimension $\sum_\lambda m_\lambda^2$. Step [](#decomposition){.pf-ref} gives multiplicities $1,1,2,1,1$, so the dimension is $1+1+4+1+1$.

:::

:::

::: pf-step

(c) The center of $\operatorname{End}_{S_5}(V)$ has dimension $\boxed{5}$.

::: pf-proof

The center of $\prod_\lambda M_{m_\lambda}(\CC)$ is the product of the scalar matrices, one copy of $\CC$ for each $\lambda$ with $m_\lambda>0$; step [](#decomposition){.pf-ref} has five such $\lambda$.

:::

:::

:::
:::
