---
schema: qual/card@1
id: D-5EOQZ
kind: definition
title: Locally compact space
prompts:
- What does it mean for a space to be locally compact?
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
A topological space $X$ is \dfn{locally compact} if every $x\in X$ has a [[D-JMRPA|neighborhood]] $U$ contained in a [[D-EILKJ|compact]] subset $K\subseteq X$.
:::

::: {.example}
Every compact space $X$ is locally compact, with $U = K = X$.
The converse fails: for $n\geq 1$, $\RR^n$ is locally compact, since each $x$ lies in an open ball whose closure is compact, but $\RR^n$ is not compact.
:::

::: {.example}
The following subspaces of Euclidean space are not locally compact:

- $\QQ\subseteq\RR$;

- $\ts{\mathbf 0} \union \ts{(x, y)\in\RR^2 \st x>0} \subseteq\RR^2$, in which the origin has no neighborhood contained in a compact subset.
:::

::: {.remark}
Some authors also require a locally compact space to be Hausdorff.
For Hausdorff $X$ the condition above is equivalent to every point having a neighborhood whose closure is compact.
:::

::: {.concept}
[@Mun00].
:::
