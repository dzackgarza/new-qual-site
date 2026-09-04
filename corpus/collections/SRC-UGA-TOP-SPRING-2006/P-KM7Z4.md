---
schema: qual/card@1
id: P-KM7Z4
kind: problem
title: Retracts of $[0,\infty)$ are exactly its nonempty closed intervals
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Connectedness
relations: []
review: draft
---

::: {.problem}
Write $Y$ for the interval $[0, \infty)$, equipped with the usual topology.

Find, with proof, all subspaces $Z$ of $Y$ which are retracts of $Y$.
:::

::: {.solution}
The retracts are precisely the sets
\[
[a,b]\qquad(0\le a\le b<\infty)
\]
and
\[
[a,\infty)\qquad(a\ge0).
\]
Thus singletons occur when $a=b$, and $Y$ itself occurs when $a=0$ in the second family.

First suppose $Z\subseteq Y$ is a retract. Let
\[
r:Y\to Z
\]
be a retraction and let $i:Z\hookrightarrow Y$ be the inclusion. Then $e=i\circ r:Y\to Y$ is continuous and
\[
Z=\{y\in Y:e(y)=y\}.
\]
Because $Y$ is Hausdorff, the diagonal $\Delta_Y\subseteq Y\times Y$ is closed. Hence
\[
Z=(e,\operatorname{id}_Y)^{-1}(\Delta_Y)
\]
is closed in $Y$.

Also $Y=[0,\infty)$ is connected, and
\[
Z=r(Y)
\]
is connected as the continuous image of a connected space. A nonempty connected subset of $\RR$ is an interval. Therefore $Z$ is a nonempty interval that is closed in $Y$, so it has one of the two forms displayed above.

Conversely, every such interval is a retract. For $Z=[a,b]$ define
\[
r(x)=\min\{b,\max\{a,x\}\}.
\]
This is continuous, takes values in $[a,b]$, and restricts to the identity on $[a,b]$.

For $Z=[a,\infty)$ define
\[
r(x)=\max\{a,x\}.
\]
Again $r$ is continuous, has image in $Z$, and satisfies $r|_Z=\operatorname{id}_Z$. Hence precisely the nonempty closed intervals in $[0,\infty)$ are retracts.
:::
