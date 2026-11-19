---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-W1
kind: problem
title: A compact subset of a $T_2$ space is closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained sheet `assets/attachments/Day_1_-_Compactness_Problems.pdf`: the statement
    is the first of its three warm-up problems, and its printed words are the card's. The sheet is
    named in the solution's opening sentence. Not checked in this pass: the argument, which the edit
    does not touch.
---

::: {.problem}
If $X$ is $T_2$ and $A\subseteq X$ is compact, then $A$ is closed.
:::

::: {.solution}
This is the first warm-up problem of the Day 1 sheet (Compactness) of the topology qual workshop, retained in this repository as `assets/attachments/Day_1_-_Compactness_Problems.pdf`; the statement below is its wording.

::: pf

::: {.pf-step #s1}

Every $x \in X \setminus A$ has an open neighborhood disjoint from $A$.

::: pf-proof

For each $a \in A$, since $X$ is Hausdorff and $x \neq a$, choose disjoint open sets $U_a \ni x$ and $V_a \ni a$. The sets $V_a$ cover $A$, so by compactness $A \subseteq V_{a_1} \cup \cdots \cup V_{a_k}$ for some $a_1, \ldots, a_k \in A$. Put $U = U_{a_1} \cap \cdots \cap U_{a_k}$, an open set containing $x$. Since $U \subseteq U_{a_i}$ and $U_{a_i} \cap V_{a_i} = \varnothing$ for each $i$, $U$ is disjoint from $V_{a_1} \cup \cdots \cup V_{a_k} \supseteq A$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $X \setminus A$ is a union of open sets, hence open, so $A$ is closed.

:::

:::

:::
