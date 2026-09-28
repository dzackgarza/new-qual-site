---
schema: qual/card@1
id: D-TVKFM
kind: definition
title: Topological notions in a metric space
classification:
  areas:
  - real-analysis
  topics:
  - Metric Spaces
  - Closure
relations: []
review: draft
---

::: {.definition}
Let $(X,d)$ be a metric space, let $A\subseteq X$, and let $p\in X$.

- A \dfn{neighborhood} of $p$ is an open set $U_p\subseteq X$ containing $p$.

- An \dfn{$\varepsilon$-neighborhood} of $p$ is an open ball $B_\varepsilon(p) \coloneqq \theset{q\in X \suchthat d(p, q) < \varepsilon}$ for some $\varepsilon>0$.

- The point $p$ is an \dfn{accumulation point} or a \dfn{limit point} of $A$ if every punctured neighborhood $U_p\setminus\theset{p}$ contains a point $q\in A$.
  Write $A'$ for the set of limit points of $A$ and $\overline{A} \coloneqq A\cup A'$ for the \dfn{closure} of $A$.

- If $p\in A$ and $p$ is not a limit point of $A$, then $p$ is an \dfn{isolated point} of $A$.

- $A$ is \dfn{closed} if $A' \subseteq A$, so that $A$ contains all of its limit points.

- A point $p\in A$ is an \dfn{interior point} of $A$ if there is a neighborhood $U_p$ of $p$ with $U_p \subseteq A$.

- $A$ is \dfn{open} if every point of $A$ is an interior point of $A$.

- $A$ is \dfn{perfect} if $A$ is closed and $A\subseteq A'$, so that every point of $A$ is a limit point of $A$.

- $A$ is \dfn{bounded} if there are a real number $M$ and a point $q\in X$ such that $d(p, q) < M$ for all $p\in A$.

- $A$ is \dfn{dense} in $X$ if every point of $X$ lies in $A$ or is a limit point of $A$, that is, $X = A\cup A' = \overline{A}$.
:::
