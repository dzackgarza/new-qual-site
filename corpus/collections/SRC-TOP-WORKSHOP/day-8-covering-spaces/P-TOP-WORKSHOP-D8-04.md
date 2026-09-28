---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-04
kind: problem
title: All fibers of a cover over a connected base have the same finite cardinality
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
(Purdue Jan ’09) Let $p:E\to B$ be a covering map with $B$ connected.
Suppose that $p^{-1}(b_0)$ is finite for some $b_0\in B$.
Prove that, for every $b\in B$, $p^{-1}(b)$ has the same number of elements as $p^{-1}(b_0)$.
:::

::: {.solution}
<1>1. Every $x \in B$ has an open neighborhood $U$ on which $y \mapsto |p^{-1}(y)|$ is constant.
::: {.proof}
Let $U$ be an evenly covered open neighborhood of $x$, with $p^{-1}(U) = \bigsqcup_{\alpha \in A} V_\alpha$ and each $p|_{V_\alpha}\colon V_\alpha \to U$ a homeomorphism. For $y \in U$, each $V_\alpha$ contains exactly one point of $p^{-1}(y)$, namely $(p|_{V_\alpha})^{-1}(y)$, and $p^{-1}(y) \subseteq p^{-1}(U)$. Hence $|p^{-1}(y)| = |A|$ for all $y \in U$.
:::

<1>2. With $k = |p^{-1}(b_0)|$, the set $S = \{b \in B : |p^{-1}(b)| = k\}$ is nonempty, open, and closed.
::: {.proof}
$b_0 \in S$. If $b \in S$, the neighborhood $U$ of $b$ from step <1>1 lies in $S$, so $S$ is open. If $b \notin S$, the neighborhood $U$ of $b$ from step <1>1 lies in $B \setminus S$, so $B \setminus S$ is open.
:::

<1>3. Q.E.D.
::: {.proof}
$B$ is connected and $S$ is a nonempty clopen subset by step <1>2, so $S = B$: every fiber has $k = |p^{-1}(b_0)|$ elements.
:::
:::
