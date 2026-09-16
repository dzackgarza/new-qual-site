---
schema: qual/card@1
id: T-YOZX6
kind: theorem
title: Characterizations of compact subsets of a metric space
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
---

::: {.theorem}
Let $(X,d)$ be a metric space and let $E\subseteq X$, with the metric induced by $d$.
The following are equivalent [@Fol13, Proposition 0.25]:

(a) $E$ is [[D-G5N6I|complete]] and totally bounded: for every $\varepsilon>0$, $E$ is covered by finitely many balls of radius $\varepsilon$.

(b) $E$ is sequentially compact: every sequence in $E$ has a subsequence that converges to a point of $E$.

(c) $E$ is [[D-EILKJ|compact]]: every cover of $E$ by open subsets of $X$ has a finite subcover.
:::

::: {.remark}
If $X$ is complete, then $E$ is complete if and only if $E$ is closed in $X$.
In $\RR^n$ with the Euclidean metric, $E$ is totally bounded if and only if $E$ is [[D-2GCTV|bounded]]; combined with the theorem, this gives the Heine--Borel theorem.
In a general metric space, a closed bounded subset need not be compact: in an infinite set with the discrete metric $d(x,y)=1$ for $x\neq y$, the whole space is closed and bounded but not totally bounded.
:::
