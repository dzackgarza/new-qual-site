---
schema: qual/card@1
id: P-M3BT5
kind: problem
title: A radical extension is radical over any intermediate field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Solvable Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Suppose $F = K[\alpha_1, \cdots, \alpha_n]$ where $\alpha_1^{n_1} \in K$ for some $n_1$ and for each $i$ we have $\alpha_i^{n_i} \in K[\alpha_1, \cdots \alpha_{i-1}]$ for some powers $n_i$.
We want to show that $F = E[\beta_1, \cdots \beta_m]$ where each $\beta_i$ satisfies a similar condition.
:::

::: solution
Let
\[
S=\{\alpha_i\in F:\alpha_i\notin E\}.
\]
Since $F=K(\alpha_1,\dots,\alpha_n)$ and $K\subseteq E$, adjoining all elements of $S$ to $E$ gives
\[
F=E(S).
\]
Write the elements of $S$ in increasing index order
\[
\alpha_{i_1},\alpha_{i_2},\dots,\alpha_{i_m},\qquad i_1<i_2<\cdots<i_m.
\]
Define recursively
\[
E_0:=E,\qquad E_r:=E_{r-1}(\alpha_{i_r}),\ r=1,\dots,m.
\]

For each $r$, by hypothesis
\[
\alpha_{i_r}^{n_{i_r}}\in K[\alpha_1,\dots,\alpha_{i_r-1}]
\]
for some $n_{i_r}>0$.
Every factor $\alpha_j$ with $j<i_r$ either belongs to $E$ or is among
$\alpha_{i_1},\dots,\alpha_{i_{r-1}}$, so
\[
K[\alpha_1,\dots,\alpha_{i_r-1}] \subseteq E_{r-1}.
\]
Hence $\alpha_{i_r}^{n_{i_r}}\in E_{r-1}$ and $E_r=E_{r-1}(\alpha_{i_r})$ is a radical extension.

After $m$ steps,
\[
E_m=E(\alpha_{i_1},\dots,\alpha_{i_m})=E(S)=F.
\]
So $F=E[\beta_1,\dots,\beta_m]$ with $\beta_r=\alpha_{i_r}$ and the required radical conditions.
:::
