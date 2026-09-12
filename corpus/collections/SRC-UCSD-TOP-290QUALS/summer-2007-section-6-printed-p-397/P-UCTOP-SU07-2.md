---
schema: qual/card@1
id: P-UCTOP-SU07-2
kind: problem
title: Coverings of bouquets of circles
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

Let $X_n$ be the bouquet of $n$ circles, whose fundamental group (based at the vertex of the bouquet) is the free group $F_n$ on $n$ generators.

(a) Draw a covering of $X_3$ by $X_5$.
Find the subgroup of $F_3 = \langle a, b, c \rangle$ to which your cover corresponds under the correspondence between subgroups of $F_3$ and based connected covers of $X_3$.

(b) Show that $X_4$ cannot cover $X_3$.

::: {.solution}
<1>1. A connected $2$-sheeted covering of $X_3$ can be constructed with two vertices $v_0,v_1$ by letting the $a$-edges interchange the vertices and letting the $b$- and $c$-edges be loops at each vertex.
::: {.proof}
At each vertex there is exactly one incoming and one outgoing edge of each label $a,b,c$, so the label-preserving graph map to the rose $X_3$ is locally a homeomorphism and has two points over the wedge vertex. The $a$-edge connects the two vertices, so the covering graph is connected.
:::

<1>2. This covering graph is homeomorphic to $X_5$.
::: {.proof}
It has $V=2$ vertices and $E=6$ edges. A connected graph has free fundamental group of rank
$$
E-V+1=6-2+1=5.
$$
Collapsing a maximal tree therefore identifies it up to homeomorphism type as a graph with rank $5$, i.e. after suppressing valence-two subdivision data it is the bouquet $X_5$.
:::

<1>3. With basepoint $v_0$, the corresponding subgroup of
$$
F_3=\langle a,b,c\rangle
$$
is
$$
H=\ker\bigl(F_3\to\mathbb Z/2\bigr),
\qquad a\mapsto1,\quad b,c\mapsto0.
$$
:::
::: {.proof}
The monodromy of a loop swaps the two sheets exactly when the total exponent of $a$ is odd. Hence a based loop lifts closed at $v_0$ exactly when its image under the displayed homomorphism is $0$.
:::

<1>4. One free basis for $H$ is
$$
a^2,\quad b,\quad c,\quad aba^{-1},\quad aca^{-1}.
$$
:::
::: {.proof}
Apply Reidemeister--Schreier to the index-$2$ subgroup using transversal $\{1,a\}$. The five nontrivial Schreier generators are precisely the displayed elements, as expected from the rank formula $1+2(3-1)=5$.
:::

<1>5. There is no covering map $X_4\to X_3$.
::: {.proof}
If a connected finite graph $Y$ is a $d$-sheeted cover of $X_3$, Euler characteristic multiplies by $d$:
$$
\chi(Y)=d\chi(X_3).
$$
But
$$
\chi(X_4)=1-4=-3,\qquad \chi(X_3)=1-3=-2,
$$
so one would need $-3=-2d$, impossible for an integer $d$.
:::
:::

