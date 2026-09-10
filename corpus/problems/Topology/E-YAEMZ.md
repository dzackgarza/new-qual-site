---
schema: qual/card@1
id: E-YAEMZ
kind: problem
title: Compactness, limit point compactness, and sequential compactness in second-countable Hausdorff or metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Countability
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}
Show that if $X$ is second countable and Hausdorff, or a metric space, then TFAE:

- $X$ is compact;

- Every infinite subset $A\subseteq X$ has a limit point in $X$;

- Every sequence in $X$ has a convergent subsequence in $X$.
:::

::: {.solution}
<1>1. If $X$ is compact and Hausdorff (hence $T_1$), every infinite subset $A\subseteq X$ has a limit point.
::: {.proof}
Assume $A$ has no limit point. For each $x\in X$ choose an open neighborhood $U_x$ meeting $A$ in at most the point $x$ itself. A finite subcover $U_{x_1},\dots,U_{x_r}$ would then meet $A$ in at most finitely many points, contradicting infinitude of $A$.
:::

<1>2. If $X$ is first countable and every infinite subset has a limit point, then every sequence has a convergent subsequence.
::: {.proof}
Given $(x_n)$, if some value occurs infinitely often, take a constant subsequence. Otherwise its range contains an infinite subset $A$ of distinct values. Let $x$ be a limit point of $A$, and choose a nested countable neighborhood basis $U_1\supseteq U_2\supseteq\cdots$ at $x$. Inductively choose distinct sequence terms $x_{n_k}\in U_k$ with $n_1<n_2<\cdots$. Then $x_{n_k}\to x$.
:::

<1>3. If $X$ is second countable and every sequence has a convergent subsequence, then $X$ is compact.
::: {.proof}
Second countability implies Lindelöf, so every open cover has a countable subcover $U_1,U_2,\dots$. If no finite subfamily covers $X$, choose
$$x_n\in X\setminus(U_1\cup\cdots\cup U_n).$$
A convergent subsequence $x_{n_k}\to x$ must eventually lie in some $U_m$ containing $x$, but for $n_k\ge m$ the construction forces $x_{n_k}\notin U_m$, a contradiction.
:::

<1>4. Therefore, in every second-countable Hausdorff space, compactness, limit-point compactness, and sequential compactness are equivalent.
::: {.proof}
Second countability implies first countability, so <1>1--<1>3 form a cycle of implications.
:::

<1>5. The same equivalence holds for every metric space.
::: {.proof}
The implications compact $\Rightarrow$ limit-point compact and limit-point compact $\Rightarrow$ sequentially compact follow from <1>1--<1>2 because metric spaces are Hausdorff and first countable. Conversely, a sequentially compact metric space is totally bounded: otherwise one can construct an $\varepsilon$-separated sequence with no convergent subsequence. For each $m$ choose a finite $1/m$-net; the union of these nets is countable and dense, so the metric space is second countable. Now apply <1>3.
:::
:::
