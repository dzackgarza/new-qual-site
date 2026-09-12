---
schema: qual/card@1
id: E-HAT-1.2-21
kind: problem
title: Join of path-connected space with any nonempty space is simply-connected
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Simply Connected
  - Joins
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 21; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Pushed an arbitrary loop off the Y-end of the join using path-connectedness of X, retracted it to X, and contracted it inside the cone X*{y0}.
---

Show that the join $X * Y$ of two nonempty spaces $X$ and $Y$ is simply-connected if $X$ is path-connected.

::: {.solution}
Use the model
\[
X*Y=(X\times Y\times I)/\sim
\]
in which at $t=0$ the $Y$-coordinate is forgotten, giving the copy of $X$, and at $t=1$ the $X$-coordinate is forgotten, giving the copy of $Y$.
Denote these two ends simply by $X$ and $Y$.

<1>1. The join $X*Y$ is path connected.
::: {.proof}
Choose $y_0\in Y$.
The subspace
\[
X*\{y_0\}
\]
is the cone $CX$, hence is path connected and contains the whole $X$-end.
Every point $[x,y,t]$ can be joined to its $X$-end point $[x,-,0]$ by varying only the coordinate $t$ from its given value down to $0$.
Thus every point can be joined to the path-connected subspace $X*\{y_0\}$.
:::

<1>2. Let
\[
J=(X*Y)\setminus Y.
\]
Then $J$ deformation retracts onto the $X$-end.
::: {.proof}
Every point of $J$ has a representative $[x,y,t]$ with $t<1$.
Define
\[
H_u([x,y,t])=[x,y,(1-u)t].
\]
This is well defined and continuous for $0\le u\le1$.
At $u=1$ all points lie at $t=0$, where the $Y$-coordinate is forgotten, so the image is exactly $X$.
Points already in $X$ remain fixed.
:::

<1>3. Any path in $X*Y$ whose endpoints lie in $J$ is homotopic relative to its endpoints to a path lying entirely in $J$, provided $X$ is path connected.
::: {.proof}
Let
\[
\alpha:I\to X*Y
\]
have endpoints outside the $Y$-end.
The set
\[
F=\alpha^{-1}(Y)
\]
is closed.
Choose finitely many parameter intervals whose interiors cover $F$, with all their endpoints mapped into $J$ and with each corresponding subpath contained in the region $t>1/3$.
It suffices to replace one such subpath at a time.

Let its endpoints be
\[
[x_0,y_0,t_0],\qquad [x_1,y_1,t_1],
\qquad t_0,t_1<1.
\]
On the region $t>1/3$, projection to the $Y$-coordinate is continuous even at $t=1$.
Let
\[
y(s)
\]
be the projected $Y$-path of the original subpath, and choose a path
\[
p:I\to X
\]
from $x_0$ to $x_1$, which exists because $X$ is path connected.

Replace the subpath by the concatenation of:

1. the vertical segment from $[x_0,y_0,t_0]$ to $[x_0,y_0,1/2]$;
2. the path
   \[
   s\longmapsto[p(s),y(s),1/2];
   \]
3. the vertical segment from $[x_1,y_1,1/2]$ to $[x_1,y_1,t_1]$.

This replacement lies in $J$.
It is homotopic rel endpoints to the original subpath: in the truncated cone region $t>1/3$, contract both paths toward the $Y$-end while tapering the contraction to zero at the two endpoints.
Both then reduce to the same projected $Y$-path with the same endpoint fibers; reversing one contraction gives the required relative homotopy.

Performing these finitely many replacements removes every intersection with the $Y$-end and leaves the original endpoints fixed.
:::

<1>4. Every loop in $X*Y$ is homotopic to a loop in the $X$-end.
::: {.proof}
Let $\gamma:S^1\to X*Y$ be a loop.
If $\gamma(S^1)\subseteq Y$, choose $x_0\in X$ and define
\[
K(s,u)=[x_0,\gamma(s),1-u/2].
\]
At $u=0$ this is the original loop in the $Y$-end, since the $X$-coordinate is forgotten at $t=1$; at $u=1$ it is a loop in the slice $t=1/2\subset J$.
Thus in this case we may first replace $\gamma$ by a homotopic loop in $J$.

Otherwise choose the basepoint of the parametrization at a point of the loop lying in $J$.

By <1>3, $\gamma$ is homotopic to a loop contained in $J$.
Apply the deformation retraction of <1>2 to obtain a loop contained in $X$.
:::

<1>5. Every loop in the $X$-end is nullhomotopic in $X*Y$.
::: {.proof}
Fix any $y_0\in Y$.
The subjoin
\[
X*\{y_0\}
\]
is a cone on $X$.
It contains the $X$-end and is contractible by moving the join coordinate from $t=0$ to the cone point $y_0$ at $t=1$.
Hence every loop in $X$ contracts inside this subspace of $X*Y$.
:::

<1>6. Therefore
\[
\boxed{\pi_1(X*Y)=0,}
\]
and since $X*Y$ is path connected, it is simply connected.
::: {.proof}
By <1>4 every loop is homotopic to one in $X$, and by <1>5 every such loop is nullhomotopic.
Path connectedness is <1>1.
:::
:::
