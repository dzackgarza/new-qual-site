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
For a partition $\lambda\vdash n$, let $S^\lambda$ be the corresponding irreducible representation of the symmetric group $S_n$ over $\mathbb{C}$.

(a) Calculate the decomposition of the induced module
\[
V=\bigl(S^{(1,1)}\otimes S^{(2)}\otimes S^{(1)}\bigr)\uparrow_{S_2\times S_2\times S_1}^{S_5}
\]
into irreducible $S_5$-modules.

(b) What is the dimension of the endomorphism ring $\operatorname{End}_{S_5}(V)$ as a $\mathbb{C}$-vector space?

(c) What is the dimension of the center of the endomorphism ring $\operatorname{End}_{S_5}(V)$ as a $\mathbb{C}$-vector space?
:::

::: {.solution}
**Goal.** Decompose the induced module $V$, and compute $\dim \operatorname{End}_{S_5}(V)$ and the dimension of its center.

::: pf

::: pf-step
(a) Decompose $V = (S^{(1,1)} \otimes S^{(2)} \otimes S^{(1)}) \uparrow_{S_2 \times S_2 \times S_1}^{S_5}$.

::: pf-proof

::: pf-step
$S^{(1,1)}$ is the sign representation of $S_2$, $S^{(2)}$ the trivial of $S_2$, $S^{(1)}$ the trivial of $S_1$.

::: pf-proof
the irreducible representations of $S_2$ are trivial $(2)$ and sign $(1,1)$; of $S_1$ only trivial $(1)$.
:::

:::

::: pf-step
By the Pieri rule, $s_{(1,1)} s_{(2)} = s_{(3,1)} + s_{(2,1,1)}$.

::: pf-proof
multiplying by $s_{(2)}$ adds a horizontal strip of size $2$ to $(1,1)$.
:::

:::

::: pf-step
Then $s_{(3,1)} s_{(1)} = s_{(4,1)} + s_{(3,2)} + s_{(3,1,1)}$ and $s_{(2,1,1)} s_{(1)} = s_{(3,1,1)} + s_{(2,2,1)} + s_{(2,1,1,1)}$.

::: pf-proof
multiplying by $s_{(1)}$ adds a single box in all valid ways.
:::

:::

::: {.pf-step #s1-4}
Hence $V = S^{(4,1)} \oplus S^{(3,2)} \oplus 2 S^{(3,1,1)} \oplus S^{(2,2,1)} \oplus S^{(2,1,1,1)}$.

::: pf-proof
collect terms; $S^{(3,1,1)}$ appears with multiplicity $2$.
:::

:::

::: pf-step
Dimensions: $\dim S^{(4,1)} = 4$, $\dim S^{(3,2)} = 5$, $\dim S^{(3,1,1)} = 6$, $\dim S^{(2,2,1)} = 5$, $\dim S^{(2,1,1,1)} = 4$.

::: pf-proof
hook-length formula.
:::

:::

:::

:::

::: pf-step
(b) $\dim \operatorname{End}_{S_5}(V)$.

::: pf-proof

::: pf-step
$V = \bigoplus_\lambda m_\lambda S^\lambda$ with multiplicities $m_{(4,1)} = m_{(3,2)} = m_{(2,2,1)} = m_{(2,1,1,1)} = 1$ and $m_{(3,1,1)} = 2$.

::: pf-proof
the decomposition from step [](#s1-4){.pf-ref}.
:::

:::

::: pf-step
$\operatorname{End}_{S_5}(V) \cong \bigoplus_\lambda M_{m_\lambda}(\CC)$.

::: pf-proof
Schur's lemma / the endomorphism algebra of a semisimple module is a product of matrix algebras.
:::

:::

::: {.pf-step #s2-3}
$\dim \operatorname{End}_{S_5}(V) = \sum_\lambda m_\lambda^2 = 1 + 1 + 4 + 1 + 1 = 8$.

::: pf-proof
sum the squares of the multiplicities.
:::

:::

:::

:::

::: pf-step
(c) Dimension of the center of $\operatorname{End}_{S_5}(V)$.

::: pf-proof

::: pf-step
The center of $\bigoplus_\lambda M_{m_\lambda}(\CC)$ is $\bigoplus_\lambda \CC$ (one copy of $\CC$ per block).

::: pf-proof
the center of $M_m(\CC)$ is $\CC$ (scalar matrices).
:::

:::

::: {.pf-step #s3-2}
Hence $\dim Z(\operatorname{End}_{S_5}(V)) = \text{number of distinct irreducibles} = 5$.

::: pf-proof
there are five distinct irreducible summands.
:::

:::

:::

:::

::: pf-qed
step [](#s1-4){.pf-ref} gives the decomposition; step [](#s2-3){.pf-ref} gives $\dim \operatorname{End} = 8$; step [](#s3-2){.pf-ref} gives $\dim Z = 5$.
:::

:::
:::
