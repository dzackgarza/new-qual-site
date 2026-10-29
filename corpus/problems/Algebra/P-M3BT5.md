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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source uses a field E that it never introduces; the statement declares E as an intermediate field K <= E <= F, as the title and solution read it.'
review: draft
---

::: {.problem}
Suppose $F = K[\alpha_1, \ldots, \alpha_n]$ where $\alpha_1^{n_1} \in K$ for some $n_1$ and for each $i$ we have $\alpha_i^{n_i} \in K[\alpha_1, \ldots, \alpha_{i-1}]$ for some powers $n_i$.
Let $E$ be a field with $K \subseteq E \subseteq F$.
We want to show that $F = E[\beta_1, \ldots, \beta_m]$ where each $\beta_i$ satisfies a similar condition.
:::

::: {.solution}
We show there are $\beta_1,\ldots,\beta_m\in F$ with $F=E(\beta_1,\ldots,\beta_m)$ and $\beta_r^{N_r}\in E(\beta_1,\ldots,\beta_{r-1})$ for some $N_r>0$. Let $S=\{\alpha_i:\alpha_i\notin E\}$, listed as $\alpha_{i_1},\ldots,\alpha_{i_m}$ with $i_1<\cdots<i_m$, and set $\beta_r=\alpha_{i_r}$, $E_0=E$ and $E_r=E_{r-1}(\beta_r)$.

::: pf

::: {.pf-step #generated}
$E_m=F$.

::: pf-proof
$E_m=E(S)$ contains $E\supseteq K$ and every $\alpha_i$, since an $\alpha_i$ outside $S$ lies in $E$. Hence $F=K(\alpha_1,\ldots,\alpha_n)\subseteq E_m\subseteq F$.
:::

:::

::: {.pf-step #radical}
$\beta_r^{N_r}\in E_{r-1}$ with $N_r=n_{i_r}$.

::: pf-proof
By hypothesis $\beta_r^{n_{i_r}}\in K[\alpha_1,\ldots,\alpha_{i_r-1}]$. Each $\alpha_j$ with $j<i_r$ either lies outside $S$, hence in $E$, or equals some $\beta_s$ with $s<r$; in both cases $\alpha_j\in E_{r-1}$. Also $K\subseteq E\subseteq E_{r-1}$, so $\beta_r^{N_r}\in E_{r-1}$.
:::

:::

::: pf-step
$F=E(\beta_1,\ldots,\beta_m)$ is radical over $E$.

::: pf-proof
By step [](#generated){.pf-ref}, $F=E(\beta_1,\ldots,\beta_m)$, and by step [](#radical){.pf-ref}, $\beta_r^{N_r}\in E_{r-1}=E(\beta_1,\ldots,\beta_{r-1})$ for each $r$.
:::

:::

:::

:::
