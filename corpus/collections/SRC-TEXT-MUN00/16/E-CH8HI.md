---
schema: qual/card@1
id: E-CH8HI
kind: problem
title: Product topologies under refinement of the factors
classification:
  areas:
  - topology
  topics:
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ and $X'$ denote a single set in the topologies $\mathcal{T}$ and $\mathcal{T}'$, respectively; let $Y$ and $Y'$ denote a single set in the topologies $\mathcal{U}$ and $\mathcal{U}'$, respectively.
Assume these sets are nonempty.

(a) Show that if $\mathcal{T}' \supset \mathcal{T}$ and $\mathcal{U}' \supset \mathcal{U}$, then the product topology on $X' \times Y'$ is finer than the product topology on $X \times Y$.

(b) Does the converse of (a) hold?
Justify your answer.
:::

::: {.solution}
(a) A basis for the product topology on $X\times Y$ consists of $U\times V$ with $U\in\mathcal T$ and $V\in\mathcal U$. Since $\mathcal T\subseteq\mathcal T'$ and $\mathcal U\subseteq\mathcal U'$, every such rectangle is open in the product topology on $X'\times Y'$. Hence the latter topology is finer.

(b) The converse does hold when both underlying sets are nonempty. Suppose the product topology from $(\mathcal T',\mathcal U')$ is finer than that from $(\mathcal T,\mathcal U)$. Let $U\in\mathcal T$ and choose $y_0\in Y$. Then $U\times Y$ is open in the coarser product topology and therefore in the finer one. For each $x\in U$, choose a basic finer-product neighborhood
\[
x\in U'_x,\qquad y_0\in V'_x,\qquad U'_x\times V'_x\subseteq U\times Y.
\]
Then $U'_x\subseteq U$, so
\[
U=\bigcup_{x\in U}U'_x\in\mathcal T'.
\]
Thus $\mathcal T\subseteq\mathcal T'$. The same argument using a fixed $x_0\in X$ gives $\mathcal U\subseteq\mathcal U'$.
:::
