---
schema: qual/card@1
id: D-EUX36
kind: definition
title: Homotopy groups
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Fundamental Group
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $x_0\in X$, and $n\geq 1$, and let $I^n = [0,1]^n$ with boundary $\del I^n$.
The \dfn{$n$th homotopy group} $\pi_n(X, x_0)$ is the set of [[D-IZI3T|homotopy classes]] of maps $f\colon(I^n, \del I^n)\to(X, x_0)$, where the homotopies $f_t$ are required to satisfy $f_t(\del I^n) = \ts{x_0}$ for all $t$, with the operation $[f]+[g]\coloneqq[f+g]$ given by
$$
(f+g)(s_1, s_2, \ldots, s_n)\coloneqq
\begin{cases}
f(2s_1, s_2, \ldots, s_n) & 0\leq s_1\leq 1/2, \\
g(2s_1-1, s_2, \ldots, s_n) & 1/2\leq s_1\leq 1.
\end{cases}
$$
:::

::: {.proposition}
For $n\geq 1$ the operation on $\pi_n(X, x_0)$ is well defined and makes $\pi_n(X, x_0)$ a group, and $\pi_1(X, x_0)$ is the [[D-EBNUE|fundamental group]].
For $n\geq 2$ the group $\pi_n(X, x_0)$ is abelian.
Since $I^n/\del I^n\cong S^n$, the set $\pi_n(X, x_0)$ is in bijection with the set $[(S^n, s_0), (X, x_0)]$ of based homotopy classes of based maps $(S^n, s_0)\to(X, x_0)$.
:::

::: {.concept}
See [@Hat02, §4.1, p. 340].
:::
