---
schema: qual/card@1
id: P-WESTOP05-10
kind: problem
title: Lift multiplication to the universal cover of a topological group and prove associativity
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Part (a) refers to a source diagram that is missing from the retained Markdown. The text still identifies p as a covering map and asks for the based lifting criterion and uniqueness, so those roles are retained without reconstructing the original diagram layout.
---

::: {.problem}
1. Suppose $p:(E,e_0)\to(B,b_0)$ is a covering map and $f:(X,x_0)\to(B,b_0)$ is a based map, with the spaces in the source path-connected and locally path-connected. State necessary and sufficient conditions for a lift
   \[
   \widetilde f:(X,x_0)\to(E,e_0),
   \qquad p\circ\widetilde f=f,
   \]
   to exist. If it exists, determine how many such based lifts there are.
2. Let $G$ be a path-connected, locally path-connected topological group with identity $e$ and multiplication
   \[
   \mu:G\times G\to G,
   \]
   and let
   \[
   p:(H,e')\to(G,e)
   \]
   be a universal cover. Show that there is a map
   \[
   \mu':H\times H\to H
   \]
   satisfying
   \[
   p\circ\mu'=\mu\circ(p\times p).
   \]
3. Prove that $\mu'$ is associative.
:::

::: {.solution}
## Part 1: the based lifting criterion

Let
\[
p:(E,e_0)\to(B,b_0)
\]
be a covering map and
\[
f:(X,x_0)\to(B,b_0)
\]
a based map, with \(X\) path connected and locally path connected.

<1>1. A based lift
\[
\widetilde f:(X,x_0)\to(E,e_0)
\]
can exist only if
\[
\boxed{
f_*\pi_1(X,x_0)
\subseteq
p_*\pi_1(E,e_0)}.
\]

::: {.proof}
If
\[
p\circ\widetilde f=f,
\]
then functoriality of \(\pi_1\) gives
\[
f_*
=
p_*\circ\widetilde f_*.
\]
Hence every element of
\[
f_*\pi_1(X,x_0)
\]
lies in the image of \(p_*\).
:::

<1>2. Conversely, if
\[
f_*\pi_1(X,x_0)
\subseteq
p_*\pi_1(E,e_0),
\]
then a based lift exists.

::: {.proof}
This is the covering-space lifting criterion. The subgroup condition says
precisely that the endpoint of the lift of \(f\circ\gamma\), starting at
\(e_0\), depends only on the endpoint of a path \(\gamma\) in \(X\), not on
the chosen path from \(x_0\). Thus one defines
\[
\widetilde f(x)
\]
as that lifted endpoint. Local path connectedness gives continuity.
:::

<1>3. Therefore the necessary and sufficient condition is
\[
\boxed{
f_*\pi_1(X,x_0)
\subseteq
p_*\pi_1(E,e_0)}.
\]

::: {.proof}
Combine steps <1>1--<1>2.
:::

<1>4. If a based lift exists, it is unique.

::: {.proof}
Suppose
\[
\widetilde f_1,\widetilde f_2:X\to E
\]
are lifts of \(f\) with
\[
\widetilde f_1(x_0)
=
\widetilde f_2(x_0)
=
e_0.
\]
For any \(x\in X\), choose a path
\[
\gamma:I\to X
\]
from \(x_0\) to \(x\). Then
\[
\widetilde f_1\circ\gamma
\qquad\text{and}\qquad
\widetilde f_2\circ\gamma
\]
are lifts of
\[
f\circ\gamma
\]
with the same initial point \(e_0\). Uniqueness of path lifting gives
\[
\widetilde f_1\circ\gamma
=
\widetilde f_2\circ\gamma.
\]
Evaluating at \(1\) yields
\[
\widetilde f_1(x)=\widetilde f_2(x).
\]
Since \(x\) was arbitrary, the lifts are equal.
:::

<1>5. Hence the number of based lifts is
\[
\boxed{
0\text{ or }1},
\]
and it is \(1\) exactly when the subgroup condition in step <1>3 holds.

::: {.proof}
Existence is step <1>3 and uniqueness is step <1>4.
:::

## Part 2: lifting the multiplication

Let \(G\) be a path-connected locally path-connected topological group with
identity \(e\), and let
\[
p:(H,e')\to(G,e)
\]
be its universal cover.

<1>6. The space \(H\) is simply connected.

::: {.proof}
This is the defining property of a universal covering space.
:::

<1>7. Therefore
\[
\boxed{
H\times H
\text{ is simply connected}}.
\]

::: {.proof}
The product is path connected, and
\[
\pi_1(H\times H,(e',e'))
\cong
\pi_1(H,e')\times\pi_1(H,e')
=
0.
\]
:::

<1>8. Define
\[
F
=
\mu\circ(p\times p):
H\times H\to G.
\]

::: {.proof}
The product map
\[
p\times p:H\times H\to G\times G
\]
is continuous, and so is the multiplication
\[
\mu:G\times G\to G.
\]
:::

<1>9. The map \(F\) is based:
\[
\boxed{
F(e',e')=e}.
\]

::: {.proof}
Since
\[
p(e')=e,
\]
one has
\[
F(e',e')
=
\mu(e,e)
=
e.
\]
:::

<1>10. The induced subgroup
\[
F_*\pi_1(H\times H,(e',e'))
\]
is trivial.

::: {.proof}
The domain is simply connected by step <1>7.
:::

<1>11. The image
\[
p_*\pi_1(H,e')
\]
is also trivial.

::: {.proof}
Again,
\[
\pi_1(H,e')=0
\]
by step <1>6.
:::

<1>12. Hence the lifting criterion gives a unique based lift
\[
\boxed{
\mu':(H\times H,(e',e'))
\to(H,e')}
\]
such that
\[
\boxed{
p\circ\mu'
=
\mu\circ(p\times p)}.
\]

::: {.proof}
By steps <1>10--<1>11,
\[
F_*\pi_1(H\times H)
=
0
\subseteq
0
=
p_*\pi_1(H).
\]
Apply the criterion from step <1>3 and uniqueness from step <1>4.
:::

<1>13. In particular,
\[
\boxed{
\mu'(e',e')=e'}.
\]

::: {.proof}
The lift in step <1>12 is based.
:::

## Part 3: associativity

Define
\[
A:H^3\to H
\]
by
\[
A(h_1,h_2,h_3)
=
\mu'(\mu'(h_1,h_2),h_3),
\]
and define
\[
B:H^3\to H
\]
by
\[
B(h_1,h_2,h_3)
=
\mu'(h_1,\mu'(h_2,h_3)).
\]

<1>14. For every \((h_1,h_2,h_3)\in H^3\),
\[
p(A(h_1,h_2,h_3))
=
\mu(
\mu(p(h_1),p(h_2)),
p(h_3)).
\]

::: {.proof}
Using step <1>12 twice,
\[
\begin{aligned}
p(A(h_1,h_2,h_3))
&=
p(\mu'(\mu'(h_1,h_2),h_3))\\
&=
\mu(
p(\mu'(h_1,h_2)),
p(h_3))\\
&=
\mu(
\mu(p(h_1),p(h_2)),
p(h_3)).
\end{aligned}
\]
:::

<1>15. Likewise,
\[
p(B(h_1,h_2,h_3))
=
\mu(
p(h_1),
\mu(p(h_2),p(h_3))).
\]

::: {.proof}
Apply step <1>12 twice in the other parenthesization.
:::

<1>16. Since multiplication in \(G\) is associative,
\[
\boxed{
p\circ A
=
p\circ B}.
\]

::: {.proof}
For all \(g_1,g_2,g_3\in G\),
\[
\mu(\mu(g_1,g_2),g_3)
=
\mu(g_1,\mu(g_2,g_3)).
\]
Apply this to
\[
g_i=p(h_i)
\]
and compare steps <1>14--<1>15.
:::

<1>17. Both \(A\) and \(B\) send
\[
(e',e',e')
\]
to \(e'\).

::: {.proof}
Using step <1>13,
\[
A(e',e',e')
=
\mu'(\mu'(e',e'),e')
=
\mu'(e',e')
=
e',
\]
and similarly
\[
B(e',e',e')=e'.
\]
:::

<1>18. The space \(H^3\) is path connected.

::: {.proof}
The universal cover \(H\) is path connected, and a finite product of
path-connected spaces is path connected.
:::

<1>19. Therefore
\[
\boxed{A=B}.
\]

::: {.proof}
By step <1>16, \(A\) and \(B\) are lifts through \(p\) of the same map
\[
H^3\to G.
\]
By step <1>17 they agree at the basepoint. Since the domain is path
connected by step <1>18, uniqueness of lifting gives
\[
A=B.
\]
:::

<1>20. Hence
\[
\boxed{
\mu'(\mu'(h_1,h_2),h_3)
=
\mu'(h_1,\mu'(h_2,h_3))}
\]
for all \(h_1,h_2,h_3\in H\).

::: {.proof}
This is the pointwise meaning of step <1>19.
:::

<1>21. Thus the lifted multiplication \(\mu'\) is associative.

::: {.proof}
Step <1>20 is exactly associativity.
:::

<1>22. Q.E.D.

::: {.proof}
Steps <1>3--<1>5 answer part \(1\), step <1>12 constructs the lifted
multiplication in part \(2\), and step <1>21 proves associativity in part
\(3\).
:::
:::
