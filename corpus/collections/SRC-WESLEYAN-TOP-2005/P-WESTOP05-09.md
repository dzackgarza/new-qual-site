---
schema: qual/card@1
id: P-WESTOP05-09
kind: problem
title: The suspension of a path-connected space is simply connected
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For a space $X$, define its suspension $\Sigma X$ as the quotient of $X\times I$ obtained by collapsing $X\times\{0\}$ to one point and $X\times\{1\}$ to another point. Assuming $X$ is path-connected, compute with proof
\[
\pi_1(\Sigma X).
\]
:::

::: {.solution}
Let
\[
q:X\times I\to\Sigma X
\]
be the quotient map. Denote the two suspension points by
\[
S=q(X\times\{0\}),
\qquad
N=q(X\times\{1\}).
\]

<1>1. Define
\[
U=q\bigl(X\times[0,2/3)\bigr)
\]
and
\[
V=q\bigl(X\times(1/3,1]\bigr).
\]

::: {.proof}
These are saturated subsets for the quotient relation because the entire
collapsed end \(X\times\{0\}\) lies in the first set and the entire collapsed
end \(X\times\{1\}\) lies in the second.
:::

<1>2. The sets \(U\) and \(V\) are open in \(\Sigma X\).

::: {.proof}
The subsets
\[
X\times[0,2/3)
\]
and
\[
X\times(1/3,1]
\]
are open in the product \(X\times I\), using the subspace topology on
\(I=[0,1]\). Since they are saturated, their quotient images are open.
:::

<1>3. One has
\[
\boxed{
\Sigma X=U\cup V}.
\]

::: {.proof}
The intervals
\[
[0,2/3)
\qquad\text{and}\qquad
(1/3,1]
\]
cover \(I\).
:::

<1>4. The space \(U\) is contractible.

::: {.proof}
It is a truncated cone on \(X\) with cone point \(S\). Define
\[
H_U(q(x,t),s)
=
q(x,(1-s)t).
\]
This is well defined because all points with \(t=0\) are already identified.
At \(s=1\), every point is sent to \(S\).
:::

<1>5. The space \(V\) is contractible.

::: {.proof}
It is a truncated cone on \(X\) with cone point \(N\). Define
\[
H_V(q(x,t),s)
=
q(x,t+s(1-t)).
\]
At \(s=1\), every point is sent to \(N\).
:::

<1>6. The intersection is
\[
\boxed{
U\cap V
=
q\bigl(X\times(1/3,2/3)\bigr)}.
\]

::: {.proof}
This is the overlap of the two interval factors from step <1>1.
No quotient identifications occur in the open middle interval.
:::

<1>7. Hence
\[
\boxed{
U\cap V
\cong
X\times(1/3,2/3)}.
\]

::: {.proof}
The quotient map is injective on
\[
X\times(1/3,2/3),
\]
since only the two endpoint slices of \(X\times I\) are collapsed.
:::

<1>8. Therefore
\[
\boxed{
U\cap V\simeq X}.
\]

::: {.proof}
The interval
\[
(1/3,2/3)
\]
is contractible, so projection onto \(X\) is a homotopy equivalence.
:::

<1>9. Since \(X\) is path connected,
\[
\boxed{
U\cap V
\text{ is path connected}}.
\]

::: {.proof}
A product of path-connected spaces is path connected. Use step <1>7 and the
fact that the interval is path connected.
:::

<1>10. The spaces \(U\) and \(V\) are path connected.

::: {.proof}
Each is contractible by steps <1>4--<1>5, hence path connected.
:::

<1>11. The Seifert--van Kampen theorem gives
\[
\pi_1(\Sigma X)
\cong
\pi_1(U)
*_{\pi_1(U\cap V)}
\pi_1(V).
\]

::: {.proof}
The cover
\[
\Sigma X=U\cup V
\]
is by open path-connected sets with path-connected intersection by steps
<1>2, <1>9, and <1>10.
:::

<1>12. One has
\[
\boxed{
\pi_1(U)=0}
\]
and
\[
\boxed{
\pi_1(V)=0}.
\]

::: {.proof}
Both spaces are contractible by steps <1>4--<1>5.
:::

<1>13. Therefore
\[
\boxed{
\pi_1(\Sigma X)=0}.
\]

::: {.proof}
The amalgamated free product of the two trivial groups is trivial,
regardless of the maps from \(\pi_1(U\cap V)\). Apply step <1>11 and step
<1>12.
:::

<1>14. Thus the suspension of every path-connected space is simply
connected.

::: {.proof}
The suspension is path connected because \(U\) and \(V\) are path connected
and intersect nontrivially, and step <1>13 gives trivial fundamental group.
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>13 is the requested computation.
:::
:::
