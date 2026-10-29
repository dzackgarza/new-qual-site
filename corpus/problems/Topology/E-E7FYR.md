---
schema: qual/card@1
id: E-E7FYR
kind: problem
title: Compactness and limit-point compactness
classification:
  areas:
  - topology
  topics:
  - Compactness
relations:
- kind: related-to
  target: E-YAEMZ
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: Source printed only the two conditions "X is compact" and "Every infinite subset A of X has a limit point in X" with no question; the statement asks for the implication that holds in every topological space.
---

::: {.problem}
Show that if $X$ is compact, then every infinite subset $A\subseteq X$ has a limit point in $X$.
:::

::: {.solution}
Let $A\subseteq X$ have no limit point in $X$. We show that $A$ is finite.

::: pf

::: {.pf-step #nbhd}

Each $x\in X$ has an open neighborhood $U_x$ with $U_x\cap A\subseteq\{x\}$.

::: pf-proof

Since $x$ is not a limit point of $A$, some open $U_x\ni x$ meets $A$ in no point other than $x$.

:::

:::

::: pf-qed

By compactness, finitely many $U_{x_1},\ldots,U_{x_r}$ from step [](#nbhd){.pf-ref} cover $X$. Then $A=\bigcup_i(U_{x_i}\cap A)\subseteq\{x_1,\ldots,x_r\}$ is finite.

:::

:::

:::

::: {.remark}
The converse holds when $X$ is second countable and Hausdorff, or metrizable; see [[E-YAEMZ]].
:::
