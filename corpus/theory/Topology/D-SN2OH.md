---
schema: qual/card@1
id: D-SN2OH
kind: definition
title: Neighborhoods, limit points, and open and closed sets in a metric space
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Limits
relations: []
review: draft
---

::: {.definition}
Let $(X,d)$ be a metric space, let $p\in X$, and let $E\subseteq X$.

(a) For $r>0$, the \dfn{neighborhood} of $p$ of \dfn{radius} $r$ is $N_r(p)\coloneqq\ts{q\in X\st d(p,q)<r}$.

(b) The point $p$ is a \dfn{limit point} of $E$ if every neighborhood of $p$ contains a point $q\in E$ with $q\neq p$.

(c) If $p\in E$ and $p$ is not a limit point of $E$, then $p$ is an \dfn{isolated point} of $E$.

(d) $E$ is \dfn{closed} if every limit point of $E$ belongs to $E$.

(e) The point $p$ is an \dfn{interior point} of $E$ if some neighborhood $N$ of $p$ satisfies $N\subseteq E$.

(f) $E$ is \dfn{open} if every point of $E$ is an interior point of $E$.

(g) The \dfn{complement} of $E$ is $E^c\coloneqq\ts{p\in X\st p\notin E}$.

(h) $E$ is \dfn{perfect} if $E$ is closed and every point of $E$ is a limit point of $E$.

(i) $E$ is \dfn{bounded} if there are $M\in\RR$ and $q\in X$ with $d(p,q)<M$ for all $p\in E$.

(j) $E$ is \dfn{dense} in $X$ if every point of $X$ is a limit point of $E$ or a point of $E$, or both.
:::

::: {.remark}
In (b) the point $q$ must differ from $p$: a limit point of $E$ is one whose punctured neighborhoods $N_r(p)\setminus\ts{p}$ all meet $E$.
A point of $E$ is therefore either a limit point or an isolated point of $E$, but not both.
:::
