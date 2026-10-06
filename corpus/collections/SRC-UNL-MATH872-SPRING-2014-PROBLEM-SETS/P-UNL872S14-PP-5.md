---
schema: qual/card@1
id: P-UNL872S14-PP-5
kind: problem
title: UNL Math 872 Spring 2014 assignment PP.5
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against assignment PP.5 on the retained UNL Math 872 Section 001 Spring 2014 problem-sets page PDF.
---

::: {.problem}
Let Y be any finite path-connected graph.
Show how to compute the simplicial homology groups of Y, and write these groups in terms of the Euler characteristic of Y (see problem (9.B.4) for the definition).
:::

::: {.solution}
Let
\[
v
\]
be the number of vertices of \(Y\), and let
\[
e
\]
be the number of edges. Choose an orientation on every edge.

<1>1. The simplicial chain groups are
\[
\boxed{
C_1(Y)\cong\mathbb Z^e,
\qquad
C_0(Y)\cong\mathbb Z^v,
\qquad
C_n(Y)=0\text{ for }n\ge2}.
\]

::: {.proof}
A graph is a \(1\)-dimensional \(\Delta\)-complex. Its \(1\)-simplices are
the \(e\) oriented edges and its \(0\)-simplices are the \(v\) vertices.
There are no simplices in higher dimensions.
:::

<1>2. For an oriented edge
\[
\epsilon:u\to w,
\]
the simplicial boundary is
\[
\boxed{
\partial_1\epsilon=w-u}.
\]

::: {.proof}
This is the degree-one simplicial boundary formula.
:::

<1>3. Every element of
\[
\operatorname{im}\partial_1
\]
has total coefficient sum \(0\) in \(C_0(Y)\).

::: {.proof}
Each generator boundary
\[
w-u
\]
has coefficient sum
\[
1-1=0.
\]
The same is true for every integer linear combination of such boundaries.
:::

<1>4. Define the augmentation homomorphism
\[
\varepsilon:C_0(Y)\to\mathbb Z
\]
by
\[
\boxed{
\varepsilon\!\left(
\sum_{i=1}^{v}n_iv_i
\right)
=
\sum_{i=1}^{v}n_i}.
\]

::: {.proof}
This is a homomorphism of free abelian groups.
:::

<1>5. One has
\[
\boxed{
\operatorname{im}\partial_1
\subseteq
\ker\varepsilon}.
\]

::: {.proof}
This is exactly step <1>3.
:::

<1>6. Choose a spanning tree
\[
T\subseteq Y.
\]

::: {.proof}
Every finite connected graph has a spanning tree: start with one vertex and
successively add an edge leading to a new vertex until all vertices have been
included, omitting any edge that would create a cycle.
:::

<1>7. Fix a root vertex
\[
v_0\in T.
\]
For every other vertex \(v_i\), the element
\[
\boxed{v_i-v_0}
\]
lies in
\[
\operatorname{im}\partial_1.
\]

::: {.proof}
In the tree \(T\), there is a unique edge path
\[
v_0=w_0,w_1,\dots,w_m=v_i.
\]
Orient each traversed edge consistently with the path, inserting a minus sign
if its chosen global orientation is opposite. The sum of the corresponding
edge boundaries telescopes:
\[
(w_1-w_0)+(w_2-w_1)+\cdots+(w_m-w_{m-1})
=
v_i-v_0.
\]
Hence \(v_i-v_0\) is a \(1\)-boundary.
:::

<1>8. The elements
\[
v_1-v_0,\dots,v_{v-1}-v_0
\]
generate
\[
\ker\varepsilon.
\]

::: {.proof}
Let
\[
z
=
n_0v_0+\sum_{i=1}^{v-1}n_iv_i
\]
satisfy
\[
\varepsilon(z)=0.
\]
Then
\[
n_0
=
-\sum_{i=1}^{v-1}n_i.
\]
Therefore
\[
\begin{aligned}
z
&=
\sum_{i=1}^{v-1}
n_iv_i
-
\left(
\sum_{i=1}^{v-1}n_i
\right)v_0\\
&=
\sum_{i=1}^{v-1}
n_i(v_i-v_0).
\end{aligned}
\]
:::

<1>9. Therefore
\[
\boxed{
\operatorname{im}\partial_1
=
\ker\varepsilon}.
\]

::: {.proof}
Step <1>5 gives one inclusion. Steps <1>7 and <1>8 show that every generator
of \(\ker\varepsilon\) lies in \(\operatorname{im}\partial_1\).
:::

<1>10. The group
\[
\ker\varepsilon
\]
is free abelian of rank
\[
\boxed{v-1}.
\]

::: {.proof}
The elements
\[
v_i-v_0,
\qquad
1\le i\le v-1,
\]
form a basis: they generate by step <1>8, and linear independence follows
by comparing coefficients of the distinct vertices \(v_i\).
:::

<1>11. Hence
\[
\boxed{
\operatorname{rank}\partial_1=v-1}.
\]

::: {.proof}
By step <1>9,
\[
\operatorname{im}\partial_1=\ker\varepsilon,
\]
whose rank is \(v-1\) by step <1>10.
:::

<1>12. Since
\[
C_1(Y)\cong\mathbb Z^e,
\]
the kernel of \(\partial_1\) is free abelian of rank
\[
\boxed{e-v+1}.
\]

::: {.proof}
The kernel of a homomorphism between free abelian groups is free. Rank-nullity
over \(\mathbb Q\) gives
\[
\operatorname{rank}\ker\partial_1
=
e-(v-1)
=
e-v+1.
\]
:::

<1>13. Therefore
\[
\boxed{
H_1(Y)
=
\ker\partial_1
\cong
\mathbb Z^{e-v+1}}.
\]

::: {.proof}
There are no \(2\)-simplices, so
\[
\operatorname{im}\partial_2=0.
\]
Thus
\[
H_1(Y)
=
\ker\partial_1.
\]
Apply step <1>12.
:::

<1>14. Also
\[
\boxed{
H_0(Y)
\cong
\mathbb Z}.
\]

::: {.proof}
By definition,
\[
H_0(Y)
=
C_0(Y)/\operatorname{im}\partial_1.
\]
Using step <1>9,
\[
H_0(Y)
=
\mathbb Z^v/\ker\varepsilon.
\]
By the first isomorphism theorem,
\[
\mathbb Z^v/\ker\varepsilon
\cong
\operatorname{im}\varepsilon
=
\mathbb Z.
\]
This also reflects path connectedness.
:::

<1>15. For every \(n\ge2\),
\[
\boxed{
H_n(Y)=0}.
\]

::: {.proof}
The chain groups \(C_n(Y)\) vanish in these dimensions by step <1>1.
:::

<1>16. The Euler characteristic of \(Y\) is
\[
\boxed{
\chi(Y)=v-e}.
\]

::: {.proof}
A graph has only \(0\)- and \(1\)-cells, so
\[
\chi(Y)
=
v-e.
\]
:::

<1>17. Hence
\[
\boxed{
e-v+1
=
1-\chi(Y)}.
\]

::: {.proof}
Rearrange
\[
\chi(Y)=v-e.
\]
:::

<1>18. Therefore the simplicial homology groups are
\[
\boxed{
H_n^{\mathrm{simpl}}(Y)
\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z^{\,1-\chi(Y)},&n=1,\\
0,&n\ge2.
\end{cases}}
\]

::: {.proof}
Combine steps <1>13--<1>17.
:::

<1>19. In particular,
\[
\boxed{
1-\chi(Y)\ge0}.
\]

::: {.proof}
It is the rank of the free abelian group \(H_1(Y)\) from step <1>18.
Equivalently, a connected finite graph satisfies
\[
e\ge v-1
\]
because it contains a spanning tree with \(v-1\) edges.
:::

<1>20. Q.E.D.

::: {.proof}
Step <1>18 gives the requested homology groups in terms of the Euler
characteristic.
:::
:::
