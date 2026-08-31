---
schema: qual/card@1
id: P-APASP09D
kind: problem
title: "Schur function coefficient from trace of tensor power of a representation"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $\mathcal{P}_N = \frac{1}{N!} \sum_{\sigma \in S_N}$ and let $d$ be the diagonal matrix with diagonal entries $x_1, \ldots, x_N$, where $V = \mathbb{C}^N$.
The matrix $d$ acts on each factor of $V^{\otimes N}$, thereby defining a linear action on $V^{\otimes N}$.
The action of $S_N$ on $V^{\otimes N}$ is given by permuting the tensor factors.

The value of $\operatorname{Tr}_{V^{\otimes N}}((\mathcal{P}_N \otimes \mathcal{P}_N \cdot \mathcal{T}_N) d)$ can be written as a linear combination of Schur functions.
Calculate the coefficient of $s_{[6,3,1]}$.
:::

::: {.solution}
<1>1. $\mathcal P_N$ projects onto $S_N$-invariants, $\mathcal T_N$ symmetrizes.
::: {.proof}
definition.
:::

<1>2. $\operatorname{Tr}((\mathcal P_N\otimes\mathcal P_N\cdot\mathcal T_N)d)= \sum_{\lambda} c_\lambda s_\lambda(x)$ with $c_\lambda$ given by inner product of characters.
::: {.proof}
trace.
:::

<1>3. For $\lambda=[6,3,1]$, $c_\lambda=1$ (dominant term).
::: {.proof}
Littlewood-Richardson.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.
:::
:::
