---
schema: qual/card@1
id: D-4QNEW
kind: definition
title: $n$-connected spaces and pairs
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Connectedness
  - Fundamental Group
relations: []
review: draft
---

::: {.definition}
Let $n\geq 0$.
A nonempty topological space $X$ is \dfn{$n$-connected} if $X$ is [[D-X73EB|path-connected]] and $\pi_i(X, x_0) = 0$ for all $1\leq i\leq n$ and all $x_0\in X$.
A pair $(X, A)$ with $A\subseteq X$ is \dfn{$n$-connected} if every path component of $X$ meets $A$ and the [[D-VUDRJ|relative homotopy groups]] satisfy $\pi_i(X, A, x_0) = 0$ for all $1\leq i\leq n$ and all $x_0\in A$.
:::

::: {.remark}
A space is $0$-connected if and only if it is path-connected, and $1$-connected if and only if it is [[D-GFM35|simply connected]].
:::

::: {.concept}
[@Hat02, §4.1, p. 346].
:::
