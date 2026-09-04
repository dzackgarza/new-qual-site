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
<1>1. The retracts are precisely the sets
\[
[a,b]\qquad(0\le a\le b<\infty)
\]
and
\[
[a,\infty)\qquad(a\ge0).
\]
Thus singletons occur when $a=b$, and $Y$ itself occurs when $a=0$ in the second family.
::: {.proof}
Steps <1>2--<1>4 show that every retract has one of these forms, and steps <1>5--<1>6 construct retractions onto every set in the list.
:::

<1>2. Every retract $Z\subseteq Y$ is closed in $Y$.
::: {.proof}
Let
\[
r:Y\to Z
\]
be a retraction and let $i:Z\hookrightarrow Y$ be the inclusion.
Then $e=i\circ r:Y\to Y$ is continuous and
\[
Z=\{y\in Y:e(y)=y\}.
\]
Because $Y$ is Hausdorff, the diagonal $\Delta_Y\subseteq Y\times Y$ is closed.
Hence
\[
Z=(e,\operatorname{id}_Y)^{-1}(\Delta_Y)
\]
is closed in $Y$.
:::

<1>3. Every retract $Z\subseteq Y$ is connected.
::: {.proof}
The space $Y=[0,\infty)$ is connected, and
\[
Z=r(Y)
\]
is connected as the continuous image of a connected space.
:::

<1>4. Every retract $Z\subseteq Y$ has one of the forms listed in <1>1.
::: {.proof}
By <1>3, $Z$ is a nonempty connected subset of $\RR$, hence an interval. By <1>2 it is closed in the subspace $Y=[0,\infty)$. The nonempty closed intervals in $Y$ are exactly the bounded intervals $[a,b]$ with $0\le a\le b<\infty$ and the rays $[a,\infty)$ with $a\ge0$.
:::

<1>5. Every bounded interval $[a,b]$ listed in <1>1 is a retract of $Y$.
::: {.proof}
Define
\[
r(x)=\min\{b,\max\{a,x\}\}.
\]
This is continuous, takes values in $[a,b]$, and restricts to the identity on $[a,b]$.
:::

<1>6. Every ray $[a,\infty)$ listed in <1>1 is a retract of $Y$.
::: {.proof}
Define
\[
r(x)=\max\{a,x\}.
\]
Again $r$ is continuous, has image in $Z$, and satisfies $r|_Z=\operatorname{id}_Z$.
:::

<1>7. The classification in <1>1 is complete.
::: {.proof}
Necessity is <1>4 and sufficiency is <1>5--<1>6.
:::
:::
