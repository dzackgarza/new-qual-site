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

::: {.problem}
Suppose $F = K[\alpha_1, \cdots, \alpha_n]$ where $\alpha_1^{n_1} \in K$ for some $n_1$ and for each $i$ we have $\alpha_i^{n_i} \in K[\alpha_1, \cdots \alpha_{i-1}]$ for some powers $n_i$.
We want to show that $F = E[\beta_1, \cdots \beta_m]$ where each $\beta_i$ satisfies a similar condition.
:::

::: {.solution}
Let $F=K(\alpha_1,\dots,\alpha_n)$ be radical over $K$, and let $K\subseteq E\subseteq F$. We show there exist $\beta_1,\dots,\beta_m\in F$ such that
$$
F=E(\beta_1,\dots,\beta_m),\qquad \beta_r^{N_r}\in E(\beta_1,\dots,\beta_{r-1})\text{ for some }N_r>0.
$$

::: pf

::: pf-step

$F=E(S)$, where $S\definedas\{\alpha_i:\alpha_i\notin E\}$.

::: pf-proof

Since $K\subseteq E$, adjoining to $E$ exactly the generators $\alpha_i$ that lie outside $E$ still produces $F$.

:::

:::

::: pf-step

Listing $S=\{\alpha_{i_1},\alpha_{i_2},\dots,\alpha_{i_m}\}$ in increasing index order $i_1<\cdots<i_m$, the tower $E_0\definedas E$, $E_r\definedas E_{r-1}(\alpha_{i_r})$ satisfies $\alpha_{i_r}^{N_r}\in E_{r-1}$ for some $N_r>0$.

::: pf-proof

By the radical hypothesis there is $n_{i_r}>0$ with
$$
\alpha_{i_r}^{n_{i_r}}\in K[\alpha_1,\dots,\alpha_{i_r-1}].
$$
Each factor on the right has index $<i_r$, hence is in $E_{r-1}$. So $\alpha_{i_r}^{n_{i_r}}\in E_{r-1}$; set $N_r\definedas n_{i_r}$.

:::

:::

::: pf-step

$E_m=F$, so $\beta_r\definedas\alpha_{i_r}$ gives the required radical tower over $E$.

::: pf-proof

By definition,
$$
E_m=E(\alpha_{i_1},\dots,\alpha_{i_m})=E(S)=F,
$$
so $F=E(\beta_1,\dots,\beta_m)$, and each step satisfies $\beta_r^{N_r}\in E_{r-1}=E(\beta_1,\dots,\beta_{r-1})$. Hence the tower is radical over $E$.

:::

:::

:::

:::
