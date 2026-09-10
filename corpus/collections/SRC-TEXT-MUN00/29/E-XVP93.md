---
schema: qual/card@1
id: E-XVP93
kind: problem
title: Closed times compact in topological groups via nets
classification:
  areas:
  - topology
  topics:
  - Nets
  - Topological Groups
relations: []
review: draft
---

::: {.exercise}

Corollary.
Let $G$ be a topological group; let $A$ and $B$ be subsets of $G$.
If $A$ is closed in $G$ and $B$ is compact, then $A \cdot B$ is closed in $G$.
[Hint: First give a proof using sequences, assuming that $G$ is metrizable.]
:::

::: {.solution}
Let \(x\) lie in the closure of \(A\cdot B\). By the closure-net theorem, choose a net
\[
a_\alpha b_\alpha\to x
\]
with \(a_\alpha\in A\) and \(b_\alpha\in B\). Since \(B\) is compact, the net \((b_\alpha)\) has an accumulation point \(b\in B\); equivalently, it has a subnet \(b_{\alpha_\beta}\to b\). Along the same subnet,
\[
a_{\alpha_\beta}b_{\alpha_\beta}\to x.
\]
Continuity of multiplication and inversion gives
\[
a_{\alpha_\beta}=(a_{\alpha_\beta}b_{\alpha_\beta})b_{\alpha_\beta}^{-1}\longrightarrow xb^{-1}.
\]
Since \(A\) is closed and all \(a_{\alpha_\beta}\in A\), we have \(xb^{-1}\in A\). Therefore
\[
x=(xb^{-1})b\in A\cdot B.
\]
Thus \(A\cdot B\) is closed.
:::
