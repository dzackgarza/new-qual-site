---
schema: qual/card@1
id: P-SEPDEF-02
kind: problem
title: Closure-neighborhood characterization of normality
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained one-page Separation and countability definitions PDF; this is the second of its two explicit “Useful facts that you should prove.”
---

::: {.problem}
Prove that a topological space $X$ is normal if and only if $X$ is $T_1$ and, for every closed set $A\subseteq X$ and every open set $U$ containing $A$, there is an open set $V$ containing $A$ such that
$$
\overline V\subseteq U.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose $X$ is normal. Then $X$ is $T_1$, and whenever $A\subseteq U$ with $A$ closed and $U$ open, there is an open set $V$ containing $A$ such that
$$
\overline V\subseteq U.
$$


::: pf-proof

Normality includes the $T_1$ condition. Let $A$ be closed and let $U$ be open with $A\subseteq U$. Put
$$
B\coloneqq X\setminus U.
$$
Then $B$ is closed and $A\cap B=\varnothing$. By normality there are disjoint open sets $V,W$ satisfying
$$
A\subseteq V,
\qquad
B\subseteq W.
$$
Since $W$ is open and disjoint from $V$, the closed set $X\setminus W$ contains $V$, so
$$
\overline V\subseteq X\setminus W.
$$
Because $B\subseteq W$,
$$
X\setminus W\subseteq X\setminus B=U.
$$
Therefore $\overline V\subseteq U$.

:::

:::

::: {.pf-step #s1-2}

Conversely, suppose $X$ is $T_1$ and has the stated closure-neighborhood property. Then $X$ is normal.


::: pf-proof

Let $A,B\subseteq X$ be disjoint closed sets. The set
$$
U\coloneqq X\setminus B
$$
is open and contains $A$. By hypothesis there is an open set $V$ such that
$$
A\subseteq V,
\qquad
\overline V\subseteq U.
$$
Set
$$
W\coloneqq X\setminus\overline V.
$$
Then $W$ is open. Since $\overline V\subseteq X\setminus B$, one has $B\subseteq W$, and clearly $V\cap W=\varnothing$. Thus $A$ and $B$ have disjoint open neighborhoods. Together with the assumed $T_1$ property, this is normality.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the forward implication, and step [](#s1-2){.pf-ref} proves the converse.

:::

:::

:::
