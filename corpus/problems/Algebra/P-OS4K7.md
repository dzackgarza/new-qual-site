---
schema: qual/card@1
id: P-OS4K7
kind: problem
title: Groups of order 14
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Classify all groups of order 14 up to isomorphism. Prove your classification.
:::

::: {.solution}
Let $G$ have order $14$.

<1>1. The Sylow $7$-subgroup $P$ is unique and hence normal.
::: {.proof}
Its number $n_7$ satisfies
\[
n_7\mid2,
\qquad
n_7\equiv1\pmod7.
\]
Thus $n_7=1$. Since $|P|=7$, we have $P\cong C_7$.
:::

<1>2. If $Q$ is a Sylow $2$-subgroup, then
\[
G\cong C_7\rtimes C_2.
\]
::: {.proof}
We have $|Q|=2$, $P\cap Q=1$, and $|PQ|=14$, so $G=PQ$. Since $P\trianglelefteq G$, this is an internal semidirect product.
:::

<1>3. There are exactly two possible actions $C_2\to\Aut(C_7)$.
::: {.proof}
Since
\[
\Aut(C_7)\cong(\ZZ/7\ZZ)^\times\cong C_6,
\]
the image of the nontrivial element of $C_2$ must have order dividing $2$. The only possibilities are the identity and inversion $y\mapsto y^{-1}$.

For the trivial action,
\[
G\cong C_7\times C_2\cong C_{14}.
\]
For inversion,
\[
G\cong
\langle y,x\mid y^7=x^2=1,\;xyx^{-1}=y^{-1}\rangle,
\]
which is the dihedral group $D_7$ of order $14$.
:::

Hence, up to isomorphism, the groups of order $14$ are exactly
\[
\boxed{C_{14}\quad\text{and}\quad D_7.}
\]
:::
