---
schema: qual/card@1
id: P-SQUAL2-05
kind: problem
title: Fundamental group of the complement of two disjoint lines in $\RR^3$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $L_1,L_2$ be disjoint lines in $\RR^3$, and set
$$X=\RR^3\setminus(L_1\cup L_2).$$
Compute $\pi_1(X)$.
:::

::: {.solution}

There are two geometric cases: the lines are parallel or skew.

## Parallel lines

::: pf

::: pf-step

If \(L_1,L_2\) are parallel, an affine change of coordinates sends them to
\[
\boxed{
L_1=\{(x,0,0):x\in\RR\},
\qquad
L_2=\{(x,0,1):x\in\RR\}}.
\]


::: pf-proof

Translate one line to pass through the origin, choose the \(x\)-axis in their common direction, and choose transverse coordinates so that the second line has transverse coordinate \((0,1)\).

:::

:::

::: pf-step

In these coordinates,
\[
\RR^3\setminus(L_1\cup L_2)
\cong
\RR\times
\left(
\RR^2\setminus\{(0,0),(0,1)\}
\right).
\]


::: pf-proof

Write a point as
\[
(x,y,z).
\]
The deleted lines are exactly
\[
\RR\times\{(0,0)\}
\]
and
\[
\RR\times\{(0,1)\}
\]
in the product decomposition
\[
\RR_x\times\RR^2_{y,z}.
\]

:::

:::

::: pf-step

Since \(\RR\) is contractible,
\[
\boxed{
\pi_1\bigl(\RR^3\setminus(L_1\cup L_2)\bigr)
\cong
\pi_1\bigl(\RR^2\setminus\{(0,0),(0,1)\}\bigr)}.
\]


::: pf-proof

Projection onto the second factor is a homotopy equivalence with inverse obtained by inserting \(x=0\).

:::

:::

::: pf-step

The plane minus two points deformation retracts onto a wedge of two circles.


::: pf-proof

Choose disjoint small circles around the two deleted points and connect them by an embedded arc. The punctured plane deformation retracts onto the union of the two circles and the connecting arc. Collapsing the arc to a point gives
\[
S^1\vee S^1.
\]

:::

:::

::: {.pf-step #s1-5}

Therefore, in the parallel case,
\[
\boxed{
\pi_1(X)\cong F_2}.
\]


::: pf-proof

The fundamental group of
\[
S^1\vee S^1
\]
is the free group on two generators.

:::

:::

::: pf-step

An affine change of coordinates sends them to
\[
\boxed{
L_1=\{(t,0,0):t\in\RR\},
\qquad
L_2=\{(0,t,1):t\in\RR\}}.
\]


::: pf-proof

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

:::

::: pf-step

Choose a continuous function
\[
\theta:\RR\to\RR
\]
such that
\[
\theta(0)=0,
\qquad
\theta(1)=-\frac{\pi}{2}.
\]


::: pf-proof

For example,
\[
\theta(z)=-\frac{\pi z}{2}
\]
works.

:::

:::

::: pf-step

Define
\[
\Phi:\RR^3\to\RR^3
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


::: pf-proof

This is a continuous, indeed smooth, map.

:::

:::

::: pf-step

The map \(\Phi\) is a diffeomorphism.


::: pf-proof

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

:::

::: {.pf-step #s1-10}

The line \(L_1\) is fixed by \(\Phi\).


::: pf-proof

On \(L_1\),
\[
z=0,\qquad y=0.
\]
Since \(\theta(0)=0\),
\[
\Phi(t,0,0)=(t,0,0).
\]

:::

:::

::: {.pf-step #s1-11}

The line \(L_2\) is sent to
\[
\boxed{
\{(t,0,1):t\in\RR\}},
\]
which is parallel to \(L_1\).


::: pf-proof

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

:::

::: {.pf-step #s1-12}

Hence the complement of a skew pair of lines is diffeomorphic to the complement of a parallel pair.


::: pf-proof

The diffeomorphism \(\Phi\) carries the union \(L_1\cup L_2\) to two parallel lines by steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref}, and therefore restricts to a diffeomorphism of complements.

:::

:::

::: {.pf-step #s1-13}

Therefore, in the skew case as well,
\[
\boxed{
\pi_1(X)\cong F_2}.
\]


::: pf-proof

Apply step [](#s1-12){.pf-ref} and the parallel-case computation from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Thus for any two disjoint lines in \(\RR^3\),
\[
\boxed{
\pi_1\bigl(
\RR^3\setminus(L_1\cup L_2)
\bigr)
\cong
F_2}.
\]


::: pf-proof

Two disjoint affine lines are either parallel or skew. Steps [](#s1-5){.pf-ref} and [](#s1-13){.pf-ref} give the same answer in both cases.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is the required computation.

:::

:::

:::
