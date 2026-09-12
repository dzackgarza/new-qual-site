---
schema: qual/card@1
id: E-HAT-1.1-7
kind: problem
title: Homotopy of Dehn twist on $S^1 \times I$ stationary on one boundary only
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Torus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the vertical arc to obstruct a homotopy relative to both boundary circles; its twisted image differs by one generator of the annulus fundamental group.
---

Define $f: S^1 \times I \longrightarrow S^1 \times I$ by $f(\theta, s) = (\theta + 2\pi s, s)$, so $f$ restricts to the identity on the two boundary circles of $S^1 \times I$.
Show that $f$ is homotopic to the identity by a homotopy $f_t$ that is stationary on one of the boundary circles, but not by any homotopy $f_t$ that is stationary on both boundary circles.
[Consider what $f$ does to the path $s \mapsto (\theta_0, s)$ for fixed $\theta_0 \in S^1$.]

::: {.solution}
Write points of $S^1$ by angles modulo $2\pi$.

<1>1. The maps
\[
f_t(\theta,s)=(\theta+2\pi ts,s),
\qquad 0\le t\le1,
\]
give a homotopy from the identity to $f$ that is stationary on the boundary circle $S^1\times\{0\}$.
::: {.proof}
At $t=0$,
\[
f_0(\theta,s)=(\theta,s),
\]
while at $t=1$ one obtains the given map $f$.
For every $t$ and every $\theta$,
\[
f_t(\theta,0)=(\theta,0),
\]
so the lower boundary circle is fixed pointwise throughout the homotopy.
:::

<1>2. Fix $\theta_0\in S^1$ and let
\[
\alpha(s)=(\theta_0,s),
\qquad 0\le s\le1.
\]
Then
\[
(f\circ\alpha)(s)=(\theta_0+2\pi s,s).
\]
::: {.proof}
This is immediate from the definition of $f$.
Both paths run from $(\theta_0,0)$ to $(\theta_0,1)$ because adding $2\pi$ does not change the point of $S^1$.
:::

<1>3. The paths $\alpha$ and $f\circ\alpha$ are not homotopic relative to their endpoints in $S^1\times I$.
::: {.proof}
Let
\[
r:S^1\times I\to S^1,
\qquad r(\theta,s)=\theta,
\]
be projection to the circle.
Then $r\circ\alpha$ is the constant loop at $\theta_0$, whereas
\[
r\circ f\circ\alpha(s)=\theta_0+2\pi s
\]
traverses $S^1$ once.

If $\alpha$ and $f\circ\alpha$ were homotopic relative to endpoints, composing such a homotopy with $r$ would give a based homotopy between these two loops in $S^1$.
But the first loop represents $0$ and the second represents $1$ in
\[
\pi_1(S^1,\theta_0)\cong\mathbb Z.
\]
They therefore cannot be based-homotopic.
:::

<1>4. There is no homotopy from the identity to $f$ that is stationary on both boundary circles.
::: {.proof}
Suppose
\[
F_t:S^1\times I\to S^1\times I
\]
were such a homotopy, with $F_0=\operatorname{id}$ and $F_1=f$, and with both boundary circles fixed pointwise for every $t$.
Define
\[
H(s,t)=F_t(\alpha(s)).
\]
Then
\[
H(s,0)=\alpha(s),
\qquad
H(s,1)=f\circ\alpha(s).
\]
Because $\alpha(0)$ and $\alpha(1)$ lie on the two boundary circles and those circles are stationary,
\[
H(0,t)=\alpha(0),
\qquad
H(1,t)=\alpha(1)
\]
for all $t$.
Thus $H$ would be a homotopy relative to endpoints between $\alpha$ and $f\circ\alpha$, contradicting <1>3.
:::

<1>5. Hence $f$ is homotopic to the identity relative to either chosen single boundary circle, but not relative to both boundary circles simultaneously.
::: {.proof}
The lower-boundary statement is <1>1.
For the upper boundary circle one can instead use
\[
g_t(\theta,s)=(\theta+2\pi t(s-1),s).
\]
At $t=0$ this is the identity, at $t=1$ it agrees with $f$ because angles differing by $2\pi$ define the same point of $S^1$, and at $s=1$ it fixes $(\theta,1)$ for every $t$.
The impossibility of fixing both is <1>4.
:::
:::
