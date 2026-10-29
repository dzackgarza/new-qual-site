---
schema: qual/card@1
id: P-SEPDEF-01
kind: problem
title: Closure-neighborhood characterization of regularity
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
  note: Checked against the retained one-page Separation and countability definitions PDF; this is the first of its two explicit “Useful facts that you should prove.”
---

::: {.problem}
Prove that a topological space $X$ is regular if and only if $X$ is $T_1$ and, for every $x\in X$ and every open set $U$ containing $x$, there is an open set $V$ containing $x$ such that
$$
\overline V\subseteq U.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose $X$ is regular. Then $X$ is $T_1$, and for every $x\in U$ with $U$ open there is an open set $V$ containing $x$ such that
$$
\overline V\subseteq U.
$$


::: pf-proof

Regularity includes the $T_1$ condition. Let $x\in U$ with $U$ open, and put
$$
F\coloneqq X\setminus U.
$$
Then $F$ is closed and $x\notin F$. By regularity there are disjoint open sets $V,W$ such that
$$
x\in V,
\qquad
F\subseteq W.
$$
Since $W$ is open and disjoint from $V$, the closed set $X\setminus W$ contains $V$, hence
$$
\overline V\subseteq X\setminus W.
$$
Also $F\subseteq W$ implies
$$
X\setminus W\subseteq X\setminus F=U.
$$
Therefore $\overline V\subseteq U$.

:::

:::

::: {.pf-step #s1-2}

Conversely, suppose $X$ is $T_1$ and has the stated closure-neighborhood property. Then $X$ is regular.


::: pf-proof

Let $x\in X$ and let $F\subseteq X$ be closed with $x\notin F$. The set
$$
U\coloneqq X\setminus F
$$
is open and contains $x$. By hypothesis there is an open set $V$ with
$$
x\in V,
\qquad
\overline V\subseteq U.
$$
Set
$$
W\coloneqq X\setminus\overline V.
$$
Then $W$ is open. Since $\overline V\subseteq X\setminus F$, one has $F\subseteq W$. Moreover $V\cap W=\varnothing$. Thus the point $x$ and the closed set $F$ have disjoint open neighborhoods. Together with the assumed $T_1$ property, this is regularity.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the forward implication, and step [](#s1-2){.pf-ref} proves the converse.

:::

:::

:::
