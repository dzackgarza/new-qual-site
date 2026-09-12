---
schema: qual/card@1
id: P-TOPS07B
kind: problem
title: "Covering spaces of bouquets of circles and subgroups of free groups"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Free Groups
  - Fundamental Group
relations: []
review: draft
---

::: problem
Let $X_n$ be the bouquet of $n$ circles, whose fundamental group (based at the vertex of the bouquet) is the free group $F_n$ on $n$ generators.

(i) Draw a covering of $X_3$ by $X_5$.
Find the subgroup of $F_3 = \langle a, b, c \rangle$ to which your cover corresponds under the correspondence between subgroups of $F_3$ and based connected covers of $X_3$.

(ii) Show that $X_4$ cannot cover $X_2$.
:::

::: {.solution}
<1>1. A connected two-sheeted cover of $X_3$ by a graph homeomorphic to $X_5$ is obtained from two vertices $v_0,v_1$ by letting the $a$-edge switch the vertices and letting the $b$- and $c$-edges be loops at each vertex.
::: {.proof}
At each vertex there is exactly one incoming and one outgoing lift of each oriented edge $a,b,c$, so the resulting graph is a covering of the bouquet $X_3$. It is connected because the $a$-edge joins the two vertices. Its Euler characteristic is $2-6=-4$, hence its rank is $1-(-4)=5$, so it is homeomorphic to a bouquet of five circles after collapsing a maximal tree.
:::

<1>2. The corresponding subgroup of $F_3=\langle a,b,c\rangle$ is
$$
\ker\bigl(F_3\to\mathbb Z/2,\ a\mapsto1,\ b,c\mapsto0\bigr).
$$
One Schreier basis is
$$
\boxed{b,\ c,\ a^2,\ aba^{-1},\ aca^{-1}}.
$$
::: {.proof}
The two vertices are the two cosets of the kernel. Using the transversal $\{1,a\}$, the Schreier generators are exactly the five displayed elements.
:::

<1>3. The space $X_4$ cannot cover $X_2$.
::: {.proof}
The wedge point of $X_4$ has valence $8$, while every point lying over the wedge point of $X_2$ in a covering must have a neighborhood homeomorphic to a neighborhood of that wedge point, hence valence $4$. The unique branch point of $X_4$ therefore cannot map locally homeomorphically to the branch point of $X_2$. Thus no covering map $X_4\to X_2$ exists.
:::
:::
