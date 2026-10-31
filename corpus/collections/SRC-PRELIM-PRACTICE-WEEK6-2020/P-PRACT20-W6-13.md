---
schema: qual/card@1
id: P-PRACT20-W6-13
kind: problem
title: Continuous images of compact sets are compact
classification:
  areas:
  - prelim
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
---

::: {.problem}
Let $X, Y$ be topological spaces and let $f : X \to Y$ be continuous.
Show that $f(K)$ is compact in $Y$ for any compact set $K \subseteq X$. In short: show that the continuous image of a compact set is compact.
:::

::: {.solution}
Suppose that $K\subseteq X$ is compact, and let $\{V_i\}_{i\in I}$ be an open cover of $f(K)$. Since $f$ is continuous, the sets $U_i=f^{-1}(V_i)$ are open in $X$. If $x\in K$, then $f(x)\in V_i$ for some $i$, so $x\in U_i$. Thus $\{U_i\}$ is an open cover of $K$. Since $K$ is compact, there are $i_1,\dots,i_n$ with $K\subseteq\bigcup_{k=1}^nU_{i_k}$. Then

$$
f(K)\subseteq\bigcup_{k=1}^nf(U_{i_k})\subseteq\bigcup_{k=1}^nV_{i_k},
$$

so $V_{i_1},\dots,V_{i_n}$ is a finite subcover. Since the cover was arbitrary, $f(K)$ is compact.
:::
