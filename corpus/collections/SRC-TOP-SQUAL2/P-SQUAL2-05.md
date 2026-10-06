---
schema: qual/card@1
id: P-SQUAL2-05
kind: problem
title: Fundamental group of the complement of two disjoint lines in $\mathbb R^3$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $L_1,L_2$ be disjoint lines in $\mathbb R^3$, and set
\[
X=\mathbb R^3\setminus(L_1\cup L_2).
\]
Compute $\pi_1(X)$.
:::

::: {.solution}
There are two geometric cases: the lines are parallel or skew.

## Parallel lines

<1>1. If \(L_1,L_2\) are parallel, an affine change of coordinates sends them to
\[
\boxed{
L_1=\{(x,0,0):x\in\mathbb R\},
\qquad
L_2=\{(x,0,1):x\in\mathbb R\}}.
\]

::: {.proof}
Translate one line to pass through the origin, choose the \(x\)-axis in their common direction, and choose transverse coordinates so that the second line has transverse coordinate \((0,1)\).
:::

<1>2. In these coordinates,
\[
\mathbb R^3\setminus(L_1\cup L_2)
\cong
\mathbb R\times
\left(
\mathbb R^2\setminus\{(0,0),(0,1)\}
\right).
\]

::: {.proof}
Write a point as
\[
(x,y,z).
\]
The deleted lines are exactly
\[
\mathbb R\times\{(0,0)\}
\]
and
\[
\mathbb R\times\{(0,1)\}
\]
in the product decomposition
\[
\mathbb R_x\times\mathbb R^2_{y,z}.
\]
:::

<1>3. Since \(\mathbb R\) is contractible,
\[
\boxed{
\pi_1\bigl(\mathbb R^3\setminus(L_1\cup L_2)\bigr)
\cong
\pi_1\bigl(\mathbb R^2\setminus\{(0,0),(0,1)\}\bigr)}.
\]

::: {.proof}
Projection onto the second factor is a homotopy equivalence with inverse obtained by inserting \(x=0\).
:::

<1>4. The plane minus two points deformation retracts onto a wedge of two circles.

::: {.proof}
Choose disjoint small circles around the two deleted points and connect them by an embedded arc. The punctured plane deformation retracts onto the union of the two circles and the connecting arc. Collapsing the arc to a point gives
\[
S^1\vee S^1.
\]
:::

<1>5. Therefore, in the parallel case,
\[
\boxed{
\pi_1(X)\cong F_2}.
\]

::: {.proof}
The fundamental group of
\[
S^1\vee S^1
\]
is the free group on two generators.
:::

## Skew lines

Assume now that \(L_1,L_2\) are skew.

<1>6. An affine change of coordinates sends them to
\[
\boxed{
L_1=\{(t,0,0):t\in\mathbb R\},
\qquad
L_2=\{(0,t,1):t\in\mathbb R\}}.
\]

::: {.proof}
Choose a point \(p_1\in L_1\), a point \(p_2\in L_2\), and direction vectors \(v_1,v_2\) for the two lines. Since the lines are skew, the vectors
\[
v_1,\ v_2,\ p_2-p_1
\]
are linearly independent. The affine map sending
\[
p_1\mapsto0,\qquad
v_1\mapsto e_1,\qquad
v_2\mapsto e_2,\qquad
p_2-p_1\mapsto e_3
\]
has the required effect.
:::

<1>7. Choose a continuous function
\[
\theta:\mathbb R\to\mathbb R
\]
such that
\[
\theta(0)=0,
\qquad
\theta(1)=-\frac{\pi}{2}.
\]

::: {.proof}
For example,
\[
\theta(z)=-\frac{\pi z}{2}
\]
works.
:::

<1>8. Define
\[
\Phi:\mathbb R^3\to\mathbb R^3
\]
by rotating each horizontal plane through angle \(\theta(z)\):
\[
\boxed{
\Phi(x,y,z)
=
\bigl(
x\cos\theta(z)-y\sin\theta(z),\,
x\sin\theta(z)+y\cos\theta(z),\,
z
\bigr)}.
\]

::: {.proof}
This is a continuous, indeed smooth, map.
:::

<1>9. The map \(\Phi\) is a diffeomorphism.

::: {.proof}
Its inverse is obtained by rotating the horizontal plane at height \(z\) through angle \(-\theta(z)\):
\[
\Phi^{-1}(x,y,z)
=
\bigl(
x\cos\theta(z)+y\sin\theta(z),\,
-x\sin\theta(z)+y\cos\theta(z),\,
z
\bigr).
\]
:::

<1>10. The line \(L_1\) is fixed by \(\Phi\).

::: {.proof}
On \(L_1\),
\[
z=0,\qquad y=0.
\]
Since \(\theta(0)=0\),
\[
\Phi(t,0,0)=(t,0,0).
\]
:::

<1>11. The line \(L_2\) is sent to
\[
\boxed{
\{(t,0,1):t\in\mathbb R\}},
\]
which is parallel to \(L_1\).

::: {.proof}
On \(L_2\),
\[
(x,y,z)=(0,t,1).
\]
Since
\[
\theta(1)=-\frac{\pi}{2},
\]
\[
\Phi(0,t,1)
=
(t,0,1).
\]
:::

<1>12. Hence the complement of a skew pair of lines is diffeomorphic to the complement of a parallel pair.

::: {.proof}
The diffeomorphism \(\Phi\) carries the union \(L_1\cup L_2\) to two parallel lines by steps <1>10--<1>11, and therefore restricts to a diffeomorphism of complements.
:::

<1>13. Therefore, in the skew case as well,
\[
\boxed{
\pi_1(X)\cong F_2}.
\]

::: {.proof}
Apply step <1>12 and the parallel-case computation from step <1>5.
:::

<1>14. Thus for any two disjoint lines in \(\mathbb R^3\),
\[
\boxed{
\pi_1\bigl(
\mathbb R^3\setminus(L_1\cup L_2)
\bigr)
\cong
F_2}.
\]

::: {.proof}
Two disjoint affine lines are either parallel or skew. Steps <1>5 and <1>13 give the same answer in both cases.
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>14 is the required computation.
:::
:::
