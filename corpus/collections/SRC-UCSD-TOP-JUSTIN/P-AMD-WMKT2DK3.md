---
schema: qual/card@1
id: P-AMD-WMKT2DK3
kind: problem
title: A path-connected space is simply connected iff every map $S^1\to X$ extends
  over $B^2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Show that for $X$ path connected, $\pi_1(X) = \mathbb{1} \iff \forall \text{cts.}~f: S^1 \rightarrow X$ $f$, extends to a continuous map $F: B^2 \rightarrow X$.
:::

::: {.solution}
<1>1. If every continuous map $f:S^1\to X$ extends to $F:B^2\to X$, then $\pi_1(X)$ is trivial.
::: {.proof}
Let $f:S^1\to X$ be any based loop. If $F:B^2\to X$ extends $f$, then contracting $B^2$ to its center and composing with $F$ gives a free null-homotopy of $f$. Since $X$ is path connected, a freely null-homotopic based loop represents the identity in $\pi_1(X)$: if the free null-homotopy moves the basepoint along a path $\gamma$, the original loop represents the conjugate by $\gamma$ of the constant loop, hence is trivial. Thus every element of $\pi_1(X)$ is the identity.
:::

<1>2. Conversely, assume $X$ is path connected and $\pi_1(X)=1$. Then every map $f:S^1\to X$ is null-homotopic.
::: {.proof}
Choose a point $s_0\in S^1$. The map $f$ is a loop based at $f(s_0)$. Since the fundamental group at that basepoint is trivial, there is a homotopy $H:S^1\times I\to X$ from $f$ to the constant map at $f(s_0)$.
:::

<1>3. A null-homotopy of $f$ is equivalent to an extension over $B^2$.
::: {.proof}
Identify
$$
B^2\cong S^1\times I/(S^1\times\{1\}),
$$
with $S^1\times\{0\}$ as the boundary. If $H$ is the null-homotopy from <1>2, then $H$ is constant on $S^1\times\{1\}$, so it descends through this quotient to a continuous map $F:B^2\to X$ whose restriction to the boundary is $f$.
:::

<1>4. Hence
$$
\boxed{\pi_1(X)=1\iff\text{every continuous }S^1\to X\text{ extends over }B^2.}
$$
::: {.proof}
Combine <1>1--<1>3.
:::
:::
