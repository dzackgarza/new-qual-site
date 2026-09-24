---
schema: qual/card@1
id: P-BKS81-1
kind: problem
title: Curl and flux over the upper hemisphere
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the curl computation and the outward flux by closing the hemisphere with its equatorial disk and applying the divergence theorem.
---

::: {.problem}
Let $\vec i,\vec j,\vec k$ be the standard unit vectors in $\mathbb R^3$, and let
\[
\vec F=(x^2+y-4)\vec i+3xy\vec j+(2xz+z^2)\vec k.
\]

1. Compute $\nabla\times\vec F$.
2. Compute the integral of $\nabla\times\vec F$ over the surface
   \[
   x^2+y^2+z^2=16,\qquad z\ge0.
   \]
:::

::: {.solution}
Let $S$ denote the upper hemisphere, oriented by the outward normal, and let
$$
D\coloneqq\{(x,y,0):x^2+y^2\le16\}
$$
be its equatorial disk. As part of the boundary of the upper half-ball, $D$
has outward unit normal $-\vec k$.

<1>1. The curl is
$$
\boxed{
\nabla\times\vec F
=
-2z\,\vec j+(3y-1)\,\vec k
}.
$$

::: {.proof}
Writing
$$
\vec F=(P,Q,R)
$$
with
$$
P=x^2+y-4,
\qquad
Q=3xy,
\qquad
R=2xz+z^2,
$$
one has
$$
\begin{aligned}
\nabla\times\vec F
&=
(R_y-Q_z)\vec i
+(P_z-R_x)\vec j
+(Q_x-P_y)\vec k\\
&=
0\,\vec i-2z\,\vec j+(3y-1)\,\vec k.
\end{aligned}
$$
:::

<1>2. The outward flux of $\nabla\times\vec F$ through $D$ is
$$
16\pi.
$$

::: {.proof}
On $D$ one has $z=0$, so step <1>1 gives
$$
(\nabla\times\vec F)\cdot(-\vec k)=1-3y.
$$
Therefore
$$
\iint_D(\nabla\times\vec F)\cdot(-\vec k)\,dA
=
\iint_D(1-3y)\,dA.
$$
The integral of $y$ over the disk is zero by symmetry, while
$\operatorname{area}(D)=\pi4^2=16\pi$. Hence the flux through $D$ is
$16\pi$.
:::

<1>3. The outward flux over the upper hemisphere is
$$
\boxed{
\iint_S(\nabla\times\vec F)\cdot\vec n\,dS=-16\pi
}.
$$

::: {.proof}
From step <1>1,
$$
\nabla\cdot(\nabla\times\vec F)=0.
$$
The divergence theorem on the upper half-ball therefore gives
$$
0
=
\iint_S(\nabla\times\vec F)\cdot\vec n\,dS
+
\iint_D(\nabla\times\vec F)\cdot(-\vec k)\,dA.
$$
Step <1>2 evaluates the second integral as $16\pi$, so the first is
$-16\pi$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 answers part (1), and step <1>3 answers part (2).
:::
:::
