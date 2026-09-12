---
schema: qual/card@1
id: E-HAT-1.1-5
kind: problem
title: Three equivalent conditions for simply-connected spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Simply Connected
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Included the free-homotopy conjugacy argument needed to pass from unbased null-homotopy to trivial based fundamental-group class.
---

Show that for a space $X$, the following three conditions are equivalent:

(a) Every map $S^1 \to X$ is homotopic to a constant map, with image a point.

(b) Every map $S^1 \to X$ extends to a map $D^2 \to X$.

(c) $\pi_1(X, x_0) = 0$ for all $x_0 \in X$.

Deduce that a space $X$ is simply-connected iff all maps $S^1 \to X$ are homotopic.
[In this problem, 'homotopic' means 'homotopic without regard to basepoints'.]

::: {.solution}
<1>1. If two loops $f_0,f_1:S^1\to X$ are freely homotopic, then after choosing a point $s_0\in S^1$ their based homotopy classes are conjugate by the path traced by the basepoint during the homotopy.
::: {.proof}
Let
\[
H:S^1\times I\to X
\]
be a homotopy from $f_0$ to $f_1$, and define
\[
h(t)=H(s_0,t).
\]
Thus $h$ is a path from $x_0=f_0(s_0)$ to $x_1=f_1(s_0)$.
The square obtained by cutting $S^1$ at $s_0$ has boundary path
\[
f_0\cdot h\cdot\overline{f_1}\cdot\bar h,
\]
which is null-homotopic because it is the image of the boundary of the homotopy square under $H$.
Hence, in path-homotopy classes,
\[
[f_0]=[h\cdot f_1\cdot\bar h]=\beta_h([f_1]).
\]
In particular, a based loop freely homotopic to a constant loop represents the identity element of its fundamental group.
:::

<1>2. Condition (a) implies condition (b).
::: {.proof}
Let $f:S^1\to X$.
By (a), there is a homotopy
\[
H:S^1\times I\to X
\]
from $f$ to a constant map with value $p\in X$.
Since $H$ is constant on the whole top circle $S^1\times\{1\}$, it factors through the quotient
\[
(S^1\times I)/(S^1\times\{1\}),
\]
which is the cone on $S^1$ and is homeomorphic to $D^2$.
The descended map $D^2\to X$ restricts on the boundary circle $S^1\times\{0\}$ to $f$.
Thus $f$ extends over $D^2$.
:::

<1>3. Condition (b) implies condition (a).
::: {.proof}
Let $f:S^1\to X$ extend to
\[
F:D^2\to X.
\]
The disk is contractible to its center by
\[
r_t(z)=(1-t)z.
\]
Hence
\[
H(z,t)=F(r_t(z)),
\qquad z\in S^1,
\]
is a homotopy from $f=F|_{S^1}$ to the constant map with value $F(0)$.
Thus (a) holds.
:::

<1>4. Condition (a) implies condition (c).
::: {.proof}
Fix $x_0\in X$ and a loop $f:S^1\to X$ based at $x_0$.
By (a), $f$ is freely homotopic to a constant map.
By <1>1, the based class $[f]\in\pi_1(X,x_0)$ is conjugate, via the basepoint track, to the class of a constant loop.
The latter is the identity, and conjugating the identity again gives the identity.
Thus every element of $\pi_1(X,x_0)$ is trivial, so
\[
\pi_1(X,x_0)=0.
\]
Since $x_0$ was arbitrary, (c) holds.
:::

<1>5. Condition (c) implies condition (a).
::: {.proof}
Let $f:S^1\to X$, choose $s_0\in S^1$, and put $x_0=f(s_0)$.
By (c),
\[
[f]=1\in\pi_1(X,x_0).
\]
Thus $f$ is homotopic relative to the basepoint to the constant loop at $x_0$.
Forgetting the basepoint condition gives an ordinary homotopy to a constant map, which is (a).
:::

<1>6. Conditions (a), (b), and (c) are equivalent.
::: {.proof}
The equivalence of (a) and (b) is <1>2--<1>3, while <1>4--<1>5 give the equivalence of (a) and (c).
:::

<1>7. If $X$ is simply connected, then every two maps $S^1\to X$ are homotopic.
::: {.proof}
Simple connectivity gives path connectedness and condition (c), hence condition (a) by <1>6.
Thus every map $S^1\to X$ is homotopic to a constant map.
If $x,y\in X$, choose a path $h:I\to X$ from $x$ to $y$.
Then
\[
H(s,t)=h(t)
\]
is a homotopy from the constant map at $x$ to the constant map at $y$.
Consequently any two maps $S^1\to X$ are homotopic through their respective constant maps.
:::

<1>8. Conversely, if all maps $S^1\to X$ are homotopic, then $X$ is simply connected.
::: {.proof}
First, for any $x,y\in X$, the constant maps $c_x,c_y:S^1\to X$ are homotopic.
If $H:S^1\times I\to X$ is such a homotopy and $s_0\in S^1$, then
\[
t\longmapsto H(s_0,t)
\]
is a path from $x$ to $y$.
Hence $X$ is path connected.

Second, every map $S^1\to X$ is homotopic to every constant map, so condition (a) holds.
By <1>6, condition (c) holds as well.
Thus $X$ is path connected and has trivial fundamental group, hence is simply connected.
:::
:::
