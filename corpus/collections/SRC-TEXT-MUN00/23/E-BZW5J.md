---
schema: qual/card@1
id: E-BZW5J
kind: problem
title: Unions of connected sets meeting a common connected set
classification:
  areas:
  - topology
  topics:
  - Connectedness
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

Let $\ts{A_\alpha}$ be a collection of connected subspaces of $X$; let $A$ be a connected subspace of $X$.
Show that if $A \cap A_\alpha \neq \varnothing$ for all $\alpha$, then $A \cup (\bigcup A_\alpha)$ is connected.
:::

::: {.solution}
Let
\[
C=A\cup\bigcup_\alpha A_\alpha.
\]
Suppose $C=U\cup V$ is a separation. Since $A$ is connected, it lies entirely in one side, say $A\subseteq U$. For each $\alpha$, the connected set $A_\alpha$ meets $A$, hence meets $U$. Therefore $A_\alpha$ cannot meet $V$, so $A_\alpha\subseteq U$. Thus $C\subseteq U$, contradicting that $V$ is nonempty. Hence $C$ is connected.
:::
