---
schema: qual/card@1
id: P-E6CQZ
kind: problem
title: Stabilizers for $\SL_2(\RR)$ acting on $\RR^2$ and by Möbius transformations
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Matrix Groups
  - Orbit-Stabilizer
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Consider $\SL_2(\RR)$ acting on $\RR^2$ by matrix multiplication.
What is the stabiliser of a point?
Does it depend which point?
Do you know what sort of subgroup this is?
What if $\SL_2(\RR)$ acts by Möbius transformations instead?
:::

::: {.solution}
For the linear action of $\SL_2(\RR)$ on $\RR^2$, the stabilizer of $0$ is the whole group.

If $v\ne0$, choose $g\in\SL_2(\RR)$ with $g e_1=v$. Then
$$
\Stab(v)=g\,\Stab(e_1)\,g^{-1},
$$
and
$$
\Stab(e_1)
=
\left\{
\begin{pmatrix}1&t\\0&1\end{pmatrix}:t\in\RR
\right\}.
$$
Thus all nonzero-point stabilizers are conjugate unipotent subgroups isomorphic to $(\RR,+)$, while the stabilizer of $0$ is all of $\SL_2(\RR)$.

For the Möbius action
$$
z\longmapsto \frac{az+b}{cz+d},
\qquad
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\SL_2(\RR),
$$
there are two natural spaces to distinguish.

On the upper half-plane $\HH$, the action is transitive and
$$
\Stab(i)
=
\left\{
\begin{pmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{pmatrix}:\theta\in\RR
\right\}
\cong \SO(2).
$$
Hence every stabilizer of a point of $\HH$ is conjugate to $\SO(2)$.

On the boundary $\PP^1(\RR)=\RR\cup\{\infty\}$, the action is also transitive, but the stabilizers are different. For example,
$$
\Stab(\infty)
=
\left\{
\begin{pmatrix}a&b\\0&a^{-1}\end{pmatrix}:a\in\RR^\times,\ b\in\RR
\right\},
$$
a Borel subgroup; every boundary-point stabilizer is conjugate to it.
:::
