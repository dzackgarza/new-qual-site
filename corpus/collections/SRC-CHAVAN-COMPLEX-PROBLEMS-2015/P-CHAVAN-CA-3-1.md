---
schema: qual/card@1
id: P-CHAVAN-CA-3-1
kind: problem
title: Discontinuities of the principal argument on the punctured plane
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let
\[
\arg:\mathbb C^*\to[0,2\pi)
\]
be the principal argument.
Show that $\arg$ is not continuous, and determine its set of discontinuities.
:::

::: {.solution}
<1>1. The function $\arg$ is discontinuous at every positive real number.

::: {.proof}
Fix $x>0$. For $m\ge1$, set
$$
z_m=xe^{-i/m}.
$$
Then $z_m\to x$, while
$$
\arg(z_m)=2\pi-\frac1m
\longrightarrow 2\pi.
$$
But $\arg(x)=0$. Hence
$$
\arg(z_m)\not\longrightarrow\arg(x),
$$
so $\arg$ is not continuous at $x$.
:::

<1>2. The function $\arg$ is continuous at every point
$$
z_0\in\mathbb C^*\setminus(0,\infty).
$$

::: {.proof}
Write
$$
z_0=r_0e^{i\theta_0},
\qquad
r_0>0,
\qquad
0<\theta_0<2\pi.
$$
Choose $\delta>0$ so small that
$$
0<\theta_0-\delta<\theta_0+\delta<2\pi.
$$
Consider the open sector
$$
S=\{re^{i\theta}:r>0,\ \theta_0-\delta<\theta<\theta_0+\delta\}.
$$
It is an open neighborhood of $z_0$ contained in
$\mathbb C^*\setminus[0,\infty)$.

On the interval
$$
I=(\theta_0-\delta,\theta_0+\delta),
$$
the map
$$
\theta\longmapsto e^{i\theta}
$$
is a continuous bijection onto the open arc
$$
A=\{e^{i\theta}:\theta\in I\}.
$$
Its inverse is continuous: after possibly shrinking $\delta$ so that
if $\sin\theta_0\ne0$, then $-\sin\theta$ stays nonzero on $I$, so
$\cos\theta$ is strictly monotone there; while if
$\sin\theta_0=0$, then $\cos\theta_0\ne0$, so $\cos\theta$ stays
nonzero on $I$ and $\sin\theta$ is strictly monotone there. In either
case the inverse can be written using the continuous inverse of the
corresponding coordinate function. Thus
$$
\arg(z)
=\left(\theta\mapsto e^{i\theta}\right)^{-1}
\left(\frac{z}{|z|}\right)
$$
for $z\in S$. The map $z\mapsto z/|z|$ is continuous on
$\mathbb C^*$, so this composition is continuous on $S$, in
particular at $z_0$.
:::

<1>3. The set of discontinuities of $\arg$ is
$$
\boxed{(0,\infty)}.
$$

::: {.proof}
Step <1>1 shows that every positive real number is a discontinuity.
Step <1>2 shows that every other point of the domain $\mathbb C^*$ is
a continuity point. Since $0\notin\mathbb C^*$, these exhaust the
domain.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the complete discontinuity set and, in particular,
shows that $\arg$ is not continuous on $\mathbb C^*$.
:::
:::
