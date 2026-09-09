---
schema: qual/card@1
id: P-UCTOP-FA12-1
kind: problem
title: X_4 cannot cover X_3 but X_5 can
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

Let $X_n$ be the bouquet of $n$ circles, whose fundamental group (based at the vertex of the bouquet) is the free group $F_n$ on $n$ generators.
Show that $X_4$ cannot cover $X_3$, but that $X_5$ can.

::: {.solution}
<1>1. If a connected finite graph $Y$ is a $d$-sheeted cover of $X_3$, then
$$
\chi(Y)=d\chi(X_3)=-2d.
$$
::: {.proof}
Euler characteristic multiplies by the degree of a finite covering, and $\chi(X_3)=1-3=-2$.
:::

<1>2. Therefore $X_4$ cannot cover $X_3$.
::: {.proof}
Since $\chi(X_4)=1-4=-3$, a covering would require $-3=-2d$ for an integer $d$, impossible.
:::

<1>3. A connected double cover of $X_3$ can be built with two vertices $v_0,v_1$: let the $a$-edges interchange the vertices and let the $b$- and $c$-edges be loops at each vertex.
::: {.proof}
At each vertex there is exactly one incoming and one outgoing edge of each label $a,b,c$, so the label-preserving map to $X_3$ is a covering. The $a$-edge connects the two vertices, hence the cover is connected.
:::

<1>4. This covering graph has rank $5$, hence is homeomorphic after suppressing subdivision vertices to $X_5$.
::: {.proof}
It has $V=2$ vertices and $E=6$ edges, so
$$
\operatorname{rank}\pi_1=E-V+1=5.
$$
A connected graph of rank $5$ with one essential vertex after collapsing a maximal tree is a bouquet of five circles.
:::

<1>5. Thus $X_5$ covers $X_3$, while $X_4$ does not.
::: {.proof}
Combine <1>2--<1>4.
:::
:::
