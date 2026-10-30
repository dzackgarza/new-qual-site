---
schema: qual/card@1
id: P-LCTOJ
kind: problem
title: $\pi_1$ and $H_*$ of $\RR^3$ minus a tetrahedron's $1$-skeleton
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Compute the fundamental group $\pi_1(X)$ and the homology groups $H_*(X;\ZZ)$ of the space $X$ obtained by removing the $1$-skeleton of a regular tetrahedron (that is, the union of the six closed line segments which are the edges) from $\RR^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #handlebody}

Let $\Gamma$ be the $1$-skeleton and $N$ a closed regular neighbourhood of $\Gamma$ in $S^3 = \RR^3 \cup \{\infty\}$. Then $S^3 \setminus \Gamma \simeq S^3 \setminus \mathring N$, and $S^3 \setminus \mathring N$ is a handlebody of genus $3$, so $S^3 \setminus \Gamma \simeq S^1 \vee S^1 \vee S^1$.

::: pf-proof

$S^3\setminus\Gamma$ deformation retracts onto $S^3\setminus\mathring N$ along the collar $N\setminus\Gamma \cong \partial N\times(0,1]$.
$\Gamma$ is a connected graph with $4$ vertices and $6$ edges, so $N$ is a handlebody of genus $1-\chi(\Gamma) = 1-(4-6) = 3$.
$\Gamma$ lies on the boundary sphere $S$ of the solid tetrahedron $\Delta$, so it is unknotted: the closure of $S^3\setminus \Delta$ is a $3$-ball, and $S^3\setminus\mathring N$ is obtained from the two $3$-balls $\Delta$ and $S^3\setminus\mathring\Delta$, each slightly shrunk away from $\Gamma$, by joining them with one $1$-handle through each of the four faces of $\partial\Delta$. Two balls joined by four $1$-handles form a handlebody of genus $4-1=3$, which deformation retracts onto a wedge of three circles.

:::

:::

::: {.pf-step #puncture}

$X = \RR^3\setminus\Gamma$ is $S^3\setminus\Gamma$ with the point $\infty$ removed, and $X \simeq S^1\vee S^1\vee S^1\vee S^2$.

::: pf-proof

In the model of Step [](#handlebody){.pf-ref}, place $\infty$ in the interior of the outer ball $S^3\setminus\mathring\Delta$. A closed $3$-ball minus an interior point deformation retracts radially onto its boundary sphere, fixing the boundary where the $1$-handles are attached, so removing $\infty$ replaces that ball by a $2$-sphere. Each $1$-handle deformation retracts onto its core arc, and the inner ball is contractible, so $X$ is homotopy equivalent to a point joined to $S^2$ by four arcs. Contracting one of the arcs leaves $S^2$ with three arcs attached at both ends to one point, which is $S^2\vee S^1\vee S^1\vee S^1$.

:::

:::

::: pf-qed

By van Kampen and Step [](#puncture){.pf-ref}, $\pi_1(X)$ is the free group on three generators, one loop through each of three faces of the tetrahedron.
The homology of the wedge is
$$
H_0(X)\cong\ZZ,\qquad H_1(X)\cong\ZZ^3,\qquad H_2(X)\cong\ZZ,\qquad H_i(X)=0\ (i\ge3).
$$
The class in $H_2$ is a large sphere enclosing the tetrahedron; it is not a boundary in $X$ by Alexander duality, $\widetilde H_2(S^3\setminus(\Gamma\cup\{\infty\}))\cong \widetilde H^0(\Gamma\sqcup\{\infty\})\cong\ZZ$.

:::

:::

:::
