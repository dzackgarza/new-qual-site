---
schema: qual/card@1
id: P-TOPS02J
kind: problem
title: "Restriction of a covering map to a connected component is a covering map"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

::: {.problem}
Let $p : E \to X$ be a covering space and let $C \subset E$ be a connected component of $E$.
Prove $p|_C : C \to X$ is also a covering space.
:::

::: {.solution}
<1>1. The statement as printed is false when the base is disconnected.
::: {.proof}
Let $X=X_1\sqcup X_2$ be a disjoint union of two nonempty connected spaces and take the identity covering $p:E=X\to X$. If $C=X_1$ is a connected component of $E$, then $p|_C:C\to X$ is not surjective, hence is not a covering map onto $X$ under the usual convention that coverings are surjective.
:::

<1>2. If the base $X$ is path-connected, then the restriction of a covering map to any connected component $C$ of $E$ is a covering map $C\to X$.
::: {.proof}
Fix $c_0\in C$ and $x_0=p(c_0)$. For any $x\in X$, choose a path $\gamma$ from $x_0$ to $x$. Its lift beginning at $c_0$ remains in the connected component $C$ and ends over $x$. Hence $p(C)=X$.

Now let $U$ be an evenly covered neighborhood in $X$. Each sheet $V$ of $p^{-1}(U)$ is connected after replacing $U$ by a path-connected evenly covered neighborhood if necessary; a sheet meeting $C$ lies entirely in $C$. Therefore
$$C\cap p^{-1}(U)$$
is a disjoint union of sheets, each mapped homeomorphically onto $U$. Thus $p|_C$ is a covering map.
:::
:::
