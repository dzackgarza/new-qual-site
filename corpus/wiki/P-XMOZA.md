---
schema: qual/card@1
id: P-XMOZA
kind: problem
title: Connectedness of $\{(x,y)\in\RR^2:x>0,\,y\geq 0,\,y/x\in\QQ\}$
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Subspace Topology
  - Euclidean Spaces
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let
\begin{align*}
X=\left\{(x, y) \in \mathbb{R}^{2} | x>0, y \geq 0, \text { and } \frac{y}{x} \text { is rational }\right\}
\end{align*}
and equip $X$ with the subspace topology induced by the usual topology on $\RR^2$.

Prove or disprove that $X$ is connected.
:::

::: {.remark}
Not convincing..
:::

::: {.solution}
\envlist

- Consider the (continuous) projection $\pi: \RR^2 \to \RP^1$ given by $(x, y) \mapsto [y/x, 1]$ in homogeneous coordinates.

  - I.e. this sends points to lines through the origin with rational slope).

- Note that the image of $\pi$ is $\RP^1\setminus\theset{\infty}$, which is homeomorphic to $\RR$.

- If we now define $f = \restrictionof{\pi}{X}$, we have $f(X) \surjects \QQ \subset \RR$.

- If $X$ were connected, then $f(X)$ would also be connected, but $\QQ \subset \RR$ is disconnected, a contradiction.
:::
