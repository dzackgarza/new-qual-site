---
schema: qual/card@1
id: P-BKS09-5A
kind: problem
title: Stable rotation of a four-legged table on an uneven floor
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed the height-imbalance argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the sign change under quarter-turn rotation and the intersection of the two lifted diagonals.
---

::: {.problem}
There is a "folk theorem" that a four-footed table can always be rotated into a stable position on an uneven floor.
Prove the following mathematical formulation of this theorem.

Define four points in $\mathbb R^2$, depending on an angle $\theta$, by
$$
P_1(\theta)=(\cos\theta,\sin\theta),\quad
P_2(\theta)=(-\sin\theta,\cos\theta),
$$
$$
P_3(\theta)=(-\cos\theta,-\sin\theta),\quad
P_4(\theta)=(\sin\theta,-\cos\theta).
$$
Show that given any continuous function $h:\mathbb R^2\to\mathbb R$, there exists a value of $\theta$ such that the four points
$$
Q_i(\theta)=(P_i(\theta),h(P_i(\theta)))
$$
on the graph of $h$ are co-planar in $\mathbb R^3$.
:::

::: {.solution}
Set
$$
\widetilde h(\theta)
\coloneqq
h(\cos\theta,\sin\theta)
$$
and
$$
g(\theta)
\coloneqq
\widetilde h(\theta)-\widetilde h(\theta+\pi/2)
+\widetilde h(\theta+\pi)-\widetilde h(\theta+3\pi/2).
$$

<1>1. The function $g$ is continuous and satisfies
$$
g(\theta+\pi/2)=-g(\theta)
$$
for every $\theta$.

::: {.proof}
Continuity follows from continuity of $h$ and the trigonometric
parametrization of the unit circle. Also $\widetilde h$ is $2\pi$-periodic,
so
$$
\begin{aligned}
g(\theta+\pi/2)
&=
\widetilde h(\theta+\pi/2)-\widetilde h(\theta+\pi)
+\widetilde h(\theta+3\pi/2)-\widetilde h(\theta+2\pi)\\
&=-g(\theta).
\end{aligned}
$$
:::

<1>2. There exists $\theta_0\in\RR$ such that $g(\theta_0)=0$.

::: {.proof}
Fix any $\theta$. If $g(\theta)=0$, take $\theta_0=\theta$. Otherwise,
step <1>1 shows that $g(\theta)$ and $g(\theta+\pi/2)$ have opposite
signs. The intermediate value theorem therefore gives a zero of $g$ on
the interval between these two angles.
:::

<1>3. For the angle $\theta_0$ from step <1>2, the line segments
$Q_1(\theta_0)Q_3(\theta_0)$ and
$Q_2(\theta_0)Q_4(\theta_0)$ have a common midpoint.

::: {.proof}
Write $P_i=P_i(\theta_0)$ and $Q_i=Q_i(\theta_0)$. From the definitions,
$$
P_3=-P_1,
\qquad
P_4=-P_2.
$$
Thus the midpoint of $Q_1Q_3$ is
$$
\left(0,0,
\frac{h(P_1)+h(P_3)}{2}
\right),
$$
while the midpoint of $Q_2Q_4$ is
$$
\left(0,0,
\frac{h(P_2)+h(P_4)}{2}
\right).
$$
The equality $g(\theta_0)=0$ is exactly
$$
h(P_1)+h(P_3)=h(P_2)+h(P_4),
$$
so these two midpoints coincide.
:::

<1>4. The four points $Q_1(\theta_0),\ldots,Q_4(\theta_0)$ are coplanar.

::: {.proof}
By step <1>3, the line through $Q_1,Q_3$ intersects the line through
$Q_2,Q_4$. Two intersecting lines lie in a common plane, and that plane
contains all four endpoints. If the two lines happen to coincide, the four
points are collinear and hence are also coplanar.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required angle and coplanarity conclusion.
:::
:::
