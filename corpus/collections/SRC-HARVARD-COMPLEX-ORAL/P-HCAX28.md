---
schema: qual/card@1
id: P-HCAX28
kind: problem
title: Analytic continuation and its uniqueness
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Continuation
relations: []
review: draft
---

::: problem
Define analytic continuation and prove its uniqueness.
:::

::: solution
Let $U,V\subset\mathbb C$ be domains, let $f$ be holomorphic on $U$, and let $g$ be holomorphic on $V$. We say that $g$ is an analytic continuation of $f$ to $V$ if there is a nonempty connected open set
\[
W\subset U\cap V
\]
on which
\[
g=f.
\]
More generally, analytic continuation along a chain of overlapping domains is obtained by repeating this condition on successive overlaps.

The uniqueness is an immediate consequence of the identity theorem. Suppose $g_1$ and $g_2$ are holomorphic on the same connected domain $V$ and both continue $f$. Then there is a nonempty open subset $W\subset V$ on which
\[
g_1=f=g_2.
\]
Thus $g_1-g_2$ is holomorphic on $V$ and vanishes on the nonempty open set $W$. By the identity theorem,
\[
g_1-g_2\equiv0
\]
on $V$, so
\[
g_1=g_2.
\]

Likewise, if two analytic continuations are defined on different domains, they agree on every connected component of their overlap that contains an open set on which both descend from the same previous branch.

This is the precise uniqueness statement. Analytic continuation along different paths need not give a single global branch on a nonsimply connected domain; that stronger path-independence statement requires an additional monodromy hypothesis.
:::
