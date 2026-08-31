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

::: problem
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

<1>1. (a) Decompose $V = (S^{(1,1)} \otimes S^{(2)} \otimes S^{(1)}) \uparrow_{S_2 \times S_2 \times S_1}^{S_5}$.
<2>1. $S^{(1,1)}$ is the sign representation of $S_2$, $S^{(2)}$ the trivial of $S_2$, $S^{(1)}$ the trivial of $S_1$.
::: {.proof}
the irreducible representations of $S_2$ are trivial $(2)$ and sign $(1,1)$; of $S_1$ only trivial $(1)$.
:::
<2>2. By the Pieri rule, $s_{(1,1)} s_{(2)} = s_{(3,1)} + s_{(2,1,1)}$.
::: {.proof}
multiplying by $s_{(2)}$ adds a horizontal strip of size $2$ to $(1,1)$.
:::
<2>3. Then $s_{(3,1)} s_{(1)} = s_{(4,1)} + s_{(3,2)} + s_{(3,1,1)}$ and $s_{(2,1,1)} s_{(1)} = s_{(3,1,1)} + s_{(2,2,1)} + s_{(2,1,1,1)}$.
::: {.proof}
multiplying by $s_{(1)}$ adds a single box in all valid ways.
:::
<2>4. Hence $V = S^{(4,1)} \oplus S^{(3,2)} \oplus 2 S^{(3,1,1)} \oplus S^{(2,2,1)} \oplus S^{(2,1,1,1)}$.
::: {.proof}
collect terms; $S^{(3,1,1)}$ appears with multiplicity $2$.
:::
<2>5. Dimensions: $\dim S^{(4,1)} = 4$, $\dim S^{(3,2)} = 5$, $\dim S^{(3,1,1)} = 6$, $\dim S^{(2,2,1)} = 5$, $\dim S^{(2,1,1,1)} = 4$.
::: {.proof}
hook-length formula.
:::

<1>2. (b) $\dim \operatorname{End}_{S_5}(V)$.
<2>1. $V = \bigoplus_\lambda m_\lambda S^\lambda$ with multiplicities $m_{(4,1)} = m_{(3,2)} = m_{(2,2,1)} = m_{(2,1,1,1)} = 1$ and $m_{(3,1,1)} = 2$.
::: {.proof}
the decomposition from <1>1.4.
:::
<2>2. $\operatorname{End}_{S_5}(V) \cong \bigoplus_\lambda M_{m_\lambda}(\CC)$.
::: {.proof}
Schur's lemma / the endomorphism algebra of a semisimple module is a product of matrix algebras.
:::
<2>3. $\dim \operatorname{End}_{S_5}(V) = \sum_\lambda m_\lambda^2 = 1 + 1 + 4 + 1 + 1 = 8$.
::: {.proof}
sum the squares of the multiplicities.
:::

<1>3. (c) Dimension of the center of $\operatorname{End}_{S_5}(V)$.
<2>1. The center of $\bigoplus_\lambda M_{m_\lambda}(\CC)$ is $\bigoplus_\lambda \CC$ (one copy of $\CC$ per block).
::: {.proof}
the center of $M_m(\CC)$ is $\CC$ (scalar matrices).
:::
<2>2. Hence $\dim Z(\operatorname{End}_{S_5}(V)) = \text{number of distinct irreducibles} = 5$.
::: {.proof}
there are five distinct irreducible summands.
:::

<1>4. Q.E.D.
::: {.proof}
<1>1.4 gives the decomposition; <1>2.3 gives $\dim \operatorname{End} = 8$; <1>3.2 gives $\dim Z = 5$.
:::
:::
