---
schema: qual/card@1
id: D-4DXA7
kind: definition
title: Separation axioms
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Separation Axioms
  - Hausdorff Spaces
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
Two subsets $S, T\subseteq X$ are \dfn{separated by neighborhoods} if there exist disjoint open sets $U\supseteq S$ and $V\supseteq T$.

- $X$ is \dfn{$T_0$} if for all $x\neq y$ in $X$ there exists an open set containing exactly one of $x$ and $y$.

- $X$ is \dfn{$T_1$} if for all $x\neq y$ in $X$ there exists an open set containing $x$ and not $y$.

- $X$ is \dfn{$T_2$}, or [[D-ZFRV4|Hausdorff]], if for all $x\neq y$ in $X$ the sets $\ts{x}$ and $\ts{y}$ are separated by neighborhoods.

- $X$ is \dfn{$T_{2\frac12}$} if for all $x\neq y$ in $X$ there exist open sets $U\ni x$ and $V\ni y$ with $\cl_X(U)\intersect\cl_X(V) = \emptyset$.

- $X$ is \dfn{$T_3$} if it is $T_0$ and [[D-EPTMG|regular]]: for every $x\in X$ and every closed $F\subseteq X$ with $x\notin F$, the sets $\ts{x}$ and $F$ are separated by neighborhoods.

- $X$ is \dfn{$T_{3\frac12}$} if it is $T_0$ and completely regular: for every $x\in X$ and every closed $F\subseteq X$ with $x\notin F$ there exists a continuous $f\colon X\to[0,1]$ with $f(x) = 0$ and $f(F)\subseteq\ts{1}$.

- $X$ is \dfn{$T_4$} if it is $T_1$ and [[D-YEQC3|normal]]: any two disjoint closed subsets of $X$ are separated by neighborhoods.
:::

::: {.remark}
A space is $T_1$ if and only if every singleton is closed.
:::

::: {.concept}
[@Mun00].
:::
