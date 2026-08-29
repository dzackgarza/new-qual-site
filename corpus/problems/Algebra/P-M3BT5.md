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
**Theorem.**  
Let $F=K(\alpha_1,\dots,\alpha_n)$ be radical over $K$, and let
$K\subseteq E\subseteq F$.
Then there exist $\beta_1,\dots,\beta_m\in F$ such that
$$
F=E(\beta_1,\dots,\beta_m),\qquad \beta_r^{N_r}\in E(\beta_1,\dots,\beta_{r-1})\text{ for some }N_r>0.
$$

**Proof.**
1. Define
$$
S:=\{\alpha_i:\alpha_i\notin E\}.
$$
Then $F=E(S)$ since $K\subseteq E$ and adjoining exactly the generators outside $E$
produces $F$.

2. List $S$ in increasing index order:
$$
\alpha_{i_1},\alpha_{i_2},\dots,\alpha_{i_m},\qquad i_1<\cdots<i_m.
$$
Then
$$
F=E(\alpha_{i_1},\dots,\alpha_{i_m}).
$$

3. Let
$$
E_0:=E,\qquad E_r:=E_{r-1}(\alpha_{i_r}),\ r=1,\dots,m.
$$
   3.1 For each $r$, there is $n_{i_r}>0$ with
   $$
   \alpha_{i_r}^{n_{i_r}}\in K[\alpha_1,\dots,\alpha_{i_r-1}]
   $$
   by the radical hypothesis.
   Each factor on the right has index $<i_r$, hence is in $E_{r-1}$.
   So
   $$
   \alpha_{i_r}^{n_{i_r}}\in E_{r-1}.
   $$
   Set $N_r:=n_{i_r}$.

4. By definition,
$$
E_m=E(\alpha_{i_1},\dots,\alpha_{i_m})=E(S)=F.
$$
Thus taking $\beta_r:=\alpha_{i_r}$ gives
$$
F=E(\beta_1,\dots,\beta_m),
$$
and each step satisfies
$$
\beta_r^{N_r}\in E_{r-1}.
$$
Hence the tower is radical over $E$. ∎
:::
