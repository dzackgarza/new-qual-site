---
schema: qual/card@1
id: E-MH2FB
kind: problem
title: Continuity of $xy^{-1}$ characterizes topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Let $H$ denote a group that is also a topological space satisfying the $T_1$ axiom.
Show that $H$ is a topological group if and only if the map of $H \times H$ into $H$ sending $x \times y$ into $x \cdot y^{-1}$ is continuous.
:::

::: {.solution}
Let $\mu(x,y)=xy$, $\iota(x)=x^{-1}$, and $\phi(x,y)=xy^{-1}$. A $T_1$ group $H$ is a topological group when $\mu\colon H\times H\to H$ and $\iota\colon H\to H$ are continuous. A map into $H\times H$ is continuous if and only if its two coordinates are.

::: pf

::: {.pf-step #forward-implication}
If $\mu$ and $\iota$ are continuous, then $\phi$ is continuous.

::: pf-proof
$\phi=\mu\circ(\operatorname{id}_H\times\iota)$, and $\operatorname{id}_H\times\iota\colon(x,y)\mapsto(x,y^{-1})$ is continuous because its coordinates $\pi_1$ and $\iota\circ\pi_2$ are.
:::

:::

::: {.pf-step #reverse-implication}
If $\phi$ is continuous, then $\iota$ and $\mu$ are continuous.

::: pf-proof
The map $j(x)=(e,x)$ is continuous, with a constant and an identity coordinate, and $\iota=\phi\circ j$ since $\phi(e,x)=x^{-1}$.
Then $\operatorname{id}_H\times\iota$ is continuous, and $\mu=\phi\circ(\operatorname{id}_H\times\iota)$ since $\phi(x,y^{-1})=xy$.
:::

:::

::: pf-qed
Steps [](#forward-implication){.pf-ref} and [](#reverse-implication){.pf-ref} give the two implications.
:::

:::

:::
